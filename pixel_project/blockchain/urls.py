from django.urls import path
from . import views

urlpatterns = [
    path('blockchain/', views.blockchain_dashboard, name='blockchain_dashboard'),
    path('blockchain/wallet/', views.blockchain_wallet, name='blockchain_wallet'),
    path('blockchain/explorer/', views.blockchain_explorer, name='blockchain_explorer'),
    path('blockchain/mining/', views.blockchain_mining, name='blockchain_mining'),

    path('tokenomics/', views.tokenomics_dashboard, name='tokenomics_dashboard'),
    path('governance/', views.governance_list, name='governance_list'),
    path('governance/<uuid:proposal_id>/', views.governance_proposal, name='governance_proposal'),
    path('staking/', views.staking_page, name='staking_page'),

    path('api/blockchain/wallet/create/', views.api_wallet_create, name='api_wallet_create'),
    path('api/blockchain/wallet/nonce/', views.api_wallet_nonce, name='api_wallet_nonce'),
    path('api/blockchain/balance/<str:address>/', views.api_balance, name='api_balance'),
    path('api/blockchain/send/', views.api_send, name='api_send'),
    path('api/blockchain/mine/', views.api_mine, name='api_mine'),
    path('api/blockchain/chain/', views.api_chain, name='api_chain'),
    path('api/blockchain/sync/', views.api_sync, name='api_sync'),
    path('api/blockchain/peers/', views.api_peers, name='api_peers'),
    path('api/blockchain/connect/', views.api_connect_peer, name='api_connect_peer'),
    path('api/blockchain/validate/', views.api_validate, name='api_validate'),
    path('api/blockchain/bridge/', views.api_send_tnd_to_crypto, name='api_bridge'),

    path('api/governance/propose/', views.api_governance_propose, name='api_governance_propose'),
    path('api/governance/vote/', views.api_governance_vote, name='api_governance_vote'),
    path('api/staking/stake/', views.api_stake, name='api_stake'),
    path('api/staking/claim/', views.api_stake_claim, name='api_stake_claim'),
    path('api/rewards/daily/', views.api_claim_daily, name='api_claim_daily'),
    path('api/premium/buy/', views.api_buy_premium, name='api_buy_premium'),

    path('security/', views.security_dashboard, name='security_dashboard'),
    path('api/security/status/', views.api_security_status, name='api_security_status'),
    path('api/security/validate/', views.api_become_validator, name='api_become_validator'),
    path('api/security/fraud/', views.api_fraud_alerts, name='api_fraud_alerts'),
    path('api/multisig/create/', views.api_multisig_create, name='api_multisig_create'),
    path('api/multisig/propose/', views.api_multisig_propose, name='api_multisig_propose'),

    path('web3-login/', views.web3_login_page, name='web3_login'),
    path('api/web3/nonce/', views.api_web3_nonce, name='api_web3_nonce'),
    path('api/web3/verify/', views.api_web3_verify, name='api_web3_verify'),
]
