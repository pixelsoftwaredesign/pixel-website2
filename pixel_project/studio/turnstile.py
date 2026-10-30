"""Vérification Cloudflare Turnstile via le Worker de bord.

Le secret Turnstile n'est pas présent dans Django : il reste dans les
variables chiffrées du Worker `pixelsoftwaredesign-contact`. Django lui envoie
le jeton et lit la réponse `{"success": true|false}`.

Le Worker doit être appelé **une seule fois** par jeton : les jetons Turnstile
sont à usage unique.
"""
import json
import logging
import urllib.request

from django.conf import settings

logger = logging.getLogger(__name__)


def verify_turnstile(token):
    """Valide un jeton Turnstile.

    Retourne ``(True, '')`` si le jeton est valide, sinon ``(False, raison)``
    avec ``raison`` parmi ``missing``, ``invalid`` ou ``unavailable``.
    """
    if not getattr(settings, 'TURNSTILE_ENABLED', False):
        return True, ''

    token = (token or '').strip()
    if not token:
        return False, 'missing'

    url = getattr(settings, 'TURNSTILE_VERIFY_PROXY_URL', '')
    if not url:
        logger.error('TURNSTILE_VERIFY_PROXY_URL absent : vérification impossible.')
        return False, 'unavailable'

    payload = json.dumps({'token': token}).encode('utf-8')
    request = urllib.request.Request(
        url,
        data=payload,
        method='POST',
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'PixelSoftwareDesign-Turnstile/1.0',
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=6) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception:
        logger.exception('Vérification Turnstile indisponible')
        return False, 'unavailable'

    if data.get('success') is True:
        return True, ''

    codes = data.get('error_codes') or []
    if 'invalid-input-secret' in codes or 'missing-input-secret' in codes:
        logger.error('Secret Turnstile invalide dans le Worker : %s', codes)
        return False, 'unavailable'
    return False, 'invalid'
