from django.db import migrations
from django.contrib.auth.hashers import make_password


def set_initial_wallet(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Wallet = apps.get_model('studio', 'Wallet')

    user, created = User.objects.get_or_create(
        username='pixelsoftwaredesign',
        defaults={
            'email': 'contact@pixelsoftwaredesign.xyz',
            'is_staff': True,
            'is_superuser': True,
            'password': make_password('PixelSoft2024!'),
        },
    )
    if not created and not user.has_usable_password():
        user.password = make_password('PixelSoft2024!')
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
