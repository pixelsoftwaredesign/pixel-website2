from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_user_hajerghiloufi(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Wallet = apps.get_model('studio', 'Wallet')

    user, created = User.objects.get_or_create(
        username='hajerghiloufi',
        defaults={
            'email': 'hajer@pixelsoftwaredesign.xyz',
            'is_staff': False,
            'is_superuser': False,
            'password': make_password('pixelsoftwaredesign'),
        },
    )
    if not created:
        user.password = make_password('pixelsoftwaredesign')
        user.save()

    import secrets
    wallet, created = Wallet.objects.get_or_create(user=user, defaults={'referral_code': secrets.token_hex(4).upper()})
    if wallet.solde == 0:
        wallet.solde = 500.00
        wallet.save()


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0022_reset_pixelsoftwaredesign_password'),
    ]

    operations = [
        migrations.RunPython(create_user_hajerghiloufi, migrations.RunPython.noop),
    ]
