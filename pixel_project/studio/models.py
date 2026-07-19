from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    entreprise = models.CharField(max_length=100, blank=True, null=True, verbose_name="Entreprise")
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")

    class Meta:
        verbose_name = "Profil utilisateur"
        verbose_name_plural = "Profils utilisateurs"

    def __str__(self):
        return f"Profil de {self.user.username}"

class ProjetContact(models.Model):
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='projets')
    nom = models.CharField(max_length=150, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    date_reception = models.DateTimeField(auto_now_add=True, verbose_name="Date de réception")

    class Meta:
        verbose_name = "Projet reçu"
        verbose_name_plural = "Projets reçus"
        ordering = ['-date_reception']

    def __str__(self):
        return f"Projet de {self.nom} - {self.date_reception.strftime('%d/%m/%Y')}"

class AtelierProfile(models.Model):
    ROLE_CHOICES = [
        ('designer', 'Designer'),
        ('developer', 'Développeur'),
        ('both', 'Designer & Développeur'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='atelier')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='designer')
    bio = models.TextField(blank=True, verbose_name="Bio")
    skills = models.CharField(max_length=500, blank=True, verbose_name="Compétences")
    avatar_url = models.URLField(blank=True, verbose_name="Avatar URL")
    github = models.URLField(blank=True, verbose_name="GitHub")
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
    website = models.URLField(blank=True, verbose_name="Site web")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Profil Atelier"
        verbose_name_plural = "Profils Atelier"

    def __str__(self):
        return f"Atelier {self.user.username} ({self.get_role_display()})"

class PortfolioProject(models.Model):
    designer = models.ForeignKey(AtelierProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(blank=True, verbose_name="Description")
    category = models.CharField(max_length=100, verbose_name="Catégorie")
    tags = models.CharField(max_length=500, blank=True, verbose_name="Tags")
    image_url = models.URLField(blank=True, verbose_name="Image URL")
    figma_url = models.URLField(blank=True, verbose_name="Lien Figma")
    likes = models.IntegerField(default=0, verbose_name="Likes")
    downloads = models.IntegerField(default=0, verbose_name="Téléchargements")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Projet portfolio"
        verbose_name_plural = "Projets portfolio"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class CodeRepository(models.Model):
    developer = models.ForeignKey(AtelierProfile, on_delete=models.CASCADE, related_name='repos')
    name = models.CharField(max_length=200, verbose_name="Nom du repo")
    description = models.TextField(blank=True, verbose_name="Description")
    language = models.CharField(max_length=50, verbose_name="Langage")
    tags = models.CharField(max_length=500, blank=True, verbose_name="Tags")
    code_content = models.TextField(blank=True, verbose_name="Code source")
    github_url = models.URLField(blank=True, verbose_name="Lien GitHub")
    stars = models.IntegerField(default=0, verbose_name="Stars")
    forks = models.IntegerField(default=0, verbose_name="Forks")
    downloads = models.IntegerField(default=0, verbose_name="Téléchargements")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Repository de code"
        verbose_name_plural = "Repositories de code"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class GraphismeResource(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='graphisme_resources')
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(blank=True, verbose_name="Description")
    category = models.CharField(max_length=100, verbose_name="Catégorie")
    tags = models.CharField(max_length=500, blank=True, verbose_name="Tags")
    file_url = models.URLField(blank=True, verbose_name="URL du fichier")
    file = models.FileField(upload_to='graphisme/files/', blank=True, verbose_name="Fichier")
    preview_url = models.URLField(blank=True, verbose_name="URL de prévisualisation")
    preview_image = models.ImageField(upload_to='graphisme/previews/', blank=True, verbose_name="Image de prévisualisation")
    file_type = models.CharField(max_length=50, blank=True, verbose_name="Type de fichier")
    is_free = models.BooleanField(default=True, verbose_name="Gratuit")
    downloads = models.IntegerField(default=0, verbose_name="Téléchargements")
    likes = models.IntegerField(default=0, verbose_name="Likes")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Prix (TND)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ressource graphique"
        verbose_name_plural = "Ressources graphiques"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ERPClient(models.Model):
    company_name = models.CharField(max_length=200, verbose_name="Entreprise")
    contact_name = models.CharField(max_length=150, verbose_name="Contact")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    matricule = models.CharField(max_length=50, blank=True, verbose_name="Matricule fiscal")
    address = models.TextField(blank=True, verbose_name="Adresse")
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Client ERP"
        verbose_name_plural = "Clients ERP"

    def __str__(self):
        return self.company_name

class ERPModule(models.Model):
    MODULE_SLUGS = [
        ('auto-ecole', 'Auto-École'),
        ('sante', 'Santé / Clinique'),
        ('hotellerie', 'Hôtellerie / Tourisme'),
        ('commerce', 'Commerce / Retail'),
        ('juridique', 'Juridique'),
        ('comptabilite', 'Comptabilité'),
        ('rh-paie', 'RH & Paie'),
    ]
    slug = models.CharField(max_length=50, unique=True, choices=MODULE_SLUGS)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, default='📦')
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Module ERP"
        verbose_name_plural = "Modules ERP"
        ordering = ['order']

    def __str__(self):
        return self.name

class ERPSubscription(models.Model):
    client = models.ForeignKey(ERPClient, on_delete=models.CASCADE, related_name='subscriptions')
    module = models.ForeignKey(ERPModule, on_delete=models.CASCADE, related_name='subscriptions')
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Abonnement module"
        verbose_name_plural = "Abonnements modules"
        unique_together = ('client', 'module')

    def __str__(self):
        return f"{self.client.company_name} - {self.module.name}"

class ERPDemoRecord(models.Model):
    module = models.ForeignKey(ERPModule, on_delete=models.CASCADE, related_name='demo_records')
    label = models.CharField(max_length=200, verbose_name="Libellé")
    value = models.CharField(max_length=200, verbose_name="Valeur")
    extra = models.TextField(blank=True, verbose_name="Info supplémentaire")
    status = models.CharField(max_length=50, default='active', verbose_name="Statut")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Enregistrement démo"
        verbose_name_plural = "Enregistrements démo"
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.module.name}] {self.label}"


# ─── Auto-École ─────────────────────────────────────────────
class Moniteur(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    specialite = models.CharField(max_length=100, blank=True, verbose_name="Spécialité")
    actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Moniteur"; verbose_name_plural = "Moniteurs"; ordering = ['nom']
    def __str__(self): return self.nom

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    date_inscription = models.DateField(auto_now_add=True, verbose_name="Date d'inscription")
    type_permis = models.CharField(max_length=20, default='B', verbose_name="Type permis")
    moniteur = models.ForeignKey(Moniteur, on_delete=models.SET_NULL, null=True, blank=True)
    total_heures = models.IntegerField(default=0, verbose_name="Heures effectuées")
    reussi = models.BooleanField(default=False, verbose_name="Réussi")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Candidat"; verbose_name_plural = "Candidats"; ordering = ['-date_inscription']
    def __str__(self): return f"{self.nom} ({self.type_permis})"

class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20, unique=True)
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.IntegerField(default=2024)
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Véhicule"; verbose_name_plural = "Véhicules"
    def __str__(self): return f"{self.marque} {self.modele} ({self.immatriculation})"

class Lecon(models.Model):
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE, related_name='lecons')
    moniteur = models.ForeignKey(Moniteur, on_delete=models.SET_NULL, null=True)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.SET_NULL, null=True)
    date_lecon = models.DateTimeField(verbose_name="Date de la leçon")
    duree_minutes = models.IntegerField(default=60)
    validee = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Leçon"; verbose_name_plural = "Leçons"; ordering = ['-date_lecon']
    def __str__(self): return f"{self.candidat.nom} - {self.date_lecon.strftime('%d/%m/%Y')}"

class Examen(models.Model):
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE, related_name='examens')
    date_examen = models.DateField(verbose_name="Date d'examen")
    type_examen = models.CharField(max_length=20, choices=[('code','Code'),('pratique','Pratique')], default='code')
    reussi = models.BooleanField(default=False)
    note = models.IntegerField(default=0)
    observations = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Examen"; verbose_name_plural = "Examens"; ordering = ['-date_examen']
    def __str__(self): return f"{self.candidat.nom} - {self.get_type_examen_display()}"


# ─── Santé / Clinique ───────────────────────────────────────
class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Médecin"; verbose_name_plural = "Médecins"
    def __str__(self): return f"Dr {self.nom} ({self.specialite})"

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField(verbose_name="Date de naissance")
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    adresse = models.TextField(blank=True)
    mutuelle = models.CharField(max_length=100, blank=True, verbose_name="Mutuelle/CNAM")
    medecin_traitant = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Médecin traitant")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Patient"; verbose_name_plural = "Patients"; ordering = ['nom']
    def __str__(self): return self.nom

class Lit(models.Model):
    numero = models.CharField(max_length=20, unique=True, verbose_name="N° Lit")
    chambre = models.CharField(max_length=50, blank=True)
    type_lit = models.CharField(max_length=50, choices=[('simple','Simple'),('double','Double'),('soins','Soins intensifs')], default='simple')
    occupe = models.BooleanField(default=False)
    patient = models.OneToOneField(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Lit"; verbose_name_plural = "Lits"
    def __str__(self): return f"Lit {self.numero} ({self.chambre})"

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='rendez_vous')
    medecin = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True)
    date_rdv = models.DateTimeField(verbose_name="Date du rendez-vous")
    motif = models.CharField(max_length=200, blank=True)
    statut = models.CharField(max_length=20, choices=[('planifie','Planifié'),('confirme','Confirmé'),('termine','Terminé'),('annule','Annulé')], default='planifie')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Rendez-vous"; verbose_name_plural = "Rendez-vous"; ordering = ['-date_rdv']
    def __str__(self): return f"{self.patient.nom} - Dr {self.medecin.nom if self.medecin else 'N/A'}"

class FacturationSante(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='factures')
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant (TND)")
    date_facture = models.DateField(auto_now_add=True)
    payee = models.BooleanField(default=False)
    type_facture = models.CharField(max_length=50, choices=[('consultation','Consultation'),('hospitalisation','Hospitalisation'),('examen','Examen'),('pharmacie','Pharmacie')], default='consultation')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Facturation santé"; verbose_name_plural = "Facturations santé"
    def __str__(self): return f"{self.patient.nom} - {self.montant} TND"


# ─── Hôtellerie / Tourisme ──────────────────────────────────
class ClientHotel(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    nationalite = models.CharField(max_length=50, blank=True)
    piece_identite = models.CharField(max_length=100, blank=True, verbose_name="Pièce d'identité")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Client hôtel"; verbose_name_plural = "Clients hôtel"
    def __str__(self): return self.nom

class Chambre(models.Model):
    numero = models.CharField(max_length=20, unique=True, verbose_name="N° Chambre")
    type_chambre = models.CharField(max_length=50, choices=[('simple','Simple'),('double','Double'),('suite','Suite'),('suite-p','Suite Présidentielle')], default='simple')
    prix_nuit = models.DecimalField(max_digits=8, decimal_places=2, default=100, verbose_name="Prix/nuit (TND)")
    disponible = models.BooleanField(default=True)
    etage = models.IntegerField(default=1)
    capacite = models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Chambre"; verbose_name_plural = "Chambres"
    def __str__(self): return f"Chambre {self.numero} ({self.get_type_chambre_display()})"

class ReservationHotel(models.Model):
    client = models.ForeignKey(ClientHotel, on_delete=models.CASCADE, related_name='reservations')
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE, related_name='reservations')
    date_arrivee = models.DateField(verbose_name="Date d'arrivée")
    date_depart = models.DateField(verbose_name="Date de départ")
    statut = models.CharField(max_length=20, choices=[('confirmee','Confirmée'),('en_cours','En cours'),('terminee','Terminée'),('annulee','Annulée')], default='confirmee')
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Réservation"; verbose_name_plural = "Réservations"; ordering = ['-date_arrivee']
    def __str__(self): return f"{self.client.nom} - Ch.{self.chambre.numero}"

class ServiceHotel(models.Model):
    reservation = models.ForeignKey(ReservationHotel, on_delete=models.CASCADE, related_name='services')
    nom_service = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_service = models.DateField(auto_now_add=True)
    class Meta: verbose_name = "Service hôtel"; verbose_name_plural = "Services hôtel"
    def __str__(self): return f"{self.nom_service} - {self.prix} TND"


# ─── Commerce / Retail ──────────────────────────────────────
class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta: verbose_name = "Catégorie"; verbose_name_plural = "Catégories"
    def __str__(self): return self.nom

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    adresse = models.TextField(blank=True)
    class Meta: verbose_name = "Fournisseur"; verbose_name_plural = "Fournisseurs"
    def __str__(self): return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='produits')
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True, blank=True)
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Prix d'achat (TND)")
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Prix de vente (TND)")
    stock_actuel = models.IntegerField(default=0)
    stock_minimum = models.IntegerField(default=5)
    code_barre = models.CharField(max_length=50, blank=True)
    actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Produit"; verbose_name_plural = "Produits"
    def __str__(self): return self.nom

class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='ventes')
    quantite = models.IntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_vente = models.DateTimeField(auto_now_add=True)
    client_nom = models.CharField(max_length=100, blank=True)
    class Meta: verbose_name = "Vente"; verbose_name_plural = "Ventes"; ordering = ['-date_vente']
    def __str__(self): return f"{self.produit.nom} x{self.quantite}"


# ─── Juridique (Avocat) ─────────────────────────────────────
class ClientJuridique(models.Model):
    nom = models.CharField(max_length=100)
    type_client = models.CharField(max_length=20, choices=[('particulier','Particulier'),('entreprise','Entreprise')], default='particulier')
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    adresse = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Client juridique"; verbose_name_plural = "Clients juridiques"
    def __str__(self): return self.nom

class DossierJuridique(models.Model):
    reference = models.CharField(max_length=50, unique=True, verbose_name="Référence")
    client = models.ForeignKey(ClientJuridique, on_delete=models.CASCADE, related_name='dossiers')
    titre = models.CharField(max_length=200)
    type_affaire = models.CharField(max_length=100, blank=True)
    tribunal = models.CharField(max_length=100, blank=True)
    statut = models.CharField(max_length=20, choices=[('ouvert','Ouvert'),('en_cours','En cours'),('clos','Clos'),('suspendu','Suspendu')], default='ouvert')
    date_ouverture = models.DateField(auto_now_add=True)
    date_cloture = models.DateField(null=True, blank=True)
    honoraires = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Honoraires (TND)")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Dossier juridique"; verbose_name_plural = "Dossiers juridiques"; ordering = ['-date_ouverture']
    def __str__(self): return f"{self.reference} - {self.client.nom}"

class Audience(models.Model):
    dossier = models.ForeignKey(DossierJuridique, on_delete=models.CASCADE, related_name='audiences')
    date_audience = models.DateField(verbose_name="Date d'audience")
    lieu = models.CharField(max_length=100, blank=True)
    resultat = models.TextField(blank=True)
    prochaine_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Audience"; verbose_name_plural = "Audiences"; ordering = ['-date_audience']
    def __str__(self): return f"{self.dossier.reference} - {self.date_audience}"


# ─── Comptabilité ───────────────────────────────────────────
class JournalComptable(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=100)
    class Meta: verbose_name = "Journal comptable"; verbose_name_plural = "Journaux comptables"
    def __str__(self): return f"{self.code} - {self.nom}"

class EcritureComptable(models.Model):
    journal = models.ForeignKey(JournalComptable, on_delete=models.SET_NULL, null=True)
    date_ecriture = models.DateField(verbose_name="Date d'écriture")
    libelle = models.CharField(max_length=200)
    compte_debit = models.CharField(max_length=20, verbose_name="Compte débit")
    compte_credit = models.CharField(max_length=20, verbose_name="Compte crédit")
    montant = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Montant (TND)")
    piece_justificative = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Écriture comptable"; verbose_name_plural = "Écritures comptables"; ordering = ['-date_ecriture']
    def __str__(self): return f"{self.date_ecriture} - {self.libelle}"

class Facture(models.Model):
    numero = models.CharField(max_length=50, unique=True)
    client_nom = models.CharField(max_length=100)
    client_matricule = models.CharField(max_length=50, blank=True, verbose_name="Matricule fiscal")
    date_facture = models.DateField(auto_now_add=True)
    montant_ht = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Montant HT (TND)")
    tva = models.DecimalField(max_digits=4, decimal_places=2, default=19, verbose_name="TVA %")
    montant_ttc = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Montant TTC (TND)")
    payee = models.BooleanField(default=False)
    date_paiement = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Facture"; verbose_name_plural = "Factures"; ordering = ['-date_facture']
    def __str__(self): return f"Facture {self.numero} - {self.client_nom}"

class DeclarationFiscale(models.Model):
    type_declaration = models.CharField(max_length=50, choices=[('tva','TVA'),('cnss','CNSS'),('irpp','IRPP'),('resultat','Résultat fiscal')])
    periode = models.CharField(max_length=50, verbose_name="Période", help_text="ex: Janvier 2026, Q1 2026")
    montant = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Montant (TND)")
    date_limite = models.DateField(verbose_name="Date limite")
    soumise = models.BooleanField(default=False)
    date_soumission = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Déclaration fiscale"; verbose_name_plural = "Déclarations fiscales"; ordering = ['-date_limite']
    def __str__(self): return f"{self.get_type_declaration_display()} - {self.periode}"


# ─── RH & Paie ──────────────────────────────────────────────
class Employe(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)
    poste = models.CharField(max_length=100)
    departement = models.CharField(max_length=100, blank=True)
    date_embauche = models.DateField(verbose_name="Date d'embauche")
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2, default=1500, verbose_name="Salaire de base (TND)")
    actif = models.BooleanField(default=True)
    nbr_enfants = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Employé"; verbose_name_plural = "Employés"; ordering = ['nom']
    def __str__(self): return f"{self.nom} ({self.poste})"

class Contrat(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='contrats')
    type_contrat = models.CharField(max_length=50, choices=[('cdi','CDI'),('cdd','CDD'),('stage','Stage'),('freelance','Freelance')], default='cdi')
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(null=True, blank=True, verbose_name="Date de fin")
    salaire_actuel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salaire actuel (TND)")
    actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Contrat"; verbose_name_plural = "Contrats"
    def __str__(self): return f"{self.employe.nom} - {self.get_type_contrat_display()}"

class FichePaie(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='fiches_paie')
    mois = models.CharField(max_length=20, verbose_name="Mois", help_text="ex: Janvier 2026")
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2)
    primes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cnss = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="CNSS")
    irpp = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="IRPP")
    net_a_payer = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Net à payer (TND)")
    date_paiement = models.DateField(null=True, blank=True)
    payee = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Fiche de paie"; verbose_name_plural = "Fiches de paie"; ordering = ['-created_at']
    def __str__(self): return f"{self.employe.nom} - {self.mois}"

class Conge(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='conges')
    type_conge = models.CharField(max_length=50, choices=[('annuel','Annuel'),('maladie','Maladie'),('maternite','Maternité'),('exceptionnel','Exceptionnel')], default='annuel')
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")
    nb_jours = models.IntegerField(verbose_name="Nombre de jours")
    valide = models.BooleanField(default=False)
    motif = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Congé"; verbose_name_plural = "Congés"; ordering = ['-date_debut']
    def __str__(self): return f"{self.employe.nom} - {self.get_type_conge_display()}"

class Formation(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='formations')
    titre = models.CharField(max_length=200)
    organisme = models.CharField(max_length=100, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    cout = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Coût (TND)")
    terminee = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Formation"; verbose_name_plural = "Formations"; ordering = ['-date_debut']
    def __str__(self): return f"{self.employe.nom} - {self.titre}"


# ─── Restaurant / Café ───────────────────────────────────────
class MenuItem(models.Model):
    CAT_CHOICES = [
        ('entree','Entrée'),('plat','Plat principal'),('dessert','Dessert'),
        ('boisson','Boisson'),('snack','Snack'),('petit-dej','Petit-déjeuner'),
    ]
    nom = models.CharField(max_length=200, verbose_name="Nom")
    categorie = models.CharField(max_length=50, choices=CAT_CHOICES, default='plat', verbose_name="Catégorie")
    prix = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Prix (TND)")
    description = models.TextField(blank=True)
    disponible = models.BooleanField(default=True)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Article menu"; verbose_name_plural = "Articles menu"; ordering = ['categorie','nom']
    def __str__(self): return f"{self.nom} ({self.get_categorie_display()})"

class TableRestaurant(models.Model):
    numero = models.CharField(max_length=10, unique=True, verbose_name="N° Table")
    capacite = models.IntegerField(default=4)
    STATUT_CHOICES = [('libre','Libre'),('occupee','Occupée'),('reservee','Réservée')]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='libre')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Table"; verbose_name_plural = "Tables"; ordering = ['numero']
    def __str__(self): return f"Table {self.numero} ({self.capacite} pers.)"


# ─── PixelSoftCode ───────────────────────────────────────────
class SoftCodeModule(models.Model):
    nom = models.CharField(max_length=200, verbose_name="Nom du module")
    description = models.TextField(blank=True)
    categorie = models.CharField(max_length=100, verbose_name="Catégorie")
    version = models.CharField(max_length=20, default='1.0.0')
    prix = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Prix (TND)")
    disponible = models.BooleanField(default=True)
    documentation_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Module PixelSoftCode"; verbose_name_plural = "Modules PixelSoftCode"; ordering = ['nom']
    def __str__(self): return f"{self.nom} v{self.version}"


# ─── Inner Studio 3D ────────────────────────────────────────
class StudioProject3D(models.Model):
    CAT_CHOICES = [('architecture','Architecture'),('interieur','Design intérieur'),('exterieur','Design extérieur'),('mecanique','Mécanique'),('autre','Autre')]
    nom = models.CharField(max_length=200, verbose_name="Nom du projet")
    description = models.TextField(blank=True)
    categorie = models.CharField(max_length=50, choices=CAT_CHOICES, default='architecture')
    fichier_url = models.URLField(blank=True, verbose_name="URL du fichier 3D")
    image_url = models.URLField(blank=True, verbose_name="Image de prévisualisation")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Projet 3D"; verbose_name_plural = "Projets 3D"; ordering = ['-created_at']
    def __str__(self): return self.nom


# ─── Pâtisserie / Boulangerie ────────────────────────────────
class PatisserieRecipe(models.Model):
    CAT_CHOICES = [('patisserie','Pâtisserie'),('boulangerie','Boulangerie'),('chocolaterie','Chocolaterie'),('confiserie','Confiserie'),('glacier','Glacier'),('traiteur','Traiteur')]
    nom = models.CharField(max_length=200, verbose_name="Recette")
    categorie = models.CharField(max_length=50, choices=CAT_CHOICES, default='patisserie')
    ingredients = models.TextField(blank=True, verbose_name="Ingrédients")
    instructions = models.TextField(blank=True)
    cout_production = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Coût de production (TND)")
    prix_vente = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Prix de vente (TND)")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Recette"; verbose_name_plural = "Recettes"; ordering = ['nom']
    def __str__(self): return self.nom

class PatisserieProduct(models.Model):
    recette = models.ForeignKey(PatisserieRecipe, on_delete=models.SET_NULL, null=True, blank=True, related_name='produits')
    nom = models.CharField(max_length=200)
    stock_actuel = models.IntegerField(default=0, verbose_name="Stock actuel")
    stock_minimum = models.IntegerField(default=5, verbose_name="Stock minimum")
    prix_vente = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Prix de vente (TND)")
    actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name = "Produit pâtisserie"; verbose_name_plural = "Produits pâtisserie"; ordering = ['nom']
    def __str__(self): return self.nom

# ─── Pages vitrine ──────────────────────────────────────────
class Temoignage(models.Model):
    nom = models.CharField(max_length=200, verbose_name="Nom client")
    entreprise = models.CharField(max_length=200, blank=True, verbose_name="Entreprise / Projet")
    role = models.CharField(max_length=100, blank=True, verbose_name="Poste / Rôle")
    contenu = models.TextField(verbose_name="Témoignage")
    note = models.IntegerField(default=5, verbose_name="Note (1-5)")
    photo = models.ImageField(upload_to='temoignages/', blank=True, verbose_name="Photo")
    actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
        ordering = ['-created_at']
    def __str__(self): return f"{self.nom} — {self.entreprise or 'Client'}"

# ─── E‑Commerce & Stock ────────────────────────────────────
class MouvementStock(models.Model):
    TYPES = [
        ('entree', 'Entrée (achat/approvisionnement)'),
        ('sortie', 'Sortie (vente/perte)'),
        ('ajustement', 'Ajustement inventaire'),
        ('retour', 'Retour fournisseur'),
    ]
    produit = models.ForeignKey('Produit', on_delete=models.CASCADE, related_name='mouvements')
    type = models.CharField(max_length=20, choices=TYPES, verbose_name="Type mouvement")
    quantite = models.IntegerField(verbose_name="Quantité")
    stock_avant = models.IntegerField(default=0)
    stock_apres = models.IntegerField(default=0)
    reference = models.CharField(max_length=100, blank=True, verbose_name="Réf. bon/document")
    notes = models.TextField(blank=True)
    cree_par = models.CharField(max_length=100, blank=True)
    date_mouvement = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Mouvement de stock"
        verbose_name_plural = "Mouvements de stock"
        ordering = ['-date_mouvement']
    def __str__(self):
        return f"{self.get_type_display()} — {self.produit.nom} x{self.quantite}"

class CommandeECommerce(models.Model):
    STATUTS = [
        ('panier', 'Panier'),
        ('en_attente', 'En attente de paiement'),
        ('confirmee', 'Confirmée'),
        ('preparation', 'En préparation'),
        ('expediee', 'Expédiée'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]
    PAIEMENTS = [
        ('especes', 'Espèces (livraison)'),
        ('online', 'Paiement en ligne'),
        ('virement', 'Virement bancaire'),
        ('carte', 'Carte bancaire (livraison)'),
    ]
    client_nom = models.CharField(max_length=200, verbose_name="Nom complet")
    client_email = models.EmailField(verbose_name="Email")
    client_tel = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    client_adresse = models.TextField(verbose_name="Adresse de livraison")
    client_ville = models.CharField(max_length=100, blank=True, verbose_name="Ville")
    client_code_postal = models.CharField(max_length=10, blank=True, verbose_name="Code postal")
    notes = models.TextField(blank=True, verbose_name="Notes / Instructions")
    statut = models.CharField(max_length=20, choices=STATUTS, default='panier')
    methode_paiement = models.CharField(max_length=20, choices=PAIEMENTS, default='online')
    total_ht = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Total HT")
    total_ttc = models.DecimalField(max_digits=10, decimal_places=3, default=0, verbose_name="Total TTC")
    reference = models.CharField(max_length=100, unique=True, blank=True)
    id_transaction = models.CharField(max_length=200, blank=True, verbose_name="ID Transaction paiement")
    date_commande = models.DateTimeField(auto_now_add=True)
    date_livraison = models.DateTimeField(null=True, blank=True)
    class Meta:
        verbose_name = "Commande e‑commerce"
        verbose_name_plural = "Commandes e‑commerce"
        ordering = ['-date_commande']
    def __str__(self):
        return f"{self.reference or 'Nouvelle'} — {self.client_nom} ({self.get_statut_display()})"

class CommandeECommerceItem(models.Model):
    commande = models.ForeignKey(CommandeECommerce, on_delete=models.CASCADE, related_name='items')
    produit = models.ForeignKey('Produit', on_delete=models.SET_NULL, null=True, related_name='commandes_items')
    nom_produit = models.CharField(max_length=200, verbose_name="Nom du produit")
    quantite = models.IntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire TTC")
    class Meta:
        verbose_name = "Ligne de commande"
        verbose_name_plural = "Lignes de commande"
    def __str__(self):
        return f"{self.nom_produit} x{self.quantite}"
    def sous_total(self):
        return self.prix_unitaire * self.quantite

# ─── Abonnements & Paiements ────────────────────────────────
class PlanAbonnement(models.Model):
    CATEGORIES = [
        ('erp', 'GestiActiv ERP'),
        ('soft', 'PixelSoftCode'),
        ('restaurant', 'Restaurant'),
        ('patisserie', 'Pâtisserie'),
        ('studio', 'Inner Studio'),
    ]
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIES, default='erp')
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Prix (TND)")
    duree_jours = models.IntegerField(default=365, verbose_name="Durée (jours)")
    features = models.TextField(blank=True, help_text="Un par ligne")
    is_available = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    class Meta:
        verbose_name = "Plan d'abonnement"
        verbose_name_plural = "Plans d'abonnement"
        ordering = ['order']
    def __str__(self): return f"{self.nom} — {self.prix} TND"
    def feature_list(self): return [f.strip() for f in self.features.split('\n') if f.strip()]

class SouscriptionClient(models.Model):
    STATUS = [
        ('en_attente', 'En attente de paiement'),
        ('actif', 'Actif'),
        ('suspendu', 'Suspendu'),
        ('expire', 'Expiré'),
    ]
    client_email = models.EmailField(verbose_name="Email client")
    client_nom = models.CharField(max_length=200, verbose_name="Nom complet")
    client_tel = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    plan = models.ForeignKey(PlanAbonnement, on_delete=models.CASCADE, related_name='souscriptions')
    status = models.CharField(max_length=20, choices=STATUS, default='en_attente')
    date_debut = models.DateField(auto_now_add=True)
    date_fin = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Souscription client"
        verbose_name_plural = "Souscriptions clients"
        ordering = ['-created_at']
    def __str__(self): return f"{self.client_nom} — {self.plan.nom}"

class Paiement(models.Model):
    METHODES = [
        ('especes', 'Espèces'),
        ('online', 'Paiement en ligne'),
        ('virement', 'Virement bancaire'),
    ]
    STATUTS = [
        ('en_attente', 'En attente'),
        ('confirme', 'Confirmé'),
        ('refuse', 'Refusé'),
        ('rembourse', 'Remboursé'),
    ]
    souscription = models.ForeignKey(SouscriptionClient, on_delete=models.CASCADE, related_name='paiements')
    methode = models.CharField(max_length=20, choices=METHODES)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=20, choices=STATUTS, default='en_attente')
    reference = models.CharField(max_length=100, unique=True, blank=True)
    transaction_id = models.CharField(max_length=200, blank=True, verbose_name="ID Transaction")
    notes = models.TextField(blank=True)
    date_paiement = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Paiement"
        verbose_name_plural = "Paiements"
        ordering = ['-date_paiement']
    def __str__(self): return f"{self.reference} — {self.montant} TND ({self.get_methode_display()})"

class CleActivation(models.Model):
    souscription = models.ForeignKey(SouscriptionClient, on_delete=models.CASCADE, related_name='cles_activation')
    code = models.CharField(max_length=50, unique=True)
    est_utilisee = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_activation = models.DateTimeField(null=True, blank=True)
    class Meta:
        verbose_name = "Clé d'activation"
        verbose_name_plural = "Clés d'activation"
    def __str__(self): return self.code

class ConfigurationBancaire(models.Model):
    BANQUES_TUNISIE = [
        ('ATB', 'ATB — Arab Tunisian Bank'),
        ('Attijari', 'Attijari Bank'),
        ('Amen', 'Amen Bank'),
        ('BH', 'Banque de l\'Habitat'),
        ('BNA', 'BNA — Banque Nationale Agricole'),
        ('BIAT', 'BIAT — Banque Internationale Arabe de Tunisie'),
        ('BT', 'BT — Banque de Tunisie'),
        ('BTE', 'BTE — Banque Tunisie Emirates'),
        ('CFT', 'CFT — Banque CFT'),
        ('CGF', 'CGF Banque'),
        ('Poste', 'La Poste Tunisienne (CCP)'),
        ('STB', 'STB — Société Tunisienne de Banque'),
        ('TQB', 'TQB — Tunisian Qatari Bank'),
        ('UBCI', 'UBCI — Union Bancaire pour le Commerce et l\'Industrie'),
        ('UIB', 'UIB — Union Internationale de Banques'),
        ('Zitouna', 'Banque Zitouna'),
        ('Wifak', 'Wifak Bank'),
        ('autre', 'Autre'),
    ]
    banque = models.CharField(max_length=50, choices=BANQUES_TUNISIE, default='BIAT', verbose_name="Banque")
    agence = models.CharField(max_length=100, blank=True, verbose_name="Agence")
    rib = models.CharField(max_length=24, verbose_name="RIB (24 chiffres)")
    rip = models.CharField(max_length=20, blank=True, verbose_name="RIP")
    swift = models.CharField(max_length=11, blank=True, verbose_name="Code SWIFT/BIC")
    titulaire = models.CharField(max_length=200, verbose_name="Titulaire du compte")
    est_defaut = models.BooleanField(default=False, verbose_name="Compte par défaut")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Configuration bancaire"
        verbose_name_plural = "Configurations bancaires"
        ordering = ['-est_defaut', 'banque']
    def __str__(self):
        return f"{self.get_banque_display()} — {self.rib[:8]}...{self.rib[-4:]}"

class ConfigurationPaiementEnLigne(models.Model):
    FOURNISSEURS = [
        ('expressee', 'Express eE (expressee.tn)'),
        ('d17', 'D17'),
        ('flouci', 'Flouci'),
        ('paymee', 'Paymee.tn'),
        ('konnect', 'Konnect'),
        ('manual', 'Manuel (instructions)'),
    ]
    fournisseur = models.CharField(max_length=50, choices=FOURNISSEURS, default='manual', verbose_name="Fournisseur")
    api_key = models.CharField(max_length=255, blank=True, verbose_name="Clé API")
    api_secret = models.CharField(max_length=255, blank=True, verbose_name="Secret API")
    endpoint_url = models.URLField(blank=True, verbose_name="URL de l'API")
    instructions = models.TextField(blank=True, verbose_name="Instructions de paiement")
    frais_pourcentage = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Frais (%)")
    est_actif = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Configuration paiement en ligne"
        verbose_name_plural = "Configurations paiement en ligne"
    def __str__(self):
        return f"Paiement en ligne — {self.get_fournisseur_display()}"

# ─── Recrutement ────────────────────────────────────────────
class Candidature(models.Model):
    TYPE_CHOICES = [
        ('worker', 'Worker (Employé)'),
        ('partner', 'Partner (Partenaire)'),
        ('freelance', 'Freelance / Prestataire'),
        ('stage', 'Stagiaire'),
        ('alternance', 'Alternance'),
    ]
    STATUT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('lu', 'Lu'),
        ('entretien', 'Entretien programmé'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
    ]
    type_candidature = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Type")
    nom = models.CharField(max_length=200, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    telephone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    poste = models.CharField(max_length=200, blank=True, verbose_name="Poste souhaité / Domaine")
    cv = models.FileField(upload_to='candidatures/cv/', blank=True, verbose_name="CV")
    message = models.TextField(blank=True, verbose_name="Message / Motivation")
    linkedin = models.URLField(blank=True, verbose_name="Profil LinkedIn")
    portfolio = models.URLField(blank=True, verbose_name="Portfolio / Site web")
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='nouveau')
    notes_privees = models.TextField(blank=True, verbose_name="Notes internes")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Candidature"
        verbose_name_plural = "Candidatures"
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.get_type_candidature_display()} — {self.nom} ({self.email})"


# ─── PixMail — Service Email ────────────────────────────────
class PixMailAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pixmail')
    username = models.CharField(max_length=30, unique=True, verbose_name="Nom d'utilisateur")
    email = models.EmailField(unique=True, verbose_name="Adresse email")
    password_hash = models.CharField(max_length=200, verbose_name="Mot de passe")
    display_name = models.CharField(max_length=100, blank=True, verbose_name="Nom d'affichage")
    avatar_url = models.URLField(blank=True, verbose_name="Avatar")
    storage_used_mb = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Stockage utilisé (Mo)")
    storage_limit_mb = models.DecimalField(max_digits=8, decimal_places=2, default=500, verbose_name="Stockage max (Mo)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Compte PixMail"
        verbose_name_plural = "Comptes PixMail"

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = f"{self.username}@pixmail.tn"
        super().save(*args, **kwargs)


class PixMailContact(models.Model):
    owner = models.ForeignKey(PixMailAccount, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=150, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    company = models.CharField(max_length=100, blank=True, verbose_name="Entreprise")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact PixMail"
        verbose_name_plural = "Contacts PixMail"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} <{self.email}>"


class PixMailMessage(models.Model):
    FOLDER_CHOICES = [
        ('inbox', 'Boîte de réception'),
        ('sent', 'Envoyés'),
        ('draft', 'Brouillons'),
        ('spam', 'Spam'),
        ('trash', 'Corbeille'),
        ('archive', 'Archives'),
    ]
    sender = models.ForeignKey(PixMailAccount, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_messages')
    sender_email = models.EmailField(verbose_name="Expéditeur")
    recipient_email = models.EmailField(verbose_name="Destinataire")
    cc = models.EmailField(blank=True, verbose_name="CC")
    bcc = models.EmailField(blank=True, verbose_name="CCI")
    subject = models.CharField(max_length=500, verbose_name="Objet")
    body = models.TextField(verbose_name="Corps du message")
    body_html = models.TextField(blank=True, verbose_name="Corps HTML")
    folder = models.CharField(max_length=20, choices=FOLDER_CHOICES, default='inbox')
    is_read = models.BooleanField(default=False, verbose_name="Lu")
    is_starred = models.BooleanField(default=False, verbose_name="Favori")
    has_attachments = models.BooleanField(default=False)
    size_kb = models.IntegerField(default=0, verbose_name="Taille (Ko)")
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
    date_sent = models.DateTimeField(auto_now_add=True)
    date_read = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Message PixMail"
        verbose_name_plural = "Messages PixMail"
        ordering = ['-date_sent']

    def __str__(self):
        return f"[{self.folder}] {self.subject} — {self.recipient_email}"


class PixMailAttachment(models.Model):
    message = models.ForeignKey(PixMailMessage, on_delete=models.CASCADE, related_name='attachments')
    filename = models.CharField(max_length=255, verbose_name="Nom du fichier")
    file = models.FileField(upload_to='pixmail/attachments/', verbose_name="Fichier")
    size_kb = models.IntegerField(default=0, verbose_name="Taille (Ko)")
    mime_type = models.CharField(max_length=100, blank=True, verbose_name="Type MIME")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pièce jointe PixMail"
        verbose_name_plural = "Pièces jointes PixMail"

    def __str__(self):
        return self.filename


class PixMailFolder(models.Model):
    account = models.ForeignKey(PixMailAccount, on_delete=models.CASCADE, related_name='custom_folders')
    name = models.CharField(max_length=100, verbose_name="Nom du dossier")
    icon = models.CharField(max_length=10, default='📁', verbose_name="Icône")
    color = models.CharField(max_length=7, default='#1EB482', verbose_name="Couleur")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Dossier PixMail"
        verbose_name_plural = "Dossiers PixMail"
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.account.email})"


class PixMailSignature(models.Model):
    account = models.OneToOneField(PixMailAccount, on_delete=models.CASCADE, related_name='signature')
    content = models.TextField(blank=True, verbose_name="Signature")
    include_name = models.BooleanField(default=True, verbose_name="Inclure le nom")
    include_email = models.BooleanField(default=True, verbose_name="Inclure l'email")
    include_phone = models.BooleanField(default=False, verbose_name="Inclure le téléphone")
    include_company = models.BooleanField(default=True, verbose_name="Inclure l'entreprise")

    class Meta:
        verbose_name = "Signature PixMail"
        verbose_name_plural = "Signatures PixMail"

    def __str__(self):
        return f"Signature — {self.account.email}"


# ─── Social Media ─────────────────────────────────────────
class SocialProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='social')
    display_name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar_url = models.URLField(blank=True)
    cover_url = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Profil Social"
        verbose_name_plural = "Profils Sociaux"

    def __str__(self):
        return self.display_name or self.user.username

    @property
    def followers_count(self):
        return Follow.objects.filter(following=self.user).count()

    @property
    def following_count(self):
        return Follow.objects.filter(follower=self.user).count()

    @property
    def posts_count(self):
        return Post.objects.filter(author=self.user).count()


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers_set')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
        verbose_name = "Abonnement"
        verbose_name_plural = "Abonnements"

    def __str__(self):
        return f"{self.follower.username} → {self.following.username}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_posts')
    content = models.TextField(max_length=5000)
    image_url = models.URLField(blank=True)
    visibility = models.CharField(max_length=20, choices=[
        ('public', 'Public'),
        ('followers', 'Abonnés'),
        ('private', 'Privé'),
    ], default='public')
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    shares_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post.id}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=2000)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return f"{self.author.username}: {self.content[:40]}"


class Notification(models.Model):
    TYPE_CHOICES = [
        ('like', 'Like'),
        ('comment', 'Commentaire'),
        ('follow', 'Abonnement'),
        ('share', 'Partage'),
        ('message', 'Message'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_notifications')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='notifications_sent')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f"{self.type} → {self.user.username}"


# ─── Messenger E2E ────────────────────────────────────────
class Conversation(models.Model):
    TYPE_CHOICES = [
        ('private', 'Privé'),
        ('group', 'Groupe'),
    ]
    title = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='private')
    avatar_url = models.URLField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = "Conversation"
        verbose_name_plural = "Conversations"

    def __str__(self):
        return self.title or f"Conv {self.id}"


class ConversationMember(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('member', 'Membre')], default='member')
    public_key = models.TextField(blank=True, verbose_name="Clé publique E2E")
    joined_at = models.DateTimeField(auto_now_add=True)
    last_read = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('conversation', 'user')

    def __str__(self):
        return f"{self.user.username} in {self.conversation}"


class EncryptedMessage(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_encrypted')
    encrypted_content = models.TextField(verbose_name="Contenu chiffré (AES-GCM)")
    encrypted_key = models.TextField(verbose_name="Clé AES chiffrée (RSA-OAEP)")
    iv = models.CharField(max_length=64, verbose_name="Nonce IV")
    message_type = models.CharField(max_length=20, choices=[
        ('text', 'Texte'),
        ('image', 'Image'),
        ('file', 'Fichier'),
    ], default='text')
    attachment_url = models.URLField(blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = "Message Chiffré"
        verbose_name_plural = "Messages Chiffrés"

    def __str__(self):
        return f"[E2E] {self.sender.username} → Conv {self.conversation.id}"

# ─── PixSoftPay — Wallet & Transactions ────────────────────────
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    solde = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Solde (TND)")
    referral_code = models.CharField(max_length=12, unique=True, blank=True, verbose_name="Code parrainage")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"

    def __str__(self):
        return f"{self.user.username} — {self.solde} TND"

    def save(self, *args, **kwargs):
        if not self.referral_code:
            import secrets
            self.referral_code = secrets.token_hex(4).upper()
        super().save(*args, **kwargs)

    @property
    def referral_count(self):
        return Referral.objects.filter(referrer=self.user).count()


class Transaction(models.Model):
    TYPE_CHOICES = [
        ('depot', 'Dépôt'),
        ('retrait', 'Retrait'),
        ('paiement', 'Paiement'),
        ('remboursement', 'Remboursement'),
    ]
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('confirme', 'Confirmé'),
        ('refuse', 'Refusé'),
        ('annule', 'Annulé'),
    ]
    METHODE_CHOICES = [
        ('d17', 'D17'),
        ('flouci', 'Flouci'),
        ('konnect', 'Konnect'),
        ('wallet', 'Wallet'),
        ('carte', 'Carte bancaire'),
        ('especes', 'Espèces'),
        ('virement', 'Virement bancaire'),
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    reference = models.CharField(max_length=100, unique=True, verbose_name="Référence")
    type_operation = models.CharField(max_length=20, choices=TYPE_CHOICES)
    montant = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Montant (TND)")
    solde_avant = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Solde avant")
    solde_apres = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Solde après")
    methode = models.CharField(max_length=20, choices=METHODE_CHOICES, default='wallet')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    description = models.TextField(blank=True, verbose_name="Description")
    qr_data = models.TextField(blank=True, verbose_name="QR Code data")
    payment_url = models.URLField(blank=True, verbose_name="Lien de paiement")
    customer_name = models.CharField(max_length=200, blank=True, verbose_name="Nom client")
    customer_email = models.EmailField(blank=True, verbose_name="Email client")
    paid_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.reference} — {self.get_type_operation_display()} {self.montant} TND ({self.get_statut_display()})"

    def save(self, *args, **kwargs):
        if not self.reference:
            import uuid
            self.reference = f"PSP-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)


# ─── PixSoftPay — 2FA (Two-Factor Authentication) ──────────────
class TwoFactorAuth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='twofactor')
    secret = models.CharField(max_length=32, verbose_name="Secret TOTP")
    is_enabled = models.BooleanField(default=False, verbose_name="2FA activée")
    backup_codes = models.TextField(blank=True, verbose_name="Codes de secours")
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Authentification 2FA"
        verbose_name_plural = "Authentifications 2FA"

    def __str__(self):
        return f"2FA {self.user.username} — {'Activée' if self.is_enabled else 'Désactivée'}"

    def save(self, *args, **kwargs):
        if not self.secret:
            import pyotp
            self.secret = pyotp.random_base32()
        if not self.backup_codes:
            import secrets
            codes = [secrets.token_hex(4).upper() for _ in range(8)]
            self.backup_codes = '\n'.join(codes)
        super().save(*args, **kwargs)

    def get_totp_uri(self):
        import pyotp
        return pyotp.totp.TOTP(self.secret).provisioning_uri(
            name=self.user.email or self.user.username,
            issuer_name='PixSoftPay'
        )

    def verify_code(self, code):
        import pyotp
        totp = pyotp.totp.TOTP(self.secret)
        return totp.verify(code, valid_window=1)

    def verify_backup(self, code):
        codes = [c.strip() for c in self.backup_codes.split('\n') if c.strip()]
        code = code.strip().upper()
        if code in codes:
            codes.remove(code)
            self.backup_codes = '\n'.join(codes)
            self.save()
            return True
        return False

    def get_backup_codes_list(self):
        return [c.strip() for c in self.backup_codes.split('\n') if c.strip()]


# ─── PixSoftPay — Parrainage (Referral) ────────────────────────
REFERRAL_BONUS_AMOUNT = 10.00
REFERRAL_THRESHOLD = 5


class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals_made')
    referred = models.OneToOneField(User, on_delete=models.CASCADE, related_name='referred_by_link')
    bonus_given = models.BooleanField(default=False, verbose_name="Bonus versé")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Parrainage"
        verbose_name_plural = "Parrainages"

    def __str__(self):
        return f"{self.referrer.username} → {self.referred.username}"


# ─── PixSoftPay — Vérification d'identité (KYC) ────────────────
class KYCVerification(models.Model):
    TYPE_CHOICES = [
        ('cin', 'Carte d\'identité nationale'),
        ('passport', 'Passeport'),
        ('bank_account', 'Relevé bancaire'),
    ]
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('approved', 'Approuvé'),
        ('rejected', 'Rejeté'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kyc_verifications')
    doc_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    doc_number = models.CharField(max_length=50, verbose_name="Numéro du document")
    full_name = models.CharField(max_length=200, verbose_name="Nom complet")
    front_image = models.ImageField(upload_to='kyc/front/', verbose_name="Recto")
    back_image = models.ImageField(upload_to='kyc/back/', verbose_name="Verso", blank=True, null=True)
    bank_rib = models.CharField(max_length=50, blank=True, verbose_name="RIB bancaire")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_note = models.TextField(blank=True, verbose_name="Note admin")
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Vérification KYC"
        verbose_name_plural = "Vérifications KYC"
        ordering = ['-created_at']

    def __str__(self):
        return f"KYC {self.user.username} — {self.get_doc_type_display()} ({self.get_status_display()})"
