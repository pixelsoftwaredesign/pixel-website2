"""Lance toutes les verifications locales sur une base SQLite neuve.

    cd pixel_project && python3 checks/run_checks.py [chemin/base.sqlite3]

La base par defaut (/tmp/pixel_checks.sqlite3) est recreee a chaque execution :
aucune donnee de production n'est utilisee, aucune connexion requise.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEFAULT_DB = '/tmp/pixel_checks.sqlite3'

SUITES = [
    'check_gestiactiv.py',
    'check_tenant_isolation.py',
    'check_links.py',
    'check_admin.py',
    'check_admin_pages.py',
    'check_modules.py',
]

TOTAL_RE = re.compile(r'=== (\d+) OK / (\d+) FAIL ===')


def main():
    db = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('PIXEL_CHECK_DB', DEFAULT_DB)
    if os.path.exists(db):
        os.remove(db)
    env = dict(os.environ, DATABASE_URL='sqlite:///' + db, DJANGO_DEBUG='True')

    print(f'Base de verification : {db} (recreee, migrations en cours…)')
    subprocess.run([sys.executable, 'manage.py', 'migrate', '--noinput'],
                   cwd=ROOT, env=env, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    total_ok = total_fail = 0
    for suite in SUITES:
        print(f'\n───────── {suite} ─────────')
        proc = subprocess.run([sys.executable, os.path.join('checks', suite)],
                              cwd=ROOT, env=env, capture_output=True, text=True)
        print(proc.stdout, end='')
        if proc.stderr.strip():
            print(proc.stderr, end='', file=sys.stderr)
        match = TOTAL_RE.search(proc.stdout)
        if match:
            total_ok += int(match.group(1))
            total_fail += int(match.group(2))
        else:
            total_fail += 1
            print(f'  !! suite interrompue (code de sortie {proc.returncode})',
                  file=sys.stderr)

    print(f'\n════ TOTAL : {total_ok} OK / {total_fail} FAIL ════')
    return 1 if total_fail else 0


if __name__ == '__main__':
    raise SystemExit(main())
