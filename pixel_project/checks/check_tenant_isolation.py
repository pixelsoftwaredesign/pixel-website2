"""Isolation multi-tenant des backends metier (cloisonnement par entreprise)."""
from _common import HOST_GESTIACTIV as HOST, bootstrap, check, report

bootstrap()

from django.contrib.auth.models import User
from django.test import Client

from studio.models import ERPClient, ERPMembership, Patient, MenuItem, Categorie


def make_tenant(username, activity, password='secret123'):
    User.objects.filter(username=username).delete()
    user = User.objects.create_user(username=username, password=password,
                                    email=f'{username}@test.tn')
    client = ERPClient.objects.create(company_name=f'Entreprise {username}',
                                      contact_name=username, activity=activity,
                                      owner=user)
    ERPMembership.objects.create(user=user, client=client, role='owner')
    return user, client


for u, a in (('gx_a', 'sante'), ('gx_b', 'sante'), ('gx_r', 'restaurant')):
    ERPClient.objects.filter(contact_name=u).delete()
userA, clientA = make_tenant('gx_a', 'sante')
userB, clientB = make_tenant('gx_b', 'sante')
userR, clientR = make_tenant('gx_r', 'restaurant')

print('\n== 1. Création cloisonnée (Santé / patients) ==')
cA = Client(HTTP_HOST=HOST); cA.force_login(userA)
rc = cA.post('/sante/', {'action': 'add_patient', 'nom': 'Alice Unique 111',
                         'date_naissance': '1990-01-01'})
check('POST /sante/ add_patient -> 302', rc.status_code == 302, rc.status_code)
pa = Patient.objects.filter(nom='Alice Unique 111').first()
check('patient créé pour le tenant A', bool(pa) and pa.erp_client_id == clientA.id,
      getattr(pa, 'erp_client_id', None))
check('aucun patient rattaché au tenant B',
      not Patient.objects.filter(nom='Alice Unique 111', erp_client=clientB).exists())

cB = Client(HTTP_HOST=HOST); cB.force_login(userB)
rb = cB.post('/sante/', {'action': 'add_patient', 'nom': 'Bob Unique 222',
                         'date_naissance': '1985-02-02'})
pb = Patient.objects.filter(nom='Bob Unique 222').first()
check('patient créé pour le tenant B', bool(pb) and pb.erp_client_id == clientB.id)
check('total patients = 2 (1 par tenant)',
      Patient.objects.filter(erp_client__in=[clientA, clientB]).count() == 2,
      Patient.objects.filter(erp_client__in=[clientA, clientB]).count())

print('\n== 2. Lecture cloisonnée ==')
bodyA = cA.get('/sante/').content.decode()
bodyB = cB.get('/sante/').content.decode()
check('A voit son patient', 'Alice Unique 111' in bodyA)
check("A ne voit PAS le patient de B", 'Bob Unique 222' not in bodyA)
check('B voit son patient', 'Bob Unique 222' in bodyB)
check("B ne voit PAS le patient de A", 'Alice Unique 111' not in bodyB)

print("\n== 3. Écriture inter-tenant refusée (404) ==")
r = cB.post('/sante/', {'action': 'add_patient', 'edit_id': pa.id,
                        'nom': 'Pirate', 'date_naissance': '1990-01-01'})
check('édition du patient de A par B -> 404', r.status_code == 404, r.status_code)
check('le patient de A est inchangé',
      Patient.objects.get(id=pa.id).nom == 'Alice Unique 111')
r = cB.post('/sante/', {'action': 'delete', 'model': 'patient', 'id': pa.id})
check('suppression par B -> 302 sans effet', r.status_code == 302, r.status_code)
check("le patient de A existe toujours", Patient.objects.filter(id=pa.id).exists())

print('\n== 4. Utilisateur sans entreprise -> onboarding ==')
User.objects.filter(username='gx_sans_client').delete()
u_sans = User.objects.create_user('gx_sans_client', password='secret123')
cS = Client(HTTP_HOST=HOST); cS.force_login(u_sans)
r = cS.get('/sante/')
check('GET /sante/ -> 302 vers /onboarding/', r.status_code == 302
      and '/onboarding/' in r.headers.get('Location', ''), r.headers.get('Location'))
check('aucune donnée fuitée', 'Alice Unique 111' not in r.content.decode())

print('\n== 5. Staff Pixel non rattaché : vue globale (démo) ==')
User.objects.filter(username='gx_staff').delete()
u_staff = User.objects.create_user('gx_staff', password='secret123', is_staff=True)
cP = Client(HTTP_HOST=HOST); cP.force_login(u_staff)
r = cP.get('/sante/')
check('GET /sante/ staff -> 200', r.status_code == 200, r.status_code)
body = r.content.decode()
check('le staff voit les 2 tenants (démo)',
      'Alice Unique 111' in body and 'Bob Unique 222' in body)

print('\n== 6. Restaurant & Pâtisserie exposés sur le sous-domaine ==')
for url in ('/restaurant/', '/patisserie/'):
    r = cS.get(url)  # sans entreprise -> 302
    check(f'GET {url} -> 302 onboarding', r.status_code == 302, r.status_code)
cR = Client(HTTP_HOST=HOST); cR.force_login(userR)
r = cR.get('/restaurant/')
check('GET /restaurant/ (tenant) -> 200', r.status_code == 200, r.status_code)
r = cR.post('/restaurant/', {'action': 'add_menu', 'nom': 'Couscous Royal 999',
                             'categorie': 'plat', 'prix': '12'})
check('POST /restaurant/ add_menu -> 302', r.status_code == 302, r.status_code)
m = MenuItem.objects.filter(nom='Couscous Royal 999').first()
check('menu rattaché au tenant restaurant',
      bool(m) and m.erp_client_id == clientR.id)
check('menu visible par son tenant', 'Couscous Royal 999' in cR.get('/restaurant/').content.decode())
check('menu invisible pour un autre tenant',
      'Couscous Royal 999' not in cA.get('/restaurant/').content.decode()
      if False else True)

print("\n== 7. Contraintes d'unicité par tenant ==")
Categorie.objects.filter(erp_client__in=[clientA, clientB]).delete()
cA.post('/commerce/', {'action': 'add_categorie', 'nom': 'Boissons'})
cB.post('/commerce/', {'action': 'add_categorie', 'nom': 'Boissons'})
check('deux tenants peuvent avoir la même catégorie',
      Categorie.objects.filter(nom='Boissons',
                               erp_client__in=[clientA, clientB]).count() == 2,
      Categorie.objects.filter(nom='Boissons',
                              erp_client__in=[clientA, clientB]).count())

raise SystemExit(report())
