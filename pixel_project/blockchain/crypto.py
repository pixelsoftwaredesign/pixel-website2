"""
PixSoftMoney — ECDSA Cryptographic Module
Elliptic Curve Digital Signature Algorithm for wallet generation,
transaction signing, and signature verification.
"""
import hashlib
import json
import os
import base64
from datetime import datetime, timezone

from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError


def generate_private_key() -> str:
    sk = SigningKey.generate(curve=SECP256k1)
    return sk.to_string().hex()


def private_key_from_hex(hex_str: str) -> SigningKey:
    return SigningKey.from_string(bytes.fromhex(hex_str), curve=SECP256k1)


def public_key_from_private(sk: SigningKey) -> str:
    return sk.get_verifying_key().to_string().hex()


def address_from_public_key(pub_hex: str) -> str:
    sha = hashlib.sha256(bytes.fromhex(pub_hex)).hexdigest()
    ripemd = hashlib.new('ripemd160', bytes.fromhex(sha)).hexdigest()
    payload = '50' + ripemd
    checksum = hashlib.sha256(hashlib.sha256(bytes.fromhex(payload)).digest()).hexdigest()[:8]
    full = payload + checksum
    return base58_encode(bytes.fromhex(full))


def base58_encode(data: bytes) -> str:
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    n = int.from_bytes(data, 'big')
    result = ''
    while n > 0:
        n, r = divmod(n, 58)
        result = alphabet[r] + result
    for byte in data:
        if byte == 0:
            result = alphabet[0] + result
        else:
            break
    return result


def generate_wallet():
    sk_hex = generate_private_key()
    sk = private_key_from_hex(sk_hex)
    pub_hex = public_key_from_private(sk)
    addr = address_from_public_key(pub_hex)
    return {
        'private_key': sk_hex,
        'public_key': pub_hex,
        'address': addr,
    }


def sign_transaction(private_key_hex: str, transaction_data: dict) -> str:
    sk = private_key_from_hex(private_key_hex)
    message = json.dumps(transaction_data, sort_keys=True, default=str).encode()
    signature = sk.sign(message)
    return signature.hex()


def verify_signature(public_key_hex: str, signature_hex: str, transaction_data: dict) -> bool:
    try:
        vk = VerifyingKey.from_string(bytes.fromhex(public_key_hex), curve=SECP256k1)
        message = json.dumps(transaction_data, sort_keys=True, default=str).encode()
        return vk.verify(bytes.fromhex(signature_hex), message)
    except (BadSignatureError, ValueError):
        return False


def hash_block(block_data: dict) -> str:
    block_string = json.dumps(block_data, sort_keys=True, default=str).encode()
    return hashlib.sha256(block_string).hexdigest()


def merkle_root(transactions: list) -> str:
    if not transactions:
        return hashlib.sha256(b'').hexdigest()
    current_level = [
        hashlib.sha256(json.dumps(tx, sort_keys=True, default=str).encode()).hexdigest()
        for tx in transactions
    ]
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            combined = hashlib.sha256((left + right).encode()).hexdigest()
            next_level.append(combined)
        current_level = next_level
    return current_level[0]
