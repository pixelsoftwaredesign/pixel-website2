"""Espaces client et entreprise.

Couvre :
- l'acces authentifie aux deux espaces (redirection sinon) et l'alias `/portail/` ;
- le catalogue du site dans les deux espaces, sans produit/categorie GestiActiv ;
- les commandes, devis et factures du client (filtrés par email) ;
- la creation et la modification de l'entreprise, l'equipe et les permissions ;
- la presence des liens croises entre les deux espaces.
"""
import time

from _common import HOST_APEX as APEX, bootstrap, check, report

bootstrap()

from django.contrib.auth.models import User
from django.test import Client

from studio.models import (
    Categorie, CommandeECommerce, Devis, ERPClient, ERPMembership,
    Facture, PreFacture, Produit, UserProfile,
)

TAG = str(int(time.time()))[-7:]
PREFIX = 'CHK ESP ' + TAG
EMAIL_OWNER = 'chk_esp_owner_%s@test.tn' % TAG
EMAIL_OTHER = 'chk_esp_other_%s@test.tn' % TAG
EMAIL_MEMBER = 'chk_esp_member_%s@test.tn' % TAG

# Nettoyage des executions precedentes.
User.objects.filter(username__in=[
    'chk_esp_owner', 'chk_esp_other', 'chk_esp_member']).delete()
ERPClient.objects.filter(company_name__startswith='CHK ESP ').delete()
Produit.objects.filter(nom__startswith='CHK ESP ').delete()
Categorie.objects.filter(nom__startswith='CHK ESP ').delete()
CommandeECommerce.objects.filter(reference__startswith='CMD-CHK-ESP-').delete()
Devis.objects.filter(client_email__startswith='chk_esp_').delete()
PreFacture.objects.filter(client_nom__startswith='CHK ESP ').delete()
Facture.objects.filter(client_nom__startswith='CHK ESP ').delete()


def mkuser(name, email):
    User.objects.filter(username=name).delete()
    user = User.objects.create_user(name, email=email, password='secret123')
    UserProfile.objects.get_or_create(user=user)
    return user


def login(user):
    c = Client(HTTP_HOST=APEX)
    c.force_login(user)
    return c


owner = mkuser('chk_esp_owner', EMAIL_OWNER)
other = mkuser('chk_esp_other', EMAIL_OTHER)
member = mkuser('chk_esp_member', EMAIL_MEMBER)

tenant = ERPClient.objects.create(
    company_name=PREFIX + 'Tenant', contact_name='Tenant',
    email='chk_esp_tenant_%s@test.tn' % TAG)
tenant_cat = Categorie.objects.create(erp_client=tenant, nom=PREFIX + 'Tenant Cat')
tenant_product = Produit.objects.create(
    erp_client=tenant, nom=PREFIX + 'Tenant Produit', categorie=tenant_cat,
    prix_vente=999, actif=True)

site_cat = Categorie.objects.create(erp_client=None, nom=PREFIX + 'Site Cat')
product = Produit.objects.create(
    erp_client=None, nom=PREFIX + 'Produit', categorie=site_cat,
    prix_vente=49.5, stock_actuel=3, actif=True)
service = Produit.objects.create(
    erp_client=None, nom=PREFIX + 'Service', categorie=site_cat,
    prix_vente=1200, stock_actuel=0, stock_minimum=0,
    est_service=True, actif=True)
inactive = Produit.objects.create(
    erp_client=None, nom=PREFIX + 'Inactif', categorie=site_cat,
    prix_vente=10, actif=False)

order_owner = CommandeECommerce.objects.create(
    reference='CMD-CHK-ESP-OWNER-' + TAG, client_nom='CHK ESP Owner',
    client_email=EMAIL_OWNER, client_adresse='Adresse test',
    total_ttc=49.5, statut='confirmee')
order_other = CommandeECommerce.objects.create(
    reference='CMD-CHK-ESP-OTHER-' + TAG, client_nom='CHK ESP Other',
    client_email=EMAIL_OTHER, client_adresse='Adresse test',
    total_ttc=99, statut='confirmee')
devis_owner = Devis.objects.create(
    client_nom='CHK ESP Owner', client_email=EMAIL_OWNER, sujet='Projet test')
devis_other = Devis.objects.create(
    client_nom='CHK ESP Other', client_email=EMAIL_OTHER, sujet='Projet test')
prefacture_owner = PreFacture.objects.create(
    client_nom='CHK ESP Owner', client_email=EMAIL_OWNER,
    montant_ht=10, montant_ttc=11.9)
facture_owner = Facture.objects.create(
    erp_client=None, numero='FAC-CHK-ESP-OWNER-' + TAG,
    client_nom='CHK ESP Owner', client_email=EMAIL_OWNER,
    montant_ht=10, montant_ttc=11.9)
facture_tenant = Facture.objects.create(
    erp_client=tenant, numero='FAC-CHK-ESP-TENANT-' + TAG,
    client_nom='CHK ESP Tenant', client_email=EMAIL_OWNER,
    montant_ht=20, montant_ttc=23.8)

anon = Client(HTTP_HOST=APEX)
owner_client = login(owner)
other_client = login(other)
member_client = login(member)

print('\n== 1. Acces aux espaces ==')
r = anon.get('/espace-client/')
check('anonyme /espace-client/ -> 302 login',
      r.status_code == 302 and '/login/' in r.headers.get('Location', ''),
      r.headers.get('Location'))
r = anon.get('/espace-entreprise/')
check('anonyme /espace-entreprise/ -> 302 login',
      r.status_code == 302 and '/login/' in r.headers.get('Location', ''),
      r.headers.get('Location'))
r = owner_client.get('/espace-client/')
check('client connecte -> 200', r.status_code == 200, r.status_code)
html = r.content.decode()
check('client : titre espace client', 'Espace client' in html)
check('client : lien vers espace entreprise', 'href="/espace-entreprise/"' in html)

r = owner_client.get('/portail/')
check('/portail/ (alias) -> 200', r.status_code == 200, r.status_code)
check('/portail/ expose le catalogue', 'Catalogue Pixel' in r.content.decode())

r = owner_client.get('/entreprise/')
check('/entreprise/ (alias) -> 200', r.status_code == 200, r.status_code)

print('\n== 2. Catalogue dans les deux espaces ==')
for url in ['/espace-client/', '/espace-entreprise/']:
    r = owner_client.get(url)
    body = r.content.decode()
    check(f'{url} : produit du site visible', product.nom in body)
    check(f'{url} : service du site visible', service.nom in body)
    check(f'{url} : badge service', 'cat-badge service' in body)
    check(f'{url} : produit inactif masque', inactive.nom not in body)
    check(f'{url} : produit GestiActiv masque', tenant_product.nom not in body)
    check(f'{url} : categorie GestiActiv masquee', tenant_cat.nom not in body)
    check(f'{url} : lien panier du produit',
          '/ecommerce/ajouter/%s/' % product.id in body)

print('\n== 3. Documents du client ==')
body = owner_client.get('/espace-client/').content.decode()
check('client : commande du client', order_owner.reference in body)
check('client : commande d\'un autre client masquee', order_other.reference not in body)

body = owner_client.get('/espace-entreprise/').content.decode()
check('entreprise : commande du client', order_owner.reference in body)
check('entreprise : commande d\'un autre client masquee', order_other.reference not in body)
check('entreprise : devis du client', devis_owner.reference in body)
check('entreprise : devis d\'un autre client masque', devis_other.reference not in body)
check('entreprise : prefacture du client', prefacture_owner.numero in body)
check('entreprise : facture du site', facture_owner.numero in body)
check('entreprise : facture GestiActiv masquee', facture_tenant.numero not in body)
check('entreprise : lien impression devis',
      '/espace-entreprise/devis/%s/imprimer/' % devis_owner.id in body)
check('entreprise : lien impression prefacture',
      '/espace-entreprise/prefactures/%s/imprimer/' % prefacture_owner.id in body)
check('entreprise : lien impression facture',
      '/espace-entreprise/factures/%s/imprimer/' % facture_owner.id in body)

print('\n== 3 bis. Impression securisee des documents ==')
url_devis = '/espace-entreprise/devis/%s/imprimer/' % devis_owner.id
url_prefacture = ('/espace-entreprise/prefactures/%s/imprimer/'
                  % prefacture_owner.id)
url_facture = '/espace-entreprise/factures/%s/imprimer/' % facture_owner.id
r = anon.get(url_devis)
check('impression anonyme -> 302 login',
      r.status_code == 302 and '/login/' in r.headers.get('Location', ''),
      r.headers.get('Location'))
r = owner_client.get(url_devis)
check('impression devis du client -> 200', r.status_code == 200, r.status_code)
check('impression devis : reference', devis_owner.reference in r.content.decode())
r = owner_client.get(url_prefacture)
check('impression prefacture du client -> 200', r.status_code == 200,
      r.status_code)
check('impression prefacture : numero',
      prefacture_owner.numero in r.content.decode())
r = owner_client.get(url_facture)
check('impression facture du client -> 200', r.status_code == 200,
      r.status_code)
check('impression facture : numero',
      facture_owner.numero in r.content.decode())
r = other_client.get(url_devis)
check('impression devis d\'un autre client -> 404', r.status_code == 404,
      r.status_code)
r = other_client.get(url_facture)
check('impression facture d\'un autre client -> 404', r.status_code == 404,
      r.status_code)
r = owner_client.get(
    '/espace-entreprise/factures/%s/imprimer/' % facture_tenant.id)
check('impression facture GestiActiv -> 404', r.status_code == 404,
      r.status_code)
r = other_client.get('/ecommerce/facture/%s/' % order_owner.id)
check('facture commande d\'un autre client -> 404', r.status_code == 404,
      r.status_code)
r = owner_client.get('/ecommerce/facture/%s/' % order_owner.id)
check('facture de sa commande -> 200', r.status_code == 200, r.status_code)

print('\n== 4. Creation de l\'entreprise ==')
body = owner_client.get('/espace-entreprise/').content.decode()
check('sans entreprise : formulaire de creation', 'Créer votre espace entreprise' in body)
check('sans entreprise : catalogue toujours present', 'Catalogue Pixel' in body)
r = owner_client.post('/espace-entreprise/', {
    'action': 'creer_entreprise',
    'company': PREFIX + 'Entreprise',
    'contact_name': 'Responsable Test',
    'email': EMAIL_OWNER,
    'phone': '+216 50 000 000',
    'matricule': 'MAT-ESP-1',
    'address': 'Adresse entreprise',
    'activity': 'sante',
})
check('creation entreprise -> 302', r.status_code == 302, r.status_code)
company = ERPClient.objects.filter(company_name=PREFIX + 'Entreprise').first()
check('ERPClient cree', company is not None)
check('proprietaire rattache',
      company is not None and ERPMembership.objects.filter(
          user=owner, client=company, role='owner').exists())
owner.profile.refresh_from_db()
check('profil entreprise synchronise', owner.profile.entreprise == PREFIX + 'Entreprise')

body = owner_client.get('/espace-entreprise/').content.decode()
check('entreprise : nom affiche', PREFIX + 'Entreprise' in body)
check('entreprise : equipe affichee', 'Équipe (1)' in body)
check('entreprise : lien GestiActiv', 'href="/gestiactiv/dashboard/"' in body)
check('entreprise : formulaire de modification', 'Modifier la fiche entreprise' in body)

print('\n== 4 bis. Invitation de l\'equipe ==')
r = owner_client.post('/espace-entreprise/', {
    'action': 'inviter_membre',
    'invite_email': EMAIL_MEMBER,
    'invite_role': 'employee',
})
check('invitation membre -> 302', r.status_code == 302, r.status_code)
check('invitation : rattachement cree',
      ERPMembership.objects.filter(
          user=member, client=company, role='employee').exists())
body = member_client.get('/espace-entreprise/').content.decode()
check('membre invite : entreprise visible', PREFIX + 'Entreprise' in body)
check('membre invite : equipe a jour', 'Équipe (2)' in body)

r = member_client.post('/espace-entreprise/', {
    'action': 'inviter_membre',
    'invite_email': EMAIL_OTHER,
    'invite_role': 'employee',
})
check('employe : invitation refusee', r.status_code == 200)
check('employe : message de permission',
      'Seuls le propriétaire et le gestionnaire' in r.content.decode())
check('employe : aucun rattachement cree',
      not ERPMembership.objects.filter(user=other, client=company).exists())

r = owner_client.post('/espace-entreprise/', {
    'action': 'inviter_membre',
    'invite_email': EMAIL_OWNER,
    'invite_role': 'employee',
})
check('invitation de soi-meme refusee', r.status_code == 200)
check('invitation de soi-meme : message',
      'déjà partie de cette entreprise' in r.content.decode())

r = owner_client.post('/espace-entreprise/', {
    'action': 'inviter_membre',
    'invite_email': 'inconnu_%s@test.tn' % TAG,
    'invite_role': 'employee',
})
check('invitation email inconnu refusee', r.status_code == 200)
check('invitation email inconnu : message',
      "Aucun compte Pixel" in r.content.decode())

print('\n== 5. Modification et permissions ==')
r = owner_client.post('/espace-entreprise/', {
    'action': 'modifier_entreprise',
    'company': PREFIX + 'Entreprise Modifiee',
    'contact_name': 'Responsable 2',
    'email': EMAIL_OWNER,
    'phone': '+216 51 111 111',
    'matricule': 'MAT-ESP-2',
    'address': 'Adresse 2',
    'activity': 'commerce',
})
check('modification entreprise -> 302', r.status_code == 302, r.status_code)
company.refresh_from_db()
check('nom entreprise modifie', company.company_name == PREFIX + 'Entreprise Modifiee')
check('activite modifiee', company.activity == 'commerce')
check('telephone modifie', company.phone == '+216 51 111 111')

# Un employe de la meme entreprise ne peut pas modifier la fiche.
ERPMembership.objects.create(user=other, client=company, role='employee')
body = other_client.get('/espace-entreprise/').content.decode()
check('employe : entreprise visible', PREFIX + 'Entreprise Modifiee' in body)
r = other_client.post('/espace-entreprise/', {
    'action': 'modifier_entreprise', 'company': 'Tentative interdite',
    'activity': 'sante',
})
company.refresh_from_db()
check('employe : modification refusee', r.status_code == 200)
check('employe : nom inchange', company.company_name == PREFIX + 'Entreprise Modifiee')
check('employe : message de permission',
      'Seuls le propriétaire et le gestionnaire' in r.content.decode())

print('\n== 6. Profil et cloisonnement ==')
r = owner_client.post('/espace-entreprise/', {
    'action': 'edit_profile', 'prenom': 'Sami', 'nom': 'Test',
    'telephone': '+216 52 222 222',
})
owner.refresh_from_db()
owner.profile.refresh_from_db()
check('profil : prenom enregistre', owner.first_name == 'Sami')
check('profil : telephone enregistre', owner.profile.telephone == '+216 52 222 222')
check('profil : entreprise non effacee',
      owner.profile.entreprise == PREFIX + 'Entreprise Modifiee')

check('catalogue : service sans stock',
      service.est_service and service.stock_actuel == 0)
check('catalogue : produit physique avec stock', product.stock_actuel == 3)
check('catalogue : produits du site sans tenant',
      product.erp_client_id is None and service.erp_client_id is None)
check('catalogue : produit tenant actif mais isole',
      tenant_product.actif and tenant_product.erp_client_id == tenant.id)

raise SystemExit(report())
