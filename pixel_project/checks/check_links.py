"""Les pages metier n'ont aucun lien casse, selon l'hote.

Sur le sous-domaine GestiActiv, tous les liens internes doivent repondre ; sur
le site principal, les liens doivent rester ceux d'origine.
"""
import re

from _common import HOST_APEX as APEX, HOST_GESTIACTIV as GX, bootstrap, check, report

bootstrap()

from django.contrib.auth.models import User
from django.test import Client

from studio.models import ERPClient, ERPMembership

MODULES = ['auto-ecole', 'sante', 'hotel', 'commerce', 'juridique',
           'comptabilite', 'rh', 'restaurant', 'patisserie']
PRODUCT_PREFIXES = ('/pixsoftpay', '/uicatalogue', '/graphisme', '/innerstudio',
                    '/pixelsoftcode', '/ecommerce', '/pixmail', '/pixmanager')


# Etat propre (owner est SET_NULL : supprimer l'utilisateur laisse l'entreprise).
User.objects.filter(username='gx_links_tenant').delete()
ERPClient.objects.filter(company_name='Tenant Liens').delete()
user = User.objects.create_user('gx_links_tenant', password='secret123',
                                email='links@test.tn')
client = ERPClient.objects.create(company_name='Tenant Liens', activity='sante',
                                 owner=user)
ERPMembership.objects.create(user=user, client=client, role='owner')

c = Client(HTTP_HOST=GX)
c.force_login(user)

internal = {}
print('\n== 1. Sous-domaine : chaque module repond et n\'a aucun lien casse ==')
for m in MODULES:
    r = c.get(f'/{m}/')
    check(f'GET /{m}/ -> 200', r.status_code == 200, r.status_code)
    if r.status_code != 200:
        continue
    html = r.content.decode()
    links = set(re.findall(r'href="(/[^"]*)"', html))
    for ln in links:
        internal.setdefault(ln, set()).add(m)
    check(f'  /{m}/ : nav GestiActiv', 'GestiActiv</strong>' in html)

for ln in sorted(internal):
    if ln == '/logout/':
        continue  # deconnecterait la session du test
    r = c.get(ln)
    check(f'lien interne {ln} (depuis {sorted(internal[ln])[0]}) -> <400',
          r.status_code < 400, r.status_code)

r = c.get('/logout/')
check('lien interne /logout/ -> 302', r.status_code == 302, r.status_code)
c.force_login(user)

print('\n== 2. Sous-domaine : index de page base + liens de tableau de bord ==')
r = c.get('/sante/')
html = r.content.decode()
check('bouton "Tableau de bord" -> /dashboard/',
      'href="/dashboard/"' in html)
check("lien GestiActiv -> / (accueil sous-domaine)", 'href="/"' in html)

print('\n== 3. Sous-domaine : plus aucun lien produit relatif ==')
html_c = c.get('/commerce/').content.decode()
bad = [p for p in PRODUCT_PREFIXES if f'href="{p}' in html_c]
check('aucun lien produit relatif', not bad, bad)
check('liens produits absolus vers le site Pixel',
      'href="https://pixelsoftwaredesign.xyz/ecommerce/stock/"' in html_c)

print('\n== 4. Site principal : comportement inchange ==')
a = Client(HTTP_HOST=APEX)
a.force_login(user)
r = a.get('/gestiactiv/sante/')
check('GET /gestiactiv/sante/ -> 200', r.status_code == 200, r.status_code)
html_a = r.content.decode()
check('lien Tableau de bord -> /gestiactiv/dashboard/',
      'href="/gestiactiv/dashboard/"' in html_a)
check('nav Pixel (pas GestiActiv)', 'Pixel Software Design</strong>' in html_a)
check('lien produit reste relatif', 'href="/pixsoftpay/' in html_a)

raise SystemExit(report())
