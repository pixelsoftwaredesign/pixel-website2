from django.db import migrations
from django.contrib.auth.hashers import make_password


def reset_password(apps, schema_editor):
    User = apps.get_model('auth', 'User')
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


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0021_add_profile_photo'),
    ]

    operations = [
        migrations.RunPython(reset_password, migrations.RunPython.noop),
    ]
