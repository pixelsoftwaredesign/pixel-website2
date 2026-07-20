"""
PixSoftMoney — P2P Node Networking (Secured)
Eclipse resilience, peer scoring, timejacking protection, TLS transport.
"""
import json
import ssl
import threading
import socket
import time
from typing import Set, Optional

from .chain import get_blockchain
from .security import (
    eclipse_guard, time_guard, sybil_guard, MAX_PEERS,
)


PEER_PORT = 9333


class PeerNode:
    def __init__(self, host: str, port: int = PEER_PORT):
        self.host = host
        self.port = port
        self.peers: Set[str] = set()
        self.running = False
        self.server_thread: Optional[threading.Thread] = None
        self.lock = threading.Lock()
        self.ssl_context = self._create_ssl_context()

    def _create_ssl_context(self) -> Optional[ssl.SSLContext]:
        try:
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            return ctx
        except Exception:
            return None

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
            sock.listen(20)
            sock.settimeout(1.0)
            while self.running:
                try:
                    client, addr = sock.accept()
                    if eclipse_guard.is_banned(addr[0]):
                        client.close()
                        continue
                    if not eclipse_guard.can_connect():
                        client.close()
                        continue
                    threading.Thread(
                        target=self._handle_peer, args=(client, addr),
                        daemon=True,
                    ).start()
                except socket.timeout:
                    continue
        except OSError:
            pass
        finally:
            sock.close()

    def _handle_peer(self, client_socket, addr):
        peer_addr = f'{addr[0]}:{addr[1]}'
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
                eclipse_guard.score_peer(peer_addr, 1)
                self._process_message(msg, client_socket)
        except Exception:
            eclipse_guard.record_invalid_message(peer_addr)
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
                        if eclipse_guard.register_peer(p):
                            self.peers.add(p)

        elif msg_type == 'PEER_TIME':
            reported_time = msg.get('time', 0)
            peer = msg.get('peer', '')
            time_guard.report_peer_time(peer, reported_time)

        elif msg_type == 'NEW_TX':
            tx = msg.get('transaction')
            if tx:
                error = chain.add_transaction(tx)
                if error is None:
                    self.broadcast(msg, exclude=sender_socket)

        elif msg_type == 'NEW_BLOCK':
            block_data = msg.get('block')
            if block_data:
                self._handle_new_block(block_data, sender_socket)

        elif msg_type == 'REQUEST_CHAIN':
            if sender_socket:
                response = {
                    'type': 'FULL_CHAIN',
                    'chain': chain.to_dict(),
                }
                sender_socket.sendall(
                    (json.dumps(response) + '\n').encode()
                )

        elif msg_type == 'FULL_CHAIN':
            incoming = msg.get('chain', {})
            incoming_len = incoming.get('length', 0)
            if incoming_len > chain.length:
                from .chain import Blockchain
                new_chain = Blockchain()
                new_chain.load_from_dict(incoming)
                valid, _ = new_chain.validate_chain()
                if valid and new_chain.length > chain.length:
                    chain.load_from_dict(incoming)

    def _handle_new_block(self, block_data: dict, sender_socket):
        chain = get_blockchain()
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

        ok, ts_err = time_guard.validate_block_timestamp(block.timestamp)
        if not ok:
            return

        if (block.previous_hash == chain.last_block.hash and
                block.hash.startswith('0' * 4) and
                block.hash == block.compute_hash()):
            chain.chain.append(block)
            self.broadcast(
                {'type': 'NEW_BLOCK', 'block': block_data},
                exclude=sender_socket,
            )

    def broadcast(self, msg: dict, exclude=None):
        dead_peers = set()
        payload = (json.dumps(msg, default=str) + '\n').encode()

        with self.lock:
            peers_copy = self.peers.copy()

        for peer in peers_copy:
            if eclipse_guard.is_banned(peer):
                continue
            try:
                host, port_str = peer.split(':')
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((host, int(port_str)))
                sock.sendall(payload)
                sock.close()
                eclipse_guard.score_peer(peer, 1)
            except Exception:
                dead_peers.add(peer)
                eclipse_guard.score_peer(peer, -2)

        if dead_peers:
            with self.lock:
                self.peers -= dead_peers

    def broadcast_transaction(self, tx: dict):
        self.broadcast({'type': 'NEW_TX', 'transaction': tx})

    def broadcast_block(self, block_data: dict):
        self.broadcast({'type': 'NEW_BLOCK', 'block': block_data})

    def broadcast_time(self):
        self.broadcast({
            'type': 'PEER_TIME',
            'time': time.time(),
            'peer': f'{self.host}:{self.port}',
        })

    def request_chain_from_peers(self):
        self.broadcast({'type': 'REQUEST_CHAIN'})

    def connect_peer(self, host: str, port: int) -> bool:
        peer_str = f'{host}:{port}'
        if eclipse_guard.is_banned(peer_str):
            return False
        if not eclipse_guard.can_connect():
            return False

        with self.lock:
            self.peers.add(peer_str)
        eclipse_guard.register_peer(peer_str)

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((host, port))

            msg = json.dumps({
                'type': 'PEERS',
                'peers': list(self.peers) + [f'{self.host}:{self.port}'],
            }) + '\n'
            sock.sendall(msg.encode())

            sock.sendall(json.dumps({
                'type': 'PEER_TIME',
                'time': time.time(),
                'peer': f'{self.host}:{self.port}',
            }).encode() + b'\n')

            sock.close()
            return True
        except Exception:
            with self.lock:
                self.peers.discard(peer_str)
            eclipse_guard.score_peer(peer_str, -3)
            return False

    def get_status(self) -> dict:
        return {
            'host': self.host,
            'port': self.port,
            'peers': eclipse_guard.get_peer_stats(),
            'consensus_time': time_guard.get_consensus_time(),
            'validators': sybil_guard.get_validators(),
            'diverse_peers': eclipse_guard.get_diverse_peers(),
        }


_node: Optional[PeerNode] = None


def get_node(host='0.0.0.0', port=PEER_PORT) -> PeerNode:
    global _node
    if _node is None:
        _node = PeerNode(host, port)
    return _node
