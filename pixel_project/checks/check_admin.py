"""Espace d'administration : cloisonnement par role et statut de personnel.

Verifie que l'acces aux tableaux de bord est reserve aux membres du personnel
(`is_staff`) porteurs du bon role, que la barre de navigation `admin_ui`
n'expose jamais un lien inaccessible, et que l'ecran « Roles & acces »
accorde bien l'acces au personnel.
"""
import os

from _common import HOST_APEX as APEX, bootstrap, check, report

bootstrap()

from django.contrib.auth.models import Group, User
from django.test import Client

from studio.templatetags.admin_ui import admin_nav

ROLE_GROUPS = ['SuperAdmin', 'Admin', 'Commercial', 'Comptable', 'Editeur']

# (chemin, roles autorises). '*staff*' = tout membre du personnel.
ROUTES = [
    ('/admin/receptions/', '*staff*'),
    ('/dashboard/', '*staff*'),
    ('/admin-bancaire/', '*staff*'),
    ('/admin/dash/commercial/', {'Commercial', 'SuperAdmin', 'Admin'}),
    ('/admin/dash/comptable/', {'Comptable', 'SuperAdmin', 'Admin'}),
    ('/admin/dash/editeur/', {'Editeur', 'SuperAdmin', 'Admin'}),
    ('/admin/dash/superadmin/', {'SuperAdmin'}),
    ('/admin/dash/admin/', {'Admin', 'SuperAdmin'}),
    ('/admin/roles/', {'Admin', 'SuperAdmin'}),
]

for g in ROLE_GROUPS:
    Group.objects.get_or_create(name=g)


def mkuser(name, groups=(), staff=False, superuser=False, active=True):
    User.objects.filter(username=name).delete()
    u = User.objects.create_user(name, password='secret123', email=name + '@test.tn')
    u.is_staff = staff
    u.is_superuser = superuser
    u.is_active = active
    u.save()
    for g in groups:
        u.groups.add(Group.objects.get(name=g))
    return u


users = {
    'staff sans role': mkuser('chk_staff_norole', staff=True),
    'commercial NON-staff': mkuser('chk_com_nonstaff', ['Commercial']),
    'commercial staff': mkuser('chk_com_staff', ['Commercial'], staff=True),
    'admin staff': mkuser('chk_adm_staff', ['Admin'], staff=True),
    'superadmin staff': mkuser('chk_sa_staff', ['SuperAdmin'], staff=True),
    'superuser': mkuser('chk_root', superuser=True, staff=True),
}


def allowed(user, roles):
    if user is None:
        return False
    if user.is_superuser:
        return True
    if not user.is_staff:
        return False
    return roles == '*staff*' or bool({g.name for g in user.groups.all()} & roles)


print('\n== 1. Matrice d\'acces (anonyme -> 302, connecte hors role -> 403) ==')
for label, user in [('anonyme', None)] + list(users.items()):
    c = Client(HTTP_HOST=APEX)
    if user is not None:
        c.force_login(user)
    for path, roles in ROUTES:
        r = c.get(path)
        if user is None:
            expected = 302
        elif allowed(user, roles):
            expected = 200
        else:
            expected = 403
        check(f'{label} {path} -> {expected}',
              r.status_code == expected, r.status_code)
    if user is not None:
        c.force_login(user)


print('\n== 2. La navigation n\'expose que des pages accessibles ==')
for label, user in users.items():
    c = Client(HTTP_HOST=APEX)
    c.force_login(user)
    groups = admin_nav(user, '')
    urls = [i['url'] for g in groups for i in g['items']]
    broken = [u for u in urls if c.get(u).status_code != 200]
    check(f'{label} : aucun lien de nav casse', not broken, broken)
    for path, roles in ROUTES:
        expected_in_nav = allowed(user, roles) and any(
            i['url'] == path for g in groups for i in g['items'])
        if allowed(user, roles) and path != '/dashboard/' and path != '/admin-bancaire/':
            check(f'{label} : {path} present dans la nav', expected_in_nav)

print('\n== 3. Pages historiques fermees au public ==')
anon = Client(HTTP_HOST=APEX)
check('anonyme /dashboard/ -> 302 (etait public)',
      anon.get('/dashboard/').status_code == 302)
check('anonyme /admin-bancaire/ -> 302',
      anon.get('/admin-bancaire/').status_code == 302)
com_nonstaff = Client(HTTP_HOST=APEX)
com_nonstaff.force_login(users['commercial NON-staff'])
check('non-staff /dashboard/ -> 403',
      com_nonstaff.get('/dashboard/').status_code == 403)
check('non-staff /admin-bancaire/ -> 403',
      com_nonstaff.get('/admin-bancaire/').status_code == 403)
check('non-staff /admin/receptions/ -> 403',
      com_nonstaff.get('/admin/receptions/').status_code == 403)

print('\n== 4. La nav est vide pour un utilisateur non-staff ==')
check('nav vide (non-staff)', admin_nav(users['commercial NON-staff'], '') == [])


print('\n== 5. « Roles & acces » accorde l\'acces au personnel ==')
target = mkuser('chk_promu', active=False)
check('cible initialement non-staff et inactive',
      not target.is_staff and not target.is_active)
adm = Client(HTTP_HOST=APEX)
adm.force_login(users['admin staff'])
r = adm.post('/admin/roles/', {'user_id': target.id, 'role': 'Commercial'})
target.refresh_from_db()
check('POST /admin/roles/ -> 302', r.status_code == 302, r.status_code)
check('redirection avec la ligne mise en evidence',
      '?changed=%s' % target.id in r.get('Location', ''), r.get('Location'))
check('role attribue', target.groups.filter(name='Commercial').exists())
check('is_staff accorde automatiquement', target.is_staff)
check('compte reactive automatiquement', target.is_active)
promu = Client(HTTP_HOST=APEX)
promu.force_login(target)
check('cible promue peut ouvrir /admin/dash/commercial/',
      promu.get('/admin/dash/commercial/').status_code == 200)

print('\n== 6. Un Admin (non-super) ne peut pas promouvoir en SuperAdmin ==')
other = mkuser('chk_cible_sa', staff=True)
adm.post('/admin/roles/', {'user_id': other.id, 'role': 'SuperAdmin'})
other.refresh_from_db()
check('SuperAdmin refuse a un Admin non-super',
      not other.groups.filter(name='SuperAdmin').exists())

print('\n== 7. Ecran « Roles & acces » : structure UX ==')
r = adm.get('/admin/roles/')
html = r.content.decode()
check('GET /admin/roles/ -> 200', r.status_code == 200, r.status_code)
for token, label in [
    ('id="userFilter"', 'champ de recherche'),
    ('class="px-pill', 'filtres par role'),
    ('data-role-filter="__none__"', 'filtre « sans role »'),
    ('data-search=', 'index de recherche par ligne'),
    ('>Enregistrer<', 'bouton Enregistrer'),
    ('data-user-row', 'lignes filtrables'),
    ('aria-live="polite"', 'compteur accessible'),
]:
    check(f'roles : {label}', token in html)
check('roles : confirmation avant changement', 'window.confirm' in html)
check('roles : description des roles', 'Demandes, clients' in html)
check('roles : ligne modifiee mise en evidence', 'is-changed' in adm.get(
    '/admin/roles/?changed=%s' % target.id).content.decode())

print('\n== 8. Coquille admin : raccourcis & accessibilite ==')
shell = adm.get('/admin/receptions/').content.decode()
for token, label in [
    ('href="/dashboard/"', 'raccourci Tableau de bord'),
    ('href="/portail/"', 'raccourci Mon espace'),
    ('aria-controls="pxadminSidebar"', 'burger relie a la sidebar'),
    ('aria-label="Se déconnecter"', 'bouton deconnexion libelle'),
    ('aria-current="page"', 'page courante signalee'),
]:
    check(f'coquille : {label}', token in shell)

css = open(os.path.join('studio', 'static', 'css', 'admin-ui.css'), encoding='utf-8').read()
check('css : focus clavier visible', ':focus-visible' in css)
check('css : respect de prefers-reduced-motion', 'prefers-reduced-motion' in css)
check('css : table filtrable (lignes masquees)', 'tr[hidden]' in css)

raise SystemExit(report())
