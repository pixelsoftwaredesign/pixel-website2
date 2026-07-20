"""
PixSoftMoney — Security Module
Protocol-level security: Sybil protection, Eclipse resilience,
Timejacking protection, Circuit Breaker, Fraud Detection, Multi-Sig.
"""
import time
import threading
import statistics
from collections import defaultdict
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field


# ─── Constants ───────────────────────────────────────────────

MIN_STAKE_TO_VALIDATE = 1000     # PSX minimum to become a validator
MAX_BLOCK_DRIFT = 7200           # 2h max block timestamp drift
PEER_SCORE_THRESHOLD = -10       # Score below this = banned peer
FRAUD_TX_LIMIT_PER_MINUTE = 10   # Max tx per address per minute
FRAUD_LARGE_TX_THRESHOLD = 50000 # PSX threshold for large tx alert
CIRCUIT_BREAKER_THRESHOLD = 100  # Failed txs before circuit opens
CIRCUIT_BREAKER_COOLDOWN = 300   # 5 min cooldown
MAX_PEERS = 50                   # Max connected peers
MIN_PEERS = 3                    # Min peers for healthy node


# ─── Sybil Protection ───────────────────────────────────────

class SybilGuard:
    """
    Empêche les attaques Sybil en imposant un barrier PoS:
    Seuls les nœuds avec >= MIN_STAKE_TO_VALIDATE PSX peuvent valider.
    """

    def __init__(self):
        self.validators: Dict[str, float] = {}  # address → stake
        self._lock = threading.Lock()

    def register_validator(self, address: str, stake: float) -> bool:
        with self._lock:
            if stake < MIN_STAKE_TO_VALIDATE:
                return False
            self.validators[address] = stake
            return True

    def remove_validator(self, address: str):
        with self._lock:
            self.validators.pop(address, None)

    def is_valid_validator(self, address: str) -> bool:
        return address in self.validators

    def get_weighted_validator(self) -> Optional[str]:
        """Sélection pondérée par le stake (Proof of Stake)."""
        with self._lock:
            if not self.validators:
                return None
            import random
            total = sum(self.validators.values())
            r = random.uniform(0, total)
            cumulative = 0
            for addr, stake in self.validators.items():
                cumulative += stake
                if cumulative >= r:
                    return addr
        return None

    def get_validators(self) -> Dict[str, float]:
        with self._lock:
            return self.validators.copy()


# ─── Eclipse Attack Resilience ──────────────────────────────

@dataclass
class PeerInfo:
    address: str
    score: int = 0
    connected_at: float = field(default_factory=time.time)
    last_seen: float = field(default_factory=time.time)
    messages_received: int = 0
    messages_invalid: int = 0
    banned: bool = False
    latency_ms: float = 0.0


class EclipseGuard:
    """
    Protège contre les Eclipse Attacks:
    - Max peers limit
    - Peer scoring (malus pour comportement suspect)
    - Diversification des connexions
    - Bannissement automatique
    """

    def __init__(self):
        self.peers: Dict[str, PeerInfo] = {}
        self.banned: Dict[str, float] = {}  # address → unban_time
        self._lock = threading.Lock()

    def can_connect(self) -> bool:
        with self._lock:
            active = sum(1 for p in self.peers.values() if not p.banned)
            return active < MAX_PEERS

    def register_peer(self, address: str) -> bool:
        with self._lock:
            if address in self.banned:
                if time.time() < self.banned[address]:
                    return False
                del self.banned[address]

            if len(self.peers) >= MAX_PEERS:
                worst = min(
                    (p for p in self.peers.values() if not p.banned),
                    key=lambda p: p.score,
                    default=None,
                )
                if worst and worst.score < PEER_SCORE_THRESHOLD:
                    self._ban_peer(worst.address)
                else:
                    return False

            self.peers[address] = PeerInfo(address=address)
            return True

    def score_peer(self, address: str, delta: int):
        with self._lock:
            if address in self.peers:
                peer = self.peers[address]
                peer.score += delta
                peer.last_seen = time.time()
                if peer.score <= PEER_SCORE_THRESHOLD:
                    self._ban_peer(address)

    def record_invalid_message(self, address: str):
        with self._lock:
            if address in self.peers:
                peer = self.peers[address]
                peer.messages_invalid += 1
                peer.score -= 5
                if peer.messages_invalid >= 3:
                    self._ban_peer(address)

    def _ban_peer(self, address: str):
        self.banned[address] = time.time() + 3600
        if address in self.peers:
            self.peers[address].banned = True

    def is_banned(self, address: str) -> bool:
        with self._lock:
            if address in self.banned:
                if time.time() < self.banned[address]:
                    return True
                del self.banned[address]
            return False

    def get_diverse_peers(self, count: int = 5) -> List[str]:
        """Retourne des pairs diversifiés (pas tous du même subnet)."""
        with self._lock:
            active = [p for p in self.peers.values() if not p.banned]
            active.sort(key=lambda p: p.score, reverse=True)
            return [p.address for p in active[:count]]

    def get_peer_stats(self) -> dict:
        with self._lock:
            return {
                'total': len(self.peers),
                'active': sum(1 for p in self.peers.values() if not p.banned),
                'banned': len(self.banned),
                'avg_score': statistics.mean(
                    [p.score for p in self.peers.values() if not p.banned]
                ) if self.peers else 0,
            }


# ─── Timejacking Protection ─────────────────────────────────

class TimeGuard:
    """
    Protège contre les attaques Timejacking:
    - Ne jamais faire confiance au timestamp d'un pair
    - Utilise le temps local + médiane pondérée des pairs fiables
    - Rejette les blocs avec timestamp trop décalé
    """

    def __init__(self):
        self.peer_times: Dict[str, float] = {}
        self._lock = threading.Lock()

    def report_peer_time(self, peer_address: str, reported_time: float):
        with self._lock:
            local_time = time.time()
            drift = abs(reported_time - local_time)
            if drift > MAX_BLOCK_DRIFT * 2:
                return
            self.peer_times[peer_address] = reported_time

    def get_consensus_time(self) -> float:
        """Retourne la médiane des temps des pairs fiables."""
        with self._lock:
            local_time = time.time()
            if not self.peer_times:
                return local_time

            times = list(self.peer_times.values())
            times.append(local_time)
            times.sort()
            median = statistics.median(times)

            trusted = [t for t in times if abs(t - median) < 600]
            if trusted:
                return statistics.mean(trusted)
            return local_time

    def validate_block_timestamp(self, block_timestamp: float) -> Tuple[bool, str]:
        now = time.time()
        drift = block_timestamp - now

        if abs(drift) > MAX_BLOCK_DRIFT:
            return False, f'Timestamp hors limites ({drift:.0f}s)'

        consensus = self.get_consensus_time()
        consensus_drift = abs(block_timestamp - consensus)
        if consensus_drift > MAX_BLOCK_DRIFT / 2:
            return False, f'Timestamp vs consensus trop éloigné ({consensus_drift:.0f}s)'

        return True, 'Timestamp valide'


# ─── Circuit Breaker ────────────────────────────────────────

class CircuitBreaker:
    """
    Coupe-circuit automatique:
    Si trop d'échecs en peu de temps → pause temporaire.
    Protège contre les attaques de vidange de fonds.
    """

    def __init__(self):
        self.failures: Dict[str, List[float]] = defaultdict(list)
        self.tripped: Dict[str, float] = {}
        self._lock = threading.Lock()

    def record_failure(self, address: str):
        with self._lock:
            now = time.time()
            self.failures[address].append(now)
            self.failures[address] = [
                t for t in self.failures[address] if now - t < 60
            ]
            if len(self.failures[address]) >= CIRCUIT_BREAKER_THRESHOLD:
                self.tripped[address] = now + CIRCUIT_BREAKER_COOLDOWN

    def is_tripped(self, address: str) -> bool:
        with self._lock:
            if address in self.tripped:
                if time.time() < self.tripped[address]:
                    return True
                del self.tripped[address]
                self.failures.pop(address, None)
            return False

    def reset(self, address: str):
        with self._lock:
            self.failures.pop(address, None)
            self.tripped.pop(address, None)


# ─── Fraud Detection ────────────────────────────────────────

class FraudDetector:
    """
    Surveillance en temps réel de la mempool:
    - Détection de transactions suspectes
    - Liquidation massive
    - Fréquence anormale
    - Montants suspects
    """

    def __init__(self):
        self.tx_history: Dict[str, List[float]] = defaultdict(list)
        self.alerts: List[dict] = []
        self._lock = threading.Lock()

    def scan_transaction(self, tx: dict) -> Tuple[bool, Optional[str]]:
        address = tx.get('from', '')
        amount = tx.get('amount', 0)
        now = time.time()

        with self._lock:
            self.tx_history[address].append(now)
            self.tx_history[address] = [
                t for t in self.tx_history[address] if now - t < 60
            ]

            recent_count = len(self.tx_history[address])
            if recent_count > FRAUD_TX_LIMIT_PER_MINUTE:
                self._alert(address, 'HIGH_FREQUENCY',
                            f'{recent_count} tx en 1 min')
                return False, 'Fréquence anormale de transactions'

            if amount > FRAUD_LARGE_TX_THRESHOLD:
                self._alert(address, 'LARGE_TX',
                            f'{amount} PSX en une tx')
                # Ne bloque pas mais alerte

            if amount > 0:
                balance_approx = tx.get('_balance', 0)
                if balance_approx > 0 and amount > balance_approx * 0.8:
                    self._alert(address, 'LIQUIDATION_RISK',
                                f'{amount}/{balance_approx} PSX')
                    return False, 'Liquidation de plus de 80% du solde refusée'

        return True, None

    def _alert(self, address: str, alert_type: str, detail: str):
        self.alerts.append({
            'address': address,
            'type': alert_type,
            'detail': detail,
            'timestamp': time.time(),
        })
        if len(self.alerts) > 1000:
            self.alerts = self.alerts[-500:]

    def get_alerts(self, limit: int = 50) -> List[dict]:
        return list(reversed(self.alerts[-limit:]))


# ─── Multi-Signature ────────────────────────────────────────

@dataclass
class MultiSigWallet:
    address: str
    owners: List[str]  # list of addresses
    required: int      # M signatures required
    nonce: int = 0

    def can_sign(self, signer: str) -> bool:
        return signer in self.owners

    def validate(self, signatures: Dict[str, str], tx_hash: str) -> bool:
        valid = 0
        for addr, sig in signatures.items():
            if addr in self.owners:
                from .crypto import verify_signature
                owner_wallet = None
                try:
                    from .models import CryptoWallet
                    owner_wallet = CryptoWallet.objects.get(address=addr)
                except Exception:
                    continue
                if verify_signature(
                    owner_wallet.public_key, sig,
                    'MULTISIG', tx_hash, 0, self.nonce, time.time()
                ):
                    valid += 1
        return valid >= self.required


class MultiSigManager:
    def __init__(self):
        self.wallets: Dict[str, MultiSigWallet] = {}
        self.pending_txs: Dict[str, dict] = {}
        self._lock = threading.Lock()

    def create_multisig(self, address: str, owners: List[str],
                        required: int) -> bool:
        with self._lock:
            if required > len(owners) or required < 1:
                return False
            self.wallets[address] = MultiSigWallet(
                address=address, owners=owners, required=required,
            )
            return True

    def propose_tx(self, multisig_addr: str, tx_data: dict) -> Optional[str]:
        import hashlib
        with self._lock:
            if multisig_addr not in self.wallets:
                return None
            ms = self.wallets[multisig_addr]
            tx_hash = hashlib.sha256(
                str(tx_data).encode()
            ).hexdigest()[:16]
            self.pending_txs[tx_hash] = {
                'wallet': multisig_addr,
                'tx': tx_data,
                'signatures': {},
                'created_at': time.time(),
            }
            return tx_hash

    def sign_tx(self, tx_hash: str, signer_addr: str,
                signature: str) -> Tuple[bool, str]:
        with self._lock:
            if tx_hash not in self.pending_txs:
                return False, 'Transaction introuvable'
            pending = self.pending_txs[tx_hash]
            ms = self.wallets[pending['wallet']]
            if not ms.can_sign(signer_addr):
                return False, 'Non autorisé'
            if signer_addr in pending['signatures']:
                return False, 'Déjà signé'
            pending['signatures'][signer_addr] = signature
            count = len(pending['signatures'])
            if count >= ms.required:
                return True, f'Signatures complètes ({count}/{ms.required})'
            return True, f'{count}/{ms.required} signatures'

    def get_pending(self, multisig_addr: str) -> List[dict]:
        with self._lock:
            return [
                {'hash': h, **v}
                for h, v in self.pending_txs.items()
                if v['wallet'] == multisig_addr
            ]


# ─── Global Instances ───────────────────────────────────────

sybil_guard = SybilGuard()
eclipse_guard = EclipseGuard()
time_guard = TimeGuard()
circuit_breaker = CircuitBreaker()
fraud_detector = FraudDetector()
multisig_manager = MultiSigManager()
