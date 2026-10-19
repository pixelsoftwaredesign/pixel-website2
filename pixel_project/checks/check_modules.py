"""Bout-en-bout : creation / edition / suppression cloisonnees pour les 9 modules.

Pour chaque action de chaque module metier :
  1. le tenant A cree un enregistrement (erp_client = A)          -> 302
  2. le tenant B cree le meme enregistrement (valeurs uniques
     identiques : prouve l'unicite *par entreprise*)              -> 302
  3. A tente d'editer l'enregistrement de B                       -> 404
  4. A tente de supprimer l'enregistrement de B                   -> 302 sans effet
  5. A supprime son propre enregistrement                         -> 302 + supprime
  6. A edite son propre enregistrement (memes valeurs)            -> 302 sans doublon
  7. A edite ses valeurs                                          -> modification persistee
"""
import time

from _common import HOST_GESTIACTIV as GX, bootstrap, check, report

bootstrap()

from django.contrib.auth.models import User
from django.test import Client

from studio import models as M
from studio.models import ERPClient, ERPMembership

TAG = str(int(time.time()))[-7:]


def dep(model, c, **kw):
    """Dependance du tenant (nom distinct des objets crees par les vues)."""
    o, _ = model.objects.get_or_create(erp_client=c, **kw)
    return o


# ─── tenants ────────────────────────────────────────────────
def make_tenant(suffix):
    u = User.objects.create_user(f'gx_mod_{suffix}_{TAG}', password='x',
                                 email=f'gx_mod_{suffix}_{TAG}@t.tn')
    c = ERPClient.objects.create(company_name=f'Tenant {suffix} {TAG}',
                                 activity='sante', owner=u)
    ERPMembership.objects.create(user=u, client=c, role='owner')
    return u, c


UA, A = make_tenant('a')
UB, B = make_tenant('b')

# Nettoyage garanti meme en cas d'exception (sinon les donnees de test
# s'accumulent et faussent les autres suites).
import atexit


def _cleanup():
    for obj in (A, B, UA, UB):
        try:
            obj.delete()
        except Exception:
            pass


atexit.register(_cleanup)


def payloads(c):
    """Charge utile de chaque action, pour le tenant `c`."""
    cand = dep(M.Candidat, c, nom=f'Cand-dep {TAG} {c.id}')
    mon = dep(M.Moniteur, c, nom=f'Mon-dep {TAG} {c.id}')
    veh = dep(M.Vehicule, c, immatriculation=f'IMMdep-{TAG}',
              defaults={'marque': 'Peugeot', 'modele': '208'})
    pat = dep(M.Patient, c, nom=f'Pat-dep {TAG} {c.id}',
              defaults={'date_naissance': '1990-01-01'})
    cli = dep(M.ClientHotel, c, nom=f'Cli-dep {TAG} {c.id}')
    cha = dep(M.Chambre, c, numero=f'CHdep-{TAG}')
    cat = dep(M.Categorie, c, nom=f'Catdep {TAG}')
    four = dep(M.Fournisseur, c, nom=f'Four-dep {TAG} {c.id}')
    prod = dep(M.Produit, c, nom=f'Prod-dep {TAG} {c.id}')
    jcli = dep(M.ClientJuridique, c, nom=f'Jcli-dep {TAG} {c.id}')
    dos = dep(M.DossierJuridique, c, reference=f'REFdep-{TAG}',
              defaults={'client': jcli, 'titre': f'Dossier-dep {TAG}'})
    jour = dep(M.JournalComptable, c, code=f'Jdep{TAG}', defaults={'nom': f'J-dep {TAG}'})
    emp = dep(M.Employe, c, nom=f'Emp-dep {TAG} {c.id}',
              defaults={'email': f'emp{c.id}@t.tn', 'poste': 'Dev',
                        'date_embauche': '2020-01-15'})
    rec = dep(M.PatisserieRecipe, c, nom=f'Recdep {TAG} {c.id}')
    return {
        'cand': cand, 'mon': mon, 'veh': veh, 'pat': pat, 'cli': cli, 'cha': cha,
        'cat': cat, 'four': four, 'prod': prod, 'jcli': jcli, 'dos': dos,
        'jour': jour, 'emp': emp, 'rec': rec,
    }


PA, PB = payloads(A), payloads(B)

# (chemin, action, modele, modele-de-suppression, payload, champ marqueur)
CASES = [
    ('/auto-ecole/', 'add_candidat', M.Candidat, 'candidat',
     lambda p: {'nom': f'Cand {TAG}', 'telephone': '20123456', 'type_permis': 'B'}, 'nom'),
    ('/auto-ecole/', 'add_moniteur', M.Moniteur, 'moniteur',
     lambda p: {'nom': f'Mon {TAG}', 'telephone': '20999999', 'specialite': 'conduite'}, 'nom'),
    ('/auto-ecole/', 'add_vehicule', M.Vehicule, 'vehicule',
     lambda p: {'immatriculation': f'IMM-{TAG}', 'marque': 'Peugeot', 'modele': '208'},
     'immatriculation'),
    ('/auto-ecole/', 'add_lecon', M.Lecon, 'lecon',
     lambda p: {'candidat': p['cand'].id, 'moniteur': p['mon'].id, 'vehicule': p['veh'].id,
                'date_lecon': '2026-11-01T10:00', 'duree': 60}, None),
    ('/auto-ecole/', 'add_examen', M.Examen, 'examen',
     lambda p: {'candidat': p['cand'].id, 'date_examen': '2026-11-05', 'type': 'code'}, None),

    ('/sante/', 'add_patient', M.Patient, 'patient',
     lambda p: {'nom': f'Pat {TAG}', 'date_naissance': '1990-05-04',
                'telephone': '20555111', 'mutuelle': 'CNSS'}, 'nom'),
    ('/sante/', 'add_rdv', M.RendezVous, 'rdv',
     lambda p: {'patient': p['pat'].id, 'medecin': '', 'date_rdv': '2026-11-06T09:30',
                'motif': 'controle'}, None),
    ('/sante/', 'add_facture', M.FacturationSante, 'facture',
     lambda p: {'patient': p['pat'].id, 'montant': 150, 'type': 'consultation'}, None),

    ('/hotel/', 'add_client', M.ClientHotel, 'client',
     lambda p: {'nom': f'Cli {TAG}', 'telephone': '20777888', 'email': 'c@t.tn',
                'nationalite': 'TN'}, 'nom'),
    ('/hotel/', 'add_chambre', M.Chambre, 'chambre',
     lambda p: {'numero': f'CH-{TAG}', 'type': 'double', 'prix': 120, 'etage': 2}, 'numero'),
    ('/hotel/', 'add_reservation', M.ReservationHotel, 'reservation',
     lambda p: {'chambre': p['cha'].id, 'client': p['cli'].id,
                'arrivee': '2026-11-10', 'depart': '2026-11-12'}, None),

    ('/commerce/', 'add_categorie', M.Categorie, 'categorie',
     lambda p: {'nom': f'Cat {TAG}'}, 'nom'),
    ('/commerce/', 'add_produit', M.Produit, 'produit',
     lambda p: {'nom': f'Prod {TAG}', 'categorie': p['cat'].id, 'fournisseur': p['four'].id,
                'prix_achat': 10, 'prix_vente': 20, 'stock': 5}, 'nom'),
    ('/commerce/', 'add_vente', M.Vente, 'vente',
     lambda p: {'produit': p['prod'].id, 'quantite': 2}, None),

    ('/juridique/', 'add_client', M.ClientJuridique, 'client',
     lambda p: {'nom': f'Jcli {TAG}', 'type': 'particulier', 'telephone': '20999888'}, 'nom'),
    ('/juridique/', 'add_dossier', M.DossierJuridique, 'dossier',
     lambda p: {'reference': f'REF-{TAG}', 'client': p['jcli'].id, 'titre': f'Titre {TAG}',
                'type_affaire': 'civil', 'tribunal': 'TPI Tunis'}, 'reference'),
    ('/juridique/', 'add_audience', M.Audience, 'audience',
     lambda p: {'dossier': p['dos'].id, 'date_audience': '2026-11-05', 'lieu': f'Lieu {TAG}'},
     'lieu'),

    ('/comptabilite/', 'add_journal', M.JournalComptable, 'journal',
     lambda p: {'code': f'J{TAG}', 'nom': f'Journal {TAG}'}, 'code'),
    ('/comptabilite/', 'add_ecriture', M.EcritureComptable, 'ecriture',
     lambda p: {'date_ecriture': '2026-11-07', 'libelle': f'Ecr {TAG}', 'compte_debit': '601',
                'compte_credit': '401', 'montant': 100, 'journal': p['jour'].id}, 'libelle'),
    ('/comptabilite/', 'add_facture', M.Facture, 'facture',
     lambda p: {'numero': f'F-{TAG}', 'client_nom': f'Client {TAG}', 'matricule': 'M1',
                'montant_ht': 1000, 'tva': 19}, 'numero'),

    ('/rh/', 'add_employe', M.Employe, 'employe',
     lambda p: {'nom': f'Emp {TAG}', 'email': f'e{TAG}@t.tn', 'poste': 'Dev',
                'departement': 'IT', 'date_embauche': '2020-01-15', 'salaire': 2000}, 'nom'),
    ('/rh/', 'add_conge', M.Conge, 'conge',
     lambda p: {'employe': p['emp'].id, 'date_debut': '2026-12-01',
                'date_fin': '2026-12-05', 'type': 'annuel'}, None),
    ('/rh/', 'add_formation', M.Formation, 'formation',
     lambda p: {'employe': p['emp'].id, 'titre': f'Form {TAG}', 'organisme': 'Org',
                'date_debut': '2026-11-01', 'date_fin': '2026-11-05', 'cout': 500}, 'titre'),

    ('/restaurant/', 'add_menu', M.MenuItem, 'menu',
     lambda p: {'nom': f'Menu {TAG}', 'categorie': 'plat', 'prix': 25, 'disponible': '1'}, 'nom'),
    ('/restaurant/', 'add_table', M.TableRestaurant, 'table',
     lambda p: {'numero': f'T-{TAG}', 'capacite': 4, 'statut': 'libre'}, 'numero'),

    ('/patisserie/', 'add_recipe', M.PatisserieRecipe, 'recipe',
     lambda p: {'nom': f'Rec {TAG}', 'categorie': 'patisserie',
                'cout_production': 5, 'prix_vente': 12}, 'nom'),
    ('/patisserie/', 'add_product', M.PatisserieProduct, 'product',
     lambda p: {'nom': f'Bp {TAG}', 'recette': p['rec'].id, 'stock_actuel': 10,
                'prix_vente': 15, 'actif': '1'}, 'nom'),
]

EDIT_PERSIST = {
    ('/auto-ecole/', 'add_candidat'): ('nom', 'ZZcand-edit', 'nom'),
    ('/auto-ecole/', 'add_moniteur'): ('specialite', 'ZZ-edit-spec', 'specialite'),
    ('/auto-ecole/', 'add_vehicule'): ('marque', 'Renault', 'marque'),
    ('/auto-ecole/', 'add_lecon'): ('duree', 45, 'duree_minutes'),
    ('/auto-ecole/', 'add_examen'): ('date_examen', '2027-01-02', 'date_examen'),
    ('/sante/', 'add_patient'): ('mutuelle', 'CNAM', 'mutuelle'),
    ('/sante/', 'add_rdv'): ('motif', 'ZZ-edit-rdv', 'motif'),
    ('/sante/', 'add_facture'): ('montant', 321, 'montant'),
    ('/hotel/', 'add_client'): ('telephone', '20999000', 'telephone'),
    ('/hotel/', 'add_chambre'): ('type', 'suite', 'type_chambre'),
    ('/hotel/', 'add_reservation'): ('depart', '2026-11-20', 'date_depart'),
    ('/commerce/', 'add_categorie'): ('nom', 'ZZ-edit-cat', 'nom'),
    ('/commerce/', 'add_produit'): ('prix_vente', 99, 'prix_vente'),
    ('/commerce/', 'add_vente'): ('quantite', 7, 'quantite'),
    ('/juridique/', 'add_client'): ('telephone', '20666000', 'telephone'),
    ('/juridique/', 'add_dossier'): ('tribunal', 'CA Tunis', 'tribunal'),
    ('/juridique/', 'add_audience'): ('lieu', 'ZZ-edit-lieu', 'lieu'),
    ('/comptabilite/', 'add_journal'): ('nom', 'ZZ-edit-journal', 'nom'),
    ('/comptabilite/', 'add_ecriture'): ('libelle', 'ZZ-edit-ecr', 'libelle'),
    ('/comptabilite/', 'add_facture'): ('client_nom', 'ZZ-edit-cli', 'client_nom'),
    ('/rh/', 'add_employe'): ('poste', 'Lead Dev', 'poste'),
    ('/rh/', 'add_conge'): ('type', 'maladie', 'type_conge'),
    ('/rh/', 'add_formation'): ('titre', 'ZZ-edit-form', 'titre'),
    ('/restaurant/', 'add_menu'): ('prix', 33, 'prix'),
    ('/restaurant/', 'add_table'): ('capacite', 9, 'capacite'),
    ('/patisserie/', 'add_recipe'): ('prix_vente', 21, 'prix_vente'),
    ('/patisserie/', 'add_product'): ('stock_actuel', 55, 'stock_actuel'),
}

ca = Client(HTTP_HOST=GX)
ca.force_login(UA)
cb = Client(HTTP_HOST=GX)
cb.force_login(UB)

created = []   # (modele, id_A, modele_nom, chemin)
print(f'== 9 modules, {len(CASES)} actions de creation (tag {TAG}) ==')
for path, action, model, del_name, mk, marker_field in CASES:
    label = f'{path:16s} {action}'
    try:
        pa, pb = mk(PA), mk(PB)

        # 1. creation par A
        n0 = model.objects.filter(erp_client=A).count()
        r = ca.post(path, {'action': action, **pa})
        n1 = model.objects.filter(erp_client=A).count()
        objA = model.objects.filter(erp_client=A).order_by('-id').first()
        okA = r.status_code == 302 and n1 == n0 + 1 and objA is not None and objA.erp_client_id == A.id
        check(f'{label} : creation tenant A', okA,
              f'status={r.status_code} n={n0}->{n1}')

        # 2. meme enregistrement pour B (valeurs uniques identiques)
        r = cb.post(path, {'action': action, **pb})
        objB = model.objects.filter(erp_client=B).order_by('-id').first()
        okB = r.status_code == 302 and objB is not None and objB.erp_client_id == B.id
        check(f'{label} : creation tenant B (memes valeurs uniques)', okB,
              f'status={r.status_code}')

        # 3. edition croisee (A edite l'objet de B) -> 404
        r = ca.post(path, {'action': action, 'edit_id': objB.id, **pa})
        check(f'{label} : edition croisee -> 404', r.status_code == 404, r.status_code)

        # 4. suppression croisee (A supprime l'objet de B) -> sans effet
        r = ca.post(path, {'action': 'delete', 'model': del_name, 'id': objB.id})
        still = model.objects.filter(id=objB.id).exists()
        check(f'{label} : suppression croisee sans effet', r.status_code == 302 and still,
              f'status={r.status_code} existe={still}')

        # 4b. edition legitime par le proprietaire -> 302, aucun doublon
        n_before = model.objects.filter(erp_client=A).count()
        r = ca.post(path, {'action': action, 'edit_id': objA.id, **pa})
        objA.refresh_from_db()
        n_after = model.objects.filter(erp_client=A).count()
        check(f'{label} : edition proprietaire -> 302 sans doublon',
              r.status_code == 302 and n_after == n_before,
              f'status={r.status_code} n={n_before}->{n_after}')
        check(f'{label} : edition conserve le tenant A', objA.erp_client_id == A.id)

        # 4c. edition avec changement de valeur -> la modification persiste
        ov = EDIT_PERSIST.get((path, action))
        if ov:
            key, val, fld = ov
            payload2 = dict(pa)
            payload2[key] = val
            r = ca.post(path, {'action': action, 'edit_id': objA.id, **payload2})
            objA.refresh_from_db()
            got = getattr(objA, fld)
            same = str(got) == str(val)
            if not same:
                try:
                    same = float(got) == float(val)
                except (TypeError, ValueError):
                    pass
            check(f'{label} : valeur modifiee persiste ({fld})',
                  r.status_code == 302 and same,
                  f'status={r.status_code} {fld}={got!r} attendu={val!r}')

        # 5. cloisonnement visuel : la ligne de A n'apparait pas chez B
        #    (data-model est inclus : deux modeles differents peuvent avoir le
        #    meme id numerique sur la meme page, ex. menu et table)
        ha = ca.get(path).content.decode()
        hb = cb.get(path).content.decode()
        mine = f'data-model="{del_name}" data-id="{objA.id}"'
        theirs = f'data-model="{del_name}" data-id="{objB.id}"'
        check(f'{label} : ligne A chez A, absente chez B',
              mine in ha and mine not in hb and theirs in hb and theirs not in ha)

        created.append((model, objA.id, del_name, path))
    except Exception as exc:  # une erreur 500 ne doit pas masquer le reste
        check(f'{label} : exception inattendue', False,
              f'{type(exc).__name__}: {exc}')
        continue

print('\n== Suppression legitime (proprietaire) ==')
for model, oid, del_name, path in reversed(created):
    r = ca.post(path, {'action': 'delete', 'model': del_name, 'id': oid})
    check(f'{path:16s} delete {del_name} #id -> supprime',
          r.status_code == 302 and not model.objects.filter(id=oid).exists())

print('\n== Lit : bascule cloisonnee (Sante) ==')
litA = M.Lit.objects.create(erp_client=A, numero=f'L-{TAG}')
r = cb.post('/sante/', {'action': 'toggle_lit', 'id': litA.id})
litA.refresh_from_db()
check('toggle_lit sur le lit d\'un autre tenant -> 404', r.status_code == 404, r.status_code)
check('  lit inchange', litA.occupe is False)
r = ca.post('/sante/', {'action': 'toggle_lit', 'id': litA.id})
litA.refresh_from_db()
check('toggle_lit par le proprietaire -> 302 + bascule',
      r.status_code == 302 and litA.occupe is True, f'{r.status_code} occupe={litA.occupe}')

print('\n== Nettoyage ==')
A.delete(); B.delete()
UA.delete(); UB.delete()
check('tenants de test supprimes',
      not ERPClient.objects.filter(company_name__contains=TAG).exists())

raise SystemExit(report())
