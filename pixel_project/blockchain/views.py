import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .chain import get_blockchain, MINING_REWARD
from .crypto import generate_wallet, sign_transaction, verify_signature
from .p2p import get_node
from .models import CryptoWallet, CryptoTransaction, MiningStats


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
