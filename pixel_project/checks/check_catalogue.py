"""Gestion du catalogue du site dans l'espace admin.

Parcours vérifié :
- consultation du catalogue par Commercial/Comptable, écriture Admin/SuperAdmin ;
- création, modification et archivage d'un produit ;
- mouvements de stock (entrée, sortie, ajustement) et historique ;
- création/modification/suppression des catégories et fournisseurs ;
- cloisonnement des produits, catégories et fournisseurs GestiActiv.
"""
import atexit
import time
from decimal import Decimal

from _common import HOST_APEX as APEX, bootstrap, check, report

bootstrap()

from django.contrib.auth.models import Group, User
from django.test import Client

from studio.forms_catalogue import ProduitForm
from studio.models import (
    Categorie, ERPClient, Fournisseur, Produit,
)

for name in ['SuperAdmin', 'Admin', 'Commercial', 'Comptable', 'Editeur']:
    Group.objects.get_or_create(name=name)

TAG = str(int(time.time()))[-7:]
NOM_PRODUIT = 'CHK CAT Produit ' + TAG


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


admin_user = mkuser('chk_cat_admin', ['Admin'], staff=True)
commercial = mkuser('chk_cat_commercial', ['Commercial'], staff=True)
editeur = mkuser('chk_cat_editeur', ['Editeur'], staff=True)
anon = Client(HTTP_HOST=APEX)
c = login(admin_user)
cc = login(commercial)

tenant = ERPClient.objects.create(
    company_name='CHK CAT Tenant ' + TAG, contact_name='Tenant',
    email='chk_cat_tenant_%s@test.tn' % TAG)
site_cat = Categorie.objects.create(
    nom='CHK CAT Site ' + TAG, description='Catégorie du site')
site_supplier = Fournisseur.objects.create(
    nom='CHK CAT Fournisseur ' + TAG, contact='Service achat',
    telephone='+216 00 000 000', email='supplier_%s@test.tn' % TAG,
    adresse='Tunis')
tenant_cat = Categorie.objects.create(
    erp_client=tenant, nom='CHK CAT Tenant Cat ' + TAG)
tenant_supplier = Fournisseur.objects.create(
    erp_client=tenant, nom='CHK CAT Tenant Sup ' + TAG)
tenant_product = Produit.objects.create(
    erp_client=tenant, nom='CHK CAT Tenant Produit ' + TAG,
    categorie=tenant_cat, fournisseur=tenant_supplier,
    prix_vente=Decimal('999.00'), stock_actuel=3, stock_minimum=1)


def cleanup():
    try:
        Produit.objects.filter(nom__startswith='CHK CAT Produit').delete()
        Categorie.objects.filter(nom__startswith='CHK CAT').delete()
        Fournisseur.objects.filter(nom__startswith='CHK CAT').delete()
        ERPClient.objects.filter(
            company_name__startswith='CHK CAT Tenant').delete()
        for u in (admin_user, commercial, editeur):
            u.delete()
    except Exception:
        pass


atexit.register(cleanup)

print('== 1. Accès et cloisonnement ==')
r = c.get('/admin/produits/')
check('catalogue admin -> 200', r.status_code == 200, r.status_code)
body = r.content.decode()
check('catalogue : produit tenant absent', tenant_product.nom not in body)
check('catalogue : bouton nouveau produit', '/admin/produits/nouveau/' in body)
check('catalogue : lien catégories', '/admin/produits/categories/' in body)
check('catalogue : lien fournisseurs', '/admin/produits/fournisseurs/' in body)

r = cc.get('/admin/produits/')
check('commercial : catalogue en lecture -> 200', r.status_code == 200)
check('commercial : pas de création produit',
      '/admin/produits/nouveau/' not in r.content.decode())
check('commercial : création produit -> 403',
      cc.get('/admin/produits/nouveau/').status_code == 403)
check('commercial : détail tenant -> 404',
      c.get('/admin/produits/%d/' % tenant_product.id).status_code == 404)

check('editeur : catalogue -> 403',
      login(editeur).get('/admin/produits/').status_code == 403)
check('anonyme : catalogue -> 302',
      anon.get('/admin/produits/').status_code == 302)

check('catégorie tenant : édition -> 404',
      c.get('/admin/produits/categories/?edit=%d' % tenant_cat.id).status_code == 404)
check('fournisseur tenant : édition -> 404',
      c.get('/admin/produits/fournisseurs/?edit=%d' % tenant_supplier.id).status_code == 404)

print('\n== 2. Création et validation produit ==')
form = ProduitForm()
check('formulaire : catégories du site seulement',
      not form.fields['categorie'].queryset.filter(pk=tenant_cat.pk).exists())
check('formulaire : fournisseurs du site seulement',
      not form.fields['fournisseur'].queryset.filter(
          pk=tenant_supplier.pk).exists())

data = {
    'nom': NOM_PRODUIT,
    'categorie': site_cat.id,
    'fournisseur': site_supplier.id,
    'prix_achat': '100.00',
    'prix_vente': '150.00',
    'stock_minimum': '3',
    'code_barre': 'CAT' + TAG,
    'actif': 'on',
    'stock_initial': '10',
}
r = c.post('/admin/produits/nouveau/', data)
check('création produit -> 302', r.status_code == 302, r.status_code)
produit = Produit.objects.filter(nom=NOM_PRODUIT).first()
check('produit créé', produit is not None)
if produit:
    check('produit : sans entreprise', produit.erp_client_id is None)
    check('produit : catégorie du site', produit.categorie_id == site_cat.id)
    check('produit : fournisseur du site', produit.fournisseur_id == site_supplier.id)
    check('produit : prix de vente', produit.prix_vente == Decimal('150.00'))
    check('produit : stock initial', produit.stock_actuel == 10)
    check('produit : code-barres', produit.code_barre == 'CAT' + TAG)
    check('produit : redirection fiche',
          r.url.endswith('/admin/produits/%d/' % produit.id), r.url)
    mouvement = produit.mouvements.first()
    check('création : mouvement de stock', mouvement is not None)
    if mouvement:
        check('création : entrée', mouvement.type == 'entree')
        check('création : stock avant 0', mouvement.stock_avant == 0)
        check('création : stock après 10', mouvement.stock_apres == 10)
        check('création : référence stock initial',
              mouvement.reference == 'Stock initial')
        check('création : auteur', mouvement.cree_par == admin_user.username)
    r = c.get('/admin/produits/%d/' % produit.id)
    check('fiche produit -> 200', r.status_code == 200, r.status_code)
    body = r.content.decode()
    check('fiche produit : nom', NOM_PRODUIT in body)
    check('fiche produit : catégorie', site_cat.nom in body)
    check('fiche produit : historique', 'Historique des mouvements' in body)
    check('fiche produit : mouvement initial', 'Stock initial' in body)
    r = c.get('/admin/produits/')
    check('liste : produit créé visible', NOM_PRODUIT in r.content.decode())

# Catégorie d'un tenant refusée par le formulaire.
data_tenant = dict(data, nom='CHK CAT Produit Tenant ' + TAG,
                   categorie=tenant_cat.id)
r = c.post('/admin/produits/nouveau/', data_tenant)
check('création avec catégorie tenant : refusée', r.status_code == 200)
check('création avec catégorie tenant : aucun produit',
      not Produit.objects.filter(nom='CHK CAT Produit Tenant ' + TAG).exists())

# Code-barres déjà utilisé.
data_dup = dict(data, nom='CHK CAT Produit Dup ' + TAG)
r = c.post('/admin/produits/nouveau/', data_dup)
check('code-barres en double : refusé', r.status_code == 200)
check('code-barres en double : aucun produit',
      not Produit.objects.filter(nom='CHK CAT Produit Dup ' + TAG).exists())
check('code-barres en double : message',
      'déjà utilisé' in r.content.decode())

# Prix négatif et stock initial négatif.
for champ, valeur, label in [
        ('prix_vente', '-1', 'prix négatif'),
        ('prix_achat', '-1', 'prix achat négatif'),
        ('stock_initial', '-1', 'stock initial négatif')]:
    payload = dict(data, nom='CHK CAT Produit KO ' + TAG, **{champ: valeur})
    r = c.post('/admin/produits/nouveau/', payload)
    check('%s : refusé' % label, r.status_code == 200)
    check('%s : aucun produit' % label,
          not Produit.objects.filter(nom='CHK CAT Produit KO ' + TAG).exists())

print('\n== 3. Modification et statut ==')
if produit:
    r = c.post('/admin/produits/%d/modifier/' % produit.id, {
        **data,
        'nom': 'CHK CAT Produit Modifié ' + TAG,
        'prix_vente': '175.00',
        'stock_minimum': '4',
        'actif': 'on',
    })
    check('modification produit -> 302', r.status_code == 302, r.status_code)
    produit.refresh_from_db()
    check('modification : nom', produit.nom == 'CHK CAT Produit Modifié ' + TAG)
    check('modification : prix', produit.prix_vente == Decimal('175.00'))
    check('modification : stock inchangé', produit.stock_actuel == 10)
    check('modification : un seul mouvement initial',
          produit.mouvements.count() == 1)

    r = c.post('/admin/produits/%d/' % produit.id,
               {'action': 'statut'})
    check('archivage produit -> 302', r.status_code == 302, r.status_code)
    produit.refresh_from_db()
    check('produit archivé', produit.actif is False)
    r = c.post('/admin/produits/%d/' % produit.id,
               {'action': 'statut'})
    produit.refresh_from_db()
    check('produit réactivé', produit.actif is True)

    r = cc.post('/admin/produits/%d/' % produit.id,
                {'action': 'statut'})
    check('commercial : archivage interdit -> 403', r.status_code == 403)
    produit.refresh_from_db()
    check('commercial : statut inchangé', produit.actif is True)

print('\n== 4. Mouvements de stock ==')
if produit:
    r = c.post('/admin/produits/%d/' % produit.id, {
        'action': 'stock', 'type': 'entree', 'quantite': '5',
        'reference': 'BON-ENTREE-' + TAG, 'notes': 'Réapprovisionnement',
    })
    check('entrée stock -> 302', r.status_code == 302, r.status_code)
    produit.refresh_from_db()
    check('entrée stock : stock 15', produit.stock_actuel == 15)
    m = produit.mouvements.order_by('-date_mouvement').first()
    check('entrée stock : mouvement créé',
          m is not None and m.type == 'entree')
    if m:
        check('entrée stock : avant 10', m.stock_avant == 10)
        check('entrée stock : après 15', m.stock_apres == 15)
        check('entrée stock : référence', m.reference == 'BON-ENTREE-' + TAG)

    r = c.post('/admin/produits/%d/' % produit.id, {
        'action': 'stock', 'type': 'sortie', 'quantite': '3',
        'reference': 'BON-SORTIE-' + TAG,
    })
    check('sortie stock -> 302', r.status_code == 302, r.status_code)
    produit.refresh_from_db()
    check('sortie stock : stock 12', produit.stock_actuel == 12)

    r = c.post('/admin/produits/%d/' % produit.id, {
        'action': 'stock', 'type': 'sortie', 'quantite': '99',
    })
    check('sortie excessive : refusée', r.status_code == 200)
    check('sortie excessive : message',
          'Stock insuffisant' in r.content.decode())
    produit.refresh_from_db()
    check('sortie excessive : stock inchangé', produit.stock_actuel == 12)

    avant_mouvements = produit.mouvements.count()
    r = c.post('/admin/produits/%d/' % produit.id, {
        'action': 'stock', 'type': 'entree', 'quantite': '0',
    })
    check('entrée quantité 0 : refusée', r.status_code == 200)
    check('entrée quantité 0 : aucun mouvement',
          produit.mouvements.count() == avant_mouvements)

    r = c.post('/admin/produits/%d/' % produit.id, {
        'action': 'stock', 'type': 'ajustement', 'quantite': '7',
        'reference': 'INVENTAIRE-' + TAG,
    })
    check('ajustement stock -> 302', r.status_code == 302, r.status_code)
    produit.refresh_from_db()
    check('ajustement stock : stock 7', produit.stock_actuel == 7)
    m = produit.mouvements.order_by('-date_mouvement').first()
    if m:
        check('ajustement : avant 12', m.stock_avant == 12)
        check('ajustement : après 7', m.stock_apres == 7)

    r = cc.get('/admin/produits/%d/' % produit.id)
    check('commercial : fiche en lecture -> 200', r.status_code == 200)
    check('commercial : pas de formulaire stock',
          'Enregistrer le mouvement' not in r.content.decode())
    r = cc.post('/admin/produits/%d/' % produit.id, {
        'action': 'stock', 'type': 'entree', 'quantite': '1',
    })
    check('commercial : mouvement interdit -> 403', r.status_code == 403)
    produit.refresh_from_db()
    check('commercial : stock inchangé', produit.stock_actuel == 7)

print('\n== 5. Catégories ==')
r = c.get('/admin/produits/categories/')
check('catégories -> 200', r.status_code == 200, r.status_code)
body = r.content.decode()
check('catégories : catégorie du site', site_cat.nom in body)
check('catégories : catégorie tenant absente', tenant_cat.nom not in body)
check('catégories : formulaire création', 'Nouvelle catégorie' in body)

r = c.post('/admin/produits/categories/', {
    'action': 'create', 'nom': 'CHK CAT Nouvelle ' + TAG,
    'description': 'Créée par le test',
})
check('création catégorie -> 302', r.status_code == 302, r.status_code)
nouvelle_cat = Categorie.objects.filter(nom='CHK CAT Nouvelle ' + TAG).first()
check('catégorie créée', nouvelle_cat is not None)
if nouvelle_cat:
    check('catégorie : sans entreprise', nouvelle_cat.erp_client_id is None)

r = c.post('/admin/produits/categories/', {
    'action': 'create', 'nom': 'CHK CAT Nouvelle ' + TAG,
})
check('catégorie en double : refusée', r.status_code == 200)
check('catégorie en double : message', 'porte déjà ce nom' in r.content.decode())

if nouvelle_cat:
    r = c.get('/admin/produits/categories/?edit=%d' % nouvelle_cat.id)
    check('édition catégorie -> 200', r.status_code == 200)
    check('édition catégorie : nom prérempli',
          ('value="%s"' % nouvelle_cat.nom) in r.content.decode())
    r = c.post('/admin/produits/categories/', {
        'action': 'update', 'categorie_id': nouvelle_cat.id,
        'nom': 'CHK CAT Modifiée ' + TAG, 'description': 'Mise à jour',
    })
    check('modification catégorie -> 302', r.status_code == 302, r.status_code)
    nouvelle_cat.refresh_from_db()
    check('catégorie modifiée', nouvelle_cat.nom == 'CHK CAT Modifiée ' + TAG)

r = c.post('/admin/produits/categories/', {
    'action': 'delete', 'categorie_id': site_cat.id,
}, follow=True)
check('suppression catégorie utilisée : refusée', r.status_code == 200)
check('catégorie utilisée : conservée',
      Categorie.objects.filter(pk=site_cat.pk).exists())
check('suppression catégorie utilisée : message',
      'Impossible de supprimer' in r.content.decode())

if nouvelle_cat:
    r = c.post('/admin/produits/categories/', {
        'action': 'delete', 'categorie_id': nouvelle_cat.id,
    })
    check('suppression catégorie vide -> 302', r.status_code == 302)
    check('catégorie vide supprimée',
          not Categorie.objects.filter(pk=nouvelle_cat.pk).exists())

r = cc.post('/admin/produits/categories/', {
    'action': 'create', 'nom': 'CHK CAT Interdite ' + TAG,
})
check('commercial : création catégorie -> 403', r.status_code == 403)
check('commercial : catégorie non créée',
      not Categorie.objects.filter(nom='CHK CAT Interdite ' + TAG).exists())

print('\n== 6. Fournisseurs ==')
r = c.get('/admin/produits/fournisseurs/')
check('fournisseurs -> 200', r.status_code == 200, r.status_code)
body = r.content.decode()
check('fournisseurs : fournisseur du site', site_supplier.nom in body)
check('fournisseurs : fournisseur tenant absent', tenant_supplier.nom not in body)
check('fournisseurs : formulaire création', 'Nouveau fournisseur' in body)

r = c.post('/admin/produits/fournisseurs/', {
    'action': 'create', 'nom': 'CHK CAT Nouveau Sup ' + TAG,
    'contact': 'Achat', 'telephone': '+216 11 111 111',
    'email': 'new_sup_%s@test.tn' % TAG, 'adresse': 'Sfax',
})
check('création fournisseur -> 302', r.status_code == 302, r.status_code)
nouveau_sup = Fournisseur.objects.filter(
    nom='CHK CAT Nouveau Sup ' + TAG).first()
check('fournisseur créé', nouveau_sup is not None)
if nouveau_sup:
    check('fournisseur : sans entreprise', nouveau_sup.erp_client_id is None)

r = c.post('/admin/produits/fournisseurs/', {
    'action': 'create', 'nom': 'CHK CAT Nouveau Sup ' + TAG,
})
check('fournisseur en double : refusé', r.status_code == 200)
check('fournisseur en double : message', 'porte déjà ce nom' in r.content.decode())

if nouveau_sup:
    r = c.get('/admin/produits/fournisseurs/?edit=%d' % nouveau_sup.id)
    check('édition fournisseur -> 200', r.status_code == 200)
    r = c.post('/admin/produits/fournisseurs/', {
        'action': 'update', 'fournisseur_id': nouveau_sup.id,
        'nom': 'CHK CAT Sup Modifié ' + TAG, 'contact': 'Direction',
        'telephone': '', 'email': '', 'adresse': '',
    })
    check('modification fournisseur -> 302', r.status_code == 302, r.status_code)
    nouveau_sup.refresh_from_db()
    check('fournisseur modifié', nouveau_sup.nom == 'CHK CAT Sup Modifié ' + TAG)

r = c.post('/admin/produits/fournisseurs/', {
    'action': 'delete', 'fournisseur_id': site_supplier.id,
}, follow=True)
check('suppression fournisseur utilisé : refusée', r.status_code == 200)
check('fournisseur utilisé : conservé',
      Fournisseur.objects.filter(pk=site_supplier.pk).exists())
check('suppression fournisseur utilisé : message',
      'Impossible de supprimer' in r.content.decode())

if nouveau_sup:
    r = c.post('/admin/produits/fournisseurs/', {
        'action': 'delete', 'fournisseur_id': nouveau_sup.id,
    })
    check('suppression fournisseur vide -> 302', r.status_code == 302)
    check('fournisseur vide supprimé',
          not Fournisseur.objects.filter(pk=nouveau_sup.pk).exists())

r = cc.post('/admin/produits/fournisseurs/', {
    'action': 'create', 'nom': 'CHK CAT Sup Interdit ' + TAG,
})
check('commercial : création fournisseur -> 403', r.status_code == 403)
check('commercial : fournisseur non créé',
      not Fournisseur.objects.filter(
          nom='CHK CAT Sup Interdit ' + TAG).exists())

print('\n== 7. Cohérence finale ==')
if produit:
    check('produit : mouvements historisés',
          produit.mouvements.count() >= 4, produit.mouvements.count())
    check('produit : toujours dans le catalogue du site',
          Produit.objects.filter(
              pk=produit.pk, erp_client__isnull=True).exists())

report()
