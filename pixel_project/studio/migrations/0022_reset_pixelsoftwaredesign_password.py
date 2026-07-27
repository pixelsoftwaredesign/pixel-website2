from django.db import migrations
from django.contrib.auth.hashers import make_password


def reset_passwords(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    # Reset pixelsoftwaredesign
    try:
        user = User.objects.get(username='pixelsoftwaredesign')
        user.password = make_password('PixelSoft2024!')
        user.is_staff = True
        user.is_superuser = True
        user.email = 'contact@pixelsoftwaredesign.xyz'
        user.save()
    except User.DoesNotExist:
        User.objects.create(
            username='pixelsoftwaredesign',
            email='contact@pixelsoftwaredesign.xyz',
            is_staff=True,
            is_superuser=True,
            password=make_password('PixelSoft2024!'),
        )

    # Reset balancetaxsafety
    try:
        user = User.objects.get(username='balancetaxsafety')
        user.password = make_password('pixelsoftwaredesign')
        user.save()
    except User.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0021_add_profile_photo'),
    ]

    operations = [
        migrations.RunPython(reset_passwords, migrations.RunPython.noop),
    ]
