"""
PixSoftMoney — P2P Node Networking
Simple peer-to-peer gossip protocol for block and transaction propagation.
"""
import json
import threading
import socket
import time
from typing import Set, Dict, Optional

from .chain import get_blockchain, Blockchain


PEER_PORT = 9333
NODE_ID = None


class PeerNode:
    def __init__(self, host: str, port: int = PEER_PORT):
        self.host = host
        self.port = port
        self.peers: Set[str] = set()
        self.running = False
        self.server_thread: Optional[threading.Thread] = None
        self.lock = threading.Lock()

    def start(self):
        self.running = True
        self.server_thread = threading.Thread(target=self._listen, daemon=True)
        self.server_thread.start()

    def stop(self):
        self.running = False

    def _listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind(('0.0.0.0', self.port))
            sock.listen(5)
            sock.settimeout(1.0)
            while self.running:
                try:
                    client, addr = sock.accept()
                    threading.Thread(
                        target=self._handle_peer, args=(client, addr),
                        daemon=True
                    ).start()
                except socket.timeout:
                    continue
        except OSError:
            pass
        finally:
            sock.close()

    def _handle_peer(self, client_socket, addr):
        try:
            data = b''
            while True:
                chunk = client_socket.recv(65536)
                if not chunk:
                    break
                data += chunk
                if b'\n' in data:
                    break

            if data:
                msg = json.loads(data.decode().strip())
                self._process_message(msg, client_socket)
        except Exception:
            pass
        finally:
            client_socket.close()

    def _process_message(self, msg: dict, sender_socket=None):
        msg_type = msg.get('type')
        chain = get_blockchain()

        if msg_type == 'PEERS':
            new_peers = msg.get('peers', [])
            with self.lock:
                for p in new_peers:
                    if p != f'{self.host}:{self.port}':
                        self.peers.add(p)

        elif msg_type == 'NEW_TX':
            tx = msg.get('transaction')
            if tx:
                error = chain.add_transaction(tx)
                if error is None:
                    self.broadcast(msg, exclude=sender_socket)

        elif msg_type == 'NEW_BLOCK':
            block_data = msg.get('block')
            if block_data:
                from .chain import Block
                block = Block(
                    index=block_data['index'],
                    timestamp=block_data['timestamp'],
                    transactions=block_data['transactions'],
                    previous_hash=block_data['previous_hash'],
                    nonce=block_data.get('nonce', 0),
                    merkle=block_data.get('merkle', ''),
                )
                block.hash = block_data.get('hash', block.compute_hash())

                if (block.previous_hash == chain.last_block.hash and
                        block.hash.startswith('0' * 4) and
                        block.hash == block.compute_hash()):
                    chain.chain.append(block)
                    chain._apply_block(block)
                    self.broadcast(msg, exclude=sender_socket)

        elif msg_type == 'REQUEST_CHAIN':
            if sender_socket:
                response = {
                    'type': 'FULL_CHAIN',
                    'chain': chain.to_dict(),
                }
                sender_socket.sendall((json.dumps(response) + '\n').encode())

        elif msg_type == 'FULL_CHAIN':
            incoming = msg.get('chain', {})
            incoming_len = incoming.get('length', 0)
            if incoming_len > chain.length:
                valid, err = chain.validate_chain()
                if valid or incoming_len > chain.length:
                    from .chain import Blockchain
                    new_chain = Blockchain()
                    new_chain.load_from_dict(incoming)
                    valid2, _ = new_chain.validate_chain()
                    if valid2:
                        chain.load_from_dict(incoming)

    def broadcast(self, msg: dict, exclude=None):
        dead_peers = set()
        payload = (json.dumps(msg, default=str) + '\n').encode()

        with self.lock:
            peers_copy = self.peers.copy()

        for peer in peers_copy:
            if exclude and peer == getattr(exclude, 'getpeername', lambda: ('', 0))()[0]:
                continue
            try:
                host, port = peer.split(':')
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((host, int(port)))
                sock.sendall(payload)
                sock.close()
            except Exception:
                dead_peers.add(peer)

        if dead_peers:
            with self.lock:
                self.peers -= dead_peers

    def broadcast_transaction(self, tx: dict):
        self.broadcast({'type': 'NEW_TX', 'transaction': tx})

    def broadcast_block(self, block_data: dict):
        self.broadcast({'type': 'NEW_BLOCK', 'block': block_data})

    def request_chain_from_peers(self):
        self.broadcast({'type': 'REQUEST_CHAIN'})

    def connect_peer(self, host: str, port: int):
        peer_str = f'{host}:{port}'
        with self.lock:
            self.peers.add(peer_str)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((host, port))
            msg = json.dumps({
                'type': 'PEERS',
                'peers': list(self.peers) + [f'{self.host}:{self.port}'],
            }) + '\n'
            sock.sendall(msg.encode())
            sock.close()
            return True
        except Exception:
            with self.lock:
                self.peers.discard(peer_str)
            return False


_node: Optional[PeerNode] = None


def get_node(host='0.0.0.0', port=PEER_PORT) -> PeerNode:
    global _node
    if _node is None:
        _node = PeerNode(host, port)
    return _node
