from django.contrib import admin
from .models import ChainState, CryptoWallet, CryptoTransaction, MiningStats


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


@admin.register(ChainState)
class ChainStateAdmin(admin.ModelAdmin):
    list_display = ('updated_at',)
