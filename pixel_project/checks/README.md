# Vérifications locales

Suites de non-régression des backends métier GestiActiv. Elles tournent sur une
base **SQLite jetable** : aucun accès à la production, aucun identifiant réel.

## Lancer tout

```sh
cd pixel_project
python3 checks/run_checks.py
```

La base `/tmp/pixel_checks.sqlite3` est supprimée puis recréée (les migrations
appliquent notamment la migration de données `0030_seed_erp_modules`, qui crée
les 9 modules métier). Un autre chemin peut être passé en argument
(`python3 checks/run_checks.py /tmp/ma_base.sqlite3`).

Lancer une seule suite :

```sh
cd pixel_project && python3 checks/check_links.py
```

## Suites

| Fichier | Couvre | Vérifs |
|---|---|---|
| `check_gestiactiv.py` | Routage du sous-domaine, inscription, SSO (session partagée avec l'apex), onboarding, module métier | 19 |
| `check_tenant_isolation.py` | Cloisonnement multi-tenant : création/lecture/écriture inter-entreprise (404), onboarding, vue staff globale, unicité par entreprise | 25 |
| `check_links.py` | Aucun lien interne cassé sur le sous-domaine ; les liens produits restent absolus vers l'apex ; comportement inchangé sur le site principal | 32 |
| `check_admin.py` | Espace d'administration : matrice d'accès par rôle/statut, navigation jamais cassée, pages historiques (`/dashboard/`, `/admin-bancaire/`) fermées au public, « Rôles & accès » accorde `is_staff`, structure UX (recherche, filtres, confirmation, raccourcis, focus clavier) | 125 |
| `check_admin_pages.py` | Pages de données de l'admin : pagination indépendante par tableau (`?cpage=`, `?dpage=`, `?page=`, `?tpage=`), pages hors limites sans erreur, filtres par statut de commande, cloisonnement des rôles, CRUD de la configuration bancaire (ajout/édition/suppression, valeur invalide, RIB jamais exposé, case « actif »), badge « à traiter » de la navigation | 61 |
| `check_modules.py` | CRUD cloisonné des 9 modules métier (création, édition propriétaire + persistance, édition inter-entreprise 404, suppression inter-entreprise sans effet, suppression légitime) | 247 |

## Conventions

- Les suites s'appuient sur `_common.py` : `bootstrap()` prépare Django et
  migre la base si nécessaire, `check(label, condition, extra)` compte les
  vérifications, `report()` imprime le total et renvoie le code de sortie.
- Chaque suite crée ses propres entreprises/utilisateurs (préfixe `gx_`) et
  nettoie au début. Les modèles métier portent un `erp_client`, donc les
  comptes de contrôle sont supprimés explicitement par nom d'entreprise
  (`ERPClient.owner` est `SET_NULL` : supprimer l'utilisateur ne suffit pas).
- Les vérifications d'isolation ne portent que sur les objets du test
  (jamais de comptage global), pour rester justes quelle que soit la base.

## Non couvert ici (par nature)

Les vérifications **en production** (habillage live, parcours HTTP complet sur
`gestiactiv.pixelsoftwaredesign.xyz`, déploiement Render) nécessitent le réseau
et des identifiants réels : elles ne font pas partie de ces suites.
