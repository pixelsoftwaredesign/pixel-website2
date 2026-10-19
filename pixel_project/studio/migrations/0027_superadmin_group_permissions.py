from django.db import migrations

GROUP = 'SuperAdmin'
CODENAMES = ['view_group', 'change_group']


def _perms(apps):
    Permission = apps.get_model('auth', 'Permission')
    return Permission.objects.filter(content_type__app_label='auth', codename__in=CODENAMES)


def grant(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    group = Group.objects.filter(name=GROUP).first()
    if group:
        group.permissions.add(*_perms(apps))


def revoke(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    group = Group.objects.filter(name=GROUP).first()
    if group:
        group.permissions.remove(*_perms(apps))


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('studio', '0026_create_roles_groups'),
    ]

    operations = [
        migrations.RunPython(grant, revoke),
    ]
