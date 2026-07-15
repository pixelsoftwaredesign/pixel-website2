import json, uuid, random, string
from datetime import datetime, date
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import UserProfile, ProjetContact, AtelierProfile, PortfolioProject, CodeRepository, GraphismeResource, ERPModule, ERPSubscription, ERPDemoRecord, ERPClient, Moniteur, Candidat, Vehicule, Lecon, Examen, Medecin, Patient, Lit, RendezVous, FacturationSante, ClientHotel, Chambre, ReservationHotel, ServiceHotel, Categorie, Fournisseur, Produit, Vente, ClientJuridique, DossierJuridique, Audience, JournalComptable, EcritureComptable, Facture, DeclarationFiscale, Employe, Contrat, FichePaie, Conge, Formation, MenuItem, TableRestaurant, SoftCodeModule, StudioProject3D, PatisserieRecipe, PatisserieProduct, PlanAbonnement, SouscriptionClient, Paiement, CleActivation, ConfigurationBancaire, ConfigurationPaiementEnLigne, Candidature, MouvementStock, CommandeECommerce, CommandeECommerceItem, Temoignage
from .services import notifier_activation_cle, notifier_confirmation_commande, notifier_statut_commande

def index(request):
    projects_delivered = PortfolioProject.objects.count() + CodeRepository.objects.count() + GraphismeResource.objects.count() + StudioProject3D.objects.count() + PatisserieRecipe.objects.count()
    contacts = ProjetContact.objects.count()
    return render(request, 'studio/index.html', {
        'projects_delivered': projects_delivered or 48,
        'clients_satisfied': 100,
    })

def gestiactiv(request):
    modules = ERPModule.objects.filter(is_available=True)
    demo_count = ERPDemoRecord.objects.count()
    active_clients = ERPClient.objects.filter(is_active=True).count()
    return render(request, 'studio/gestiactiv.html', {
        'modules': modules,
        'demo_count': demo_count or 1240,
        'active_clients': active_clients or 85,
        'module_count': modules.count(),
    })

def gestiactiv_dashboard(request):
    modules = ERPModule.objects.filter(is_available=True)
    active_client = ERPClient.objects.filter(is_active=True).first()
    subs = ERPSubscription.objects.filter(client=active_client) if active_client else []
    demo_records = ERPDemoRecord.objects.all()[:20]
    stats = {}
    for m in modules:
        stats[m.slug] = ERPDemoRecord.objects.filter(module=m).count()
    return render(request, 'studio/gestiactiv_dashboard.html', {
        'modules': modules,
        'client': active_client,
        'subs': subs,
        'demo_records': demo_records,
        'stats': stats,
    })

def gestiactiv_module(request, module_slug):
    module = get_object_or_404(ERPModule, slug=module_slug, is_available=True)
    records = ERPDemoRecord.objects.filter(module=module)[:30]
    all_modules = ERPModule.objects.filter(is_available=True)
    return render(request, 'studio/gestiactiv_module.html', {
        'module': module,
        'records': records,
        'all_modules': all_modules,
    })

# ─── Auto-École ─────────────────────────────────────────────
@login_required
def gestion_auto_ecole(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_candidat':
            if eid:
                o = Candidat.objects.get(id=eid); o.nom=request.POST['nom']; o.telephone=request.POST.get('telephone',''); o.type_permis=request.POST.get('type_permis','B'); o.save()
            else:
                Candidat.objects.create(nom=request.POST['nom'], telephone=request.POST.get('telephone',''), type_permis=request.POST.get('type_permis','B'))
        elif action == 'add_moniteur':
            if eid:
                o = Moniteur.objects.get(id=eid); o.nom=request.POST['nom']; o.telephone=request.POST.get('telephone',''); o.specialite=request.POST.get('specialite',''); o.save()
            else:
                Moniteur.objects.create(nom=request.POST['nom'], telephone=request.POST.get('telephone',''), specialite=request.POST.get('specialite',''))
        elif action == 'add_vehicule':
            if eid:
                o = Vehicule.objects.get(id=eid); o.immatriculation=request.POST['immatriculation']; o.marque=request.POST['marque']; o.modele=request.POST['modele']; o.save()
            else:
                Vehicule.objects.create(immatriculation=request.POST['immatriculation'], marque=request.POST['marque'], modele=request.POST['modele'])
        elif action == 'add_lecon':
            if eid:
                o = Lecon.objects.get(id=eid); o.candidat_id=request.POST['candidat']; o.moniteur_id=request.POST.get('moniteur'); o.vehicule_id=request.POST.get('vehicule'); o.date_lecon=request.POST['date_lecon'].replace('T',' '); o.duree_minutes=request.POST.get('duree',60); o.save()
            else:
                Lecon.objects.create(candidat_id=request.POST['candidat'], moniteur_id=request.POST.get('moniteur'), vehicule_id=request.POST.get('vehicule'), date_lecon=request.POST['date_lecon'].replace('T',' '), duree_minutes=request.POST.get('duree',60))
        elif action == 'add_examen':
            if eid:
                o = Examen.objects.get(id=eid); o.candidat_id=request.POST['candidat']; o.date_examen=request.POST['date_examen']; o.type_examen=request.POST.get('type','code'); o.save()
            else:
                Examen.objects.create(candidat_id=request.POST['candidat'], date_examen=request.POST['date_examen'], type_examen=request.POST.get('type','code'))
        elif action == 'delete':
            model_map = {'candidat':Candidat,'moniteur':Moniteur,'vehicule':Vehicule,'lecon':Lecon,'examen':Examen}
            m = model_map.get(request.POST.get('model'))
            if m: m.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_auto_ecole')
    candidats = Candidat.objects.all()
    moniteurs = Moniteur.objects.filter(actif=True)
    vehicules = Vehicule.objects.filter(disponible=True)
    lecons = Lecon.objects.all().select_related('candidat','moniteur','vehicule')[:30]
    examens = Examen.objects.all().select_related('candidat')[:20]
    return render(request, 'studio/erp_auto_ecole.html', {
        'module': ERPModule.objects.get(slug='auto-ecole'),
        'candidats': candidats, 'moniteurs': moniteurs, 'vehicules': vehicules,
        'lecons': lecons, 'examens': examens,
        'total_candidats': candidats.count(), 'total_moniteurs': moniteurs.count(),
        'total_lecons': Lecon.objects.count(), 'total_reussite': Examen.objects.filter(reussi=True).count(),
        'total_examens': Examen.objects.count(),
    })

# ─── Santé / Clinique ───────────────────────────────────────
@login_required
def gestion_sante(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_patient':
            if eid:
                o = Patient.objects.get(id=eid); o.nom=request.POST['nom']; o.date_naissance=request.POST['date_naissance']; o.telephone=request.POST.get('telephone',''); o.mutuelle=request.POST.get('mutuelle',''); o.save()
            else:
                Patient.objects.create(nom=request.POST['nom'], date_naissance=request.POST['date_naissance'], telephone=request.POST.get('telephone',''), mutuelle=request.POST.get('mutuelle',''))
        elif action == 'add_rdv':
            if eid:
                o = RendezVous.objects.get(id=eid); o.patient_id=request.POST['patient']; o.medecin_id=request.POST.get('medecin'); o.date_rdv=request.POST['date_rdv'].replace('T',' '); o.motif=request.POST.get('motif',''); o.save()
            else:
                RendezVous.objects.create(patient_id=request.POST['patient'], medecin_id=request.POST.get('medecin'), date_rdv=request.POST['date_rdv'].replace('T',' '), motif=request.POST.get('motif',''))
        elif action == 'add_facture':
            if eid:
                o = FacturationSante.objects.get(id=eid); o.patient_id=request.POST['patient']; o.montant=request.POST['montant']; o.type_facture=request.POST.get('type','consultation'); o.save()
            else:
                FacturationSante.objects.create(patient_id=request.POST['patient'], montant=request.POST['montant'], type_facture=request.POST.get('type','consultation'))
        elif action == 'toggle_lit':
            lit = Lit.objects.get(id=request.POST['id'])
            lit.occupe = not lit.occupe
            lit.save()
        elif action == 'delete':
            model_map = {'patient':Patient,'rdv':RendezVous,'facture':FacturationSante}
            m = model_map.get(request.POST.get('model'))
            if m: m.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_sante')
    patients = Patient.objects.all()
    medecins = Medecin.objects.filter(actif=True)
    rdvs = RendezVous.objects.all()[:30]
    lits = Lit.objects.all()
    factures = FacturationSante.objects.all()[:20]
    return render(request, 'studio/erp_sante.html', {
        'module': ERPModule.objects.get(slug='sante'),
        'patients': patients, 'medecins': medecins, 'rdvs': rdvs, 'lits': lits, 'factures': factures,
        'total_patients': patients.count(), 'total_medecins': medecins.count(),
        'lits_occupes': lits.filter(occupe=True).count(), 'total_lits': lits.count(),
    })

# ─── Hôtellerie / Tourisme ──────────────────────────────────
@login_required
def gestion_hotel(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_client':
            if eid:
                o = ClientHotel.objects.get(id=eid); o.nom=request.POST['nom']; o.telephone=request.POST.get('telephone',''); o.email=request.POST.get('email',''); o.nationalite=request.POST.get('nationalite',''); o.save()
            else:
                ClientHotel.objects.create(nom=request.POST['nom'], telephone=request.POST.get('telephone',''), email=request.POST.get('email',''), nationalite=request.POST.get('nationalite',''))
        elif action == 'add_reservation':
            ch = Chambre.objects.get(id=request.POST['chambre'])
            cl = ClientHotel.objects.get(id=request.POST['client'])
            if eid:
                o = ReservationHotel.objects.get(id=eid); o.client=cl; o.chambre=ch; o.date_arrivee=request.POST['arrivee']; o.date_depart=request.POST['depart']; o.save()
            else:
                ReservationHotel.objects.create(client=cl, chambre=ch, date_arrivee=request.POST['arrivee'], date_depart=request.POST['depart'])
        elif action == 'add_chambre':
            if eid:
                o = Chambre.objects.get(id=eid); o.numero=request.POST['numero']; o.type_chambre=request.POST.get('type','simple'); o.prix_nuit=request.POST.get('prix',100); o.etage=request.POST.get('etage',1); o.save()
            else:
                Chambre.objects.create(numero=request.POST['numero'], type_chambre=request.POST.get('type','simple'), prix_nuit=request.POST.get('prix',100), etage=request.POST.get('etage',1))
        elif action == 'delete':
            model_map = {'client':ClientHotel,'reservation':ReservationHotel,'chambre':Chambre}
            m = model_map.get(request.POST.get('model'))
            if m: m.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_hotel')
    clients = ClientHotel.objects.all()
    chambres = Chambre.objects.all()
    base_reservations = ReservationHotel.objects.all()
    reservations = base_reservations[:30]
    return render(request, 'studio/erp_hotel.html', {
        'module': ERPModule.objects.get(slug='hotellerie'),
        'clients': clients, 'chambres': chambres, 'reservations': reservations,
        'total_chambres': chambres.count(), 'disponibles': chambres.filter(disponible=True).count(),
        'reservations_actives': base_reservations.filter(statut__in=['confirmee','en_cours']).count(),
    })

# ─── Commerce / Retail ──────────────────────────────────────
@login_required
def gestion_commerce(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_produit':
            if eid:
                o = Produit.objects.get(id=eid); o.nom=request.POST['nom']; o.categorie_id=request.POST.get('categorie'); o.fournisseur_id=request.POST.get('fournisseur'); o.prix_achat=request.POST.get('prix_achat',0); o.prix_vente=request.POST.get('prix_vente',0); o.stock_actuel=request.POST.get('stock',0); o.save()
            else:
                Produit.objects.create(nom=request.POST['nom'], categorie_id=request.POST.get('categorie'), fournisseur_id=request.POST.get('fournisseur'), prix_achat=request.POST.get('prix_achat',0), prix_vente=request.POST.get('prix_vente',0), stock_actuel=request.POST.get('stock',0))
        elif action == 'add_categorie':
            if eid:
                o = Categorie.objects.get(id=eid); o.nom=request.POST['nom']; o.save()
            else:
                Categorie.objects.create(nom=request.POST['nom'])
        elif action == 'add_vente':
            p = Produit.objects.get(id=request.POST['produit'])
            if eid:
                o = Vente.objects.get(id=eid); o.produit=p; o.quantite=request.POST.get('quantite',1); o.prix_unitaire=p.prix_vente; o.save()
            else:
                Vente.objects.create(produit=p, quantite=request.POST.get('quantite',1), prix_unitaire=p.prix_vente)
        elif action == 'delete':
            model_map = {'produit':Produit,'categorie':Categorie,'vente':Vente,'fournisseur':Fournisseur}
            m = model_map.get(request.POST.get('model'))
            if m: m.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_commerce')
    produits = Produit.objects.filter(actif=True)
    categories = Categorie.objects.all()
    fournisseurs = Fournisseur.objects.all()
    ventes = Vente.objects.all()[:30]
    stock_faible = Produit.objects.filter(stock_actuel__lte=models.F('stock_minimum'), actif=True)
    return render(request, 'studio/erp_commerce.html', {
        'module': ERPModule.objects.get(slug='commerce'),
        'produits': produits, 'categories': categories, 'fournisseurs': fournisseurs, 'ventes': ventes,
        'total_produits': produits.count(), 'total_categories': categories.count(),
        'alerte_stock': stock_faible.count(), 'total_ventes': Vente.objects.count(),
    })

# ─── Juridique (Avocat) ─────────────────────────────────────
@login_required
def gestion_juridique(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_client':
            if eid:
                o = ClientJuridique.objects.get(id=eid); o.nom=request.POST['nom']; o.type_client=request.POST.get('type','particulier'); o.telephone=request.POST.get('telephone',''); o.save()
            else:
                ClientJuridique.objects.create(nom=request.POST['nom'], type_client=request.POST.get('type','particulier'), telephone=request.POST.get('telephone',''))
        elif action == 'add_dossier':
            if eid:
                o = DossierJuridique.objects.get(id=eid); o.reference=request.POST['reference']; o.client_id=request.POST['client']; o.titre=request.POST['titre']; o.type_affaire=request.POST.get('type_affaire',''); o.tribunal=request.POST.get('tribunal',''); o.save()
            else:
                DossierJuridique.objects.create(reference=request.POST['reference'], client_id=request.POST['client'], titre=request.POST['titre'], type_affaire=request.POST.get('type_affaire',''), tribunal=request.POST.get('tribunal',''))
        elif action == 'add_audience':
            if eid:
                o = Audience.objects.get(id=eid); o.dossier_id=request.POST['dossier']; o.date_audience=request.POST['date_audience'].replace('T',' '); o.lieu=request.POST.get('lieu',''); o.save()
            else:
                Audience.objects.create(dossier_id=request.POST['dossier'], date_audience=request.POST['date_audience'].replace('T',' '), lieu=request.POST.get('lieu',''))
        elif action == 'delete':
            model_map = {'client':ClientJuridique,'dossier':DossierJuridique,'audience':Audience}
            m = model_map.get(request.POST.get('model'))
            if m: m.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_juridique')
    dossiers = DossierJuridique.objects.all()
    clients = ClientJuridique.objects.all()
    audiences = Audience.objects.all()[:20]
    return render(request, 'studio/erp_juridique.html', {
        'module': ERPModule.objects.get(slug='juridique'),
        'dossiers': dossiers, 'clients': clients, 'audiences': audiences,
        'total_dossiers': dossiers.count(), 'dossiers_ouverts': dossiers.filter(statut='ouvert').count(),
        'total_clients': clients.count(),
    })

# ─── Comptabilité ───────────────────────────────────────────
@login_required
def gestion_comptabilite(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_ecriture':
            if eid:
                o = EcritureComptable.objects.get(id=eid); o.date_ecriture=request.POST['date_ecriture']; o.libelle=request.POST['libelle']; o.compte_debit=request.POST['compte_debit']; o.compte_credit=request.POST['compte_credit']; o.montant=request.POST['montant']; o.journal_id=request.POST.get('journal'); o.save()
            else:
                EcritureComptable.objects.create(date_ecriture=request.POST['date_ecriture'], libelle=request.POST['libelle'], compte_debit=request.POST['compte_debit'], compte_credit=request.POST['compte_credit'], montant=request.POST['montant'], journal_id=request.POST.get('journal'))
        elif action == 'add_facture':
            ht = float(request.POST.get('montant_ht',0))
            tva = float(request.POST.get('tva',19))
            if eid:
                o = Facture.objects.get(id=eid); o.numero=request.POST['numero']; o.client_nom=request.POST['client_nom']; o.client_matricule=request.POST.get('matricule',''); o.montant_ht=ht; o.tva=tva; o.montant_ttc=ht*(1+tva/100); o.save()
            else:
                Facture.objects.create(numero=request.POST['numero'], client_nom=request.POST['client_nom'], client_matricule=request.POST.get('matricule',''), montant_ht=ht, tva=tva, montant_ttc=ht*(1+tva/100))
        elif action == 'add_journal':
            if eid:
                o = JournalComptable.objects.get(id=eid); o.code=request.POST['code']; o.nom=request.POST['nom']; o.save()
            else:
                JournalComptable.objects.create(code=request.POST['code'], nom=request.POST['nom'])
        elif action == 'delete':
            model_map = {'ecriture':EcritureComptable,'facture':Facture,'journal':JournalComptable}
            m = model_map.get(request.POST.get('model'))
            if m: m.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_comptabilite')
    ecritures = EcritureComptable.objects.all()[:30]
    factures = Facture.objects.all()[:30]
    journaux = JournalComptable.objects.all()
    return render(request, 'studio/erp_comptabilite.html', {
        'module': ERPModule.objects.get(slug='comptabilite'),
        'ecritures': ecritures, 'factures': factures, 'journaux': journaux,
        'total_ecritures': EcritureComptable.objects.count(),
        'total_factures': Facture.objects.count(),
        'factures_impayees': Facture.objects.filter(payee=False).count(),
    })

# ─── RH & Paie ──────────────────────────────────────────────
@login_required
def gestion_rh(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_employe':
            if eid:
                o = Employe.objects.get(id=eid); o.nom=request.POST['nom']; o.email=request.POST['email']; o.poste=request.POST['poste']; o.departement=request.POST.get('departement',''); o.date_embauche=request.POST['date_embauche']; o.salaire_base=request.POST.get('salaire',1500); o.save()
            else:
                Employe.objects.create(nom=request.POST['nom'], email=request.POST['email'], poste=request.POST['poste'], departement=request.POST.get('departement',''), date_embauche=request.POST['date_embauche'], salaire_base=request.POST.get('salaire',1500))
        elif action == 'add_conge':
            deb = datetime.strptime(request.POST['date_debut'],'%Y-%m-%d').date()
            fin = datetime.strptime(request.POST['date_fin'],'%Y-%m-%d').date()
            if eid:
                o = Conge.objects.get(id=eid); o.employe_id=request.POST['employe']; o.date_debut=deb; o.date_fin=fin; o.nb_jours=(fin-deb).days+1; o.type_conge=request.POST.get('type','annuel'); o.save()
            else:
                Conge.objects.create(employe_id=request.POST['employe'], date_debut=deb, date_fin=fin, nb_jours=(fin-deb).days+1, type_conge=request.POST.get('type','annuel'))
        elif action == 'add_formation':
            if eid:
                o = Formation.objects.get(id=eid); o.employe_id=request.POST['employe']; o.titre=request.POST['titre']; o.organisme=request.POST.get('organisme',''); o.date_debut=request.POST['date_debut']; o.date_fin=request.POST['date_fin']; o.cout=request.POST.get('cout',0); o.save()
            else:
                Formation.objects.create(employe_id=request.POST['employe'], titre=request.POST['titre'], organisme=request.POST.get('organisme',''), date_debut=request.POST['date_debut'], date_fin=request.POST['date_fin'], cout=request.POST.get('cout',0))
        elif action == 'delete':
            model_map = {'employe':Employe,'conge':Conge,'formation':Formation,'contrat':Contrat}
            m = model_map.get(request.POST.get('model'))
            if m: m.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_rh')
    employes = Employe.objects.filter(actif=True)
    conges = Conge.objects.all()[:20]
    formations = Formation.objects.all()[:20]
    return render(request, 'studio/erp_rh.html', {
        'module': ERPModule.objects.get(slug='rh-paie'),
        'employes': employes, 'conges': conges, 'formations': formations,
        'total_employes': employes.count(),
        'conges_en_cours': Conge.objects.filter(valide=True).count(),
        'masse_salariale': sum(e.salaire_base for e in Employe.objects.filter(actif=True)),
    })

@csrf_exempt
def api_erp_demo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            module_slug = data.get('module', '')
            module = get_object_or_404(ERPModule, slug=module_slug)
            ERPDemoRecord.objects.create(module=module, label=data.get('label',''), value=data.get('value',''))
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"status": "error"}, status=405)

# ─── Restaurant ──────────────────────────────────────────────
@login_required
def gestion_restaurant(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_menu':
            if eid:
                o = MenuItem.objects.get(id=eid); o.nom=request.POST['nom']; o.categorie=request.POST.get('categorie','plat'); o.prix=request.POST.get('prix',0); o.disponible=request.POST.get('disponible','1')=='1'; o.save()
            else:
                MenuItem.objects.create(nom=request.POST['nom'], categorie=request.POST.get('categorie','plat'), prix=request.POST.get('prix',0), disponible=request.POST.get('disponible','1')=='1')
        elif action == 'add_table':
            if eid:
                o = TableRestaurant.objects.get(id=eid); o.numero=request.POST['numero']; o.capacite=request.POST.get('capacite',4); o.statut=request.POST.get('statut','libre'); o.save()
            else:
                TableRestaurant.objects.create(numero=request.POST['numero'], capacite=request.POST.get('capacite',4), statut=request.POST.get('statut','libre'))
        elif action == 'delete':
            m = {'menu':MenuItem,'table':TableRestaurant}.get(request.POST.get('model'))
            if m: m.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_restaurant')
    menus = MenuItem.objects.all()
    tables = TableRestaurant.objects.all()
    return render(request, 'studio/erp_restaurant.html', {
        'menus': menus, 'tables': tables,
        'total_menus': menus.count(), 'total_tables': tables.count(),
        'tables_libres': tables.filter(statut='libre').count(),
        'menus_disponibles': menus.filter(disponible=True).count(),
    })

# ─── PixelSoftCode ───────────────────────────────────────────
@login_required
def gestion_pixelsoftcode(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_module':
            if eid:
                o = SoftCodeModule.objects.get(id=eid); o.nom=request.POST['nom']; o.categorie=request.POST.get('categorie',''); o.version=request.POST.get('version','1.0.0'); o.prix=request.POST.get('prix',0); o.disponible=request.POST.get('disponible','1')=='1'; o.save()
            else:
                SoftCodeModule.objects.create(nom=request.POST['nom'], categorie=request.POST.get('categorie',''), version=request.POST.get('version','1.0.0'), prix=request.POST.get('prix',0), disponible=request.POST.get('disponible','1')=='1')
        elif action == 'delete':
            if request.POST.get('model') == 'module':
                SoftCodeModule.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_pixelsoftcode')
    modules = SoftCodeModule.objects.all()
    cats = SoftCodeModule.objects.values_list('categorie', flat=True).distinct().order_by('categorie')
    return render(request, 'studio/erp_pixelsoftcode.html', {
        'modules': modules, 'categories': cats,
        'total_modules': modules.count(), 'modules_dispo': modules.filter(disponible=True).count(),
    })

# ─── Inner Studio ────────────────────────────────────────────
@login_required
def gestion_innerstudio(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_project':
            if eid:
                o = StudioProject3D.objects.get(id=eid); o.nom=request.POST['nom']; o.categorie=request.POST.get('categorie','architecture'); o.description=request.POST.get('description',''); o.save()
            else:
                StudioProject3D.objects.create(nom=request.POST['nom'], categorie=request.POST.get('categorie','architecture'), description=request.POST.get('description',''))
        elif action == 'delete':
            if request.POST.get('model') == 'project':
                StudioProject3D.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_innerstudio')
    projects = StudioProject3D.objects.all()
    stats = {}
    for c, _ in StudioProject3D.CAT_CHOICES:
        stats[c] = projects.filter(categorie=c).count()
    return render(request, 'studio/erp_innerstudio.html', {
        'projects': projects, 'stats': stats,
        'total_projects': projects.count(),
    })

# ─── Pâtisserie ──────────────────────────────────────────────
@login_required
def gestion_patisserie(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_recipe':
            if eid:
                o = PatisserieRecipe.objects.get(id=eid); o.nom=request.POST['nom']; o.categorie=request.POST.get('categorie','patisserie'); o.cout_production=request.POST.get('cout_production',0); o.prix_vente=request.POST.get('prix_vente',0); o.save()
            else:
                PatisserieRecipe.objects.create(nom=request.POST['nom'], categorie=request.POST.get('categorie','patisserie'), cout_production=request.POST.get('cout_production',0), prix_vente=request.POST.get('prix_vente',0))
        elif action == 'add_product':
            if eid:
                o = PatisserieProduct.objects.get(id=eid); o.nom=request.POST['nom']; o.recette_id=request.POST.get('recette'); o.stock_actuel=request.POST.get('stock_actuel',0); o.prix_vente=request.POST.get('prix_vente',0); o.actif=request.POST.get('actif','1')=='1'; o.save()
            else:
                PatisserieProduct.objects.create(nom=request.POST['nom'], recette_id=request.POST.get('recette'), stock_actuel=request.POST.get('stock_actuel',0), prix_vente=request.POST.get('prix_vente',0), actif=request.POST.get('actif','1')=='1')
        elif action == 'delete':
            m = {'recipe':PatisserieRecipe,'product':PatisserieProduct}.get(request.POST.get('model'))
            if m: m.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_patisserie')
    recipes = PatisserieRecipe.objects.all()
    products = PatisserieProduct.objects.all().select_related('recette')
    alert_stock = products.filter(stock_actuel__lt=models.F('stock_minimum'), actif=True).count()
    return render(request, 'studio/erp_patisserie.html', {
        'recipes': recipes, 'products': products,
        'total_recipes': recipes.count(), 'total_products': products.count(),
        'alert_stock': alert_stock,
    })

def restaurant(request):
    menus_count = MenuItem.objects.count()
    tables_count = TableRestaurant.objects.count()
    menus_dispo = MenuItem.objects.filter(disponible=True).count()
    return render(request, 'studio/restaurant.html', {
        'menus_count': menus_count or 48,
        'tables_count': tables_count or 20,
        'menus_dispo': menus_dispo or 36,
    })

def pixelsoftcode(request):
    modules_count = SoftCodeModule.objects.count()
    modules_dispo = SoftCodeModule.objects.filter(disponible=True).count()
    cats = SoftCodeModule.objects.values_list('categorie', flat=True).distinct().count()
    return render(request, 'studio/pixelsoftcode.html', {
        'modules_count': modules_count or 50,
        'modules_dispo': modules_dispo or 42,
        'categories_count': cats or 8,
    })

def innerstudio(request):
    projects_count = StudioProject3D.objects.count()
    return render(request, 'studio/innerstudio.html', {
        'projects_count': projects_count or 120,
    })

def patisserie(request):
    recipes_count = PatisserieRecipe.objects.count()
    products_count = PatisserieProduct.objects.count()
    return render(request, 'studio/patisserie.html', {
        'recipes_count': recipes_count or 85,
        'products_count': products_count or 200,
    })

def graphiste(request):
    resources = GraphismeResource.objects.all()[:12]
    free_count = GraphismeResource.objects.filter(is_free=True).count()
    total_resources = GraphismeResource.objects.count()
    total_dl = sum(r.downloads for r in GraphismeResource.objects.all())
    cats = GraphismeResource.objects.values_list('category', flat=True).distinct()
    return render(request, 'studio/graphiste.html', {
        'resources': resources,
        'free_count': free_count or 1200,
        'total_resources': total_resources or 2800,
        'total_dl': total_dl or 45000,
        'categories': cats,
    })

@login_required
def graphisme_dashboard(request):
    resources = GraphismeResource.objects.filter(author=request.user)
    return render(request, 'studio/graphisme_dashboard.html', {'resources': resources})

def graphisme_explore(request):
    q = request.GET.get('q', '')
    cat = request.GET.get('cat', '')
    typ = request.GET.get('type', '')
    free = request.GET.get('free', '')
    resources = GraphismeResource.objects.all()
    if q: resources = resources.filter(title__icontains=q) | resources.filter(tags__icontains=q)
    if cat: resources = resources.filter(category__icontains=cat)
    if typ: resources = resources.filter(file_type__icontains=typ)
    if free == '1': resources = resources.filter(is_free=True)
    cats = GraphismeResource.objects.values_list('category', flat=True).distinct().order_by('category')
    types = GraphismeResource.objects.values_list('file_type', flat=True).distinct().order_by('file_type')
    return render(request, 'studio/graphisme_explore.html', {
        'resources': resources, 'q': q, 'cat': cat, 'typ': typ, 'free': free,
        'categories': cats, 'file_types': types,
    })

@login_required
def graphisme_upload(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title', '').strip()
            desc = request.POST.get('description', '').strip()
            cat = request.POST.get('category', '').strip()
            tags = request.POST.get('tags', '').strip()
            file_url = request.POST.get('file_url', '').strip()
            preview_url = request.POST.get('preview_url', '').strip()
            file_type = request.POST.get('file_type', '').strip()
            is_free = request.POST.get('is_free', 'true') == 'true'
            price = request.POST.get('price', '0')
            if not title or not cat:
                return JsonResponse({"status": "error", "message": "Titre et catégorie requis."}, status=400)
            resource = GraphismeResource(
                author=request.user, title=title, description=desc, category=cat,
                tags=tags, file_url=file_url, preview_url=preview_url,
                file_type=file_type, is_free=is_free, price=price
            )
            if request.FILES.get('file'):
                resource.file = request.FILES['file']
            if request.FILES.get('preview_image'):
                resource.preview_image = request.FILES['preview_image']
            resource.save()
            return JsonResponse({"status": "success", "id": resource.id, "message": "Ressource publiée !"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    cats = ["Logos", "Cartes de visite", "Flyers & Dépliants", "Affiches & Roll-ups",
            "Réseaux sociaux", "Packaging & Étiquettes", "Plaquettes", "Bannières web",
            "Mockups", "Icônes", "Polices", "Templates", "Présentations", "CV & Portfolio"]
    types = ["AI", "PSD", "PNG", "SVG", "PDF", "INDD", "EPS", "CDR", "FIG", "PPT"]
    return render(request, 'studio/graphisme_upload.html', {'categories': cats, 'file_types': types})

def graphisme_detail(request, resource_id):
    resource = get_object_or_404(GraphismeResource, id=resource_id)
    similar = GraphismeResource.objects.filter(category=resource.category).exclude(id=resource_id)[:4]
    return render(request, 'studio/graphisme_detail.html', {'resource': resource, 'similar': similar})

@csrf_exempt
def api_graphisme_download(request, resource_id):
    if request.method == 'POST':
        r = get_object_or_404(GraphismeResource, id=resource_id)
        r.downloads += 1
        r.save()
        url = r.file.url if r.file else r.file_url
        return JsonResponse({"status": "success", "downloads": r.downloads, "file_url": url})
    return JsonResponse({"status": "error"}, status=405)

@csrf_exempt
def api_graphisme_like(request, resource_id):
    if request.method == 'POST':
        r = get_object_or_404(GraphismeResource, id=resource_id)
        r.likes += 1
        r.save()
        return JsonResponse({"status": "success", "likes": r.likes})
    return JsonResponse({"status": "error"}, status=405)

def uicatalogue(request):
    projects = PortfolioProject.objects.all()[:6]
    repos = CodeRepository.objects.all()[:6]
    designers_count = AtelierProfile.objects.filter(role__in=['designer', 'both']).count()
    devs_count = AtelierProfile.objects.filter(role__in=['developer', 'both']).count()
    total_projects = PortfolioProject.objects.count() + CodeRepository.objects.count()
    total_downloads = sum(p.downloads for p in PortfolioProject.objects.all()) + sum(r.downloads for r in CodeRepository.objects.all())
    return render(request, 'studio/uicatalogue.html', {
        'projects': projects,
        'repos': repos,
        'designers_count': designers_count or 250,
        'devs_count': devs_count or 500,
        'total_projects': total_projects or 2000,
        'total_downloads': total_downloads or 18000,
    })

def atelierdev(request):
    devs = AtelierProfile.objects.filter(role__in=['developer', 'both']).count()
    projects_count = PortfolioProject.objects.count() + CodeRepository.objects.count()
    downloads = sum(p.downloads for p in PortfolioProject.objects.all()) + sum(r.downloads for r in CodeRepository.objects.all())
    recruiters = AtelierProfile.objects.filter(role__in=['developer', 'both']).count()
    return render(request, 'studio/atelierdev.html', {
        'devs_count': devs or 500,
        'projects_count': projects_count or 800,
        'downloads_count': downloads or 3000,
        'recruiters_count': recruiters or 120,
    })

def atelier_explore(request):
    q = request.GET.get('q', '')
    cat = request.GET.get('cat', '')
    projects = PortfolioProject.objects.all()
    repos = CodeRepository.objects.all()
    if q:
        projects = projects.filter(title__icontains=q)
        repos = repos.filter(name__icontains=q)
    if cat:
        projects = projects.filter(category__icontains=cat)
        repos = repos.filter(language__icontains=cat)
    return render(request, 'studio/atelier_explore.html', {
        'projects': projects, 'repos': repos, 'q': q, 'cat': cat
    })

def atelier_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(AtelierProfile, user=user)
    projects = PortfolioProject.objects.filter(designer=profile)
    repos = CodeRepository.objects.filter(developer=profile)
    return render(request, 'studio/atelier_profile.html', {
        'profile': profile, 'projects': projects, 'repos': repos
    })

def atelier_project_detail(request, project_id):
    project = get_object_or_404(PortfolioProject, id=project_id)
    return render(request, 'studio/atelier_project_detail.html', {'project': project})

def atelier_repo_detail(request, repo_id):
    repo = get_object_or_404(CodeRepository, id=repo_id)
    return render(request, 'studio/atelier_repo_detail.html', {'repo': repo})

@login_required
def atelier_dashboard(request):
    atelier, _ = AtelierProfile.objects.get_or_create(user=request.user)
    projects = PortfolioProject.objects.filter(designer=atelier)
    repos = CodeRepository.objects.filter(developer=atelier)
    return render(request, 'studio/atelier_dashboard.html', {
        'atelier': atelier, 'projects': projects, 'repos': repos
    })

@login_required
def atelier_upload_project(request):
    atelier, _ = AtelierProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        try:
            title = request.POST.get('title', '').strip()
            description = request.POST.get('description', '').strip()
            category = request.POST.get('category', '').strip()
            tags = request.POST.get('tags', '').strip()
            image_url = request.POST.get('image_url', '').strip()
            figma_url = request.POST.get('figma_url', '').strip()
            if not title or not category:
                return JsonResponse({"status": "error", "message": "Titre et catégorie requis."}, status=400)
            project = PortfolioProject.objects.create(
                designer=atelier, title=title, description=description,
                category=category, tags=tags, image_url=image_url, figma_url=figma_url
            )
            return JsonResponse({"status": "success", "project_id": project.id, "message": "Projet publié !"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    cats = ["UI/UX Design", "Application Mobile", "Dashboard & Analytics", "Site Web",
            "E-commerce", "ERP & Gestion", "Restauration & POS", "Santé & Médical",
            "Pâtisserie & Boulangerie", "Branding & Identité"]
    return render(request, 'studio/atelier_upload_project.html', {'categories': cats})

@login_required
def atelier_upload_repo(request):
    atelier, _ = AtelierProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '').strip()
            description = request.POST.get('description', '').strip()
            language = request.POST.get('language', '').strip()
            tags = request.POST.get('tags', '').strip()
            code_content = request.POST.get('code_content', '').strip()
            github_url = request.POST.get('github_url', '').strip()
            if not name or not language:
                return JsonResponse({"status": "error", "message": "Nom et langage requis."}, status=400)
            repo = CodeRepository.objects.create(
                developer=atelier, name=name, description=description,
                language=language, tags=tags, code_content=code_content, github_url=github_url
            )
            return JsonResponse({"status": "success", "repo_id": repo.id, "message": "Repository publié !"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    langs = ["Python & Django", "Java & Spring", "React & TypeScript", "Flutter & Dart",
             "PHP & Laravel", "C# & .NET", "Node.js & Express", "Vue.js & Nuxt",
             "Go", "Rust", "Kotlin", "Swift", "Ruby on Rails"]
    return render(request, 'studio/atelier_upload_repo.html', {'languages': langs})

@csrf_exempt
def api_project_like(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(PortfolioProject, id=project_id)
        project.likes += 1
        project.save()
        return JsonResponse({"status": "success", "likes": project.likes})
    return JsonResponse({"status": "error"}, status=405)

@csrf_exempt
def api_repo_star(request, repo_id):
    if request.method == 'POST':
        repo = get_object_or_404(CodeRepository, id=repo_id)
        repo.stars += 1
        repo.save()
        return JsonResponse({"status": "success", "stars": repo.stars})
    return JsonResponse({"status": "error"}, status=405)

@csrf_exempt
def api_contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nom = data.get('username', '').strip()
            email = data.get('useremail', '').strip()
            message = data.get('usermessage', '').strip()
            if not nom or not email or not message:
                return JsonResponse({"status": "error", "message": "Tous les champs sont requis."}, status=400)
            ProjetContact.objects.create(
                client=request.user if request.user.is_authenticated else None,
                nom=nom, email=email, message=message
            )
            return JsonResponse({
                "status": "success",
                "message": "Demande enregistrée avec succès ! Notre équipe vous contacte sous 24h."
            }, status=201)
        except Exception:
            return JsonResponse({"status": "error", "message": "Erreur interne du serveur."}, status=500)
    return JsonResponse({"status": "error", "message": "Méthode non autorisée."}, status=405)

@csrf_exempt
def api_inscription(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '').strip()
            email = data.get('email', '').strip()
            password = data.get('password', '')
            entreprise = data.get('entreprise', '').strip()
            role = data.get('role', 'designer')
            if not username or not email or not password:
                return JsonResponse({"status": "error", "message": "Champs obligatoires manquants."}, status=400)
            if User.objects.filter(username=username).exists():
                return JsonResponse({"status": "error", "message": "Cet identifiant existe déjà."}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({"status": "error", "message": "Cet email existe déjà."}, status=400)
            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(user=user, entreprise=entreprise)
            AtelierProfile.objects.create(user=user, role=role)
            login(request, user)
            return JsonResponse({"status": "success", "message": "Inscription réussie !"}, status=201)
        except Exception:
            return JsonResponse({"status": "error", "message": "Erreur lors de l'inscription."}, status=500)
    return JsonResponse({"status": "error", "message": "Méthode non autorisée."}, status=405)

@csrf_exempt
def api_connexion(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '').strip()
            password = data.get('password', '')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"status": "success", "message": f"Bonjour {user.username} !"}, status=200)
            else:
                return JsonResponse({"status": "error", "message": "Identifiants invalides."}, status=401)
        except Exception:
            return JsonResponse({"status": "error", "message": "Erreur serveur."}, status=500)
    return JsonResponse({"status": "error", "message": "Méthode non autorisée."}, status=405)

def api_deconnexion(request):
    logout(request)
    return JsonResponse({"status": "success", "message": "Déconnexion réussie."}, status=200)

# ─── Login / Register Pages ──────────────────────────────────
def login_page(request):
    return render(request, 'studio/login.html')

def register_page(request):
    return render(request, 'studio/register.html')

# ─── Subscription Management ───────────────────────────────
@login_required
def gestion_subscriptions(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        eid = request.POST.get('edit_id')
        if action == 'add_sub':
            client_id = request.POST.get('client')
            module_id = request.POST.get('module')
            if eid:
                o = ERPSubscription.objects.get(id=eid)
                o.client_id = client_id or o.client_id
                o.module_id = module_id or o.module_id
                o.is_active = request.POST.get('is_active', '1') == '1'
                o.end_date = request.POST.get('end_date') or None
                o.save()
            else:
                ERPSubscription.objects.create(
                    client_id=client_id, module_id=module_id,
                    is_active=request.POST.get('is_active', '1') == '1',
                    end_date=request.POST.get('end_date') or None
                )
        elif action == 'delete':
            if request.POST.get('model') == 'subscription':
                ERPSubscription.objects.filter(id=request.POST.get('id')).delete()
        return redirect('gestion_subscriptions')
    subs = ERPSubscription.objects.select_related('client', 'module').all()
    clients = ERPClient.objects.all()
    modules = ERPModule.objects.all()
    return render(request, 'studio/erp_subscriptions.html', {
        'subs': subs, 'clients': clients, 'modules': modules,
        'total_subs': subs.count(),
        'active_subs': subs.filter(is_active=True).count(),
        'total_clients': clients.count(),
    })

# ─── Price List ──────────────────────────────────────────────
def prix_liste(request):
    modules = ERPModule.objects.filter(is_available=True)
    soft_modules = SoftCodeModule.objects.filter(disponible=True)
    return render(request, 'studio/prix.html', {
        'modules': modules,
        'soft_modules': soft_modules,
    })

# ─── Offline Software ────────────────────────────────────────
def logiciel_offline(request):
    modules = SoftCodeModule.objects.filter(disponible=True)
    return render(request, 'studio/logiciel_offline.html', {
        'modules': modules,
        'total_modules': modules.count(),
    })

# ─── Abonnements & Paiements ─────────────────────────────────
def abonnement_choisir(request):
    plans = PlanAbonnement.objects.filter(is_available=True)
    return render(request, 'studio/abonnement_choisir.html', {'plans': plans})

def abonnement_souscrire(request, plan_slug):
    plan = get_object_or_404(PlanAbonnement, slug=plan_slug, is_available=True)
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        nom = request.POST.get('nom', '').strip()
        tel = request.POST.get('tel', '').strip()
        methode = request.POST.get('methode', '')
        if not email or not nom or not methode:
            return render(request, 'studio/abonnement_souscrire.html', {
                'plan': plan, 'error': 'Champs obligatoires manquants.'
            })
        sub = SouscriptionClient.objects.create(
            client_email=email, client_nom=nom, client_tel=tel, plan=plan
        )
        from datetime import timedelta
        sub.date_fin = sub.date_debut + timedelta(days=plan.duree_jours)
        sub.save()
        ref = f"PAY-{uuid.uuid4().hex[:8].upper()}"
        Paiement.objects.create(
            souscription=sub, methode=methode, montant=plan.prix, reference=ref
        )
        if methode == 'especes':
            return redirect('abonnement_cash', sub_id=sub.id)
        elif methode == 'online':
            return redirect('abonnement_online', sub_id=sub.id)
        elif methode == 'virement':
            return redirect('abonnement_virement', sub_id=sub.id)
    return render(request, 'studio/abonnement_souscrire.html', {'plan': plan})

def abonnement_cash(request, sub_id):
    sub = get_object_or_404(SouscriptionClient, id=sub_id)
    paiement = sub.paiements.last()
    if request.method == 'POST':
        code_saisi = request.POST.get('code', '').strip().upper()
        cle = CleActivation.objects.filter(souscription=sub, code=code_saisi, est_utilisee=False).first()
        if cle:
            cle.est_utilisee = True
            cle.date_activation = timezone.now()
            cle.save()
            paiement.statut = 'confirme'
            paiement.save()
            sub.status = 'actif'
            sub.save()
            notifier_activation_cle(sub, cle.code)
            return render(request, 'studio/abonnement_succes.html', {
                'sub': sub, 'code': cle.code, 'plan': sub.plan
            })
        else:
            return render(request, 'studio/abonnement_cash.html', {
                'sub': sub, 'paiement': paiement, 'plan': sub.plan,
                'error': 'Code invalide ou déjà utilisé.'
            })
    return render(request, 'studio/abonnement_cash.html', {
        'sub': sub, 'paiement': paiement, 'plan': sub.plan
    })

def abonnement_online(request, sub_id):
    sub = get_object_or_404(SouscriptionClient, id=sub_id)
    paiement = sub.paiements.last()
    config_paiement = ConfigurationPaiementEnLigne.objects.filter(est_actif=True).first()
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id', '').strip()
        if transaction_id:
            paiement.transaction_id = transaction_id
            paiement.statut = 'confirme'
            paiement.save()
            sub.status = 'actif'
            sub.save()
            code = genere_cle_activation(sub)
            notifier_activation_cle(sub, code)
            return render(request, 'studio/abonnement_succes.html', {
                'sub': sub, 'code': code, 'plan': sub.plan, 'paiement': paiement
            })
        return render(request, 'studio/abonnement_online.html', {
            'sub': sub, 'paiement': paiement, 'plan': sub.plan,
            'error': 'Veuillez fournir un ID de transaction.'
        })
    return render(request, 'studio/abonnement_online.html', {
        'sub': sub, 'paiement': paiement, 'plan': sub.plan, 'config_paiement': config_paiement
    })

def abonnement_virement(request, sub_id):
    sub = get_object_or_404(SouscriptionClient, id=sub_id)
    paiement = sub.paiements.last()
    banque = ConfigurationBancaire.objects.filter(is_active=True, est_defaut=True).first()
    if not banque:
        banque = ConfigurationBancaire.objects.filter(is_active=True).first()
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id', '').strip()
        if transaction_id:
            paiement.transaction_id = transaction_id
            paiement.statut = 'confirme'
            paiement.save()
            sub.status = 'actif'
            sub.save()
            code = genere_cle_activation(sub)
            notifier_activation_cle(sub, code)
            return render(request, 'studio/abonnement_succes.html', {
                'sub': sub, 'code': code, 'plan': sub.plan, 'paiement': paiement
            })
        return render(request, 'studio/abonnement_virement.html', {
            'sub': sub, 'paiement': paiement, 'plan': sub.plan,
            'error': 'Veuillez fournir le numéro de virement.'
        })
    return render(request, 'studio/abonnement_virement.html', {
        'sub': sub, 'paiement': paiement, 'plan': sub.plan, 'banque': banque
    })

def genere_cle_activation(souscription):
    code = 'PXL-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    CleActivation.objects.create(souscription=souscription, code=code)
    return code

# ─── Recrutement ────────────────────────────────────────────
def recrutement(request):
    if request.method == 'POST':
        type_cand = request.POST.get('type', 'worker')
        nom = request.POST.get('nom', '').strip()
        email = request.POST.get('email', '').strip()
        telephone = request.POST.get('telephone', '').strip()
        poste = request.POST.get('poste', '').strip()
        message = request.POST.get('message', '').strip()
        linkedin = request.POST.get('linkedin', '').strip()
        portfolio = request.POST.get('portfolio', '').strip()
        cv_file = request.FILES.get('cv')
        if not nom or not email:
            error = 'Le nom et l\'email sont obligatoires.'
            type_choices = Candidature.TYPE_CHOICES
            return render(request, 'studio/recrutement.html', {
                'type_choices': type_choices, 'error': error
            })
        candidature = Candidature.objects.create(
            type_candidature=type_cand, nom=nom, email=email,
            telephone=telephone, poste=poste, message=message,
            linkedin=linkedin, portfolio=portfolio
        )
        if cv_file:
            candidature.cv = cv_file
            candidature.save()
        return render(request, 'studio/recrutement_succes.html', {
            'nom': nom, 'type': type_cand
        })
    type_choices = Candidature.TYPE_CHOICES
    return render(request, 'studio/recrutement.html', {'type_choices': type_choices})

@login_required
def gestion_recrutement(request):
    candidatures = Candidature.objects.all()
    if request.method == 'POST':
        cid = request.POST.get('id')
        action = request.POST.get('action')
        if cid and action:
            cand = get_object_or_404(Candidature, id=cid)
            if action == 'statut':
                cand.statut = request.POST.get('statut', 'lu')
                cand.save()
            elif action == 'delete':
                cand.delete()
            return redirect('gestion_recrutement')
    return render(request, 'studio/gestion_recrutement.html', {'candidatures': candidatures})

# ─── E‑Commerce & Stock ────────────────────────────────────
def ecommerce_index(request):
    categories = Categorie.objects.all()
    produits = Produit.objects.filter(actif=True).order_by('-created_at')[:50]
    panier = request.session.get('panier', {})
    nb_articles = sum(panier.values())
    return render(request, 'studio/ecommerce.html', {
        'categories': categories, 'produits': produits,
        'nb_articles': nb_articles,
    })

def ecommerce_categorie(request, cat_id):
    cat = get_object_or_404(Categorie, id=cat_id)
    produits = Produit.objects.filter(categorie=cat, actif=True)
    panier = request.session.get('panier', {})
    nb_articles = sum(panier.values())
    return render(request, 'studio/ecommerce.html', {
        'categories': Categorie.objects.all(), 'produits': produits,
        'categorie_active': cat, 'nb_articles': nb_articles,
    })

def ecommerce_panier(request):
    panier_ids = request.session.get('panier', {})
    produits = Produit.objects.filter(id__in=panier_ids.keys(), actif=True)
    items = []
    total = 0
    for p in produits:
        qte = panier_ids.get(str(p.id), 0)
        st = p.prix_vente * qte
        items.append({'produit': p, 'quantite': qte, 'sous_total': st})
        total += st
    return render(request, 'studio/ecommerce_panier.html', {
        'items': items, 'total': total,
    })

def ecommerce_ajouter_panier(request, prod_id):
    prod = get_object_or_404(Produit, id=prod_id, actif=True)
    panier = request.session.get('panier', {})
    key = str(prod.id)
    panier[key] = panier.get(key, 0) + 1
    request.session['panier'] = panier
    return redirect(request.META.get('HTTP_REFERER', 'ecommerce_index'))

def ecommerce_supprimer_panier(request, prod_id):
    panier = request.session.get('panier', {})
    panier.pop(str(prod_id), None)
    request.session['panier'] = panier
    return redirect('ecommerce_panier')

def ecommerce_checkout(request):
    panier_ids = request.session.get('panier', {})
    if not panier_ids:
        return redirect('ecommerce_index')
    produits = Produit.objects.filter(id__in=panier_ids.keys(), actif=True)
    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        email = request.POST.get('email', '').strip()
        tel = request.POST.get('telephone', '').strip()
        adresse = request.POST.get('adresse', '').strip()
        ville = request.POST.get('ville', '').strip()
        cp = request.POST.get('code_postal', '').strip()
        methode = request.POST.get('methode_paiement', 'online')
        notes = request.POST.get('notes', '').strip()
        if not nom or not email or not adresse:
            return render(request, 'studio/ecommerce_checkout.html', {
                'error': 'Nom, email et adresse sont obligatoires.',
                'total': sum(p.prix_vente * panier_ids.get(str(p.id), 0) for p in produits),
                'produits': produits,
            })
        import uuid
        ref = f"EC-{uuid.uuid4().hex[:8].upper()}"
        total_ttc = sum(p.prix_vente * panier_ids.get(str(p.id), 0) for p in produits)
        commande = CommandeECommerce.objects.create(
            client_nom=nom, client_email=email, client_tel=tel,
            client_adresse=adresse, client_ville=ville,
            client_code_postal=cp, methode_paiement=methode,
            total_ttc=total_ttc, reference=ref, notes=notes,
            statut='en_attente',
        )
        for p in produits:
            qte = panier_ids.get(str(p.id), 0)
            if qte > 0:
                CommandeECommerceItem.objects.create(
                    commande=commande, produit=p,
                    nom_produit=p.nom, quantite=qte,
                    prix_unitaire=p.prix_vente,
                )
                p.stock_actuel -= qte
                p.save()
        request.session['panier'] = {}
        notifier_confirmation_commande(commande)
        if methode == 'online':
            config_paiement = ConfigurationPaiementEnLigne.objects.filter(est_actif=True).first()
            return render(request, 'studio/ecommerce_paiement.html', {
                'commande': commande, 'total_ttc': total_ttc, 'config_paiement': config_paiement,
            })
        request.session['commande_success'] = ref
        return redirect('ecommerce_succes')
    total = sum(p.prix_vente * panier_ids.get(str(p.id), 0) for p in produits)
    return render(request, 'studio/ecommerce_checkout.html', {
        'total': total, 'produits': produits,
    })

def ecommerce_paiement_confirm(request, cmd_id):
    commande = get_object_or_404(CommandeECommerce, id=cmd_id)
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id', '').strip()
        if transaction_id:
            commande.id_transaction = transaction_id
            commande.statut = 'confirmee'
            commande.save()
            notifier_confirmation_commande(commande)
            request.session['commande_success'] = commande.reference
            return redirect('ecommerce_succes')
        config_paiement = ConfigurationPaiementEnLigne.objects.filter(est_actif=True).first()
        return render(request, 'studio/ecommerce_paiement.html', {
            'commande': commande, 'total_ttc': commande.total_ttc,
            'config_paiement': config_paiement, 'error': 'ID de transaction requis.',
        })
    return redirect('ecommerce_checkout')

def ecommerce_succes(request):
    ref = request.session.pop('commande_success', None)
    if not ref:
        return redirect('ecommerce_index')
    commande = get_object_or_404(CommandeECommerce, reference=ref)
    return render(request, 'studio/ecommerce_succes.html', {'commande': commande})

@login_required
def gestion_stock(request):
    produits = Produit.objects.all()
    mouvements = MouvementStock.objects.all()[:50]
    alerte_stock = Produit.objects.filter(actif=True, stock_actuel__lte=models.F('stock_minimum'))
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add_mouvement':
            pid = request.POST.get('produit_id')
            typ = request.POST.get('type')
            qte = int(request.POST.get('quantite', 0))
            notes = request.POST.get('notes', '')
            reference = request.POST.get('reference', '')
            prod = get_object_or_404(Produit, id=pid)
            avant = prod.stock_actuel
            if typ == 'entree':
                prod.stock_actuel += qte
            elif typ == 'retour':
                prod.stock_actuel += qte
            else:
                prod.stock_actuel = max(0, prod.stock_actuel - qte)
            prod.save()
            MouvementStock.objects.create(
                produit=prod, type=typ, quantite=qte,
                stock_avant=avant, stock_apres=prod.stock_actuel,
                reference=reference, notes=notes,
            )
        elif action == 'edit_produit':
            pid = request.POST.get('produit_id')
            prod = get_object_or_404(Produit, id=pid)
            prod.nom = request.POST.get('nom', prod.nom)
            prod.prix_achat = request.POST.get('prix_achat', prod.prix_achat)
            prod.prix_vente = request.POST.get('prix_vente', prod.prix_vente)
            prod.stock_minimum = request.POST.get('stock_minimum', prod.stock_minimum)
            prod.save()
        return redirect('gestion_stock')
    return render(request, 'studio/ecommerce_stock.html', {
        'produits': produits, 'mouvements': mouvements,
        'alerte_stock': alerte_stock, 'categories': Categorie.objects.all(),
        'fournisseurs': Fournisseur.objects.all(),
    })

@login_required
def gestion_commandes(request):
    statut_filtre = request.GET.get('statut', '')
    if statut_filtre:
        commandes = CommandeECommerce.objects.filter(statut=statut_filtre)
    else:
        commandes = CommandeECommerce.objects.all()
    commandes = commandes.order_by('-date_commande')[:100]
    if request.method == 'POST':
        cid = request.POST.get('commande_id')
        action = request.POST.get('action')
        cmd = get_object_or_404(CommandeECommerce, id=cid)
        if action == 'statut':
            cmd.statut = request.POST.get('statut', cmd.statut)
            cmd.save()
            if cmd.statut in ('expediee', 'livree', 'annulee'):
                notifier_statut_commande(cmd)
        elif action == 'delete':
            cmd.delete()
        return redirect('gestion_commandes')
    stats = {
        'total': CommandeECommerce.objects.count(),
        'en_attente': CommandeECommerce.objects.filter(statut='en_attente').count(),
        'confirmees': CommandeECommerce.objects.filter(statut='confirmee').count(),
        'livrees': CommandeECommerce.objects.filter(statut='livree').count(),
    }
    return render(request, 'studio/gestion_commandes.html', {
        'commandes': commandes, 'statut_filtre': statut_filtre, 'stats': stats,
    })

# ─── Portail client ──────────────────────────────────────────
@login_required
def portail(request):
    email = request.user.email
    commandes = CommandeECommerce.objects.filter(client_email=email).order_by('-date_commande')[:20]
    souscriptions = SouscriptionClient.objects.filter(client_email=email).order_by('-created_at')[:20]
    candidatures = Candidature.objects.filter(email=email).order_by('-created_at')[:10]
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'edit_profile':
            profile = request.user.profile
            profile.entreprise = request.POST.get('entreprise', '')
            profile.telephone = request.POST.get('telephone', '')
            profile.save()
            request.user.first_name = request.POST.get('prenom', '')
            request.user.last_name = request.POST.get('nom', '')
            request.user.save()
            return redirect('portail')
    return render(request, 'studio/portail.html', {
        'commandes': commandes, 'souscriptions': souscriptions,
        'candidatures': candidatures,
    })

# ─── Administration bancaire ─────────────────────────────────
@login_required
def admin_bancaire(request):
    banques = ConfigurationBancaire.objects.all()
    configs_enligne = ConfigurationPaiementEnLigne.objects.all()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add_banque':
            ConfigurationBancaire.objects.create(
                banque=request.POST.get('banque'), agence=request.POST.get('agence',''),
                rib=request.POST.get('rib',''), swift=request.POST.get('swift',''),
                titulaire=request.POST.get('titulaire',''),
                est_defaut=request.POST.get('est_defaut','0')=='1'
            )
        elif action == 'edit_banque':
            b = get_object_or_404(ConfigurationBancaire, id=request.POST.get('edit_id'))
            b.banque = request.POST.get('banque'); b.agence = request.POST.get('agence','')
            b.rib = request.POST.get('rib',''); b.swift = request.POST.get('swift','')
            b.titulaire = request.POST.get('titulaire','')
            b.est_defaut = request.POST.get('est_defaut','0')=='1'
            b.is_active = request.POST.get('is_active','1')=='1'
            b.save()
        elif action == 'delete_banque':
            ConfigurationBancaire.objects.filter(id=request.POST.get('id')).delete()
        elif action == 'save_paiement_config':
            cfg, _ = ConfigurationPaiementEnLigne.objects.get_or_create(id=request.POST.get('config_id',0))
            cfg.fournisseur = request.POST.get('fournisseur','manual')
            cfg.instructions = request.POST.get('instructions','')
            cfg.frais_pourcentage = request.POST.get('frais_pourcentage',0)
            cfg.est_actif = request.POST.get('est_actif','1')=='1'
            cfg.save()
        return redirect('admin_bancaire')
    return render(request, 'studio/admin_bancaire.html', {
        'banques': banques, 'configs_enligne': configs_enligne
    })

# ─── API: Vérifier clé d'activation ─────────────────────────
@csrf_exempt
def api_verifier_cle(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('code', '').strip().upper()
            cle = CleActivation.objects.filter(code=code, est_utilisee=True).first()
            if cle:
                return JsonResponse({
                    "status": "success", "valide": True,
                    "client": cle.souscription.client_nom,
                    "plan": cle.souscription.plan.nom,
                    "date_activation": cle.date_activation.strftime('%d/%m/%Y') if cle.date_activation else '',
                })
            return JsonResponse({"status": "error", "valide": False, "message": "Clé invalide ou non activée."})
        except Exception:
            return JsonResponse({"status": "error", "message": "Erreur serveur."}, status=500)
    return JsonResponse({"status": "error", "message": "Méthode non autorisée."}, status=405)

def api_me(request):
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
        atelier = getattr(request.user, 'atelier', None)
        return JsonResponse({
            "status": "success",
            "user": {
                "username": request.user.username,
                "email": request.user.email,
                "entreprise": profile.entreprise if profile else '',
                "atelier_role": atelier.role if atelier else None,
            }
        })
    return JsonResponse({"status": "error", "user": None}, status=401)

# ─── Dashboard central ──────────────────────────────────────
def dashboard(request):
    from django.db.models import Sum, Count
    stats = {
        'produits': Produit.objects.filter(actif=True).count(),
        'commandes': CommandeECommerce.objects.count(),
        'ca_total': CommandeECommerce.objects.filter(statut__in=['confirmee','livree','expediee']).aggregate(t=Sum('total_ttc'))['t'] or 0,
        'commandes_en_attente': CommandeECommerce.objects.filter(statut='en_attente').count(),
        'souscriptions_actives': SouscriptionClient.objects.filter(status='actif').count(),
        'total_souscriptions': SouscriptionClient.objects.count(),
        'candidatures_nouvelles': Candidature.objects.filter(statut='nouveau').count(),
        'total_candidatures': Candidature.objects.count(),
        'alerte_stock': Produit.objects.filter(actif=True, stock_actuel__lte=models.F('stock_minimum')).count(),
        'total_produits_stock': Produit.objects.count(),
        'utilisateurs': User.objects.count(),
        'revenu_abonnements': Paiement.objects.filter(statut='confirme').aggregate(t=Sum('montant'))['t'] or 0,
    }
    commandes_recentes = CommandeECommerce.objects.all().order_by('-date_commande')[:10]
    return render(request, 'studio/dashboard.html', {
        'stats': stats, 'commandes_recentes': commandes_recentes,
    })

# ─── Facture PDF (print-friendly) ────────────────────────────
@login_required
def facture_commande(request, cmd_id):
    commande = get_object_or_404(CommandeECommerce, id=cmd_id)
    items = commande.items.all()
    from django.conf import settings
    societe = {
        'nom': 'Pixel Software Design',
        'slogan': "L'architecture de l'innovation",
        'adresse': 'Tunis, Tunisie',
        'email': 'contact@pixelsoftwaredesign.com',
        'tel': '+216 XX XXX XXX',
        'registre': 'Matricule: XXXXXXXX/X/X/XXX',
    }
    return render(request, 'studio/facture.html', {
        'commande': commande, 'items': items, 'societe': societe,
    })

# ─── API REST e‑commerce & stock ───────────────────────────
@csrf_exempt
def api_produits(request, prod_id=None):
    if request.method == 'GET':
        if prod_id:
            p = get_object_or_404(Produit, id=prod_id, actif=True)
            return JsonResponse({
                'id': p.id, 'nom': p.nom, 'prix_vente': str(p.prix_vente),
                'stock': p.stock_actuel, 'categorie': p.categorie.nom if p.categorie else None,
                'code_barre': p.code_barre,
            })
        qs = Produit.objects.filter(actif=True)
        cat = request.GET.get('categorie')
        if cat: qs = qs.filter(categorie_id=cat)
        data = [{
            'id': p.id, 'nom': p.nom, 'prix_vente': str(p.prix_vente),
            'stock': p.stock_actuel, 'categorie': p.categorie.nom if p.categorie else None,
        } for p in qs]
        return JsonResponse({'produits': data})
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def api_categories(request):
    if request.method == 'GET':
        data = [{'id': c.id, 'nom': c.nom, 'description': c.description} for c in Categorie.objects.all()]
        return JsonResponse({'categories': data})
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def api_stock_mouvements(request):
    if request.method == 'GET':
        qs = MouvementStock.objects.all()
        produit = request.GET.get('produit')
        if produit: qs = qs.filter(produit_id=produit)
        type_f = request.GET.get('type')
        if type_f: qs = qs.filter(type=type_f)
        data = [{
            'id': m.id, 'produit': m.produit.nom, 'produit_id': m.produit_id,
            'type': m.type, 'quantite': m.quantite,
            'stock_avant': m.stock_avant, 'stock_apres': m.stock_apres,
            'reference': m.reference, 'notes': m.notes,
            'date': m.date_mouvement.isoformat(),
        } for m in qs]
        return JsonResponse({'mouvements': data})
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            prod = get_object_or_404(Produit, id=body.get('produit_id'))
            type_mvt = body.get('type', 'ajustement')
            quantite = int(body.get('quantite', 0))
            avant = prod.stock_actuel
            if type_mvt == 'entree':
                prod.stock_actuel += quantite
            elif type_mvt == 'sortie':
                prod.stock_actuel = max(0, prod.stock_actuel - quantite)
            else:
                prod.stock_actuel = max(0, quantite)
            prod.save()
            mvt = MouvementStock.objects.create(
                produit=prod, type=type_mvt, quantite=quantite,
                stock_avant=avant, stock_apres=prod.stock_actuel,
                reference=body.get('reference', ''), notes=body.get('notes', ''),
                cree_par=body.get('cree_par', ''),
            )
            return JsonResponse({'status': 'ok', 'id': mvt.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def api_commandes(request, cmd_id=None):
    if request.method == 'GET':
        if cmd_id:
            c = get_object_or_404(CommandeECommerce, id=cmd_id)
            items = [{'id': i.id, 'produit': i.nom_produit, 'quantite': i.quantite, 'prix_unitaire': str(i.prix_unitaire), 'sous_total': str(i.sous_total())} for i in c.items.all()]
            return JsonResponse({
                'id': c.id, 'reference': c.reference, 'client_nom': c.client_nom,
                'client_email': c.client_email, 'client_tel': c.client_tel,
                'client_adresse': c.client_adresse, 'client_ville': c.client_ville,
                'statut': c.statut, 'methode_paiement': c.methode_paiement,
                'total_ttc': str(c.total_ttc), 'notes': c.notes,
                'date_commande': c.date_commande.isoformat(),
                'items': items,
            })
        qs = CommandeECommerce.objects.all()
        statut = request.GET.get('statut')
        if statut: qs = qs.filter(statut=statut)
        email = request.GET.get('email')
        if email: qs = qs.filter(client_email=email)
        data = [{
            'id': c.id, 'reference': c.reference, 'client_nom': c.client_nom,
            'client_email': c.client_email, 'statut': c.statut,
            'methode_paiement': c.methode_paiement, 'total_ttc': str(c.total_ttc),
            'date_commande': c.date_commande.isoformat(),
            'items_count': c.items.count(),
        } for c in qs]
        return JsonResponse({'commandes': data})
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def api_commande_statut(request, cmd_id):
    if request.method in ('PATCH', 'POST'):
        try:
            body = json.loads(request.body) if request.body else {}
            nouveau_statut = body.get('statut', request.POST.get('statut', ''))
            statuts_valides = [s[0] for s in CommandeECommerce.STATUTS]
            if nouveau_statut not in statuts_valides:
                return JsonResponse({"error": f"Statut invalide. Valeurs: {', '.join(statuts_valides)}"}, status=400)
            c = get_object_or_404(CommandeECommerce, id=cmd_id)
            c.statut = nouveau_statut
            c.save()
            return JsonResponse({'status': 'ok', 'statut': c.statut})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def api_panier(request):
    panier = request.session.get('panier', {})
    if request.method == 'GET':
        produits = Produit.objects.filter(id__in=[int(k) for k in panier.keys() if panier[k] > 0])
        items = []
        total = 0
        for p in produits:
            qty = panier.get(str(p.id), 0)
            if qty > 0:
                st = float(p.prix_vente) * qty
                items.append({'id': p.id, 'nom': p.nom, 'prix_unitaire': str(p.prix_vente), 'quantite': qty, 'sous_total': str(st)})
                total += st
        return JsonResponse({'items': items, 'total_ttc': str(total)})
    if request.method == 'DELETE':
        request.session['panier'] = {}
        request.session.modified = True
        return JsonResponse({'status': 'ok', 'message': 'Panier vidé'})
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def api_panier_ajouter(request, prod_id):
    if request.method == 'POST':
        prod = get_object_or_404(Produit, id=prod_id, actif=True)
        panier = request.session.get('panier', {})
        key = str(prod.id)
        panier[key] = panier.get(key, 0) + 1
        request.session['panier'] = panier
        request.session.modified = True
        return JsonResponse({'status': 'ok', 'quantite': panier[key]})
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def api_panier_retirer(request, prod_id):
    if request.method == 'POST':
        panier = request.session.get('panier', {})
        key = str(prod_id)
        if key in panier:
            if panier[key] > 1:
                panier[key] -= 1
            else:
                del panier[key]
            request.session['panier'] = panier
            request.session.modified = True
        return JsonResponse({'status': 'ok'})
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

# ─── Pages vitrine ─────────────────────────────────────────
def a_propos(request):
    return render(request, 'studio/a_propos.html')

def contact_page(request):
    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if not nom or not email or not message:
            return render(request, 'studio/contact.html', {'error': 'Veuillez remplir tous les champs obligatoires.'})
        ProjetContact.objects.create(nom=nom, email=email, message=message)
        return render(request, 'studio/contact.html', {'success': 'Merci pour votre message. Nous vous répondrons dans les plus brefs délais.'})
    return render(request, 'studio/contact.html')

def faq(request):
    faqs = [
        {'q': "Quels types de logiciels développez-vous ?", 'a': "Nous développons des logiciels de gestion (ERP GestiActiv), des sites web, des applications mobiles, des solutions e-commerce, des logiciels sur mesure et des produits SaaS. Chaque solution est adaptée aux besoins spécifiques de votre entreprise."},
        {'q': "Proposez-vous des solutions pour les PME tunisiennes ?", 'a': "Absolument. GestiActiv est conçu spécifiquement pour les PME tunisiennes avec des modules couvrant la comptabilité, les RH, la paie, le commerce, la santé, l'hôtellerie, la restauration, l'auto-école et le juridique."},
        {'q': "Comment puis-je souscrire à un abonnement PixelSoftCode ?", 'a': "Rendez-vous sur la page Prix pour consulter nos offres, choisissez le plan qui vous convient, suivez la procédure de souscription et effectuez le paiement en ligne, par virement bancaire ou en espèces."},
        {'q': "Quels modes de paiement acceptez-vous ?", 'a': "Nous acceptons les paiements en ligne (carte bancaire via notre passerelle sécurisée), le virement bancaire vers nos comptes en Tunisie, et les espèces en agence."},
        {'q': "Proposez-vous un essai gratuit de GestiActiv ?", 'a': "Oui, vous pouvez demander une démo gratuite sur la page GestiActiv. Notre équipe vous contactera pour organiser une présentation personnalisée de vos modules d'intérêt."},
        {'q': "Quel est le délai de livraison pour un projet sur mesure ?", 'a': "Le délai varie selon la complexité du projet. En moyenne, un site web vitrine est livré en 1 à 2 semaines, une application e-commerce en 3 à 6 semaines, et un ERP sur mesure en 2 à 6 mois."},
        {'q': "Proposez-vous des services de maintenance après livraison ?", 'a': "Oui, nous proposons des contrats de maintenance et de support technique pour tous nos logiciels. Les abonnements PixelSoftCode incluent la maintenance et les mises à jour."},
        {'q': "Comment rejoindre l'équipe Pixel Software Design ?", 'a': "Consultez notre page Recrutement pour postuler en tant que worker (employé), partenaire ou freelance. Nous sommes toujours à la recherche de talents passionnés par l'innovation technologique."},
    ]
    return render(request, 'studio/faq.html', {'faqs': faqs})

def temoignages(request):
    temoignages = Temoignage.objects.filter(actif=True)
    return render(request, 'studio/temoignages.html', {'temoignages': temoignages})
