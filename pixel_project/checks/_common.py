"""Socle commun des verifications locales Pixel.

Chaque `check_*.py` s'execute sur une base SQLite jetable (voir
`run_checks.py`) et ne cree que ses propres donnees : aucun acces a la
production, aucun identifiant reel.

Une suite peut aussi etre lancee seule :

    cd pixel_project && python3 checks/check_links.py
"""
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB = '/tmp/pixel_checks.sqlite3'

HOST_GESTIACTIV = 'gestiactiv.pixelsoftwaredesign.xyz'
HOST_APEX = 'pixelsoftwaredesign.xyz'

_state = {'ok': 0, 'fail': 0}


def bootstrap():
    """Prepare Django sur la base de verification (migrations au besoin)."""
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
    os.chdir(PROJECT_ROOT)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pixel_project.settings')
    os.environ['DJANGO_DEBUG'] = 'True'
    os.environ.setdefault('DATABASE_URL', 'sqlite:///' + DEFAULT_DB)

    import django

    django.setup()

    from django.core.management import call_command
    from django.db import connection

    if connection.vendor != 'sqlite':
        raise SystemExit(
            "Refus d'executer les suites sur '%s' : elles ne tournent que sur une "
            "base SQLite jetable (elles creent et suppriment des donnees). "
            "Utiliser checks/run_checks.py, ou definir PIXEL_CHECK_DB."
            % connection.vendor)

    if 'studio_erpmodule' not in connection.introspection.table_names():
        # Base neuve : la migration de donnees 0030_seed_erp_modules cree les
        # 9 modules metier attendus par les suites.
        call_command('migrate', run_syncdb=True, verbosity=0)


def check(label, cond, extra=''):
    if cond:
        _state['ok'] += 1
        print(f'  OK   {label}')
    else:
        _state['fail'] += 1
        print(f'  FAIL {label} {extra}')


def report():
    ok, fail = _state['ok'], _state['fail']
    print(f'\n=== {ok} OK / {fail} FAIL ===')
    return 1 if fail else 0
