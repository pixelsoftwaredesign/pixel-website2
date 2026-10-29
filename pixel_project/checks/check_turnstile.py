"""Verification humaine (Cloudflare Turnstile) des demandes de devis.

Le jeton est valide a la peripherie par le Worker Cloudflare
(`cloudflare/turnstile-worker.mjs`). Ces controles verifient que les pages
exposent bien le widget et que le parcours de devis reste coherent.
"""
from _common import HOST_APEX as APEX, bootstrap, check, report

bootstrap()

from pathlib import Path

from django.conf import settings
from django.test import Client

from studio.models import ProjetContact

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

raise SystemExit(report())
