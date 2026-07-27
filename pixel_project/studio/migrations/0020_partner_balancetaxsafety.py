from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_partner(apps, schema_editor):
    import secrets
    User = apps.get_model('auth', 'User')
    Wallet = apps.get_model('studio', 'Wallet')

    user, created = User.objects.get_or_create(
        username='balancetaxsafety',
        defaults={
            'email': 'partner@balancetaxsafety.com',
            'is_staff': False,
            'is_superuser': False,
            'password': make_password('BalanceTax2023@'),
        },
    )
    if not created and not user.has_usable_password():
        user.password = make_password('BalanceTax2023@')
        user.save()

    try:
        wallet, _ = Wallet.objects.get_or_create(user=user)
    except Exception:
        for _ in range(10):
            code = secrets.token_hex(4).upper()
            if not Wallet.objects.filter(referral_code=code).exists():
                wallet = Wallet(user=user, referral_code=code)
                wallet.save()
                break
    wallet.solde = 100000.00
    wallet.save()


def reverse_partner(apps, schema_editor):
    Wallet = apps.get_model('studio', 'Wallet')
    Wallet.objects.filter(solde=100000.00).update(solde=0)


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0019_kyc_verification'),
    ]

    operations = [
        migrations.RunPython(create_partner, reverse_partner),
    ]
