#!/bin/sh
# Démarrage du conteneur de production.
#
# 1. Vérifie que DJANGO_SECRET_KEY est bien fourni (jamais la valeur publique
#    du dépôt : sinon les sessions et jetons signés sont forgeables).
# 2. Applique les migrations avec réessais : Neon peut couper brièvement la
#    connexion SSL au démarrage, ce qui faisait échouer tout le déploiement.
# 3. Lance Gunicorn.
set -u

if [ -z "${DJANGO_SECRET_KEY:-}" ]; then
  echo "entrypoint: DJANGO_SECRET_KEY absent — refus de démarrer en production" >&2
  exit 1
fi

attempts="${MIGRATE_ATTEMPTS:-6}"
delay="${MIGRATE_DELAY:-10}"
i=1
while [ "$i" -le "$attempts" ]; do
  if python manage.py migrate --noinput; then
    echo "entrypoint: migrations appliquées (tentative $i/$attempts)"
    break
  fi
  if [ "$i" -eq "$attempts" ]; then
    echo "entrypoint: migrations en échec après $attempts tentatives — arrêt" >&2
    exit 1
  fi
  echo "entrypoint: migration échouée (tentative $i/$attempts), nouvel essai dans ${delay}s" >&2
  sleep "$delay"
  i=$((i + 1))
done

exec gunicorn pixel_project.wsgi:application \
  --bind "0.0.0.0:${PORT:-8000}" \
  --workers "${WEB_CONCURRENCY:-3}" \
  --timeout 120
