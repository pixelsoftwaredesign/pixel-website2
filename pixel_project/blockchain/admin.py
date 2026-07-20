from django.contrib import admin
from .models import (
    CryptoWallet, CryptoTransaction, MiningStats,
    Proposal, Vote, Stake, RewardLog, PremiumAccess, DailyLogin,
)


@admin.register(CryptoWallet)
class CryptoWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'created_at')
    search_fields = ('user__username', 'address')


@admin.register(CryptoTransaction)
class CryptoTransactionAdmin(admin.ModelAdmin):
    list_display = ('from_address', 'to_address', 'amount', 'status', 'block_index', 'created_at')
    list_filter = ('status',)
    search_fields = ('from_address', 'to_address')


@admin.register(MiningStats)
class MiningStatsAdmin(admin.ModelAdmin):
    list_display = ('total_blocks', 'total_mined', 'difficulty', 'hashrate', 'last_block_time')


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'votes_for', 'votes_against', 'ends_at')
    list_filter = ('status', 'category')


@admin.register(Stake)
class StakeAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'apy', 'lock_days', 'status', 'unlocks_at')
    list_filter = ('status', 'lock_days')


@admin.register(RewardLog)
class RewardLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'reason', 'created_at')
    list_filter = ('reason',)


@admin.register(PremiumAccess)
class PremiumAccessAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'psx_paid', 'expires_at')
