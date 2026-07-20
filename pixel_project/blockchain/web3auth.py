"""
PixSoftMoney — Web3 Authentication
Sign-In with Wallet: nonce challenge + ECDSA signature verification.
Supporte MetaMask (EVM) et tout wallet ECDSA.
"""
import hashlib
import time
import secrets
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


DOMAIN = 'pixelsoftwaredesign.xyz'
CHAIN_ID = 1  # Mainnet Ethereum (ou 31337 pour local)


def get_sign_message(address: str, nonce: str) -> str:
    """Message EIP-4361 (Sign-In with Ethereum) simplifié."""
    return (
        f"{DOMAIN} wants you to sign in with your Ethereum account:\n"
        f"{address}\n"
        f"\n"
        f"Sign in to PixSoftMoney\n"
        f"\n"
        f"Nonce: {nonce}\n"
        f"Chain ID: {CHAIN_ID}\n"
        f"Issued at: {timezone.now().isoformat()}"
    )


class Web3Nonce(models.Model):
    address = models.CharField(max_length=42, db_index=True)
    nonce = models.CharField(max_length=64, unique=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    @classmethod
    def create_for_address(cls, address: str) -> 'Web3Nonce':
        nonce = secrets.token_hex(32)
        message = get_sign_message(address, nonce)
        return cls.objects.create(
            address=address.lower(),
            nonce=nonce,
            message=message,
        )

    @property
    def is_valid(self) -> bool:
        return not self.used and (timezone.now() - self.created_at).total_seconds() < 300


class Web3Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='web3_sessions')
    address = models.CharField(max_length=42, db_index=True)
    session_token = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    @property
    def is_active(self) -> bool:
        return timezone.now() < self.expires_at
