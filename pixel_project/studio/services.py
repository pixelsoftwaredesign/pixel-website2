from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone

SITE_NAME = "Pixel Software Design"

def envoyer_email(destinataire, sujet, message):
    msg_id = '<pixel-{}-{}@localhost>'.format(
        int(timezone.now().timestamp()), destinataire.split('@')[0]
    )
    msg = EmailMessage(
        subject=f"[{SITE_NAME}] {sujet}",
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[destinataire],
        headers={'Message-ID': msg_id},
    )
    msg.send(fail_silently=False)

def notifier_activation_cle(souscription, code):
    sujet = "Votre clé d'activation PixelSoftCode"
    message = f"""Bonjour {souscription.client_nom},

Votre paiement a été confirmé. Voici votre clé d'activation :

🔑 {code}

Plan : {souscription.plan.nom if souscription.plan else 'N/A'}
Date d'activation : {timezone.now().strftime('%d/%m/%Y à %H:%M')}

Utilisez cette clé dans votre logiciel pour l'activer.

Merci de votre confiance,
L'équipe {SITE_NAME}
{settings.SITE_URL}"""
    envoyer_email(souscription.client_email, sujet, message)

def notifier_confirmation_commande(commande):
    sujet = f"Confirmation de commande {commande.reference}"
    items_text = "\n".join([
        f"  - {i.nom_produit} x{i.quantite} = {i.sous_total()} TND"
        for i in commande.items.all()
    ])
    message = f"""Bonjour {commande.client_nom},

Merci pour votre commande sur PixelShop.

📦 Réf : {commande.reference}
📅 Date : {commande.date_commande.strftime('%d/%m/%Y')}
💳 Paiement : {commande.get_methode_paiement_display()}
📍 Adresse : {commande.client_adresse}

Articles commandés :
{items_text}

💰 Total TTC : {commande.total_ttc} TND

Nous vous tiendrons informé de l'avancement de votre commande.

Merci de votre confiance,
L'équipe {SITE_NAME}
{settings.SITE_URL}"""
    envoyer_email(commande.client_email, sujet, message)

def notifier_statut_commande(commande):
    sujet = f"Votre commande {commande.reference} est {commande.get_statut_display()}"
    message = f"""Bonjour {commande.client_nom},

Le statut de votre commande {commande.reference} a été mis à jour :

📦 Statut : {commande.get_statut_display()}

{'Votre commande a été expédiée !' if commande.statut == 'expediee' else ''}
{'Votre commande a été livrée. Merci !' if commande.statut == 'livree' else ''}

Merci de votre confiance,
L'équipe {SITE_NAME}
{settings.SITE_URL}"""
    envoyer_email(commande.client_email, sujet, message)
