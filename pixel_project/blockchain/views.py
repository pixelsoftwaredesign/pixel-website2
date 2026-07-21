import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
import secrets
from django.utils import timezone
from datetime import timedelta
from django.db import transaction
from django.db.models import Sum, Count

from .chain import get_blockchain, MINING_REWARD
from .crypto import generate_wallet, sign_transaction, verify_signature
from .p2p import get_node
from .models import (
    CryptoWallet, CryptoTransaction, MiningStats, ChainState,
    Proposal, Vote, Stake, RewardLog, PremiumAccess, DailyLogin,
)
from .security import (
    sybil_guard, eclipse_guard, time_guard, circuit_breaker,
    fraud_detector, multisig_manager, MIN_STAKE_TO_VALIDATE,
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
@transaction.atomic
def api_wallet_create(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Non authentifié'}, status=401)
    if CryptoWallet.objects.filter(user=request.user).exists():
        w = CryptoWallet.objects.get(user=request.user)
        return JsonResponse({'address': w.address, 'public_key': w.public_key, 'nonce': w.nonce, 'created': False})

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
        'nonce': 0,
        'created': True,
    })


@csrf_exempt
def api_balance(request, address):
    chain = get_blockchain()
    balance = chain.get_balance(address)
    return JsonResponse({'address': address, 'balance': balance})


@csrf_exempt
def api_wallet_nonce(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Non authentifié'}, status=401)
    cw = CryptoWallet.objects.filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Aucun wallet'}, status=404)
    return JsonResponse({'address': cw.address, 'nonce': cw.nonce})


@csrf_exempt
@transaction.atomic
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

    cw = CryptoWallet.objects.select_for_update().filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Aucun wallet crypto. Créez-en un d\'abord.'}, status=400)

    chain = get_blockchain()
    balance = chain.get_balance(cw.address)
    total = amount + fee
    if balance < total:
        return JsonResponse({'error': f'Solde insuffisant ({balance} PSX < {total} PSX)'}, status=400)

    new_nonce = cw.nonce + 1
    timestamp = __import__('time').time()

    signature = sign_transaction(
        private_key_hex=cw.private_key_encrypted,
        sender=cw.address,
        receiver=to_addr,
        amount=amount,
        nonce=new_nonce,
        timestamp=timestamp,
    )

    tx = {
        'from': cw.address,
        'to': to_addr,
        'amount': amount,
        'fee': fee,
        'nonce': new_nonce,
        'signature': signature,
        'public_key': cw.public_key,
        'timestamp': timestamp,
    }

    error = chain.add_transaction(tx)
    if error:
        return JsonResponse({'error': error}, status=400)

    cw.nonce = new_nonce
    cw.save(update_fields=['nonce'])

    CryptoTransaction.objects.create(
        from_address=cw.address,
        to_address=to_addr,
        amount=amount,
        fee=fee,
        nonce=new_nonce,
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
        'nonce': new_nonce,
    })


@csrf_exempt
@transaction.atomic
def api_mine(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Non authentifié'}, status=401)

    cw = CryptoWallet.objects.select_for_update().filter(user=request.user).first()
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
@transaction.atomic
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
    tnd_wallet = Wallet.objects.select_for_update().get(user=request.user)
    if tnd_wallet.solde < amount_tnd:
        return JsonResponse({'error': f'Solde TND insuffisant ({tnd_wallet.solde})'}, status=400)

    cw = CryptoWallet.objects.select_for_update().filter(user=request.user).first()
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
@transaction.atomic
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
@transaction.atomic
def api_stake(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    cw = CryptoWallet.objects.select_for_update().filter(user=request.user).first()
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
@transaction.atomic
def api_claim_daily(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    today = timezone.now().date()
    login_obj, created = DailyLogin.objects.select_for_update().get_or_create(user=request.user, date=today)
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
@transaction.atomic
def api_buy_premium(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    cw = CryptoWallet.objects.select_for_update().filter(user=request.user).first()
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


# ─── SECURITY ────────────────────────────────────────────────

@login_required
def security_dashboard(request):
    chain = get_blockchain()
    cw = CryptoWallet.objects.filter(user=request.user).first()
    validators = sybil_guard.get_validators()
    peer_stats = eclipse_guard.get_peer_stats()
    node_status = get_node().get_status()
    fraud_alerts = fraud_detector.get_alerts(20)

    return render(request, 'studio/security_dashboard.html', {
        'chain': chain,
        'my_wallet': cw,
        'validators': validators,
        'peer_stats': peer_stats,
        'node_status': node_status,
        'fraud_alerts': fraud_alerts,
        'min_stake_validator': MIN_STAKE_TO_VALIDATE,
    })


@csrf_exempt
def api_security_status(request):
    chain = get_blockchain()
    return JsonResponse({
        'chain': {
            'length': chain.length,
            'pending': len(chain.pending_transactions),
            'valid': chain.validate_chain()[0],
        },
        'sybil': {
            'validators': sybil_guard.get_validators(),
        },
        'eclipse': eclipse_guard.get_peer_stats(),
        'time': {
            'consensus': time_guard.get_consensus_time(),
            'local': __import__('time').time(),
        },
        'circuit_breaker': {
            'tripped_addresses': len(circuit_breaker.tripped),
        },
        'fraud': {
            'alerts_count': len(fraud_detector.alerts),
            'recent': fraud_detector.get_alerts(10),
        },
    })


@csrf_exempt
@login_required
def api_become_validator(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    cw = CryptoWallet.objects.select_for_update().filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Wallet crypto requis'}, status=400)

    chain = get_blockchain()
    balance = chain.get_balance(cw.address)
    if balance < MIN_STAKE_TO_VALIDATE:
        return JsonResponse({
            'error': f'Il faut {MIN_STAKE_TO_VALIDATE} PSX (vous avez {balance})',
        }, status=400)

    ok = sybil_guard.register_validator(cw.address, balance)
    if ok:
        return JsonResponse({
            'status': 'Validateur activé',
            'address': cw.address,
            'stake': balance,
        })
    return JsonResponse({'error': 'Échec'}, status=500)


@csrf_exempt
def api_fraud_alerts(request):
    alerts = fraud_detector.get_alerts(50)
    return JsonResponse({'alerts': alerts, 'count': len(alerts)})


@csrf_exempt
@login_required
def api_multisig_create(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    try:
        data = json.loads(request.body)
        owners = data.get('owners', [])
        required = int(data.get('required', 2))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Données invalides'}, status=400)

    cw = CryptoWallet.objects.filter(user=request.user).first()
    if not cw:
        return JsonResponse({'error': 'Wallet requis'}, status=400)

    if cw.address not in owners:
        owners.append(cw.address)

    addr = f'MSIG-{cw.address[:16]}'
    ok = multisig_manager.create_multisig(addr, owners, required)
    if ok:
        return JsonResponse({
            'status': 'MultiSig créé',
            'address': addr,
            'owners': owners,
            'required': required,
        })
    return JsonResponse({'error': 'Paramètres invalides'}, status=400)


@csrf_exempt
@login_required
def api_multisig_propose(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    try:
        data = json.loads(request.body)
        multisig_addr = data.get('wallet')
        tx_data = data.get('tx', {})
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Données invalides'}, status=400)

    tx_hash = multisig_manager.propose_tx(multisig_addr, tx_data)
    if tx_hash:
        return JsonResponse({'status': 'Transaction proposée', 'hash': tx_hash})
    return JsonResponse({'error': 'Wallet introuvable'}, status=400)


# ─── Web3 Login ─────────────────────────────────────────────

def web3_login_page(request):
    return render(request, 'studio/web3_login.html')


@csrf_exempt
def api_web3_nonce(request):
    try:
        data = json.loads(request.body)
        address = data.get('address', '').strip().lower()
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Adresse invalide'}, status=400)

    if not address or len(address) != 42 or not address.startswith('0x'):
        return JsonResponse({'error': 'Adresse Ethereum invalide'}, status=400)

    from .web3auth import Web3Nonce
    Web3Nonce.objects.filter(address=address, used=False).update(used=True)
    nonce_obj = Web3Nonce.create_for_address(address)

    return JsonResponse({
        'message': nonce_obj.message,
        'nonce': nonce_obj.nonce,
    })


@csrf_exempt
def api_web3_verify(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST requis'}, status=405)
    try:
        data = json.loads(request.body)
        address = data.get('address', '').strip().lower()
        signature = data.get('signature', '')
        nonce = data.get('nonce', '')
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Données invalides'}, status=400)

    if not address or not signature or not nonce:
        return JsonResponse({'error': 'Champs requis manquants'}, status=400)

    from .web3auth import Web3Nonce, get_sign_message, Web3Session

    nonce_obj = Web3Nonce.objects.filter(
        address=address, nonce=nonce, used=False,
    ).first()
    if not nonce_obj or not nonce_obj.is_valid:
        return JsonResponse({'error': 'Nonce invalide ou expiré'}, status=400)

    nonce_obj.used = True
    nonce_obj.save(update_fields=['used'])

    expected_message = nonce_obj.message
    recovered = recover_address(expected_message, signature)

    if recovered and recovered.lower() == address:
        user = link_or_create_user(address)
        login(request, user)

        import secrets as _secrets
        session_token = _secrets.token_hex(32)
        Web3Session.objects.create(
            user=user,
            address=address,
            session_token=session_token,
            expires_at=timezone.now() + timezone.timedelta(days=7),
        )

        return JsonResponse({
            'status': 'success',
            'address': address,
            'username': user.username,
            'session': session_token,
        })
    else:
        return JsonResponse({
            'error': 'Signature invalide — le wallet ne correspond pas',
        }, status=403)


def recover_address(message: str, signature_hex: str) -> str:
    """
    Récupère l'adresse Ethereum à partir d'un message signé (personal_sign).
    Pure Python — utilise ecdsa (secp256k1) + keccak256 implémenté en ligne.
    """
    import hashlib
    import struct
    from ecdsa import SECP256k1
    N = SECP256k1.order

    # ── Keccak-256 (Ethereum's hash, NOT SHA3-256) ──
    def keccak256(data: bytes) -> bytes:
        def rot64(x, n):
            return ((x << n) | (x >> (64 - n))) & 0xFFFFFFFFFFFFFFFF

        def enc64(x):
            return struct.pack('<Q', x)

        def dec64(b):
            return struct.unpack('<Q', b)[0]

        ROUNDS = 24
        RC = [
            0x0000000000000001, 0x0000000000008082, 0x800000000000808A,
            0x8000000080008000, 0x000000000000808B, 0x0000000080000001,
            0x8000000080008081, 0x8000000000008009, 0x000000000000008A,
            0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
            0x000000008000808B, 0x800000000000008B, 0x8000000000008089,
            0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
            0x000000000000800A, 0x800000008000000A, 0x8000000080008081,
            0x8000000000008080, 0x0000000080000001, 0x8000000080000088,
        ]
        ROT = [
            [0,1,3,6,10,15,21,28,36,45,55,2,14,27,41,56],
            [1,3,6,10,15,21,28,36,45,55,2,14,27,41,56,8],
            [3,6,10,15,21,28,36,45,55,2,14,27,41,56,8,13],
            [6,10,15,21,28,36,45,55,2,14,27,41,56,8,13,16],
            [10,15,21,28,36,45,55,2,14,27,41,56,8,13,16,18],
            [15,21,28,36,45,55,2,14,27,41,56,8,13,16,18,23],
            [21,28,36,45,55,2,14,27,41,56,8,13,16,18,23,25],
            [28,36,45,55,2,14,27,41,56,8,13,16,18,23,25,39],
            [36,45,55,2,14,27,41,56,8,13,16,18,23,25,39,43],
            [45,55,2,14,27,41,56,8,13,16,18,23,25,39,43,54],
            [55,2,14,27,41,56,8,13,16,18,23,25,39,43,54,56],
            [2,14,27,41,56,8,13,16,18,23,25,39,43,54,56,9],
            [14,27,41,56,8,13,16,18,23,25,39,43,54,56,9,12],
        ]

        rate = 1088 // 64  # 17
        rate_bytes = 136
        lane = [0] * 25

        padded = bytearray(data)
        padded.append(0x01)
        while len(padded) % rate_bytes != 0:
            padded.append(0x00)
        padded[-1] |= 0x80

        for block_start in range(0, len(padded), rate_bytes):
            block = padded[block_start:block_start + rate_bytes]
            for i in range(rate):
                lane[i] ^= dec64(block[i*8:(i+1)*8])

            for rnd in range(ROUNDS):
                C = [0] * 5
                for x in range(5):
                    C[x] = lane[x] ^ lane[x+5] ^ lane[x+10] ^ lane[x+15] ^ lane[x+20]
                for x in range(5):
                    D = C[(x-1) % 5] ^ rot64(C[(x+1) % 5], 1)
                    for y in range(5):
                        lane[x + y*5] ^= D

                B = [0] * 25
                for x in range(5):
                    for y in range(5):
                        B[y + x*5] = rot64(lane[(0*x+1*y) % 5 + 5*((0*x+2*y) % 5)], ROT[x][y])

                for y in range(5):
                    for x in range(5):
                        lane[x + y*5] = B[x + y*5] ^ ((~B[(x+1)%5 + y*5]) & B[(x+2)%5 + y*5])

                lane[0] ^= RC[rnd]

        out = b''
        for i in range(rate):
            out += enc64(lane[i])
        return out[:32]

    # ── Ethereum prefix ──
    prefix = f"\x19Ethereum Signed Message:\n{len(message)}"
    full_message = prefix.encode('utf-8') + message.encode('utf-8')
    msg_hash = keccak256(full_message)

    # ── Parse signature (r,s,v) ──
    sig_str = signature_hex[2:] if signature_hex.startswith('0x') else signature_hex
    sig_bytes = bytes.fromhex(sig_str)
    if len(sig_bytes) != 65:
        return ''

    r = int.from_bytes(sig_bytes[:32], 'big')
    s = int.from_bytes(sig_bytes[32:64], 'big')
    v = sig_bytes[64]

    if v >= 27:
        v -= 27

    if s > N // 2:
        s = N - s

    # ── Recover public key via ecdsa ──
    from ecdsa import SECP256k1 as curve
    from ecdsa import VerifyingKey, InvalidSignatureError

    n = curve.order
    G = curve.generator

    z = int.from_bytes(msg_hash, 'big')
    r_inv = pow(r, n - 2, n)

    for j in range(2):
        x = r + j * n
        if x >= curve.curve.p():
            continue
        try:
            y_sq = (pow(x, 3, curve.curve.p()) + curve.curve.a() * x + curve.curve.b()) % curve.curve.p()
            y = pow(y_sq, (curve.curve.p() + 1) // 4, curve.curve.p())
            if y % 2 != (v % 2):
                y = curve.curve.p() - y
            from ecdsa.ellipticcurve import Point
            R = Point(curve.curve, x, y)
            u1 = (-(z * r_inv)) % n
            u2 = (s * r_inv) % n
            pub_point = u1 * G + u2 * R
            vk = VerifyingKey.from_public_key(pub_point, curve)
            # Verify
            if vk.verify_digest(sig_bytes[:64], msg_hash, sigdecode='binary'):
                # Derive Ethereum address
                pub_uncompressed = pub_point.to_bytes('uncompressed')[1:]
                addr_hash = keccak256(pub_uncompressed)
                return '0x' + addr_hash[-20:].hex()
        except Exception:
            continue

    return ''


def link_or_create_user(address: str) -> User:
    """Lie ou crée un user Django à partir d'une adresse Ethereum."""
    username = f'web3_{address[-8:]}'
    user = User.objects.filter(
        web3_sessions__address=address.lower(),
    ).first()
    if user:
        return user

    base_username = username
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f'{base_username}_{counter}'
        counter += 1

    user = User.objects.create_user(
        username=username,
        email=f'{address[-8:]}@web3.local',
        password=secrets.token_hex(16),
    )
    return user
