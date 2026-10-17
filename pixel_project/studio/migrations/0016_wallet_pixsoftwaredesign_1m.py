import os

from django.db import migrations
from django.contrib.auth.hashers import make_password


# Le mot de passe ne doit jamais être en clair dans le dépôt (repo public).
# En prod, définir DJANGO_ADMIN_PASSWORD. Sinon => mot de passe inutilisable.
ADMIN_PASSWORD = os.getenv('DJANGO_ADMIN_PASSWORD')


def set_initial_wallet(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Wallet = apps.get_model('studio', 'Wallet')

    user, created = User.objects.get_or_create(
        username='pixelsoftwaredesign',
        defaults={
            'email': 'contact@pixelsoftwaredesign.xyz',
            'is_staff': True,
            'is_superuser': True,
            'password': make_password(ADMIN_PASSWORD),
        },
    )
    if not created and not user.has_usable_password():
        user.password = make_password(ADMIN_PASSWORD)
        user.save()

    wallet, created = Wallet.objects.get_or_create(user=user)
    wallet.solde = 1000000.00
    wallet.save()


def reverse_wallet(apps, schema_editor):
    Wallet = apps.get_model('studio', 'Wallet')
    Wallet.objects.filter(solde=1000000.00).update(solde=0)


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0015_wallet_transaction'),
    ]

    operations = [
        migrations.RunPython(set_initial_wallet, reverse_wallet),
    ]
