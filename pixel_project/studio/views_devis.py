"""Espace admin : devis structurés, ventes et préfactures.

Les pages sont accessibles aux rôles Commercial, Comptable, Admin et
SuperAdmin. Les ventes affichées ici sont celles du site (sans entreprise
GestiActiv) afin de ne pas exposer les données des tenants.
"""
from django.contrib import messages
from django.db.models import F, Q, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.html import escape

from .emailing import envoyer_email
from .forms_devis import (
    DevisForm, DevisLigneFormSet, PreFactureForm, PreFactureLigneFormSet,
    VenteForm,
)
from .models import (
    Devis, Facture, PreFacture, Produit, ProjetContact, Vente,
)
from .views import _paginate, role_required

ADMIN_ROLES = ('Commercial', 'Comptable', 'SuperAdmin', 'Admin')


def _societe():
    return {
        'nom': 'Pixel Software Design',
        'slogan': "L'architecture de l'innovation",
        'adresse': 'El Hamma, Gabès, Tunisie',
        'email': 'pixelsoftwaredesign@gmail.com',
        'tel': '+216 52 675 027',
        'registre': 'Matricule: XXXXXXXX/X/X/XXX',
    }


def _produits_json(produits):
    return {
        str(p.id): {'nom': p.nom, 'prix': str(p.prix_vente)}
        for p in produits
    }


def _lignes_initiales(document):
    return [{
        'produit': ligne.produit_id,
        'designation': ligne.designation,
        'quantite': ligne.quantite,
        'prix_unitaire': ligne.prix_unitaire,
        'remise': ligne.remise,
    } for ligne in document.lignes.all()]


def _corps_email_devis(devis):
    lignes = list(devis.lignes.all())
    texte = [
        "Bonjour %s," % devis.client_nom,
        "",
        "Merci pour votre demande. Voici notre devis %s." % devis.reference,
        "",
    ]
    for ligne in lignes:
        texte.append("- %s x%s : %s TND" % (
            ligne.designation or (ligne.produit.nom if ligne.produit else 'Prestation'),
            ligne.quantite, ligne.total))
    texte += [
        "",
        "Total HT : %s TND" % devis.montant_ht,
        "TVA (%s%%) : %s TND" % (
            devis.tva, devis.montant_ttc - devis.montant_ht),
        "Total TTC : %s TND" % devis.montant_ttc,
        "",
        "Pour accepter ce devis, répondez simplement à cet email.",
        "",
        "Cordialement,",
        "L'équipe Pixel Software Design",
        "+216 52 675 027",
    ]
    html = [
        "<p>Bonjour %s,</p>" % escape(devis.client_nom),
        "<p>Merci pour votre demande. Voici notre devis "
        "<strong>%s</strong>.</p>" % escape(devis.reference),
        "<table style=\"width:100%%;border-collapse:collapse\">",
        "<thead><tr><th style=\"text-align:left\">Désignation</th>"
        "<th>Qté</th><th>Total</th></tr></thead><tbody>",
    ]
    for ligne in lignes:
        designation = ligne.designation or (
            ligne.produit.nom if ligne.produit else 'Prestation')
        html.append(
            "<tr><td>%s</td><td>%s</td><td>%s TND</td></tr>" % (
                escape(designation), ligne.quantite, ligne.total))
    html += [
        "</tbody></table>",
        "<p><strong>Total HT :</strong> %s TND<br>" % devis.montant_ht,
        "<strong>TVA (%s%%) :</strong> %s TND<br>" % (
            devis.tva, devis.montant_ttc - devis.montant_ht),
        "<strong>Total TTC :</strong> %s TND</p>" % devis.montant_ttc,
        "<p>Pour accepter ce devis, répondez simplement à cet email.</p>",
        "<p>Cordialement,<br>L'équipe Pixel Software Design<br>"
        "+216 52 675 027</p>",
    ]
    return "\n".join(texte), "\n".join(html)


def _envoyer_devis(devis):
    sujet = "Votre devis %s — Pixel Software Design" % devis.reference
    texte, html = _corps_email_devis(devis)
    try:
        envoyer_email(sujet, texte, html, [devis.client_email])
        return True, ''
    except Exception as exc:  # SMTP/Resend non configuré, erreur réseau…
        return False, str(exc)


@role_required(*ADMIN_ROLES)
def devis_list(request):
    qs = Devis.objects.select_related('projet').order_by('-date_creation')
    statut = (request.GET.get('statut') or '').strip()
    if statut in dict(Devis.STATUTS):
        qs = qs.filter(statut=statut)
    else:
        statut = ''
    q = (request.GET.get('q') or '').strip()
    if q:
        qs = qs.filter(
            Q(reference__icontains=q) | Q(client_nom__icontains=q) |
            Q(client_email__icontains=q) | Q(sujet__icontains=q))
    devis, pager = _paginate(qs, 'page', request, 15)
    stats = {
        'total': Devis.objects.count(),
        'a_traiter': Devis.objects.filter(
            statut__in=['nouveau', 'en_cours']).count(),
        'acceptes': Devis.objects.filter(statut='accepte').count(),
        'convertis': Devis.objects.filter(statut='converti').count(),
        'montant': Devis.objects.filter(
            statut__in=['accepte', 'converti']).aggregate(
                s=Sum('montant_ttc'))['s'] or 0,
    }
    return render(request, 'studio/admin_devis_list.html', {
        'devis': devis,
        'pager': pager,
        'statut': statut,
        'statut_choices': Devis.STATUTS,
        'statut_counts': [
            {'value': value, 'label': label,
             'count': Devis.objects.filter(statut=value).count()}
            for value, label in Devis.STATUTS
        ],
        'stats': stats,
        'q': q,
        'projets_disponibles': ProjetContact.objects.filter(
            devis__isnull=True).order_by('-date_reception')[:50],
    })


@role_required(*ADMIN_ROLES)
def devis_create(request):
    projet = None
    projet_id = request.GET.get('projet') or request.POST.get('projet')
    if projet_id:
        projet = get_object_or_404(ProjetContact, pk=projet_id)

    initial = {}
    if projet:
        initial = {
            'client_nom': projet.nom,
            'client_email': projet.email,
            'sujet': 'Réponse à votre demande de projet',
            'message': projet.message,
        }

    produit = None
    produit_id = request.GET.get('produit') or request.POST.get('produit')
    if produit_id:
        produit = Produit.objects.filter(
            pk=produit_id, actif=True, erp_client__isnull=True).first()
    lignes_initiales = []
    if produit:
        lignes_initiales = [{
            'produit': produit.id,
            'designation': produit.nom,
            'quantite': 1,
            'prix_unitaire': produit.prix_vente,
        }]

    if request.method == 'POST':
        form = DevisForm(request.POST)
        formset = DevisLigneFormSet(request.POST, prefix='lignes')
        if form.is_valid() and formset.is_valid():
            devis = form.save(commit=False)
            devis.projet = projet
            devis.cree_par = request.user
            devis.save()
            formset.instance = devis
            for line_form in formset.forms:
                line_form.instance.devis = devis
            formset.save()
            for index, ligne in enumerate(devis.lignes.all()):
                ligne.ordre = index
                ligne.save(update_fields=['ordre'])
            devis.recalculer_totaux()
            messages.success(
                request, "Devis %s créé." % devis.reference)
            return redirect('admin_devis_detail', pk=devis.pk)
        messages.error(
            request, "Le devis contient des erreurs. Vérifiez les champs et les lignes.")
    else:
        form = DevisForm(initial=initial)
        formset = DevisLigneFormSet(initial=lignes_initiales, prefix='lignes')

    produits = list(Produit.objects.filter(
        actif=True, erp_client__isnull=True).order_by('nom'))
    return render(request, 'studio/admin_devis_form.html', {
        'form': form,
        'formset': formset,
        'devis': None,
        'projet': projet,
        'produits': produits,
        'produits_json': _produits_json(produits),
        'mode': 'create',
    })


@role_required(*ADMIN_ROLES)
def devis_detail(request, pk):
    devis = get_object_or_404(
        Devis.objects.select_related('projet'), pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action', 'save')
        if action == 'supprimer':
            reference = devis.reference
            devis.delete()
            messages.success(request, "Devis %s supprimé." % reference)
            return redirect('admin_devis_list')

        form = DevisForm(request.POST, instance=devis)
        formset = DevisLigneFormSet(
            request.POST, instance=devis, prefix='lignes')
        if form.is_valid() and formset.is_valid():
            devis = form.save()
            formset.save()
            for index, ligne in enumerate(devis.lignes.all()):
                ligne.ordre = index
                ligne.save(update_fields=['ordre'])
            devis.recalculer_totaux()

            if action == 'envoyer':
                if not devis.lignes.exists():
                    messages.error(
                        request, "Ajoutez au moins une ligne avant d'envoyer le devis.")
                    return redirect('admin_devis_detail', pk=devis.pk)
                ok, erreur = _envoyer_devis(devis)
                if devis.statut not in ('accepte', 'converti', 'refuse'):
                    devis.statut = 'envoye'
                devis.date_envoi = timezone.now()
                devis.save(update_fields=['statut', 'date_envoi'])
                if devis.projet:
                    devis.projet.a_repondu = True
                    devis.projet.date_reponse = timezone.now()
                    devis.projet.save(update_fields=['a_repondu', 'date_reponse'])
                if ok:
                    messages.success(
                        request, "Devis %s envoyé à %s." % (
                            devis.reference, devis.client_email))
                else:
                    messages.warning(
                        request, "Devis enregistré et marqué envoyé, mais "
                        "l'email n'a pas pu être expédié : %s. Utilisez "
                        "« Imprimer » pour transmettre le document." % erreur)
                return redirect('admin_devis_detail', pk=devis.pk)

            if action == 'accepter':
                if devis.statut == 'converti':
                    messages.info(
                        request, "Ce devis est déjà converti en vente.")
                    return redirect('admin_devis_detail', pk=devis.pk)
                devis.statut = 'accepte'
                devis.date_acceptation = timezone.now()
                devis.save(update_fields=['statut', 'date_acceptation'])
                messages.success(request, "Devis marqué comme accepté.")
                return redirect('admin_devis_detail', pk=devis.pk)

            if action == 'convertir':
                if devis.ventes.exists():
                    messages.info(request, "Ce devis a déjà été converti en vente.")
                    return redirect('admin_ventes')
                if devis.lignes.filter(produit__isnull=True).exists():
                    messages.error(
                        request, "Chaque ligne doit être liée à un produit du "
                        "catalogue pour créer une vente.")
                    return redirect('admin_devis_detail', pk=devis.pk)
                nombre = devis.convertir_en_vente()
                if nombre:
                    messages.success(
                        request, "%d vente(s) créée(s) depuis le devis %s." % (
                            nombre, devis.reference))
                    return redirect('admin_ventes')
                messages.error(
                    request, "Impossible de convertir ce devis : aucune ligne produit.")
                return redirect('admin_devis_detail', pk=devis.pk)

            if action == 'prefacture':
                if not devis.lignes.exists():
                    messages.error(
                        request, "Ajoutez au moins une ligne avant de créer "
                        "une préfacture.")
                    return redirect('admin_devis_detail', pk=devis.pk)
                prefacture = devis.creer_prefacture(request.user)
                messages.success(
                    request, "Préfacture %s créée depuis le devis %s." % (
                        prefacture.numero, devis.reference))
                return redirect('admin_prefacture_detail', pk=prefacture.pk)

            messages.success(request, "Devis %s enregistré." % devis.reference)
            return redirect('admin_devis_detail', pk=devis.pk)

        messages.error(
            request, "Le devis contient des erreurs. Vérifiez les champs et les lignes.")
    else:
        form = DevisForm(instance=devis)
        formset = DevisLigneFormSet(instance=devis, prefix='lignes')

    produits = list(Produit.objects.filter(
        actif=True, erp_client__isnull=True).order_by('nom'))
    return render(request, 'studio/admin_devis_form.html', {
        'form': form,
        'formset': formset,
        'devis': devis,
        'projet': devis.projet,
        'produits': produits,
        'produits_json': _produits_json(produits),
        'mode': 'edit',
    })


@role_required(*ADMIN_ROLES)
def devis_print(request, pk):
    devis = get_object_or_404(Devis.objects.select_related('projet'), pk=pk)
    return render(request, 'studio/admin_devis_print.html', {
        'devis': devis,
        'lignes': devis.lignes.all(),
        'tva_montant': devis.montant_ttc - devis.montant_ht,
        'societe': _societe(),
    })


@role_required(*ADMIN_ROLES)
def ventes_list(request):
    if request.method == 'POST':
        action = request.POST.get('action', 'create')
        if action == 'supprimer':
            vente = get_object_or_404(
                Vente, pk=request.POST.get('vente_id'), erp_client__isnull=True)
            vente.delete()
            messages.success(request, "Vente supprimée.")
            return redirect('admin_ventes')

        form = VenteForm(request.POST)
        if form.is_valid():
            produit = form.cleaned_data['produit']
            prix = form.cleaned_data.get('prix_unitaire') or produit.prix_vente
            vente = Vente.objects.create(
                erp_client=None, produit=produit,
                quantite=form.cleaned_data['quantite'],
                prix_unitaire=prix,
                client_nom=form.cleaned_data.get('client_nom') or '',
                devis=form.cleaned_data.get('devis'))
            messages.success(request, "Vente #%s enregistrée." % vente.pk)
            return redirect('admin_ventes')
        messages.error(request, "La vente contient des erreurs.")
    else:
        form = VenteForm()

    qs = Vente.objects.filter(erp_client__isnull=True).select_related(
        'produit', 'devis').order_by('-date_vente')
    q = (request.GET.get('q') or '').strip()
    if q:
        qs = qs.filter(
            Q(client_nom__icontains=q) | Q(produit__nom__icontains=q) |
            Q(devis__reference__icontains=q))
    ventes, pager = _paginate(qs, 'page', request, 20)
    now = timezone.localdate()
    total = qs.aggregate(s=Sum(F('quantite') * F('prix_unitaire')))['s'] or 0
    mois = qs.filter(date_vente__year=now.year, date_vente__month=now.month)
    montant_mois = mois.aggregate(
        s=Sum(F('quantite') * F('prix_unitaire')))['s'] or 0
    return render(request, 'studio/admin_ventes.html', {
        'ventes': ventes,
        'pager': pager,
        'form': form,
        'q': q,
        'stats': {
            'total': qs.count(),
            'montant': total,
            'mois': mois.count(),
            'montant_mois': montant_mois,
        },
    })


@role_required(*ADMIN_ROLES)
def prefactures_list(request):
    qs = PreFacture.objects.select_related(
        'devis', 'vente').order_by('-date_creation')
    statut = (request.GET.get('statut') or '').strip()
    if statut in dict(PreFacture.STATUTS):
        qs = qs.filter(statut=statut)
    else:
        statut = ''
    q = (request.GET.get('q') or '').strip()
    if q:
        qs = qs.filter(
            Q(numero__icontains=q) | Q(client_nom__icontains=q) |
            Q(client_email__icontains=q))
    prefactures, pager = _paginate(qs, 'page', request, 15)
    return render(request, 'studio/admin_prefactures.html', {
        'prefactures': prefactures,
        'pager': pager,
        'statut': statut,
        'statut_choices': PreFacture.STATUTS,
        'statut_counts': [
            {'value': value, 'label': label,
             'count': PreFacture.objects.filter(statut=value).count()}
            for value, label in PreFacture.STATUTS
        ],
        'q': q,
        'stats': {
            'total': PreFacture.objects.count(),
            'brouillon': PreFacture.objects.filter(statut='brouillon').count(),
            'envoyees': PreFacture.objects.filter(statut='envoyee').count(),
            'montant': PreFacture.objects.aggregate(
                s=Sum('montant_ttc'))['s'] or 0,
        },
    })


@role_required(*ADMIN_ROLES)
def prefacture_create(request):
    devis = None
    vente = None
    devis_id = request.POST.get('devis') or request.GET.get('devis')
    vente_id = request.POST.get('vente') or request.GET.get('vente')
    if devis_id:
        devis = get_object_or_404(Devis, pk=devis_id)
    if vente_id:
        vente = get_object_or_404(
            Vente.objects.filter(erp_client__isnull=True), pk=vente_id)

    initial = {}
    lignes_initiales = []
    if devis:
        initial = {
            'client_nom': devis.client_nom,
            'client_email': devis.client_email,
            'client_adresse': devis.client_adresse,
            'tva': devis.tva,
            'notes': devis.message,
        }
        lignes_initiales = _lignes_initiales(devis)
    elif vente:
        initial = {'client_nom': vente.client_nom or '', 'tva': 19}
        lignes_initiales = [{
            'produit': vente.produit_id,
            'designation': vente.produit.nom,
            'quantite': vente.quantite,
            'prix_unitaire': vente.prix_unitaire,
            'remise': 0,
        }]

    if request.method == 'POST':
        form = PreFactureForm(request.POST)
        formset = PreFactureLigneFormSet(request.POST, prefix='lignes')
        if form.is_valid() and formset.is_valid():
            prefacture = form.save(commit=False)
            prefacture.devis = devis
            prefacture.vente = vente
            prefacture.cree_par = request.user
            prefacture.save()
            formset.instance = prefacture
            for line_form in formset.forms:
                line_form.instance.prefacture = prefacture
            formset.save()
            for index, ligne in enumerate(prefacture.lignes.all()):
                ligne.ordre = index
                ligne.save(update_fields=['ordre'])
            prefacture.recalculer_totaux()
            messages.success(
                request, "Préfacture %s créée." % prefacture.numero)
            return redirect('admin_prefacture_detail', pk=prefacture.pk)
        messages.error(
            request, "La préfacture contient des erreurs. Vérifiez les champs "
            "et les lignes.")
    else:
        form = PreFactureForm(initial=initial)
        formset = PreFactureLigneFormSet(
            initial=lignes_initiales, prefix='lignes')

    produits = list(Produit.objects.filter(
        actif=True, erp_client__isnull=True).order_by('nom'))
    return render(request, 'studio/admin_prefacture_form.html', {
        'form': form,
        'formset': formset,
        'prefacture': None,
        'devis': devis,
        'vente': vente,
        'produits': produits,
        'produits_json': _produits_json(produits),
        'mode': 'create',
    })


@role_required(*ADMIN_ROLES)
def prefacture_detail(request, pk):
    prefacture = get_object_or_404(
        PreFacture.objects.select_related('devis', 'vente'), pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action', 'save')
        if action == 'supprimer':
            numero = prefacture.numero
            prefacture.delete()
            messages.success(request, "Préfacture %s supprimée." % numero)
            return redirect('admin_prefactures')

        if action == 'convertir':
            if prefacture.statut == 'convertie':
                messages.info(request, "Cette préfacture est déjà convertie.")
                return redirect('admin_prefacture_detail', pk=prefacture.pk)
            facture = prefacture.convertir_en_facture(request.user)
            messages.success(
                request, "Facture %s créée depuis la préfacture." % facture.numero)
            return redirect('admin_facture_detail', pk=facture.pk)

        form = PreFactureForm(request.POST, instance=prefacture)
        formset = PreFactureLigneFormSet(
            request.POST, instance=prefacture, prefix='lignes')
        if form.is_valid() and formset.is_valid():
            prefacture = form.save()
            formset.save()
            for index, ligne in enumerate(prefacture.lignes.all()):
                ligne.ordre = index
                ligne.save(update_fields=['ordre'])
            prefacture.recalculer_totaux()
            messages.success(
                request, "Préfacture %s enregistrée." % prefacture.numero)
            return redirect('admin_prefacture_detail', pk=prefacture.pk)
        messages.error(
            request, "La préfacture contient des erreurs. Vérifiez les champs "
            "et les lignes.")
    else:
        form = PreFactureForm(instance=prefacture)
        formset = PreFactureLigneFormSet(
            instance=prefacture, prefix='lignes')

    produits = list(Produit.objects.filter(
        actif=True, erp_client__isnull=True).order_by('nom'))
    return render(request, 'studio/admin_prefacture_form.html', {
        'form': form,
        'formset': formset,
        'prefacture': prefacture,
        'devis': prefacture.devis,
        'vente': prefacture.vente,
        'produits': produits,
        'produits_json': _produits_json(produits),
        'mode': 'edit',
    })


@role_required(*ADMIN_ROLES)
def prefacture_print(request, pk):
    prefacture = get_object_or_404(
        PreFacture.objects.select_related('devis', 'vente'), pk=pk)
    return render(request, 'studio/admin_prefacture_print.html', {
        'prefacture': prefacture,
        'lignes': prefacture.lignes.all(),
        'tva_montant': prefacture.montant_ttc - prefacture.montant_ht,
        'societe': _societe(),
    })


@role_required(*ADMIN_ROLES)
def factures_list(request):
    qs = Facture.objects.filter(
        erp_client__isnull=True).select_related('prefacture').order_by(
            '-date_facture')
    paiement = (request.GET.get('paiement') or '').strip()
    if paiement == 'payee':
        qs = qs.filter(payee=True)
    elif paiement == 'impayee':
        qs = qs.filter(payee=False)
    else:
        paiement = ''
    q = (request.GET.get('q') or '').strip()
    if q:
        qs = qs.filter(
            Q(numero__icontains=q) | Q(client_nom__icontains=q) |
            Q(client_email__icontains=q))
    factures, pager = _paginate(qs, 'page', request, 20)
    site = Facture.objects.filter(erp_client__isnull=True)
    return render(request, 'studio/admin_factures.html', {
        'factures': factures,
        'pager': pager,
        'paiement': paiement,
        'q': q,
        'stats': {
            'total': site.count(),
            'payees': site.filter(payee=True).count(),
            'impayees': site.filter(payee=False).count(),
            'montant': site.aggregate(s=Sum('montant_ttc'))['s'] or 0,
            'montant_impaye': site.filter(payee=False).aggregate(
                s=Sum('montant_ttc'))['s'] or 0,
        },
    })


@role_required(*ADMIN_ROLES)
def facture_detail(request, pk):
    facture = get_object_or_404(
        Facture.objects.filter(erp_client__isnull=True).select_related(
            'prefacture'), pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action', '')
        if action in ('marquer_payee', 'marquer_impayee'):
            facture.payee = action == 'marquer_payee'
            facture.date_paiement = (
                timezone.localdate() if facture.payee else None)
            facture.save(update_fields=['payee', 'date_paiement'])
            messages.success(
                request, "Facture %s marquée %s." % (
                    facture.numero, 'payée' if facture.payee else 'impayée'))
        return redirect('admin_facture_detail', pk=facture.pk)

    return render(request, 'studio/admin_facture_detail.html', {
        'facture': facture,
        'lignes': facture.lignes.all(),
        'tva_montant': facture.montant_ttc - facture.montant_ht,
    })


@role_required(*ADMIN_ROLES)
def facture_print(request, pk):
    facture = get_object_or_404(
        Facture.objects.filter(erp_client__isnull=True).select_related(
            'prefacture'), pk=pk)
    return render(request, 'studio/admin_facture_print.html', {
        'facture': facture,
        'lignes': facture.lignes.all(),
        'tva_montant': facture.montant_ttc - facture.montant_ht,
        'societe': _societe(),
    })
