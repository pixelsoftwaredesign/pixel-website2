"""Sème (ou met à jour) les 9 modules GestiActiv.

Rend l'application autonome : les backends métier et l'espace client
référencent `ERPModule` par slug, qui doit donc toujours exister.
"""
from django.db import migrations

MODULES = [
    ('auto-ecole', 'Auto-École', '🚗', "Candidats, moniteurs, véhicules, leçons et examens.", 1),
    ('sante', 'Santé / Clinique', '🏥', "Patients, médecins, rendez-vous, lits et facturation.", 2),
    ('hotellerie', 'Hôtellerie / Tourisme', '🏨', "Chambres, réservations et services hôteliers.", 3),
    ('commerce', 'Commerce / Retail', '🛒', "Produits, stock, fournisseurs et ventes.", 4),
    ('juridique', 'Juridique', '⚖️', "Dossiers, audiences et suivi client.", 5),
    ('comptabilite', 'Comptabilité', '📊', "Écritures, factures et déclarations fiscales.", 6),
    ('rh-paie', 'RH & Paie', '👥', "Employés, contrats, fiches de paie, congés et formation.", 7),
    ('restaurant', 'Restaurant & Café', '🍽️', "Tables, menu, commandes et caisse.", 8),
    ('patisserie', 'Pâtisserie & Boulangerie', '🧁', "Recettes, production, stock et ventes.", 9),
]


def seed(apps, schema_editor):
    ERPModule = apps.get_model('studio', 'ERPModule')
    for slug, name, icon, description, order in MODULES:
        ERPModule.objects.update_or_create(
            slug=slug,
            defaults={
                'name': name,
                'icon': icon,
                'description': description,
                'order': order,
                'is_available': True,
            },
        )


def unseed(apps, schema_editor):
    ERPModule = apps.get_model('studio', 'ERPModule')
    ERPModule.objects.filter(slug__in=[m[0] for m in MODULES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0029_alter_erpmodule_slug'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
