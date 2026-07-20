import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


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


class Proposal(models.Model):
    CATEGORY_CHOICES = [
        ('feature', 'Fonctionnalité'),
        ('fee', 'Frais'),
        ('upgrade', 'Mise à jour'),
        ('community', 'Communauté'),
    ]
    STATUS_CHOICES = [
        ('active', 'En cours'),
        ('passed', 'Adopté'),
        ('rejected', 'Rejeté'),
        ('expired', 'Expiré'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proposals')
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='feature')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    votes_for = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    votes_against = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField()
    executed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} [{self.status}]"


class Vote(models.Model):
    VOTE_CHOICES = [('for', 'Pour'), ('against', 'Contre')]
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name='votes')
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    choice = models.CharField(max_length=10, choices=VOTE_CHOICES)
    weight = models.DecimalField(max_digits=20, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('proposal', 'voter')


class Stake(models.Model):
    LOCK_CHOICES = [
        (30, '30 jours'),
        (90, '90 jours'),
        (180, '6 mois'),
        (365, '12 mois'),
    ]
    STATUS_CHOICES = [
        ('active', 'Actif'),
        ('completed', 'Terminé'),
        ('cancelled', 'Annulé'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stakes')
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    apy = models.DecimalField(max_digits=5, decimal_places=2)
    lock_days = models.IntegerField(choices=LOCK_CHOICES)
    earned = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    staked_at = models.DateTimeField(auto_now_add=True)
    unlocks_at = models.DateTimeField()
    last_claim = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-staked_at']

    def __str__(self):
        return f"{self.user.username} staked {self.amount} PSX ({self.apy}%)"


class RewardLog(models.Model):
    REASON_CHOICES = [
        ('referral', 'Parrainage'),
        ('daily_login', 'Connexion quotidienne'),
        ('first_tx', 'Première transaction'),
        ('monthly_active', 'Utilisateur actif'),
        ('milestone', 'Palier atteint'),
        ('staking', 'Récompense staking'),
        ('mining', 'Récompense minage'),
        ('bonus', 'Bonus'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reward_logs')
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class PremiumAccess(models.Model):
    PLAN_CHOICES = [
        ('monthly', 'Mensuel'),
        ('yearly', 'Annuel'),
        ('lifetime', 'À vie'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='premium')
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    activated_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    psx_paid = models.DecimalField(max_digits=20, decimal_places=8)

    @property
    def is_active(self):
        return timezone.now() < self.expires_at

    def __str__(self):
        return f"{self.user.username} — Premium {self.plan} ({'actif' if self.is_active else 'expiré'})"


class DailyLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_logins')
    date = models.DateField()
    bonus_claimed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'date')
