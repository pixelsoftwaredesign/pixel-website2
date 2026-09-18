import json
import urllib.request

from django.conf import settings
from django.core.mail import send_mail


def envoyer_email(sujet, texte, html, destinataires):
    """Envoie un email via l'API Resend (HTTPS) si RESEND_API_KEY est configuré,
    sinon via le backend Django (SMTP). Lève une exception en cas d'échec."""
    api_key = getattr(settings, 'RESEND_API_KEY', '')
    if api_key:
        if not isinstance(destinataires, list):
            destinataires = [destinataires]
        payload = {
            'from': getattr(settings, 'RESEND_FROM_EMAIL', '') or settings.DEFAULT_FROM_EMAIL,
            'to': destinataires,
            'subject': sujet,
            'html': html,
            'text': texte,
        }
        req = urllib.request.Request(
            'https://api.resend.com/emails',
            data=json.dumps(payload).encode('utf-8'),
            headers={
                'Authorization': 'Bearer ' + api_key,
                'Content-Type': 'application/json',
            },
            method='POST',
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.getcode()
        if status < 200 or status >= 300:
            raise RuntimeError('Resend HTTP %s' % status)
        return
    send_mail(
        sujet,
        texte,
        settings.DEFAULT_FROM_EMAIL,
        destinataires,
        html_message=html,
        fail_silently=False,
    )