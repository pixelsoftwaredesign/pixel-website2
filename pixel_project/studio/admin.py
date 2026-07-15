from django.contrib import admin
from .models import UserProfile, ProjetContact, AtelierProfile, PortfolioProject, CodeRepository, GraphismeResource, ERPClient, ERPModule, ERPSubscription, ERPDemoRecord, Moniteur, Candidat, Vehicule, Lecon, Examen, Medecin, Patient, Lit, RendezVous, FacturationSante, ClientHotel, Chambre, ReservationHotel, ServiceHotel, Categorie, Fournisseur, Produit, Vente, ClientJuridique, DossierJuridique, Audience, JournalComptable, EcritureComptable, Facture, DeclarationFiscale, Employe, Contrat, FichePaie, Conge, Formation, MenuItem, TableRestaurant, SoftCodeModule, StudioProject3D, PatisserieRecipe, PatisserieProduct, PlanAbonnement, SouscriptionClient, Paiement, CleActivation, ConfigurationBancaire, ConfigurationPaiementEnLigne, Candidature, MouvementStock, CommandeECommerce, CommandeECommerceItem, Temoignage

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'entreprise', 'telephone')
    search_fields = ('user__username', 'entreprise')

@admin.register(ProjetContact)
class ProjetContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'date_reception')
    search_fields = ('nom', 'email', 'message')
    list_filter = ('date_reception',)
    readonly_fields = ('date_reception',)

@admin.register(AtelierProfile)
class AtelierProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'created_at')
    list_filter = ('role',)
    search_fields = ('user__username',)

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'designer', 'category', 'likes', 'downloads', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'designer__user__username')

@admin.register(CodeRepository)
class CodeRepositoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'developer', 'language', 'stars', 'forks', 'created_at')
    list_filter = ('language',)
    search_fields = ('name', 'developer__user__username')

@admin.register(GraphismeResource)
class GraphismeResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_free', 'downloads', 'likes', 'created_at')
    list_filter = ('category', 'is_free', 'file_type')
    search_fields = ('title', 'author__username')

@admin.register(ERPClient)
class ERPClientAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name', 'email', 'is_active', 'created_at')
    search_fields = ('company_name', 'contact_name', 'email')
    list_filter = ('is_active',)

@admin.register(ERPModule)
class ERPModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon', 'is_available', 'order')
    list_filter = ('is_available',)

@admin.register(ERPSubscription)
class ERPSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('client', 'module', 'is_active', 'start_date')
    list_filter = ('is_active', 'module')

@admin.register(ERPDemoRecord)
class ERPDemoRecordAdmin(admin.ModelAdmin):
    list_display = ('module', 'label', 'value', 'status', 'created_at')
    list_filter = ('module', 'status')

# ─── Auto-École ───
@admin.register(Moniteur)
class MoniteurAdmin(admin.ModelAdmin): list_display = ('nom','telephone','specialite','actif')
@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin): list_display = ('nom','type_permis','moniteur','total_heures','reussi')
@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin): list_display = ('immatriculation','marque','modele','disponible')
@admin.register(Lecon)
class LeconAdmin(admin.ModelAdmin): list_display = ('candidat','moniteur','date_lecon','validee')
@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin): list_display = ('candidat','type_examen','date_examen','reussi','note')

# ─── Santé ───
@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin): list_display = ('nom','specialite','actif')
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin): list_display = ('nom','telephone','mutuelle')
@admin.register(Lit)
class LitAdmin(admin.ModelAdmin): list_display = ('numero','chambre','type_lit','occupe')
@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin): list_display = ('patient','medecin','date_rdv','statut')
@admin.register(FacturationSante)
class FacturationSanteAdmin(admin.ModelAdmin): list_display = ('patient','montant','payee','type_facture')

# ─── Hôtel ───
@admin.register(ClientHotel)
class ClientHotelAdmin(admin.ModelAdmin): list_display = ('nom','telephone','email','nationalite')
@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin): list_display = ('numero','type_chambre','prix_nuit','disponible')
@admin.register(ReservationHotel)
class ReservationHotelAdmin(admin.ModelAdmin): list_display = ('client','chambre','date_arrivee','date_depart','statut')
@admin.register(ServiceHotel)
class ServiceHotelAdmin(admin.ModelAdmin): list_display = ('reservation','nom_service','prix')

# ─── Commerce ───
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin): list_display = ('nom',)
@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin): list_display = ('nom','telephone','email')
@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin): list_display = ('nom','categorie','prix_vente','stock_actuel','actif')
@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin): list_display = ('produit','quantite','prix_unitaire','date_vente')

# ─── Juridique ───
@admin.register(ClientJuridique)
class ClientJuridiqueAdmin(admin.ModelAdmin): list_display = ('nom','type_client')
@admin.register(DossierJuridique)
class DossierJuridiqueAdmin(admin.ModelAdmin): list_display = ('reference','client','type_affaire','statut')
@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin): list_display = ('dossier','date_audience','lieu')

# ─── Comptabilité ───
@admin.register(JournalComptable)
class JournalComptableAdmin(admin.ModelAdmin): list_display = ('code','nom')
@admin.register(EcritureComptable)
class EcritureComptableAdmin(admin.ModelAdmin): list_display = ('date_ecriture','libelle','compte_debit','compte_credit','montant')
@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin): list_display = ('numero','client_nom','montant_ttc','payee')
@admin.register(DeclarationFiscale)
class DeclarationFiscaleAdmin(admin.ModelAdmin): list_display = ('type_declaration','periode','montant','soumise')

# ─── RH & Paie ───
@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin): list_display = ('nom','poste','departement','salaire_base','actif')
@admin.register(Contrat)
class ContratAdmin(admin.ModelAdmin): list_display = ('employe','type_contrat','date_debut','date_fin','actif')
@admin.register(FichePaie)
class FichePaieAdmin(admin.ModelAdmin): list_display = ('employe','mois','net_a_payer','payee')
@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin): list_display = ('employe','type_conge','date_debut','date_fin','valide')
@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin): list_display = ('employe','titre','date_debut','date_fin','cout','terminee')

# ─── Restaurant ───
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin): list_display = ('nom','categorie','prix','disponible')
@admin.register(TableRestaurant)
class TableRestaurantAdmin(admin.ModelAdmin): list_display = ('numero','capacite','statut')

# ─── PixelSoftCode ───
@admin.register(SoftCodeModule)
class SoftCodeModuleAdmin(admin.ModelAdmin): list_display = ('nom','categorie','version','prix','disponible')

# ─── Inner Studio ───
@admin.register(StudioProject3D)
class StudioProject3DAdmin(admin.ModelAdmin): list_display = ('nom','categorie','created_at')

# ─── Pâtisserie ───
@admin.register(PatisserieRecipe)
class PatisserieRecipeAdmin(admin.ModelAdmin): list_display = ('nom','categorie','cout_production','prix_vente')
@admin.register(PatisserieProduct)
class PatisserieProductAdmin(admin.ModelAdmin): list_display = ('nom','recette','stock_actuel','prix_vente','actif')

# ─── Abonnements & Paiements ───
@admin.register(PlanAbonnement)
class PlanAbonnementAdmin(admin.ModelAdmin): list_display = ('nom','categorie','prix','duree_jours','is_available','order')
@admin.register(SouscriptionClient)
class SouscriptionClientAdmin(admin.ModelAdmin): list_display = ('client_nom','client_email','plan','status','date_debut','date_fin')
@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin): list_display = ('reference','souscription','methode','montant','statut','date_paiement')
@admin.register(CleActivation)
class CleActivationAdmin(admin.ModelAdmin): list_display = ('code','souscription','est_utilisee','date_creation','date_activation')
@admin.register(ConfigurationBancaire)
class ConfigurationBancaireAdmin(admin.ModelAdmin): list_display = ('banque','titulaire','rib','est_defaut','is_active')
@admin.register(ConfigurationPaiementEnLigne)
class ConfigurationPaiementEnLigneAdmin(admin.ModelAdmin): list_display = ('fournisseur','est_actif','frais_pourcentage')

# ─── Recrutement ───
@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin): list_display = ('nom','type_candidature','poste','statut','email','created_at'); list_filter = ('type_candidature','statut')

# ─── Pages vitrine ───
@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'entreprise', 'note', 'actif', 'created_at')
    list_filter = ('actif', 'note')
    search_fields = ('nom', 'entreprise')

# ─── E‑Commerce & Stock ───
@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin): list_display = ('produit','type','quantite','stock_avant','stock_apres','date_mouvement')
@admin.register(CommandeECommerce)
class CommandeECommerceAdmin(admin.ModelAdmin): list_display = ('reference','client_nom','total_ttc','statut','methode_paiement','date_commande')
@admin.register(CommandeECommerceItem)
class CommandeECommerceItemAdmin(admin.ModelAdmin): list_display = ('commande','nom_produit','quantite','prix_unitaire')
