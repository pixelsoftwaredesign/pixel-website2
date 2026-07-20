"""
PixSoftMoney — Blockchain Core Engine
Proof-of-Work blockchain with block validation, mining, and chain integrity.
"""
import time
import json
from dataclasses import dataclass, field, asdict
from typing import List, Optional

from .crypto import hash_block, merkle_root, verify_signature


DIFFICULTY = 4
MINING_REWARD = 50.0
BLOCK_MAX_TX = 100


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
        self.balances: dict = {}
        self.utxos: dict = {}
        self.miners: set = set()

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
        self.balances['PXSGENESIS000000000000000000000000000'] = 21000000.0
        return genesis

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    @property
    def length(self) -> int:
        return len(self.chain)

    def add_transaction(self, tx: dict) -> Optional[str]:
        if not tx.get('from') or not tx.get('to') or not tx.get('amount'):
            return 'Transaction incomplète'

        if tx['from'] != 'COINBASE':
            if tx.get('signature') and tx.get('public_key'):
                verify_data = {k: v for k, v in tx.items() if k not in ('signature',)}
                if not verify_signature(tx['public_key'], tx['signature'], verify_data):
                    return 'Signature invalide'

            sender_balance = self.balances.get(tx['from'], 0)
            if sender_balance < tx['amount']:
                return f'Solde insuffisant ({sender_balance} < {tx["amount"]})'

        if len(self.pending_transactions) >= BLOCK_MAX_TX:
            return 'Pool de transactions plein'

        self.pending_transactions.append(tx)
        return None

    def mine_pending(self, miner_address: str) -> Optional[Block]:
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

        self._apply_block(block)
        self.chain.append(block)
        self.pending_transactions = self.pending_transactions[BLOCK_MAX_TX:]
        return block

    def _apply_block(self, block: Block):
        for tx in block.transactions:
            sender = tx.get('from', '')
            receiver = tx.get('to', '')
            amount = tx.get('amount', 0)

            if sender and sender != 'COINBASE' and sender != 'SYSTEM':
                self.balances[sender] = self.balances.get(sender, 0) - amount

            if receiver:
                self.balances[receiver] = self.balances.get(receiver, 0) + amount

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

        return True, 'Chaîne valide'

    def recalculate_balances(self):
        self.balances = {}
        for block in self.chain:
            self._apply_block(block)

    def get_balance(self, address: str) -> float:
        return self.balances.get(address, 0.0)

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
        self.recalculate_balances()


_instance = None


def get_blockchain() -> Blockchain:
    global _instance
    if _instance is None:
        _instance = Blockchain()
        _instance.create_genesis_block()
    return _instance
