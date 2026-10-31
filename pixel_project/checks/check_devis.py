"""Devis structurés, ventes et préfactures.

Parcours complet dans l'espace admin :
- création d'un devis depuis une demande de projet, avec lignes produits ;
- envoi (email simulé), acceptation, conversion en vente ;
- création d'une préfacture depuis le devis, impression et conversion en facture ;
- saisie manuelle d'une vente et suppression ;
- catalogue produits, navigation et cloisonnement des rôles.
"""
import atexit
import time
from decimal import Decimal
from unittest.mock import patch

from _common import HOST_APEX as APEX, bootstrap, check, report

bootstrap()

from django.contrib.auth.models import Group, User
from django.db.models import F
from django.test import Client

from studio.models import (
    Categorie, Devis, ERPClient, Facture, PreFacture, Produit, ProjetContact,
    Vente,
)
from studio.templatetags.admin_ui import admin_nav

for name in ['SuperAdmin', 'Admin', 'Commercial', 'Comptable', 'Editeur']:
    Group.objects.get_or_create(name=name)

TAG = str(int(time.time()))[-7:]


def mkuser(name, groups=(), staff=True, superuser=False):
    User.objects.filter(username=name).delete()
    u = User.objects.create_user(name, password='secret123', email=name + '@test.tn')
    u.is_staff = staff
    u.is_superuser = superuser
    u.save()
    for g in groups:
        u.groups.add(Group.objects.get(name=g))
    return u


def login(user):
    c = Client(HTTP_HOST=APEX)
    c.force_login(user)
    return c


superuser = mkuser('chk_dev_super', ['SuperAdmin'], staff=True, superuser=True)
editeur = mkuser('chk_dev_editeur', ['Editeur'], staff=True)
commercial_nonstaff = mkuser('chk_dev_com_nonstaff', ['Commercial'], staff=False)
anon = Client(HTTP_HOST=APEX)
c = login(superuser)

# ─── données ─────────────────────────────────────────────────
categorie = Categorie.objects.create(nom='CHK Catégorie ' + TAG)
p1 = Produit.objects.create(
    nom='CHK Produit A ' + TAG, categorie=categorie, prix_vente=Decimal('100.00'),
    stock_actuel=10, stock_minimum=2, actif=True)
p2 = Produit.objects.create(
    nom='CHK Produit B ' + TAG, categorie=categorie, prix_vente=Decimal('50.00'),
    stock_actuel=1, stock_minimum=2, actif=True)
tenant = ERPClient.objects.create(
    company_name='CHK Tenant ' + TAG, contact_name='Tenant',
    email='chk_tenant_%s@test.tn' % TAG)
p_tenant = Produit.objects.create(
    erp_client=tenant, nom='CHK Tenant Produit ' + TAG, categorie=categorie,
    prix_vente=Decimal('999.00'), stock_actuel=0, stock_minimum=5, actif=True)
projet = ProjetContact.objects.create(
    nom='CHKD Client ' + TAG, email='chkd_%s@test.tn' % TAG,
    message='Besoin d\'un site web et d\'un logo.')


def cleanup():
    try:
        Facture.objects.filter(client_nom__startswith='CHKD Client').delete()
        Facture.objects.filter(
            client_nom__startswith='CHK Tenant Facture').delete()
        PreFacture.objects.filter(client_nom__startswith='CHKD Client').delete()
        Devis.objects.filter(client_nom__startswith='CHKD Client').delete()
        Vente.objects.filter(client_nom__startswith='CHKD').delete()
        Produit.objects.filter(
            nom__startswith='CHK Produit').delete()
        Produit.objects.filter(
            nom__startswith='CHK Tenant Produit').delete()
        ERPClient.objects.filter(
            company_name__startswith='CHK Tenant').delete()
        Categorie.objects.filter(nom__startswith='CHK Catégorie').delete()
        ProjetContact.objects.filter(nom__startswith='CHKD').delete()
        for u in (superuser, editeur, commercial_nonstaff):
            u.delete()
    except Exception:
        pass


atexit.register(cleanup)


def donnees_devis(instance, action='save'):
    lignes = list(instance.lignes.all())
    data = {
        'client_nom': instance.client_nom,
        'client_email': instance.client_email,
        'client_tel': instance.client_tel,
        'client_adresse': instance.client_adresse,
        'sujet': instance.sujet,
        'message': instance.message,
        'statut': instance.statut,
        'tva': str(instance.tva),
        'notes': instance.notes,
        'action': action,
        'projet': str(instance.projet_id or ''),
        'lignes-TOTAL_FORMS': str(len(lignes)),
        'lignes-INITIAL_FORMS': str(len(lignes)),
        'lignes-MIN_NUM_FORMS': '0',
        'lignes-MAX_NUM_FORMS': '1000',
    }
    for i, ligne in enumerate(lignes):
        data.update({
            'lignes-%d-id' % i: str(ligne.pk),
            'lignes-%d-produit' % i: str(ligne.produit_id or ''),
            'lignes-%d-designation' % i: ligne.designation,
            'lignes-%d-quantite' % i: str(ligne.quantite),
            'lignes-%d-prix_unitaire' % i: str(ligne.prix_unitaire),
            'lignes-%d-remise' % i: str(ligne.remise),
        })
    return data


print('\n== 1. Liste et formulaire de devis ==')
r = c.get('/admin/devis/')
check('liste devis -> 200', r.status_code == 200, r.status_code)
body = r.content.decode()
check('liste devis : bouton nouveau', 'Nouveau devis' in body)
check('liste devis : demande disponible', 'CHKD Client ' + TAG in body)

r = c.get('/admin/devis/nouveau/?projet=%d' % projet.id)
check('formulaire devis -> 200', r.status_code == 200, r.status_code)
body = r.content.decode()
check('formulaire : client pré-rempli', ('CHKD Client ' + TAG) in body)
check('formulaire : catalogue produits', p1.nom in body and p2.nom in body)
check('formulaire : produit tenant absent', p_tenant.nom not in body)
check('formulaire : message de la demande', 'site web' in body)

r = c.get('/admin/devis/nouveau/?produit=%d' % p1.id)
check('formulaire depuis un produit -> 200', r.status_code == 200, r.status_code)
check('formulaire depuis un produit : ligne pré-remplie',
      ('value="%d" selected' % p1.id) in r.content.decode())

print('\n== 2. Création, totaux et catalogue ==')
data = {
    'client_nom': 'CHKD Client Devis',
    'client_email': 'chkd_devis_%s@test.tn' % TAG,
    'client_tel': '+216 00 000 000',
    'client_adresse': 'Tunis',
    'sujet': 'Site web',
    'message': 'Livraison sous 30 jours.',
    'statut': 'nouveau',
    'tva': '19',
    'notes': 'Note interne.',
    'projet': str(projet.id),
    'lignes-TOTAL_FORMS': '2',
    'lignes-INITIAL_FORMS': '0',
    'lignes-MIN_NUM_FORMS': '0',
    'lignes-MAX_NUM_FORMS': '1000',
    'lignes-0-produit': str(p1.id),
    'lignes-0-designation': p1.nom,
    'lignes-0-quantite': '2',
    'lignes-0-prix_unitaire': '100.00',
    'lignes-0-remise': '0',
    'lignes-1-produit': str(p2.id),
    'lignes-1-designation': p2.nom,
    'lignes-1-quantite': '1',
    'lignes-1-prix_unitaire': '50.00',
    'lignes-1-remise': '10',
}
r = c.post('/admin/devis/nouveau/', data)
check('création devis -> 302', r.status_code == 302, r.status_code)
devis = Devis.objects.filter(client_nom='CHKD Client Devis').first()
check('devis créé', devis is not None)
if devis:
    check('référence DEV générée', devis.reference.startswith('DEV-'), devis.reference)
    check('deux lignes créées', devis.lignes.count() == 2, devis.lignes.count())
    check('total HT = 245.00', devis.montant_ht == Decimal('245.00'), devis.montant_ht)
    check('total TTC = 291.55', devis.montant_ttc == Decimal('291.55'), devis.montant_ttc)
    check('devis lié à la demande', devis.projet_id == projet.id)
    check('ligne remisée = 45.00',
          devis.lignes.get(produit=p2).total == Decimal('45.00'))

    r = c.get('/admin/devis/%d/' % devis.id)
    check('détail devis -> 200', r.status_code == 200, r.status_code)
    body = r.content.decode()
    check('détail : produits visibles', p1.nom in body and p2.nom in body)
    check('détail : total TTC visible',
          ('291,55' in body or '291.55' in body))
    check('détail : catalogue visible', 'Catalogue produits' in body)

    r = c.get('/admin/devis/%d/imprimer/' % devis.id)
    check('impression devis -> 200', r.status_code == 200, r.status_code)
    body = r.content.decode()
    check('impression devis : référence', devis.reference in body)
    check('impression devis : TVA', 'TVA' in body)
    check('impression devis : total TTC',
          ('291,55' in body or '291.55' in body))

print('\n== 3. Envoi, acceptation, conversion en vente ==')
if devis:
    with patch('studio.views_devis.envoyer_email') as mock_mail:
        r = c.post('/admin/devis/%d/' % devis.id, donnees_devis(devis, 'envoyer'))
    check('envoi devis -> 302', r.status_code == 302, r.status_code)
    devis.refresh_from_db()
    projet.refresh_from_db()
    check('devis marqué envoyé', devis.statut == 'envoye', devis.statut)
    check('date d\'envoi renseignée', devis.date_envoi is not None)
    check('email appelé une fois', mock_mail.call_count == 1, mock_mail.call_count)
    check('email destinataire correct',
          mock_mail.call_args and mock_mail.call_args[0][3] == ['chkd_devis_%s@test.tn' % TAG],
          mock_mail.call_args)
    check('demande marquée répondue', projet.a_repondu is True)

    r = c.post('/admin/devis/%d/' % devis.id, donnees_devis(devis, 'accepter'))
    check('acceptation devis -> 302', r.status_code == 302, r.status_code)
    devis.refresh_from_db()
    check('devis accepté', devis.statut == 'accepte', devis.statut)
    check('date d\'acceptation renseignée', devis.date_acceptation is not None)

    with patch('studio.views_devis.envoyer_email'):
        r = c.post('/admin/devis/%d/' % devis.id, donnees_devis(devis, 'envoyer'))
    check('renvoi d\'un devis accepté -> 302', r.status_code == 302, r.status_code)
    devis.refresh_from_db()
    check('le renvoi ne rétrograde pas le statut',
          devis.statut == 'accepte', devis.statut)

    r = c.post('/admin/devis/%d/' % devis.id, donnees_devis(devis, 'convertir'))
    check('conversion devis -> 302', r.status_code == 302, r.status_code)
    devis.refresh_from_db()
    check('devis converti', devis.statut == 'converti', devis.statut)
    ventes = Vente.objects.filter(devis=devis)
    check('deux ventes créées', ventes.count() == 2, ventes.count())
    check('vente liée au bon produit', ventes.filter(produit=p1).exists())
    check('quantité de vente conservée',
          ventes.get(produit=p1).quantite == 2)
    check('prix de vente conservé',
          ventes.get(produit=p1).prix_unitaire == Decimal('100.00'))

    r = c.post('/admin/devis/%d/' % devis.id, donnees_devis(devis, 'accepter'))
    check('acceptation après conversion -> 302', r.status_code == 302, r.status_code)
    devis.refresh_from_db()
    check('la conversion n\'est pas rétrogradée',
          devis.statut == 'converti', devis.statut)

print('\n== 4. Page ventes, saisie manuelle et suppression ==')
r = c.get('/admin/ventes/')
check('liste ventes -> 200', r.status_code == 200, r.status_code)
body = r.content.decode()
check('liste ventes : produit visible', p1.nom in body)
check('liste ventes : devis visible', devis.reference in body if devis else False)

r = c.post('/admin/ventes/', {
    'action': 'create', 'produit': str(p1.id), 'quantite': '3',
    'prix_unitaire': '', 'client_nom': 'CHKD Vente Manuelle', 'devis': '',
})
check('vente manuelle -> 302', r.status_code == 302, r.status_code)
vente_tenant = Vente.objects.create(
    erp_client=tenant, produit=p_tenant, quantite=1,
    prix_unitaire=Decimal('999.00'), client_nom='CHK Tenant Vente')
r = c.post('/admin/ventes/', {
    'action': 'supprimer', 'vente_id': str(vente_tenant.id)})
check('vente tenant : suppression refusée', r.status_code == 404, r.status_code)
check('vente tenant : toujours présente',
      Vente.objects.filter(pk=vente_tenant.pk).exists())

vente = Vente.objects.filter(client_nom='CHKD Vente Manuelle').first()
check('vente manuelle créée', vente is not None)
if vente:
    check('prix manuel = prix produit',
          vente.prix_unitaire == p1.prix_vente, vente.prix_unitaire)
    check('total vente = 300.00', vente.total == Decimal('300.00'), vente.total)
    r = c.post('/admin/ventes/', {
        'action': 'supprimer', 'vente_id': str(vente.id)})
    check('suppression vente -> 302', r.status_code == 302, r.status_code)
    check('vente supprimée', not Vente.objects.filter(pk=vente.pk).exists())

print('\n== 5. Préfacture depuis le devis, impression, facture ==')
if devis:
    r = c.get('/admin/prefactures/nouvelle/?devis=%d' % devis.id)
    check('formulaire préfacture depuis devis -> 200',
          r.status_code == 200, r.status_code)
    body = r.content.decode()
    check('préfacture : client repris', devis.client_nom in body)
    check('préfacture : lignes reprises', p1.nom in body and p2.nom in body)

    data_pf = {
        'devis': str(devis.id), 'vente': '',
        'client_nom': devis.client_nom,
        'client_email': devis.client_email,
        'client_adresse': devis.client_adresse,
        'date_validite': '2026-12-31',
        'statut': 'brouillon',
        'tva': '19',
        'notes': 'Proforma.',
        'lignes-TOTAL_FORMS': '2',
        'lignes-INITIAL_FORMS': '0',
        'lignes-MIN_NUM_FORMS': '0',
        'lignes-MAX_NUM_FORMS': '1000',
        'lignes-0-produit': str(p1.id),
        'lignes-0-designation': p1.nom,
        'lignes-0-quantite': '2',
        'lignes-0-prix_unitaire': '100.00',
        'lignes-0-remise': '0',
        'lignes-1-produit': str(p2.id),
        'lignes-1-designation': p2.nom,
        'lignes-1-quantite': '1',
        'lignes-1-prix_unitaire': '50.00',
        'lignes-1-remise': '10',
    }
    r = c.post('/admin/prefactures/nouvelle/', data_pf)
    check('création préfacture -> 302', r.status_code == 302, r.status_code)
    pf = PreFacture.objects.filter(devis=devis).first()
    check('préfacture créée', pf is not None)
    if pf:
        check('numéro PRE généré', pf.numero.startswith('PRE-'), pf.numero)
        check('préfacture : deux lignes', pf.lignes.count() == 2, pf.lignes.count())
        check('préfacture : total HT 245.00',
              pf.montant_ht == Decimal('245.00'), pf.montant_ht)
        check('préfacture : total TTC 291.55',
              pf.montant_ttc == Decimal('291.55'), pf.montant_ttc)
        check('préfacture liée au devis', pf.devis_id == devis.id)

        r = c.get('/admin/prefactures/%d/' % pf.id)
        check('détail préfacture -> 200', r.status_code == 200, r.status_code)
        check('détail préfacture : numéro', pf.numero in r.content.decode())

        r = c.get('/admin/prefactures/%d/imprimer/' % pf.id)
        check('impression préfacture -> 200', r.status_code == 200, r.status_code)
        body = r.content.decode()
        check('impression : titre', 'PRÉFACTURE' in body)
        check('impression : client', pf.client_nom in body)
        check('impression : total TTC',
              ('291,55' in body or '291.55' in body))

        r = c.post('/admin/prefactures/%d/' % pf.id, {'action': 'convertir'})
        check('conversion préfacture -> 302', r.status_code == 302, r.status_code)
        pf.refresh_from_db()
        check('préfacture convertie', pf.statut == 'convertie', pf.statut)
        facture = Facture.objects.filter(client_nom=pf.client_nom).first()
        check('facture créée', facture is not None)
        if facture:
            check('facture : montant TTC repris',
                  facture.montant_ttc == pf.montant_ttc, facture.montant_ttc)
            check('facture : numéro FAC généré',
                  facture.numero.startswith('FAC-'), facture.numero)
            check('facture : préfacture liée',
                  facture.prefacture_id == pf.id, facture.prefacture_id)
            check('facture : deux lignes figées',
                  facture.lignes.count() == 2, facture.lignes.count())
            check('facture : email client repris',
                  facture.client_email == pf.client_email)
            check('facture : notes reprises', facture.notes == pf.notes)
            check('conversion -> page facture personnalisée',
                  r.url.endswith('/admin/factures/%d/' % facture.id), r.url)

            r = c.get('/admin/factures/')
            check('liste factures -> 200', r.status_code == 200, r.status_code)
            body = r.content.decode()
            check('liste factures : document visible', facture.numero in body)
            check('liste factures : client visible', facture.client_nom in body)

            r = c.get('/admin/factures/%d/' % facture.id)
            check('détail facture -> 200', r.status_code == 200, r.status_code)
            body = r.content.decode()
            check('détail facture : numéro', facture.numero in body)
            check('détail facture : lignes', p1.nom in body and p2.nom in body)
            check('détail facture : total TTC',
                  ('291,55' in body or '291.55' in body))

            r = c.get('/admin/factures/%d/imprimer/' % facture.id)
            check('impression facture -> 200', r.status_code == 200, r.status_code)
            body = r.content.decode()
            check('impression facture : titre', 'FACTURE' in body)
            check('impression facture : client', facture.client_nom in body)
            check('impression facture : total TTC',
                  ('291,55' in body or '291.55' in body))

            r = c.post('/admin/factures/%d/' % facture.id,
                       {'action': 'marquer_payee'})
            check('facture marquée payée -> 302', r.status_code == 302, r.status_code)
            facture.refresh_from_db()
            check('facture payée', facture.payee is True)
            check('date de paiement renseignée',
                  facture.date_paiement is not None)

            r = c.post('/admin/factures/%d/' % facture.id,
                       {'action': 'marquer_impayee'})
            check('facture marquée impayée -> 302', r.status_code == 302, r.status_code)
            facture.refresh_from_db()
            check('facture impayée', facture.payee is False)
            check('date de paiement effacée', facture.date_paiement is None)

print('\n== 6. Liste des préfactures et catalogue produits ==')
r = c.get('/admin/prefactures/')
check('liste préfactures -> 200', r.status_code == 200, r.status_code)
body = r.content.decode()
check('liste préfactures : document visible',
      pf.numero in body if 'pf' in locals() and pf else False)

r = c.get('/admin/produits/')
check('catalogue produits -> 200', r.status_code == 200, r.status_code)
body = r.content.decode()
check('catalogue : produits visibles', p1.nom in body and p2.nom in body)
check('catalogue : produit tenant absent', p_tenant.nom not in body)
check('catalogue : alerte stock', 'min 2' in body)
check('catalogue : lien devis', ('/admin/devis/nouveau/?produit=%d' % p1.id) in body)

facture_tenant = Facture.objects.create(
    erp_client=tenant, numero='FAC-TENANT-%s' % TAG,
    client_nom='CHK Tenant Facture', montant_ht=Decimal('999.00'),
    tva=Decimal('19'), montant_ttc=Decimal('1188.81'))
r = c.get('/admin/factures/')
check('liste factures : facture tenant exclue',
      facture_tenant.numero not in r.content.decode())
r = c.get('/admin/factures/%d/' % facture_tenant.id)
check('détail facture tenant -> 404', r.status_code == 404, r.status_code)

print('\n== 7. Navigation et cloisonnement ==')
groupes = admin_nav(superuser, '/admin/devis/')
urls = [i['url'] for g in groupes for i in g['items']]
for url in ['/admin/devis/', '/admin/ventes/', '/admin/prefactures/',
            '/admin/factures/', '/admin/produits/']:
    check('nav : %s présent' % url, url in urls)
actifs = [i['active'] for g in groupes for i in g['items'] if i['url'] == '/admin/devis/']
check('nav : devis actif sur une sous-page', actifs == [True], actifs)
groupes_facture = admin_nav(superuser, '/admin/factures/')
actifs_facture = [i['active'] for g in groupes_facture
                  for i in g['items'] if i['url'] == '/admin/factures/']
check('nav : factures actives sur une sous-page', actifs_facture == [True],
      actifs_facture)

alertes_site = Produit.objects.filter(
    erp_client__isnull=True, actif=True,
    stock_actuel__lte=F('stock_minimum')).count()
badges_produits = [i['count'] for g in groupes for i in g['items']
                   if i['url'] == '/admin/produits/']
check('nav : alerte stock tenant exclue',
      badges_produits == [alertes_site], (badges_produits, alertes_site))

editeur_client = login(editeur)
for url in ['/admin/devis/', '/admin/ventes/', '/admin/prefactures/',
            '/admin/factures/', '/admin/produits/']:
    check('rôle Editeur : %s -> 403' % url,
          editeur_client.get(url).status_code == 403,
          editeur_client.get(url).status_code)

nonstaff_client = login(commercial_nonstaff)
check('commercial non-staff : devis -> 403',
      nonstaff_client.get('/admin/devis/').status_code == 403)
check('anonyme : devis -> 302', anon.get('/admin/devis/').status_code == 302)
check('anonyme : ventes -> 302', anon.get('/admin/ventes/').status_code == 302)
check('anonyme : factures -> 302', anon.get('/admin/factures/').status_code == 302)

raise SystemExit(report())
