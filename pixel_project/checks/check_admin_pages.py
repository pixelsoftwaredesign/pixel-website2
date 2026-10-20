"""Pages de donnees de l'espace d'administration.

Couvre les tableaux de bord metier (receptions, commercial, comptable,
editeur, superadmin, admin) et la configuration bancaire :

- pagination independante par tableau (`?cpage=`, `?dpage=`, `?kpage=`,
  `?page=`, `?tpage=`) sans erreur sur une page hors limites ;
- filtres par statut de commande (`?statut=`) ;
- cloisonnement des roles sur ces pages ;
- CRUD de la configuration bancaire (ajout, edition, suppression,
  valeurs invalides) et bandeau « comment ca marche ».
"""
from _common import HOST_APEX as APEX, bootstrap, check, report

bootstrap()

from django.contrib.auth.models import Group, User
from django.test import Client

from studio.models import (
    Candidature, CommandeECommerce, ConfigurationBancaire,
    ConfigurationPaiementEnLigne, ProjetContact,
)

for name in ['SuperAdmin', 'Admin', 'Commercial', 'Comptable', 'Editeur']:
    Group.objects.get_or_create(name=name)


def mkuser(name, groups=(), staff=True):
    User.objects.filter(username=name).delete()
    u = User.objects.create_user(name, password='secret123', email=name + '@test.tn')
    u.is_staff = staff
    u.save()
    for g in groups:
        u.groups.add(Group.objects.get(name=g))
    return u


def login(user):
    c = Client(HTTP_HOST=APEX)
    c.force_login(user)
    return c


admin = mkuser('chk_dp_admin', ['Admin', 'Comptable'], staff=True)
commercial = mkuser('chk_dp_commercial', ['Commercial'], staff=True)
editeur = mkuser('chk_dp_editeur', ['Editeur'], staff=True)
superadmin = mkuser('chk_dp_super', ['SuperAdmin'], staff=True)

print('\n== 1. Jeu de donnees de pagination ==')
# Suite relancable : on repart d'une base propre pour ces modeles.
CommandeECommerce.objects.filter(reference__startswith='CHK').delete()
ProjetContact.objects.filter(nom__startswith='CHKD').delete()
Candidature.objects.filter(nom__startswith='CHKC').delete()
ConfigurationBancaire.objects.filter(titulaire__startswith='Chk ').delete()
# 45 commandes : 1 en attente (la plus recente), 44 livrees.
for i in range(45):
    CommandeECommerce.objects.create(
        reference='CHK%02d' % i, client_nom='Client %d' % i,
        client_email='chk%d@test.tn' % i, client_adresse='Adresse',
        statut='livree', total_ttc=10)
CommandeECommerce.objects.create(
    reference='CHKATT', client_nom='En attente', client_email='att@test.tn',
    client_adresse='Adresse', statut='en_attente', total_ttc=10)
for i in range(25):
    ProjetContact.objects.create(nom='CHKD%02d' % i, email='chkd%d@test.tn' % i, message='msg')
for i in range(25):
    Candidature.objects.create(nom='CHKC%02d' % i, email='chkc%d@test.tn' % i)
check('45 commandes + 1 en attente creees',
      CommandeECommerce.objects.filter(reference__startswith='CHK').count() == 46)
check('25 demandes creees', ProjetContact.objects.filter(nom__startswith='CHKD').count() == 25)

print('\n== 2. Pagination des tableaux de bord ==')
c = login(superadmin)
import re as _re


def tables(html):
    """Decoupe le HTML en tableaux (`<table ...>...</table>`)."""
    return _re.findall(r'<table\b.*?</table>', html, _re.S)


def refs(html, prefix, index=None):
    """References d'un tableau (colonnes `cell-strong`).

    Une page peut contenir plusieurs tableaux (commandes, demandes,
    candidatures) : `index` selectionne le tableau vise, sinon la recherche
    porte sur tous les tableaux de la page.
    """
    pattern = 'cell-strong">(%s\\w*)' % prefix
    blocks = tables(html)
    if index is not None:
        blocks = blocks[index:index + 1]
    found = []
    for block in blocks:
        found.extend(_re.findall(pattern, block))
    return found


body1 = c.get('/admin/receptions/').content.decode()
check('receptions : 3 tableaux', len(tables(body1)) == 3, len(tables(body1)))
page1_cmd = refs(body1, 'CHK', index=0)
page1_dem = refs(body1, 'CHKD', index=1)
check('receptions page 1 : 10 commandes', len(page1_cmd) == 10, len(page1_cmd))
check('receptions page 1 : commandes recentes (CHKATT puis CHK44)',
      page1_cmd[:2] == ['CHKATT', 'CHK44'], page1_cmd[:3])
check('receptions page 1 : 10 demandes', len(page1_dem) == 10, len(page1_dem))
check('receptions page 1 : pagination affichee', 'pxadmin-pager' in body1)

body2 = c.get('/admin/receptions/?cpage=2').content.decode()
page2_cmd = refs(body2, 'CHK', index=0)
check('cpage=2 : 10 commandes differentes',
      len(page2_cmd) == 10 and set(page2_cmd).isdisjoint(page1_cmd), page2_cmd[:2])
check('cpage=2 : la page des demandes est inchangee',
      refs(body2, 'CHKD', index=1) == page1_dem)

body25 = c.get('/admin/receptions/?dpage=2').content.decode()
check('dpage=2 : les commandes sont inchangees',
      refs(body25, 'CHK', index=0) == page1_cmd)
check('dpage=2 : les demandes sont decalees',
      'CHKD24' not in refs(body25, 'CHKD', index=1) and
      len(refs(body25, 'CHKD', index=1)) == 10)

check('page hors limites (cpage=99) : 200 sans erreur',
      c.get('/admin/receptions/?cpage=99').status_code == 200)
check('page invalide (cpage=abc) : 200 sans erreur',
      c.get('/admin/receptions/?cpage=abc').status_code == 200)
check('page negative (cpage=-4) : 200 sans erreur',
      c.get('/admin/receptions/?cpage=-4').status_code == 200)

print('\n== 3. Filtre par statut (comptable) ==')
cc = login(admin)
body = cc.get('/admin/dash/comptable/').content.decode()
check('comptable : pastilles de filtre', 'px-pill' in body)
check('comptable : libelle du filtre', 'Filtrer les commandes par statut' in body)
check('comptable : lien vers la config bancaire', '/admin-bancaire/' in body)
livrees = refs(cc.get('/admin/dash/comptable/?statut=livree').content.decode(), 'CHK')
check('filtre livree : aucune commande en attente', 'CHKATT' not in livrees, livrees[:3])
check('filtre livree : 10 lignes', len(livrees) == 10, len(livrees))
enatt = refs(cc.get('/admin/dash/comptable/?statut=en_attente').content.decode(), 'CHK')
check('filtre en_attente : uniquement CHKATT', enatt[:1] == ['CHKATT'], enatt[:3])
next_html = cc.get('/admin/dash/comptable/?statut=livree&page=2').content.decode()
check('pagination : le filtre est conserve', 'statut=livree' in next_html and 'page=3' in next_html)
check('statut inconnu ignore : 200', cc.get('/admin/dash/comptable/?statut=zzz').status_code == 200)
vide = cc.get('/admin/dash/comptable/?statut=annulee').content.decode()
check('statut sans resultat : etat vide explicite',
      'Aucune commande pour ce filtre' in vide)

print('\n== 4. Pagination des autres tableaux de bord ==')
body = login(superadmin).get('/admin/dash/editeur/').content.decode()
check('editeur : pager campagnes', 'pxadmin-pager' in body or 'Aucune campagne' in body)
body = login(superadmin).get('/admin/dash/superadmin/').content.decode()
check('superadmin : pager commandes', 'pxadmin-pager' in body)
body = cc.get('/admin/dash/admin/').content.decode()
check('admin : pager commandes', 'pxadmin-pager' in body)
body = cc.get('/admin/dash/commercial/').content.decode()
check('commercial : pager demandes', 'pxadmin-pager' in body)

print('\n== 5. Cloisonnement des roles sur les pages de donnees ==')
check('commercial : pas acces aux commandes (403)',
      login(commercial).get('/admin/dash/comptable/').status_code == 403)
check('editeur : pas acces au commercial (403)',
      login(editeur).get('/admin/dash/commercial/').status_code == 403)
check('comptable : acces a la config bancaire (200)',
      cc.get('/admin-bancaire/').status_code == 200)
check('staff sans role : acces a la page banque (200)',
      login(mkuser('chk_dp_staff')).get('/admin-bancaire/').status_code == 200)
check('anonyme : config bancaire fermee (302)',
      Client(HTTP_HOST=APEX).get('/admin-bancaire/').status_code == 302)

print('\n== 6. Configuration bancaire : interface ==')
body = cc.get('/admin-bancaire/').content.decode()
for token, label in [
    ('data-bank-edit', 'bouton Modifier'),
    ('data-bank-delete', 'suppression avec confirmation'),
    ('bankEditForm', 'formulaire d\'edition'),
    ('Comment ça marche', 'bandeau d\'aide'),
    ('data-bank-form-toggle', 'formulaire d\'ajout repliable'),
]:
    check('banque : %s' % label, token in body)
check('banque : aucune page autonome (coquille admin)', 'pxadmin-sidebar' in body)
cc.post('/admin-bancaire/', {
    'action': 'add_banque', 'banque': 'BIAT', 'titulaire': 'Chk RIB',
    'rib': '1111222233334444555566'})
body = cc.get('/admin-bancaire/').content.decode()
check('banque : RIB masque dans le tableau',
      'cell-mono' in body and '1111222233334444555566' not in body and
      '1111••••5566' in body)
check('banque : RIB complet jamais expose au navigateur',
      'data-rib="' not in body and 'data-rib-mask=' in body)

print('\n== 7. Configuration bancaire : operations ==')
avant = ConfigurationBancaire.objects.count()
r = cc.post('/admin-bancaire/', {
    'action': 'add_banque', 'banque': 'BIAT', 'titulaire': 'Chk SARL',
    'rib': '1234567890123456789012', 'swift': 'BIATTNTT',
    'agence': 'Tunis', 'est_defaut': '1'})
check('ajout : redirection 302', r.status_code == 302, r.status_code)
compte = ConfigurationBancaire.objects.filter(titulaire='Chk SARL').first()
check('ajout : compte cree', compte is not None)
check('ajout : compte par defaut retenu', bool(compte and compte.est_defaut))
check('ajout : base incrementee', ConfigurationBancaire.objects.count() == avant + 1)

cc.post('/admin-bancaire/', {'action': 'add_banque', 'banque': '<inject>',
                             'titulaire': 'Chk Invalide', 'rib': '1'})
invalide = ConfigurationBancaire.objects.filter(titulaire='Chk Invalide').first()
check('ajout : banque inconnue remplacee par une valeur valide',
      bool(invalide) and invalide.get_banque_display() != '<inject>' and invalide.banque == 'BIAT',
      invalide.banque if invalide else None)

r = cc.post('/admin-bancaire/', {
    'action': 'edit_banque', 'edit_id': compte.id, 'banque': 'Attijari',
    'titulaire': 'Chk SARL 2', 'rib': '9999999999999999999999',
    'agence': 'Sfax', 'is_active': '1'})
compte.refresh_from_db()
check('edition : 302', r.status_code == 302, r.status_code)
check('edition : champs mis a jour',
      compte.banque == 'Attijari' and compte.titulaire == 'Chk SARL 2', compte.banque)
check('edition : nouveau RIB pris en compte',
      compte.rib == '9999999999999999999999', compte.rib)
check('edition : case « actif » cochee = compte actif', compte.is_active is True)
r = cc.post('/admin-bancaire/', {
    'action': 'edit_banque', 'edit_id': compte.id, 'banque': 'Attijari',
    'titulaire': 'Chk SARL 3', 'rib': '', 'agence': 'Sfax', 'is_active': '1'})
compte.refresh_from_db()
check('edition : RIB vide = RIB conserve',
      compte.rib == '9999999999999999999999', compte.rib)
check('edition : case « actif » cochee = compte toujours actif', compte.is_active is True)
r = cc.post('/admin-bancaire/', {
    'action': 'edit_banque', 'edit_id': compte.id, 'banque': 'Attijari',
    'titulaire': 'Chk SARL 3', 'rib': '', 'agence': 'Sfax'})
compte.refresh_from_db()
check('edition : case decochee = compte desactive', compte.is_active is False)
r = cc.post('/admin-bancaire/', {'action': 'edit_banque', 'edit_id': 999999,
                                 'banque': 'BIAT', 'titulaire': 'x'})
check('edition : identifiant inconnu -> 404', r.status_code == 404, r.status_code)

r = cc.post('/admin-bancaire/', {'action': 'delete_banque', 'id': compte.id})
check('suppression : 302', r.status_code == 302, r.status_code)
check('suppression : compte retire',
      not ConfigurationBancaire.objects.filter(id=compte.id).exists())

cfg = ConfigurationPaiementEnLigne.objects.first() or ConfigurationPaiementEnLigne.objects.create()
r = cc.post('/admin-bancaire/', {
    'action': 'save_paiement_config', 'config_id': cfg.id,
    'fournisseur': 'paymee', 'instructions': 'Payez ici', 'frais_pourcentage': '2.5',
    'est_actif': '1'})
cfg.refresh_from_db()
check('paiement : 302', r.status_code == 302, r.status_code)
check('paiement : fournisseur enregistre', cfg.fournisseur == 'paymee', cfg.fournisseur)
check('paiement : instructions enregistrees', cfg.instructions == 'Payez ici')

print('\n== 8. Navigation : badge « a traiter » ==')
body = cc.get('/admin/dash/admin/').content.decode()
check('badge de nav present sur la coquille', 'pxadmin-nav-count' in body)
attendu = (CommandeECommerce.objects.filter(statut='en_attente').count() +
           ProjetContact.objects.filter(a_repondu=False).count())
valeurs = _re.findall(r'pxadmin-nav-count[^>]*>(\d+)<', body)
check('badge = commandes en attente + demandes a traiter',
      str(attendu) in valeurs, (attendu, valeurs))
# Le badge disparait quand il n'y a plus rien a traiter.
CommandeECommerce.objects.filter(reference__startswith='CHK').delete()
ProjetContact.objects.filter(nom__startswith='CHKD').delete()
body = cc.get('/admin/dash/admin/').content.decode()
restant = (CommandeECommerce.objects.filter(statut='en_attente').count() +
           ProjetContact.objects.filter(a_repondu=False).count())
if restant == 0:
    check('badge masque quand rien a traiter', 'pxadmin-nav-count' not in body)
else:
    check('badge toujours coherent avec la base',
          str(restant) in _re.findall(r'pxadmin-nav-count[^>]*>(\d+)<', body))

raise SystemExit(report())
