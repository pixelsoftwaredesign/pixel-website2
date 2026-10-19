"""Parcours GestiActiv : routage, inscription, SSO, onboarding, modules."""
from _common import HOST_GESTIACTIV as HOST, bootstrap, check, report

bootstrap()

from django.contrib.auth.models import User
from django.test import Client

from studio.models import ERPClient, ERPMembership

# Etat propre pour les comptes/entreprises de test (owner est SET_NULL : les
# supprimer via l'utilisateur ne suffit pas).
User.objects.filter(username__in=['gx_test_user', 'gx_no_tenant']).delete()
ERPClient.objects.filter(company_name__in=['Clinique Test', 'Pâtisserie X']).delete()

print('\n== 1. Routage sous-domaine ==')
c = Client(HTTP_HOST=HOST)
r = c.get('/')
check('GET / (anonyme) -> 200', r.status_code == 200, r.status_code)
check('page GestiActiv servie', 'GestiActiv' in r.content.decode())
check('X-Robots-Tag noindex', r.headers.get('X-Robots-Tag') == 'noindex, nofollow')

r = c.get('/connexion/')
check('GET /connexion/ -> 200', r.status_code == 200, r.status_code)

r = c.get('/dashboard/')
check('GET /dashboard/ anonyme -> 302 vers /login/', r.status_code == 302 and '/login/' in r.headers.get('Location', ''),
      getattr(r, 'headers', {}).get('Location'))

print('\n== 2. Site principal toujours OK ==')
c2 = Client(HTTP_HOST='pixelsoftwaredesign.xyz')
r = c2.get('/')
check('GET / site principal -> 200', r.status_code == 200, r.status_code)
check("pas la landing GestiActiv", 'GestiActiv' not in r.content.decode()[:4000] or '/gestiactiv/' in r.content.decode())

print('\n== 3. Inscription GestiActiv ==')
u = 'gx_test_user'
User.objects.filter(username=u).delete()
c = Client(HTTP_HOST=HOST)
r = c.post('/inscription/', {
    'company': 'Clinique Test', 'activity': 'sante',
    'username': u, 'email': 'gx@test.tn', 'password': 'secret123',
})
check('POST /inscription/ -> 302', r.status_code == 302, r.status_code)
check('redirige vers /dashboard/', r.headers.get('Location', '').endswith('/dashboard/'), r.headers.get('Location'))
user = User.objects.filter(username=u).first()
check('utilisateur créé', user is not None)
check('ERPClient créé (activité sante)', bool(user and ERPClient.objects.filter(owner=user, activity='sante').exists()))
check('ERPMembership owner', bool(user and ERPMembership.objects.filter(user=user, role='owner').exists()))

r = c.get('/dashboard/')
body = r.content.decode()
check('GET /dashboard/ connecté -> 200', r.status_code == 200, r.status_code)
check('entreprise affichée', 'Clinique Test' in body)
check('activité affichée', 'Santé / Clinique' in body)

print('\n== 4. SSO : même session depuis le site principal ==')
c3 = Client(HTTP_HOST='pixelsoftwaredesign.xyz')
c3.cookies = c.cookies
r = c3.get('/gestiactiv/dashboard/')
check('session partagée (cookie domaine) -> 200', r.status_code == 200, r.status_code)

print('\n== 5. Module métier accessible une fois connecté ==')
r = c.get('/sante/')
check('GET /sante/ connecté -> 200', r.status_code == 200, r.status_code)

print('\n== 6. Onboarding (compte Pixel sans espace) ==')
u2 = 'gx_no_tenant'
User.objects.filter(username=u2).delete()
User.objects.create_user(u2, 'gx2@test.tn', 'secret123')
c4 = Client(HTTP_HOST=HOST)
c4.login(username=u2, password='secret123')
r = c4.get('/dashboard/')
check('redirige vers onboarding', r.status_code == 302 and 'onboarding' in r.headers.get('Location', ''), r.headers.get('Location'))
r = c4.post('/onboarding/', {'company': 'Pâtisserie X', 'activity': 'patisserie', 'phone': '21612345678'})
check('POST onboarding -> 302 dashboard', r.status_code == 302 and r.headers.get('Location', '').endswith('/dashboard/'), r.status_code)

raise SystemExit(report())
