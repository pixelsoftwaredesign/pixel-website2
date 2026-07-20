"""
PixSoftMoney — Blockchain Core Engine
Proof-of-Work blockchain with block validation, mining, and chain integrity.
Balance model: Sum(received) - Sum(sent) per address (account-based).
"""
import time
import json
import threading
from dataclasses import dataclass
from typing import List, Optional
from collections import defaultdict

from .crypto import hash_block, merkle_root, verify_signature


DIFFICULTY = 4
MINING_REWARD = 50.0
BLOCK_MAX_TX = 100

_lock = threading.Lock()


@dataclass
class Block:
    index: int
    timestamp: float
    transactions: list
    previous_hash: str
    nonce: int = 0
    merkle: str = ''
    hash: str = ''

    def compute_hash(self) -> str:
        block_data = {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'merkle': self.merkle,
        }
        return hash_block(block_data)

    def compute_merkle(self):
        self.merkle = merkle_root(self.transactions)

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'merkle': self.merkle,
            'hash': self.hash,
        }


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[dict] = []
        self._lock = threading.Lock()

    def create_genesis_block(self):
        genesis = Block(
            index=0,
            timestamp=time.time(),
            transactions=[{
                'type': 'genesis',
                'to': 'PXSGENESIS000000000000000000000000000',
                'amount': 21000000.0,
                'from': 'SYSTEM',
                'timestamp': time.time(),
            }],
            previous_hash='0' * 64,
        )
        genesis.compute_merkle()
        genesis.hash = genesis.compute_hash()
        self.chain.append(genesis)
        return genesis

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    @property
    def length(self) -> int:
        return len(self.chain)

    def add_transaction(self, tx: dict) -> Optional[str]:
        with self._lock:
            if not tx.get('from') or not tx.get('to') or not tx.get('amount'):
                return 'Transaction incomplète'

            if tx['from'] != 'COINBASE':
                if tx.get('signature') and tx.get('public_key'):
                    verify_data = {k: v for k, v in tx.items() if k not in ('signature',)}
                    if not verify_signature(tx['public_key'], tx['signature'], verify_data):
                        return 'Signature invalide'

                sender_balance = self.get_balance(tx['from'])
                if sender_balance < tx['amount']:
                    return f'Solde insuffisant ({sender_balance} < {tx["amount"]})'

            if len(self.pending_transactions) >= BLOCK_MAX_TX:
                return 'Pool de transactions plein'

            self.pending_transactions.append(tx)
            return None

    def mine_pending(self, miner_address: str) -> Optional[Block]:
        with self._lock:
            if not self.pending_transactions:
                return None

            coinbase = {
                'type': 'coinbase',
                'from': 'COINBASE',
                'to': miner_address,
                'amount': MINING_REWARD,
                'timestamp': time.time(),
            }

            txs = [coinbase] + self.pending_transactions[:BLOCK_MAX_TX]

            block = Block(
                index=self.last_block.index + 1,
                timestamp=time.time(),
                transactions=txs,
                previous_hash=self.last_block.hash,
            )
            block.compute_merkle()

            target = '0' * DIFFICULTY
            while True:
                block.hash = block.compute_hash()
                if block.hash.startswith(target):
                    break
                block.nonce += 1

            self.chain.append(block)
            self.pending_transactions = self.pending_transactions[BLOCK_MAX_TX:]
            return block

    def get_balance(self, address: str) -> float:
        """Balance = Sum(received) - Sum(sent). O((n)) scan."""
        received = 0.0
        sent = 0.0
        for block in self.chain:
            for tx in block.transactions:
                if tx.get('to') == address:
                    received += tx.get('amount', 0)
                if tx.get('from') == address:
                    sent += tx.get('amount', 0)
        return round(received - sent, 8)

    def get_all_balances(self) -> dict:
        """Recalculer tous les comptes: Sum(received) - Sum(sent)."""
        balances = defaultdict(float)
        for block in self.chain:
            for tx in block.transactions:
                to_addr = tx.get('to', '')
                from_addr = tx.get('from', '')
                amount = tx.get('amount', 0)
                if to_addr:
                    balances[to_addr] += amount
                if from_addr and from_addr not in ('SYSTEM', 'COINBASE', 'BRIDGE_TND'):
                    balances[from_addr] -= amount
        return dict(balances)

    def validate_chain(self) -> tuple:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False, f'Hash invalide au bloc {i}'
            if current.previous_hash != previous.hash:
                return False, f'previous_hash cassé au bloc {i}'
            if not current.hash.startswith('0' * DIFFICULTY):
                return False, f'Preuve de travail invalide au bloc {i}'

        balances = self.get_all_balances()
        for addr, bal in balances.items():
            if bal < 0:
                return False, f'Solde négatif détecté pour {addr}: {bal}'

        return True, 'Chaîne valide'

    def get_history(self, address: str, limit=50) -> list:
        history = []
        for block in reversed(self.chain):
            for tx in block.transactions:
                if tx.get('from') == address or tx.get('to') == address:
                    history.append({
                        'block': block.index,
                        'hash': block.hash,
                        'timestamp': tx.get('timestamp', block.timestamp),
                        'from': tx.get('from', ''),
                        'to': tx.get('to', ''),
                        'amount': tx.get('amount', 0),
                        'type': tx.get('type', 'transfer'),
                    })
                    if len(history) >= limit:
                        return history
        return history

    def to_dict(self):
        return {
            'length': self.length,
            'difficulty': DIFFICULTY,
            'mining_reward': MINING_REWARD,
            'pending': len(self.pending_transactions),
            'chain': [b.to_dict() for b in self.chain],
        }

    def load_from_dict(self, data: dict):
        self.chain = []
        for bd in data.get('chain', []):
            block = Block(
                index=bd['index'],
                timestamp=bd['timestamp'],
                transactions=bd['transactions'],
                previous_hash=bd['previous_hash'],
                nonce=bd.get('nonce', 0),
                merkle=bd.get('merkle', ''),
            )
            block.hash = bd.get('hash', block.compute_hash())
            self.chain.append(block)


_instance = None


def get_blockchain() -> Blockchain:
    global _instance
    if _instance is None:
        _instance = Blockchain()
        _instance.create_genesis_block()
    return _instance
