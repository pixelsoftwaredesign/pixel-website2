"""Ajoute les logiciels et applications au catalogue du site.

Les fiches creees ici sont des services (licences / abonnements) : elles ne
participent pas a la gestion de stock. Elles restent rattachees au site
(``erp_client=None``) et ne reprennent jamais les produits d'un tenant
GestiActiv.
"""
from decimal import Decimal

from django.db import migrations, models


CATEGORIE = 'Logiciels & applications'
FOURNISSEUR = 'Pixel Software Design'

APPLICATIONS = [
    ('GestiActiv ERP — Auto-École', '1200.00'),
    ('GestiActiv ERP — Santé / Clinique', '1200.00'),
    ('GestiActiv ERP — Hôtellerie / Tourisme', '1200.00'),
    ('GestiActiv ERP — Commerce / Retail', '1200.00'),
    ('GestiActiv ERP — Juridique', '1200.00'),
    ('GestiActiv ERP — Comptabilité', '1200.00'),
    ('GestiActiv ERP — RH & Paie', '1200.00'),
    ('GestiActiv ERP — Restaurant & Café', '1200.00'),
    ('GestiActiv ERP — Pâtisserie & Boulangerie', '1200.00'),
    ('GestiActiv CRM — Relation client', '1200.00'),
    ('PixOffice — Suite bureautique', '0.00'),
    ('PixMaps — Cartographie web', '0.00'),
]


def _site_first(model, **lookup):
    return model.objects.filter(erp_client__isnull=True, **lookup).first()


def seed(apps, schema_editor):
    Categorie = apps.get_model('studio', 'Categorie')
    Fournisseur = apps.get_model('studio', 'Fournisseur')
    Produit = apps.get_model('studio', 'Produit')

    categorie = _site_first(Categorie, nom__iexact=CATEGORIE)
    if categorie is None:
        categorie = Categorie.objects.create(
            erp_client=None,
            nom=CATEGORIE,
            description='Applications et logiciels édités par Pixel Software Design.')

    fournisseur = _site_first(Fournisseur, nom__iexact=FOURNISSEUR)
    if fournisseur is None:
        fournisseur = Fournisseur.objects.create(
            erp_client=None,
            nom=FOURNISSEUR,
            contact='Éditeur de logiciels')

    for nom, prix in APPLICATIONS:
        produit = _site_first(Produit, nom=nom)
        valeurs = {
            'categorie': categorie,
            'fournisseur': fournisseur,
            'prix_achat': Decimal('0.00'),
            'prix_vente': Decimal(prix),
            'stock_actuel': 0,
            'stock_minimum': 0,
            'est_service': True,
            'actif': True,
        }
        if produit is None:
            Produit.objects.create(
                erp_client=None,
                nom=nom,
                **valeurs,
            )
        else:
            for champ, valeur in valeurs.items():
                setattr(produit, champ, valeur)
            produit.save(update_fields=list(valeurs))


def unseed(apps, schema_editor):
    Categorie = apps.get_model('studio', 'Categorie')
    Fournisseur = apps.get_model('studio', 'Fournisseur')
    Produit = apps.get_model('studio', 'Produit')

    noms = [item[0] for item in APPLICATIONS]
    Produit.objects.filter(
        erp_client__isnull=True, nom__in=noms, est_service=True).delete()

    Categorie.objects.filter(
        erp_client__isnull=True, nom__iexact=CATEGORIE,
        produits__isnull=True).delete()

    Fournisseur.objects.filter(
        erp_client__isnull=True, nom__iexact=FOURNISSEUR,
        produit__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0033_facture_client_adresse_facture_client_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='est_service',
            field=models.BooleanField(
                default=False,
                verbose_name='Service / logiciel sans gestion de stock'),
        ),
        migrations.RunPython(seed, unseed),
    ]
