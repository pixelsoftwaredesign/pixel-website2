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
    ConfigurationPaiementEnLigne, NewsletterCampaign, ProjetContact,
    Temoignage,
)

for name in ['SuperAdmin', 'Admin', 'Commercial', 'Comptable', 'Editeur']:
    Group.objects.get_or_create(name=name)


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


admin = mkuser('chk_dp_admin', ['Admin', 'Comptable'], staff=True)
commercial = mkuser('chk_dp_commercial', ['Commercial'], staff=True)
editeur = mkuser('chk_dp_editeur', ['Editeur'], staff=True)
superadmin = mkuser('chk_dp_super', ['SuperAdmin'], staff=True)

print('\n== 1. Jeu de donnees de pagination ==')
# Suite relancable : on repart d'une base propre pour ces modeles.
CommandeECommerce.objects.filter(reference__startswith='CHK').delete()
ProjetContact.objects.filter(nom__startswith='CHKD').delete()
Candidature.objects.filter(nom__startswith='CHKC').delete()
NewsletterCampaign.objects.filter(sujet__startswith='CHKC').delete()
Temoignage.objects.filter(nom__startswith='CHKC').delete()
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
# Une campagne et un temoignage : le tableau editeur a ainsi des lignes
# cliquables a verifier.
NewsletterCampaign.objects.create(sujet='CHKC Campagne', contenu_html='<p>x</p>')
Temoignage.objects.create(nom='CHKC Temoignage', entreprise='Chk', note=5)
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
    pattern = 'cell-strong">(?:<a[^>]*>)?#?(%s\\w*)' % prefix
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
check('editeur : pager campagnes',
      'pxadmin-pager' in body or 'Aucune campagne' in body or 'CHKC' in body)
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

print('\n== 8. Navigation actionnable : KPI cliquables et lignes navigables ==')
# Les cartes de statistiques pointent vers la liste Django admin correspondante.
CARTE = r'<a class="stat-card[^"]*" href="([^"]+)"'


def cartes(html):
    return _re.findall(CARTE, html)


for url, attendu, client in [
    ('/admin/receptions/', '/admin/studio/commandeecommerce/', cc),
    ('/admin/dash/commercial/', '/admin/studio/projetcontact/', cc),
    ('/admin/dash/comptable/', '/admin/studio/commandeecommerce/', cc),
    ('/admin/dash/editeur/', '/admin/studio/newslettercampaign/', cc),
    ('/admin/dash/superadmin/', '/admin/auth/user/', login(superadmin)),
    ('/admin/dash/admin/', '/admin/auth/group/', cc),
]:
    body = client.get(url).content.decode()
    liens = cartes(body)
    check('%s : KPI cliquables' % url, len(liens) >= 3, len(liens))
    check('%s : KPI vers la liste admin' % url,
          any(l.startswith(attendu) for l in liens), liens[:2])
    check('%s : KPI sans cible vide' % url, all(l.strip() for l in liens))

# Les liens de filtre utilisent la syntaxe du list_filter Django (pas __exact
# sur un choix, pas de __in : Django tronque la valeur caractere par caractere).
body = cc.get('/admin/dash/comptable/').content.decode()
check('KPI commande : filtre par statut (syntaxe list_filter)',
      '/admin/studio/commandeecommerce/?statut=en_attente' in body)
check('KPI commande : pas de lookup __in (incompatible Django)',
      'statut__in' not in body)
body = cc.get('/admin/dash/commercial/').content.decode()
check('KPI demande : filtre sur les non repondues',
      '/admin/studio/projetcontact/?a_repondu__exact=0' in body)

# Les cibles des KPI repondent 200 (et non 404) pour un superuser Django admin.
root = mkuser('chk_dp_root', superuser=True, staff=True)
dc = login(root)
for href in set(cartes(cc.get('/admin/receptions/').content.decode())):
    r = dc.get(href)
    check('cible KPI joignable : %s' % href, r.status_code == 200, r.status_code)

# Les lignes de tableau sont cliquables (data-href) et portent un lien
# accessible au clavier dans la premiere colonne.
body = cc.get('/admin/receptions/').content.decode()
check('receptions : lignes cliquables', 'data-href="/admin/studio/commandeecommerce/' in body)
check('receptions : lien accessible dans la cellule',
      _re.search(r'cell-strong"><a href="/admin/studio/commandeecommerce/\d+/change/">', body)
      is not None)
for url, prefix, client in [
    ('/admin/dash/commercial/', '/admin/studio/projetcontact/', cc),
    ('/admin/dash/comptable/', '/admin/studio/commandeecommerce/', cc),
    ('/admin/dash/editeur/', '/admin/studio/temoignage/', cc),
    ('/admin/dash/superadmin/', '/admin/studio/commandeecommerce/', login(superadmin)),
    ('/admin/dash/admin/', '/admin/studio/commandeecommerce/', cc),
]:
    body = client.get(url).content.decode()
    check('%s : lignes cliquables' % url, ('data-href="%s' % prefix) in body)

# Le gestionnaire JS des lignes cliquables est present sur la coquille admin.
body = cc.get('/admin/dash/admin/').content.decode()
check('coquille : gestionnaire des lignes cliquables',
      "tr[data-href]" in body and 'is-clickable' in body)
check('coquille : les boutons internes ne declenchent pas la navigation',
      "closest('a, button, input, select, textarea, form, label')" in body)

print('\n== 9. Filtres et recherche dans l\'admin Django ==')
# Les KPI pointent vers des listes reellement filtrees.
body = dc.get('/admin/studio/commandeecommerce/?statut=en_attente').content.decode()
check('admin commandes : filtre en_attente -> seule la commande en attente',
      'CHKATT' in body and 'CHK00' not in body)
body = dc.get('/admin/studio/commandeecommerce/?statut=livree').content.decode()
check('admin commandes : filtre livree -> pas la commande en attente',
      'CHKATT' not in body)
check('admin commandes : filtre livree -> des commandes livrees',
      len(_re.findall(r'CHK\d\d', body)) >= 10, len(_re.findall(r'CHK\d\d', body)))
body = dc.get('/admin/studio/projetcontact/?a_repondu__exact=0').content.decode()
check('admin demandes : filtre non repondu -> les demandes CHKD sont la',
      'CHKD00' in body)
check('admin commandes : recherche par reference disponible',
      dc.get('/admin/studio/commandeecommerce/?q=CHKATT').status_code == 200)
check('admin commandes : tri par date disponible',
      dc.get('/admin/studio/commandeecommerce/?o=-1').status_code == 200)

print('\n== 10. Aucun lien mort vers l\'administration Django ==')
# Chaque lien "/admin/..." rendu par l'espace d'administration doit resoudre
# vers une vraie page (le "catch-all" de l'admin renvoie un 404 silencieux).
from django.urls import resolve, reverse  # noqa: E402

PAGES_ADMIN = [
    ('/admin/receptions/', cc),
    ('/admin/dash/commercial/', cc),
    ('/admin/dash/comptable/', cc),
    ('/admin/dash/editeur/', cc),
    ('/admin/dash/superadmin/', login(superadmin)),
    ('/admin/dash/admin/', cc),
    ('/admin/roles/', login(superadmin)),
    ('/admin-bancaire/', cc),
]
LIEN_ADMIN = _re.compile(r'(?:href|data-href)="(/admin/[^"{}\s]+)"')
liens_morts = []
nb_liens = 0
for url, client in PAGES_ADMIN:
    body = client.get(url).content.decode()
    trouves = sorted(set(LIEN_ADMIN.findall(body)))
    nb_liens += len(trouves)
    for href in trouves:
        chemin = href.split('?')[0].split('#')[0]
        try:
            match = resolve(chemin)
            if getattr(match.func, '__name__', '') == 'catch_all_view':
                liens_morts.append((url, href))
        except Exception:
            liens_morts.append((url, href))
check('tous les liens /admin/... rendus resolus (%d liens)' % nb_liens,
      not liens_morts, liens_morts[:5])

# Garde-fou statique : chaque cible d'admin citee dans les gabarits de
# l'espace d'administration doit exister (un nom d'URL ou un modele resolu
# par le tag `admin_url`).
import os  # noqa: E402

from django.template import Context, Template  # noqa: E402

from studio.templatetags.admin_ui import admin_url  # noqa: E402

GABARITS = [
    'studio/templates/studio/admin_dashboard_admin.html',
    'studio/templates/studio/admin_dashboard_commercial.html',
    'studio/templates/studio/admin_dashboard_comptable.html',
    'studio/templates/studio/admin_dashboard_editeur.html',
    'studio/templates/studio/admin_dashboard_superadmin.html',
    'studio/templates/studio/admin_receptions_dashboard.html',
    'studio/templates/studio/admin_roles.html',
    'studio/templates/studio/admin_bancaire.html',
    'studio/templates/studio/admin/_stat.html',
]
racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cibles_mortes = []
for rel in GABARITS:
    chemin = os.path.join(racine, rel)
    if not os.path.exists(chemin):
        continue
    source = open(chemin, encoding='utf-8').read()
    for model in set(_re.findall(r'model="([\w.]+)"', source)):
        if not admin_url(model):
            cibles_mortes.append((rel, 'model=%s' % model))
    for nom in set(_re.findall(r"\{%\s*url\s*'(admin:[^']+)'", source)):
        try:
            if nom.endswith(('_change', '_repondre')):
                reverse(nom, args=[1])
            else:
                reverse(nom)
        except Exception:
            cibles_mortes.append((rel, nom))
check('cibles admin citees dans les gabarits toutes valides',
      not cibles_mortes, cibles_mortes[:5])

# Contrat DOM du script de lignes cliquables (admin_base.html) : le script
# cible `tr[data-href]`, pose la classe `is-clickable` (stylee par
# `.panel table.pxadmin-table tbody tr.is-clickable`) et suit le lien
# `data-href`. On verifie que le HTML rendu remplit ce contrat.
LIGNE = _re.compile(r'<tr([^>]*)data-href="([^"]+)"([^>]*)>(.*?)</tr>', _re.S)
contrat = []
nb_lignes = 0
for url, client in PAGES_ADMIN:
    body = client.get(url).content.decode()
    for bloc in _re.findall(r'<table\b.*?</table>', body, _re.S):
        if 'pxadmin-table' not in bloc.split('>')[0]:
            contrat.append((url, 'table sans la classe pxadmin-table'))
            continue
        for attrs_avant, href, attrs_apres, contenu in LIGNE.findall(bloc):
            nb_lignes += 1
            if 'is-clickable' in attrs_avant + attrs_apres:
                # la classe est posee par le JS, pas par le HTML
                contrat.append((url, 'classe is-clickable posee en dur'))
            liens = _re.findall(r'<a\b[^>]*href="([^"]+)"', contenu)
            if not liens:
                contrat.append((url, 'ligne cliquable sans lien accessible'))
            elif liens[0] != href:
                contrat.append((url, 'lien (%s) != data-href (%s)' % (liens[0], href)))
check('contrat DOM des lignes cliquables respectee (%d lignes)' % nb_lignes,
      not contrat and nb_lignes > 0, (contrat[:5], nb_lignes))
check('style de la ligne cliquable present',
      'is-clickable' in open(os.path.join(racine, 'studio/static/css/admin-ui.css'),
                             encoding='utf-8').read())

# Un KPI dont le modele n'est pas resolu devient silencieusement un <div> :
# on verifie donc que chaque tableau de bord expose bien tous ses KPI cliquables.
for url, attendu_nb, client in [
    ('/admin/receptions/', 5, cc),
    ('/admin/dash/commercial/', 4, cc),
    ('/admin/dash/comptable/', 5, cc),
    ('/admin/dash/editeur/', 3, cc),
    ('/admin/dash/superadmin/', 5, login(superadmin)),
    ('/admin/dash/admin/', 4, cc),
    ('/admin-bancaire/', 4, cc),
    ('/admin/roles/', 3, login(superadmin)),
]:
    body = client.get(url).content.decode()
    nb = len(cartes(body))
    check('%s : %d KPI cliquables' % (url, attendu_nb), nb == attendu_nb, nb)

# Les KPI banque pointent sur les listes admin filtrees.
body = cc.get('/admin-bancaire/').content.decode()
check('banque : KPI comptes -> liste admin',
      '/admin/studio/configurationbancaire/' in body)
check('banque : KPI comptes actifs -> filtre is_active',
      'configurationbancaire/?is_active__exact=1' in body)
check('banque : KPI compte par defaut -> filtre est_defaut',
      'configurationbancaire/?est_defaut__exact=1' in body)
check('banque : KPI fournisseurs -> liste admin',
      '/admin/studio/configurationpaiementenligne/' in body)
body = login(superadmin).get('/admin/roles/').content.decode()
check('roles : KPI roles -> liste admin', '/admin/auth/group/' in body)
check('roles : KPI utilisateurs -> liste admin', '/admin/auth/user/' in body)

print('\n== 11. Navigation : badge « a traiter » ==')

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
