"""Composants de navigation pour l'espace d'administration.

Fournit une navigation filtrée par rôle, cohérente avec le décorateur
`studio.views.role_required` (superuser = accès total, sinon appartenance
à un groupe).
"""

from django import template

register = template.Library()


# Chaque entrée : clé, libellé, description, icône, url, rôles autorisés
# (None = tout membre du staff), et section de menu.
DASHBOARDS = [
    {
        'key': 'receptions',
        'label': "Vue d'ensemble",
        'desc': 'Commandes & devis',
        'icon': '📋',
        'url': '/admin/receptions/',
        'roles': None,
        'group': 'Pilotage',
    },
    {
        'key': 'superadmin',
        'label': 'SuperAdmin',
        'desc': 'Vue globale',
        'icon': '🔐',
        'url': '/admin/dash/superadmin/',
        'roles': ['SuperAdmin'],
        'group': 'Pilotage',
    },
    {
        'key': 'commercial',
        'label': 'Commercial',
        'desc': 'Demandes & clients',
        'icon': '💼',
        'url': '/admin/dash/commercial/',
        'roles': ['Commercial', 'SuperAdmin', 'Admin'],
        'group': 'Métiers',
    },
    {
        'key': 'comptable',
        'label': 'Comptable',
        'desc': 'Commandes & paiements',
        'icon': '💳',
        'url': '/admin/dash/comptable/',
        'roles': ['Comptable', 'SuperAdmin', 'Admin'],
        'group': 'Métiers',
    },
    {
        'key': 'editeur',
        'label': 'Éditeur',
        'desc': 'Contenu & newsletter',
        'icon': '✍️',
        'url': '/admin/dash/editeur/',
        'roles': ['Editeur', 'SuperAdmin', 'Admin'],
        'group': 'Métiers',
    },
    {
        'key': 'admin',
        'label': 'Admin',
        'desc': 'Système & utilisateurs',
        'icon': '🛠️',
        'url': '/admin/dash/admin/',
        'roles': ['Admin', 'SuperAdmin'],
        'group': 'Système',
    },
]

# Ordre de priorité pour l'étiquette de rôle affichée.
ROLE_ORDER = ['SuperAdmin', 'Admin', 'Commercial', 'Comptable', 'Editeur']


def _user_roles(user):
    try:
        return set(user.groups.values_list('name', flat=True))
    except Exception:
        return set()


def user_can(user, dashboard):
    """Vrai si l'utilisateur peut accéder au dashboard donné."""
    if not user or not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    roles = dashboard.get('roles')
    if roles is None:
        return True
    return bool(_user_roles(user) & set(roles))


@register.simple_tag
def admin_nav(user, current_path=''):
    """Retourne les dashboards accessibles, regroupés par section."""
    groups = []
    if not user or not user.is_authenticated:
        return groups
    current = (current_path or '').rstrip('/')
    for d in DASHBOARDS:
        if not user_can(user, d):
            continue
        item = {
            'key': d['key'],
            'label': d['label'],
            'desc': d['desc'],
            'icon': d['icon'],
            'url': d['url'],
            'active': current == d['url'].rstrip('/'),
        }
        if not groups or groups[-1]['name'] != d['group']:
            groups.append({'name': d['group'], 'items': []})
        groups[-1]['items'].append(item)
    return groups


@register.simple_tag
def admin_role(user):
    """Étiquette de rôle affichée dans l'interface."""
    if not user or not user.is_authenticated:
        return 'Invité'
    if user.is_superuser:
        return 'Superutilisateur'
    roles = _user_roles(user)
    for name in ROLE_ORDER:
        if name in roles:
            return name
    return 'Staff'
