import uuid
from django.db import models
from django.contrib.auth.models import User


class ChainState(models.Model):
    data = models.JSONField(default=dict)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "État de la blockchain"
        verbose_name_plural = "États de la blockchain"


class CryptoWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='crypto_wallet')
    address = models.CharField(max_length=64, unique=True)
    public_key = models.CharField(max_length=130)
    private_key_encrypted = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Wallet Crypto"
        verbose_name_plural = "Wallets Crypto"

    def __str__(self):
        return f"{self.user.username} → {self.address[:16]}..."


class CryptoTransaction(models.Model):
    tx_id = models.CharField(max_length=64, unique=True, default=uuid.uuid4)
    from_address = models.CharField(max_length=64)
    to_address = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    fee = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    signature = models.TextField(blank=True, default='')
    public_key = models.CharField(max_length=130, blank=True, default='')
    status = models.CharField(max_length=20, choices=[
        ('pending', 'En attente'),
        ('confirmed', 'Confirmé'),
        ('failed', 'Échoué'),
    ], default='pending')
    block_index = models.IntegerField(null=True, blank=True)
    block_hash = models.CharField(max_length=64, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Transaction Crypto"
        verbose_name_plural = "Transactions Crypto"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.from_address[:12]}... → {self.to_address[:12]}... ({self.amount} PSX)"


class MiningStats(models.Model):
    total_blocks = models.IntegerField(default=0)
    total_mined = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=4)
    hashrate = models.FloatField(default=0.0)
    last_block_time = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Stats Mining"
        verbose_name_plural = "Stats Mining"
