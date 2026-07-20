import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum, Count

from .chain import get_blockchain, MINING_REWARD
from .crypto import generate_wallet, sign_transaction, verify_signature
from .p2p import get_node
from .models import (
    CryptoWallet, CryptoTransaction, MiningStats, ChainState,
    Proposal, Vote, Stake, RewardLog, PremiumAccess, DailyLogin,
)
from .tokenomics import (
    GOVERNANCE, UTILITY, REWARDS, MAX_SUPPLY, get_block_reward,
    get_total_circulating, HALVING_INTERVAL,
)


def _save_chain():
    chain = get_blockchain()
    from .models import ChainState
    state, _ = ChainState.objects.get_or_create(pk=1)
    state.data = chain.to_dict()
    state.save()


# ─── Blockchain Pages ───────────────────────────────────────
@login_required
def blockchain_dashboard(request):
    chain = get_blockchain()
    my_wallet = CryptoWallet.objects.filter(user=request.user).first()
    stats = MiningStats.objects.first()
    return render(request, 'studio/blockchain_dashboard.html', {
        'chain': chain,
        'my_wallet': my_wallet,
        'stats': stats,
    })


@login_required
def blockchain_wallet(request):
    my_wallet = CryptoWallet.objects.filter(user=request.user).first()
    if not my_wallet:
        return render(request, 'studio/blockchain_wallet.html', {
            'my_wallet': None, 'balance': 0, 'history': [],
        })
    chain = get_blockchain()
    balance = chain.get_balance(my_wallet.address)
    history = chain.get_history(my_wallet.address)
    return render(request, 'studio/blockchain_wallet.html', {
        'my_wallet': my_wallet, 'balance': balance, 'history': history,
    })


@login_required
def blockchain_explorer(request):
    chain = get_blockchain()
    blocks = [b.to_dict() for b in reversed(chain.chain)]
    return render(request, 'studio/blockchain_explorer.html', {
        'blocks': blocks[:50], 'chain_length': chain.length,
    })


@login_required
def blockchain_mining(request):
    stats = MiningStats.objects.first()
    return render(request, 'studio/blockchain_mining.html', {
        'stats': stats, 'difficulty': 4, 'reward': MINING_REWARD,
    })


# ─── Blockchain API ─────────────────────────────────────────
@csrf_exempt
def api_wallet_create(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Non authentifié'}, status=401)
    if CryptoWallet.objects.filter(user=request.user).exists():
        w = CryptoWallet.objects.get(user=request.user)
        return JsonResponse({'address': w.address, 'public_key': w.public_key, 'created': False})

    wallet = generate_wallet()
    cw = CryptoWallet.objects.create(
        user=request.user,
        address=wallet['address'],
        public_key=wallet['public_key'],
        private_key_encrypted=wallet['private_key'],
    )
    return JsonResponse({
        'address': wallet['address'],
        'public_key': wallet['public_key'],
        'private_key': wallet['private_key'],
        'created': True,
    })


@csrf_exempt
def api_balance(request, address):
    chain = get_blockchain()
    balance = chain.get_balance(address)
    return JsonResponse({'address': address, 'balance': balance})


@csrf_exempt
def api_send(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Non authentifié'}, status=401)
    try:
        data = json.loads(request.body)
        to_addr = data.get('to', '').strip()
        amount = float(data.get('amount', 0))
        fee = float(data.get('fee', 0))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Données invalides'}, status=400)

    if amount <= 0:
        return JsonResponse({'error': 'Montant invalide'}, status=400)

    cw = CryptoWallet.objects.filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Aucun wallet crypto. Créez-en un d\'abord.'}, status=400)

    chain = get_blockchain()
    balance = chain.get_balance(cw.address)
    total = amount + fee
    if balance < total:
        return JsonResponse({'error': f'Solde insuffisant ({balance} PSX < {total} PSX)'}, status=400)

    tx_data = {
        'from': cw.address,
        'to': to_addr,
        'amount': amount,
        'fee': fee,
    }
    signature = sign_transaction(cw.private_key_encrypted, tx_data)
    tx = {**tx_data, 'signature': signature, 'public_key': cw.public_key, 'timestamp': __import__('time').time()}

    error = chain.add_transaction(tx)
    if error:
        return JsonResponse({'error': error}, status=400)

    CryptoTransaction.objects.create(
        from_address=cw.address,
        to_address=to_addr,
        amount=amount,
        fee=fee,
        signature=signature,
        public_key=cw.public_key,
        status='pending',
    )

    node = get_node()
    node.broadcast_transaction(tx)

    return JsonResponse({
        'status': 'Transaction soumise',
        'from': cw.address,
        'to': to_addr,
        'amount': amount,
        'fee': fee,
    })


@csrf_exempt
def api_mine(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Non authentifié'}, status=401)

    cw = CryptoWallet.objects.filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Aucun wallet crypto'}, status=400)

    chain = get_blockchain()
    block = chain.mine_pending(cw.address)
    if not block:
        return JsonResponse({'error': 'Aucune transaction à miner'}, status=400)

    stats, _ = MiningStats.objects.get_or_create(pk=1)
    stats.total_blocks = chain.length
    stats.total_mined += 1
    stats.last_block_time = __import__('django.utils.timezone', fromlist=['now']).now()
    stats.save()

    node = get_node()
    node.broadcast_block(block.to_dict())

    _save_chain()

    return JsonResponse({
        'status': 'Bloc miné',
        'index': block.index,
        'hash': block.hash,
        'transactions': len(block.transactions),
        'nonce': block.nonce,
        'reward': MINING_REWARD,
    })


@csrf_exempt
def api_chain(request):
    chain = get_blockchain()
    return JsonResponse(chain.to_dict())


@csrf_exempt
def api_sync(request):
    node = get_node()
    node.request_chain_from_peers()
    return JsonResponse({'status': 'Sync lancé'})


@csrf_exempt
def api_peers(request):
    node = get_node()
    return JsonResponse({
        'node': f'{node.host}:{node.port}',
        'peers': list(node.peers),
    })


@csrf_exempt
def api_connect_peer(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    try:
        data = json.loads(request.body)
        host = data.get('host', '')
        port = int(data.get('port', 9333))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Données invalides'}, status=400)

    node = get_node()
    ok = node.connect_peer(host, port)
    return JsonResponse({
        'status': 'Connecté' if ok else 'Échec',
        'peers': list(node.peers),
    })


@csrf_exempt
def api_validate(request):
    chain = get_blockchain()
    valid, message = chain.validate_chain()
    return JsonResponse({
        'valid': valid,
        'message': message,
        'length': chain.length,
    })


@csrf_exempt
def api_send_tnd_to_crypto(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Non authentifié'}, status=401)

    try:
        data = json.loads(request.body)
        amount_tnd = float(data.get('amount', 0))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Montant invalide'}, status=400)

    if amount_tnd <= 0:
        return JsonResponse({'error': 'Montant invalide'}, status=400)

    from studio.models import Wallet
    tnd_wallet, _ = Wallet.objects.get_or_create(user=request.user)
    if tnd_wallet.solde < amount_tnd:
        return JsonResponse({'error': f'Solde TND insuffisant ({tnd_wallet.solde})'}, status=400)

    cw = CryptoWallet.objects.filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Aucun wallet crypto'}, status=400)

    tnd_wallet.solde -= amount_tnd
    tnd_wallet.save()

    psx_amount = amount_tnd * 1.0
    chain = get_blockchain()
    tx = {
        'from': 'BRIDGE_TND',
        'to': cw.address,
        'amount': psx_amount,
        'fee': 0,
        'type': 'bridge_tnd_to_psx',
        'timestamp': __import__('time').time(),
    }
    chain.add_transaction(tx)

    block = chain.mine_pending('SYSTEM')
    _save_chain()

    CryptoTransaction.objects.create(
        from_address='BRIDGE_TND',
        to_address=cw.address,
        amount=psx_amount,
        status='confirmed',
        block_index=block.index if block else chain.length,
        block_hash=block.hash if block else '',
    )

    return JsonResponse({
        'status': 'Conversion effectuée',
        'tnd_spent': amount_tnd,
        'psx_received': psx_amount,
        'psx_balance': chain.get_balance(cw.address),
    })


# ─── TOKENOMICS ──────────────────────────────────────────────

@login_required
def tokenomics_dashboard(request):
    chain = get_blockchain()
    cw = CryptoWallet.objects.filter(user=request.user).first()
    balance = chain.get_balance(cw.address) if cw else 0
    circulating = get_total_circulating(chain.length)
    total_staked = Stake.objects.filter(status='active').aggregate(t=Sum('amount'))['t'] or 0
    active_proposals = Proposal.objects.filter(status='active').count()
    total_users = CryptoWallet.objects.count()

    user_stakes = Stake.objects.filter(user=request.user, status='active') if cw else []
    user_proposals = Proposal.objects.filter(author=request.user)[:5] if cw else []
    my_premium = PremiumAccess.objects.filter(user=request.user).first()

    return render(request, 'studio/tokenomics_dashboard.html', {
        'balance': balance,
        'max_supply': MAX_SUPPLY,
        'circulating': circulating,
        'total_staked': total_staked,
        'active_proposals': active_proposals,
        'total_users': total_users,
        'chain_length': chain.length,
        'halving_in': HALVING_INTERVAL - (chain.length % HALVING_INTERVAL),
        'next_reward': get_block_reward(chain.length),
        'governance': GOVERNANCE,
        'utility': UTILITY,
        'rewards': REWARDS,
        'user_stakes': user_stakes,
        'user_proposals': user_proposals,
        'my_premium': my_premium,
        'my_wallet': cw,
    })


# ─── Governance ──────────────────────────────────────────────

@login_required
def governance_list(request):
    proposals = Proposal.objects.all()[:50]
    return render(request, 'studio/governance_list.html', {
        'proposals': proposals, 'governance': GOVERNANCE,
    })


@login_required
def governance_proposal(request, proposal_id):
    proposal = Proposal.objects.get(id=proposal_id)
    user_vote = Vote.objects.filter(proposal=proposal, voter=request.user).first()
    cw = CryptoWallet.objects.filter(user=request.user).first()
    return render(request, 'studio/governance_proposal.html', {
        'proposal': proposal, 'user_vote': user_vote,
        'balance': get_blockchain().get_balance(cw.address) if cw else 0,
    })


@csrf_exempt
@login_required
def api_governance_propose(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    cw = CryptoWallet.objects.filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Wallet crypto requis'}, status=400)

    balance = get_blockchain().get_balance(cw.address)
    if balance < GOVERNANCE['min_to_propose']:
        return JsonResponse({
            'error': f'Il vous faut {GOVERNANCE["min_to_propose"]} PSX pour proposer (vous avez {balance})'
        }, status=400)

    try:
        data = json.loads(request.body)
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Données invalides'}, status=400)

    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    category = data.get('category', 'feature')

    if not title or not description:
        return JsonResponse({'error': 'Titre et description requis'}, status=400)

    proposal = Proposal.objects.create(
        author=request.user,
        title=title,
        description=description,
        category=category,
        ends_at=timezone.now() + timedelta(days=GOVERNANCE['voting_period_days']),
    )
    return JsonResponse({
        'status': 'Proposition créée',
        'id': str(proposal.id),
        'title': proposal.title,
    })


@csrf_exempt
@login_required
def api_governance_vote(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    cw = CryptoWallet.objects.filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Wallet crypto requis'}, status=400)

    balance = get_blockchain().get_balance(cw.address)
    if balance <= 0:
        return JsonResponse({'error': 'Solde insuffisant pour voter'}, status=400)

    try:
        data = json.loads(request.body)
        proposal_id = data.get('proposal_id')
        choice = data.get('choice')
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Données invalides'}, status=400)

    if choice not in ('for', 'against'):
        return JsonResponse({'error': 'Vote invalide'}, status=400)

    proposal = Proposal.objects.get(id=proposal_id)
    if proposal.status != 'active':
        return JsonResponse({'error': 'Proposition non active'}, status=400)
    if proposal.ends_at < timezone.now():
        proposal.status = 'expired'
        proposal.save()
        return JsonResponse({'error': 'Proposition expirée'}, status=400)

    existing = Vote.objects.filter(proposal=proposal, voter=request.user).first()
    if existing:
        return JsonResponse({'error': 'Vous avez déjà voté'}, status=400)

    Vote.objects.create(
        proposal=proposal, voter=request.user, choice=choice, weight=balance,
    )
    if choice == 'for':
        proposal.votes_for += balance
    else:
        proposal.votes_against += balance
    proposal.save()

    return JsonResponse({'status': 'Vote enregistré', 'choice': choice, 'weight': balance})


# ─── Staking ─────────────────────────────────────────────────

@login_required
def staking_page(request):
    cw = CryptoWallet.objects.filter(user=request.user).first()
    balance = get_blockchain().get_balance(cw.address) if cw else 0
    user_stakes = Stake.objects.filter(user=request.user, status='active')
    total_staked_user = user_stakes.aggregate(t=Sum('amount'))['t'] or 0
    total_staked_network = Stake.objects.filter(status='active').aggregate(t=Sum('amount'))['t'] or 0

    return render(request, 'studio/staking_page.html', {
        'balance': balance, 'user_stakes': user_stakes,
        'total_staked_user': total_staked_user,
        'total_staked_network': total_staked_network,
        'rewards': REWARDS,
    })


@csrf_exempt
@login_required
def api_stake(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    cw = CryptoWallet.objects.filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Wallet crypto requis'}, status=400)

    chain = get_blockchain()
    balance = chain.get_balance(cw.address)

    try:
        data = json.loads(request.body)
        amount = float(data.get('amount', 0))
        lock_days = int(data.get('lock_days', 30))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Données invalides'}, status=400)

    if amount < REWARDS['min_stake']:
        return JsonResponse({'error': f'Minimum {REWARDS["min_stake"]} PSX'}, status=400)
    if balance < amount:
        return JsonResponse({'error': 'Solde insuffisant'}, status=400)
    if lock_days not in REWARDS['lock_periods']:
        return JsonResponse({'error': 'Durée invalide'}, status=400)

    apy = REWARDS['lock_periods'][lock_days]
    unlocks_at = timezone.now() + timedelta(days=lock_days)

    Stake.objects.create(
        user=request.user, amount=amount, apy=apy,
        lock_days=lock_days, unlocks_at=unlocks_at,
    )

    return JsonResponse({
        'status': f'{amount} PSX stakés pour {lock_days} jours',
        'apy': apy, 'unlocks_at': unlocks_at.isoformat(),
    })


@csrf_exempt
@login_required
def api_stake_claim(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    try:
        data = json.loads(request.body)
        stake_id = data.get('stake_id')
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Données invalides'}, status=400)

    stake = Stake.objects.get(id=stake_id, user=request.user)
    if stake.status != 'active':
        return JsonResponse({'error': 'Stake non actif'}, status=400)
    if stake.unlocks_at > timezone.now():
        remaining = (stake.unlocks_at - timezone.now()).days
        return JsonResponse({'error': f'Verrouillé encore {remaining} jours'}, status=400)

    chain = get_blockchain()
    cw = CryptoWallet.objects.get(user=request.user)
    total = float(stake.amount) + float(stake.earned)

    stake.status = 'completed'
    stake.save()

    return JsonResponse({
        'status': f'{total} PSX récupérés',
        'principal': float(stake.amount),
        'earned': float(stake.earned),
    })


# ─── Rewards ─────────────────────────────────────────────────

@csrf_exempt
@login_required
def api_claim_daily(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    today = timezone.now().date()
    login_obj, created = DailyLogin.objects.get_or_create(user=request.user, date=today)
    if login_obj.bonus_claimed:
        return JsonResponse({'error': 'Déjà réclamé aujourd\'hui'}, status=400)

    login_obj.bonus_claimed = True
    login_obj.save()

    cw = CryptoWallet.objects.filter(user=request.user).first()
    if cw:
        chain = get_blockchain()
        tx = {
            'from': 'REWARD_SYSTEM', 'to': cw.address,
            'amount': REWARDS['daily_login'],
            'type': 'reward_daily_login', 'timestamp': __import__('time').time(),
        }
        chain.add_transaction(tx)
        chain.mine_pending('SYSTEM')

    RewardLog.objects.create(
        user=request.user, amount=REWARDS['daily_login'],
        reason='daily_login', description='Bonus connexion quotidienne',
    )
    return JsonResponse({'status': f'+{REWARDS["daily_login"]} PSX', 'bonus': REWARDS['daily_login']})


# ─── Premium ─────────────────────────────────────────────────

@csrf_exempt
@login_required
def api_buy_premium(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    cw = CryptoWallet.objects.filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Wallet crypto requis'}, status=400)

    try:
        data = json.loads(request.body)
        plan = data.get('plan', 'monthly')
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Données invalides'}, status=400)

    cost = UTILITY.get(f'premium_{plan}')
    if not cost:
        return JsonResponse({'error': 'Plan invalide'}, status=400)

    chain = get_blockchain()
    balance = chain.get_balance(cw.address)
    if balance < cost:
        return JsonResponse({'error': f'Il vous faut {cost} PSX (solde: {balance})'}, status=400)

    if plan == 'monthly':
        expires = timezone.now() + timedelta(days=30)
    else:
        expires = timezone.now() + timedelta(days=365)

    existing = PremiumAccess.objects.filter(user=request.user).first()
    if existing and existing.is_active:
        existing.expires_at = existing.expires_at + (expires - timezone.now())
        existing.psx_paid += cost
        existing.save()
    else:
        PremiumAccess.objects.create(
            user=request.user, plan=plan, expires_at=expires, psx_paid=cost,
        )

    tx = {
        'from': cw.address, 'to': 'SYSTEM_PREMIUM',
        'amount': cost, 'type': 'premium_payment',
        'timestamp': __import__('time').time(),
    }
    chain.add_transaction(tx)
    chain.mine_pending('SYSTEM')
    _save_chain()

    return JsonResponse({'status': f'Premium {plan} activé', 'cost': cost, 'expires': expires.isoformat()})
