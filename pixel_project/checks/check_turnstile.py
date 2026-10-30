"""Verification humaine (Cloudflare Turnstile) des demandes de devis.

Django valide le jeton aupres du Worker Cloudflare
(`cloudflare/turnstile-worker.mjs`), qui garde le secret. Ces controles
verifient le widget, le parcours de devis et le refus des demandes non
verifiees.
"""
from _common import HOST_APEX as APEX, bootstrap, check, report

bootstrap()

import json
from pathlib import Path
from unittest.mock import patch

from django.conf import settings
from django.test import Client, override_settings

from studio.models import ProjetContact
from studio.turnstile import verify_turnstile

c = Client(HTTP_HOST=APEX)
sitekey = settings.TURNSTILE_SITE_KEY
check('cle publique Turnstile configuree', bool(sitekey))

print('\n== 1. Accueil : widget Turnstile dans le formulaire de projet ==')
r = c.get('/')
html = r.content.decode()
check('GET / -> 200', r.status_code == 200, r.status_code)
check('script Turnstile charge', 'challenges.cloudflare.com/turnstile/v0/api.js' in html)
check('widget Turnstile present', 'class="cf-turnstile"' in html and sitekey in html)
js = (Path(settings.BASE_DIR) / 'studio/static/js/main.js').read_text()
check('jeton Turnstile transmis par le formulaire', 'turnstile_token' in js and 'cf-turnstile-response' in js)

print('\n== 2. Page contact : widget et mode devis ==')
r = c.get('/contact/')
html = r.content.decode()
check('GET /contact/ -> 200', r.status_code == 200, r.status_code)
check('widget Turnstile present', 'class="cf-turnstile"' in html and sitekey in html)
check('libelle contact standard', 'Envoyer le message' in html)

r = c.get('/contact/?devis=1&offre=GestiActiv')
html = r.content.decode()
check('GET /contact/?devis=1 -> 200', r.status_code == 200, r.status_code)
check('titre devis', 'Demander un devis' in html)
check('offre pre-remplie', 'GestiActiv' in html)
check('selecteur de type de projet', 'name="type_projet"' in html)
check('bouton envoi devis', 'Envoyer ma demande de devis' in html)

print('\n== 3. Erreur de verification relayee par le Worker ==')
r = c.get('/contact/?erreur=robot')
check('message anti-robot affiche', "valider la vérification anti-robot" in r.content.decode())
r = c.get('/contact/?erreur=indisponible')
check('message indisponibilite affiche', 'momentanément indisponible' in r.content.decode())

print('\n== 4. Prix : le CTA devis mene au formulaire ==')
r = c.get('/prix/')
html = r.content.decode()
check('GET /prix/ -> 200', r.status_code == 200, r.status_code)
check('CTA devis vers /contact/', '/contact/?devis=1&amp;offre=' in html)
check('plus de CTA devis vers /login/', 'href="/login/" class="btn-s">Demander un devis' not in html)

print('\n== 5. Enregistrement d\'une demande de devis ==')
email = 'turnstile-check@example.test'
ProjetContact.objects.filter(email=email).delete()
r = c.post('/contact/?devis=1', {
    'nom': 'Verification Turnstile',
    'email': email,
    'type_projet': 'Logiciel de gestion / ERP',
    'message': 'Je souhaite un devis pour GestiActiv.',
    'devis': '1',
})
html = r.content.decode()
check('POST /contact/ -> 200', r.status_code == 200, r.status_code)
check('confirmation affichee', 'Merci pour votre message' in html)
contact = ProjetContact.objects.filter(email=email).first()
check('demande enregistree', contact is not None)
if contact:
    check('type de projet conserve dans le message',
          contact.message.startswith('[Logiciel de gestion / ERP]'))
ProjetContact.objects.filter(email=email).delete()

print('\n== 6. Verification serveur aupres du Worker ==')


class _ReponseWorker:
    def __init__(self, payload):
        self.payload = payload

    def read(self):
        return json.dumps(self.payload).encode()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


check('URL de verification du Worker configuree', bool(settings.TURNSTILE_VERIFY_PROXY_URL))
with override_settings(
    TURNSTILE_ENABLED=True,
    TURNSTILE_VERIFY_PROXY_URL='https://verify.test/verify',
):
    check('jeton absent refuse', verify_turnstile('') == (False, 'missing'))
    with patch(
        'studio.turnstile.urllib.request.urlopen',
        return_value=_ReponseWorker({'success': True}),
    ):
        check('jeton valide accepte', verify_turnstile('jeton') == (True, ''))
    with patch(
        'studio.turnstile.urllib.request.urlopen',
        return_value=_ReponseWorker({'success': False, 'error_codes': ['invalid-input-response']}),
    ):
        check('jeton invalide refuse', verify_turnstile('faux') == (False, 'invalid'))
    with patch('studio.turnstile.urllib.request.urlopen', side_effect=OSError('down')):
        check('Worker indisponible signale', verify_turnstile('jeton') == (False, 'unavailable'))
    with patch(
        'studio.turnstile.urllib.request.urlopen',
        return_value=_ReponseWorker({'success': False, 'error_codes': ['invalid-input-secret']}),
    ):
        check('secret invalide = indisponible', verify_turnstile('jeton') == (False, 'unavailable'))

print('\n== 7. Le serveur refuse une demande non verifiee ==')
email = 'turnstile-gate@example.test'
ProjetContact.objects.filter(email=email).delete()
with patch('studio.views.verify_turnstile', return_value=(False, 'invalid')):
    r = c.post('/contact/?devis=1', {
        'nom': 'Tentative non verifiee',
        'email': email,
        'type_projet': 'Site web',
        'message': 'Sans jeton.',
        'devis': '1',
    })
    check('formulaire non verifie : erreur affichee',
          "valider la vérification anti-robot" in r.content.decode(), r.status_code)
    check('formulaire non verifie : aucune demande creee',
          not ProjetContact.objects.filter(email=email).exists())

    r = c.post('/api/contact/', data=json.dumps({
        'username': 'Tentative API',
        'useremail': email,
        'usermessage': 'Sans jeton.',
        'turnstile_token': 'faux',
    }), content_type='application/json')
    check('API non verifiee : 400', r.status_code == 400, r.status_code)
    check('API non verifiee : aucune demande creee',
          not ProjetContact.objects.filter(email=email).exists())

with patch('studio.views.verify_turnstile', return_value=(True, '')):
    r = c.post('/api/contact/', data=json.dumps({
        'username': 'Demande verifiee',
        'useremail': email,
        'usermessage': 'Avec jeton.',
        'type_projet': 'Site web',
        'turnstile_token': 'valide',
    }), content_type='application/json')
    check('API verifiee : 201', r.status_code == 201, r.status_code)
    contact = ProjetContact.objects.filter(email=email).first()
    check('API verifiee : demande creee', contact is not None)
    check('API verifiee : type de projet conserve',
          bool(contact and contact.message.startswith('[Site web]')))
ProjetContact.objects.filter(email=email).delete()

raise SystemExit(report())
