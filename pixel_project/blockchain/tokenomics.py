"""
PixSoftMoney — PSX Tokenomics Configuration
Supply, distribution, governance, utility, and reward rules.

TOKEN: PSX (PixSoftMoney Coin)
CHAIN: PixSoftMoney Blockchain (from scratch, PoW)
ALGORITHM: ECDSA secp256k1 + SHA-256 Proof of Work
"""

# ─── Supply ──────────────────────────────────────────────────
MAX_SUPPLY = 21_000_000        # Supply max (21M PSX, comme Bitcoin)
INITIAL_SUPPLY = 0             # Supply initial (tout est miné)
MINING_REWARD = 50.0           # Récompense par bloc miné
HALVING_INTERVAL = 210_000     # Blocs entre chaque halving
MINING_DIFFICULTY = 4          # Zéros requis pour PoW

# ─── Distribution Genesis ────────────────────────────────────
# Quand le système démarre, la répartition est:
GENESIS_ALLOCATION = {
    'ecosystem': 5_000_000,       # Écosystème (développement, grants)
    'community_rewards': 3_000_000, # Récompenses communauté
    'liquidity_pool': 2_000_000,  # Pool de liquidité TND↔PSX
    'team_vesting': 1_000_000,    # Équipe (vesting 24 mois)
    'reserve': 10_000_000,        # Réserve (stabilisation)
}

# ─── Governance (Token de Gouvernance) ───────────────────────
# Chaque PSX = 1 vote. Min 100 PSX pour proposer.
GOVERNANCE = {
    'min_to_propose': 100,        # PSX min pour créer une proposition
    'voting_period_days': 7,      # Durée du vote en jours
    'quorum_percent': 10,         # % du supply total pour quorum
    'pass_threshold': 50,         # % de votes OUI pour passer
    'categories': [
        'feature',       # Nouvelles fonctionnalités
        'fee',           # Modification des frais
        'upgrade',       # Mise à jour protocole
        'community',     # Initiatives communautaires
    ],
}

# ─── Utility (Token Utilitaire) ─────────────────────────────
# Le PSX peut être utilisé pour:
UTILITY = {
    # Accès premium
    'premium_monthly': 50,        # PSX/mois pour accès premium
    'premium_yearly': 500,        # PSX/an (2 mois gratuits)
    
    # Services
    'qr_generation': 1,          # PSX par QR code généré
    'api_call': 0.01,            # PSX par appel API
    'priority_tx': 0.5,          # PSX pour transaction prioritaire
    
    # Frais de transaction
    'transfer_fee_percent': 0.1, # 0.1% frais de transfert
    'min_fee': 0.001,            # Frais minimum
    
    # Modules ERP (via blockchain)
    'module_erp_starter': 100,   # PSX pour activer module starter
    'module_erp_pro': 500,       # PSX pour activer module pro
    'module_erp_enterprise': 2000, # PSX pour activer module enterprise
}

# ─── Rewards (Token de Récompense) ──────────────────────────
REWARDS = {
    # Parrainage
    'referral_bonus': 10,         # PSX par parrainage réussi
    'referral_threshold': 5,      # Parrains nécessaires pour bonus
    
    # Staking
    'staking_apy_base': 5.0,     # 5% APY de base
    'staking_apy_boost': 10.0,   # 10% APY max (avec lock 12 mois)
    'min_stake': 100,            # PSX min pour staker
    'lock_periods': {
        30: 5.0,    # 30 jours → 5% APY
        90: 7.0,    # 90 jours → 7% APY
        180: 8.5,   # 180 jours → 8.5% APY
        365: 10.0,  # 365 jours → 10% APY
    },
    
    # Activité
    'daily_login': 0.5,          # PSX par connexion quotidienne
    'first_tx_bonus': 5,         # Bonus première transaction
    'monthly_active': 10,        # Bonus utilisateur actif/mois
    
    # Milestones
    'milestones': [
        {'transactions': 10, 'bonus': 25, 'label': 'Débutant'},
        {'transactions': 50, 'bonus': 100, 'label': 'Actif'},
        {'transactions': 200, 'bonus': 500, 'label': 'Vétéran'},
        {'transactions': 1000, 'bonus': 2000, 'label': 'Légende'},
    ],
}

# ─── Halving Schedule ────────────────────────────────────────
def get_block_reward(block_height: int) -> float:
    """Récompense du bloc avec halving progressif."""
    halvings = block_height // HALVING_INTERVAL
    reward = MINING_REWARD / (2 ** halvings)
    return max(reward, 0.001)  # Minimum 0.001 PSX


def get_total_circulating(block_height: int) -> float:
    """Supply en circulation à une hauteur donnée."""
    full_cycles = block_height // HALVING_INTERVAL
    remaining = block_height % HALVING_INTERVAL
    
    total = 0
    for i in range(full_cycles):
        total += HALVING_INTERVAL * (MINING_REWARD / (2 ** i))
    total += remaining * (MINING_REWARD / (2 ** full_cycles))
    return min(total, MAX_SUPPLY)
