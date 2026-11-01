"""Gestion du catalogue du site dans l'espace admin Pixel.

Le catalogue public est volontairement séparé des données GestiActiv :
toutes les requêtes filtrent ``erp_client__isnull=True``. Les rôles
Commercial et Comptable consultent le catalogue ; Admin et SuperAdmin
peuvent créer, modifier, archiver et ajuster le stock.
"""
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.db.models import Count, F, Q, Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms_catalogue import (
    CategorieForm, FournisseurForm, MouvementStockForm, ProduitForm,
)
from .models import Categorie, Fournisseur, MouvementStock, Produit
from .views import _paginate, role_required

ADMIN_ROLES = ('Commercial', 'Comptable', 'SuperAdmin', 'Admin')
GESTION_ROLES = ('SuperAdmin', 'Admin')


def _peut_gerer(user):
    return bool(
        user.is_authenticated and (
            user.is_superuser or
            user.groups.filter(name__in=GESTION_ROLES).exists()))


def _exiger_gestion(user):
    if not _peut_gerer(user):
        raise PermissionDenied(
            "La modification du catalogue est réservée aux rôles "
            "Admin et SuperAdmin.")


def _auteur(user):
    return (user.get_full_name() or user.username)[:100]


class StockInsuffisant(Exception):
    pass


def _mouvement(produit, type_mouvement, quantite, reference, notes, user):
    with transaction.atomic():
        produit = Produit.objects.select_for_update().get(
            pk=produit.pk, erp_client__isnull=True)
        avant = produit.stock_actuel
        if type_mouvement in ('entree', 'retour'):
            apres = avant + quantite
        elif type_mouvement == 'sortie':
            if quantite > avant:
                raise StockInsuffisant(avant)
            apres = avant - quantite
        else:
            apres = max(0, quantite)
        produit.stock_actuel = apres
        produit.save(update_fields=['stock_actuel'])
        MouvementStock.objects.create(
            produit=produit, type=type_mouvement, quantite=quantite,
            stock_avant=avant, stock_apres=apres,
            reference=reference, notes=notes, cree_par=_auteur(user))
    return avant, apres


def _produit_site(pk):
    return get_object_or_404(
        Produit.objects.filter(erp_client__isnull=True).select_related(
            'categorie', 'fournisseur'), pk=pk)


def _contexte_produit(produit, user, stock_form=None):
    return {
        'produit': produit,
        'stock_form': stock_form or MouvementStockForm(),
        'mouvements': produit.mouvements.order_by('-date_mouvement')[:25],
        'valeur_stock': (
            0 if produit.est_service else produit.prix_vente * produit.stock_actuel),
        'counts': {
            'devis': produit.lignes_devis.count(),
            'ventes': produit.ventes.count(),
            'prefactures': produit.lignes_prefacture.count(),
            'factures': produit.lignes_facture.count(),
            'commandes': produit.commandes_items.count(),
        },
        'peut_gerer': _peut_gerer(user),
    }


@role_required(*ADMIN_ROLES)
def produits_list(request):
    qs = Produit.objects.filter(
        erp_client__isnull=True).select_related('categorie').order_by('nom')
    q = (request.GET.get('q') or '').strip()
    if q:
        qs = qs.filter(
            Q(nom__icontains=q) | Q(categorie__nom__icontains=q) |
            Q(fournisseur__nom__icontains=q) | Q(code_barre__icontains=q))
    actif = (request.GET.get('actif') or '').strip()
    if actif == '1':
        qs = qs.filter(actif=True)
    elif actif == '0':
        qs = qs.filter(actif=False)
    else:
        actif = ''
    produits, pager = _paginate(qs, 'page', request, 20)
    site = Produit.objects.filter(erp_client__isnull=True)
    valeur_stock = site.filter(est_service=False).aggregate(
        total=Sum(F('prix_vente') * F('stock_actuel')))['total'] or 0
    return render(request, 'studio/admin_produits.html', {
        'produits': produits,
        'pager': pager,
        'q': q,
        'actif': actif,
        'peut_gerer': _peut_gerer(request.user),
        'stats': {
            'total': site.count(),
            'actifs': site.filter(actif=True).count(),
            'alertes': site.filter(
                actif=True, est_service=False,
                stock_actuel__lte=F('stock_minimum')).count(),
            'valeur_stock': valeur_stock,
            'categories': Categorie.objects.filter(
                erp_client__isnull=True).count(),
            'fournisseurs': Fournisseur.objects.filter(
                erp_client__isnull=True).count(),
        },
    })


@role_required(*ADMIN_ROLES)
def produit_detail(request, pk):
    produit = _produit_site(pk)
    stock_form = MouvementStockForm()

    if request.method == 'POST':
        _exiger_gestion(request.user)
        action = request.POST.get('action', '')
        if action == 'statut':
            produit.actif = not produit.actif
            produit.save(update_fields=['actif'])
            messages.success(
                request, "Produit %s %s." % (
                    produit.nom, 'activé' if produit.actif else 'archivé'))
            return redirect('admin_produit_detail', pk=produit.pk)
        if action == 'stock':
            stock_form = MouvementStockForm(request.POST)
            if stock_form.is_valid():
                type_mouvement = stock_form.cleaned_data['type']
                quantite = stock_form.cleaned_data['quantite']
                try:
                    avant, apres = _mouvement(
                        produit, type_mouvement, quantite,
                        stock_form.cleaned_data.get('reference', ''),
                        stock_form.cleaned_data.get('notes', ''),
                        request.user)
                except StockInsuffisant as exc:
                    stock_form.add_error(
                        'quantite',
                        "Stock insuffisant : %s disponible(s)." % exc)
                else:
                    messages.success(
                        request, "Stock mis à jour : %s → %s." % (avant, apres))
                    return redirect('admin_produit_detail', pk=produit.pk)

    return render(
        request, 'studio/admin_produit_detail.html',
        _contexte_produit(produit, request.user, stock_form))


@role_required(*ADMIN_ROLES)
def produit_create(request):
    _exiger_gestion(request.user)
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            stock_initial = form.cleaned_data.get('stock_initial') or 0
            with transaction.atomic():
                produit = form.save(commit=False)
                produit.erp_client = None
                produit.stock_actuel = 0
                produit.save()
                if stock_initial:
                    _mouvement(
                        produit, 'entree', stock_initial, 'Stock initial',
                        'Création de la fiche produit', request.user)
            messages.success(
                request, "Produit %s créé." % produit.nom)
            return redirect('admin_produit_detail', pk=produit.pk)
    else:
        form = ProduitForm()
    return render(request, 'studio/admin_produit_form.html', {
        'form': form,
        'mode': 'create',
        'peut_gerer': True,
        'categories': Categorie.objects.filter(
            erp_client__isnull=True).count(),
        'fournisseurs': Fournisseur.objects.filter(
            erp_client__isnull=True).count(),
    })


@role_required(*ADMIN_ROLES)
def produit_edit(request, pk):
    _exiger_gestion(request.user)
    produit = _produit_site(pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            produit = form.save(commit=False)
            produit.erp_client = None
            produit.save()
            messages.success(
                request, "Produit %s mis à jour." % produit.nom)
            return redirect('admin_produit_detail', pk=produit.pk)
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'studio/admin_produit_form.html', {
        'form': form,
        'mode': 'edit',
        'produit': produit,
        'peut_gerer': True,
        'categories': Categorie.objects.filter(
            erp_client__isnull=True).count(),
        'fournisseurs': Fournisseur.objects.filter(
            erp_client__isnull=True).count(),
    })


@role_required(*ADMIN_ROLES)
def categories_list(request):
    peut_gerer = _peut_gerer(request.user)
    site = Categorie.objects.filter(erp_client__isnull=True)
    edit_id = request.GET.get('edit') or request.POST.get('categorie_id')
    edit_categorie = None
    if edit_id:
        edit_categorie = get_object_or_404(
            Categorie, pk=edit_id, erp_client__isnull=True)

    if request.method == 'POST':
        _exiger_gestion(request.user)
        action = request.POST.get('action', '')
        if action == 'delete':
            categorie = get_object_or_404(
                Categorie, pk=request.POST.get('categorie_id'),
                erp_client__isnull=True)
            if categorie.produits.exists():
                messages.error(
                    request,
                    "Impossible de supprimer « %s » : des produits "
                    "l'utilisent encore." % categorie.nom)
            else:
                categorie.delete()
                messages.success(request, "Catégorie supprimée.")
            return redirect('admin_categories')
        if action == 'update':
            if edit_categorie is None:
                messages.error(request, "Catégorie introuvable.")
                return redirect('admin_categories')
            form = CategorieForm(request.POST, instance=edit_categorie)
            if form.is_valid():
                categorie = form.save(commit=False)
                categorie.erp_client = None
                categorie.save()
                messages.success(request, "Catégorie mise à jour.")
                return redirect('admin_categories')
        else:
            form = CategorieForm(request.POST)
            if form.is_valid():
                categorie = form.save(commit=False)
                categorie.erp_client = None
                categorie.save()
                messages.success(request, "Catégorie créée.")
                return redirect('admin_categories')
    else:
        form = CategorieForm(instance=edit_categorie)

    qs = site.annotate(
        nb_produits=Count(
            'produits', filter=Q(produits__erp_client__isnull=True))
    ).order_by('nom')
    q = (request.GET.get('q') or '').strip()
    if q:
        qs = qs.filter(
            Q(nom__icontains=q) | Q(description__icontains=q))
    categories, pager = _paginate(qs, 'page', request, 20)
    utilisees = site.filter(
        produits__erp_client__isnull=True).distinct().count()
    total = site.count()
    return render(request, 'studio/admin_categories.html', {
        'categories': categories,
        'pager': pager,
        'q': q,
        'form': form,
        'edit_categorie': edit_categorie,
        'peut_gerer': peut_gerer,
        'stats': {
            'total': total,
            'utilisees': utilisees,
            'vides': max(0, total - utilisees),
        },
    })


@role_required(*ADMIN_ROLES)
def fournisseurs_list(request):
    peut_gerer = _peut_gerer(request.user)
    site = Fournisseur.objects.filter(erp_client__isnull=True)
    edit_id = request.GET.get('edit') or request.POST.get('fournisseur_id')
    edit_fournisseur = None
    if edit_id:
        edit_fournisseur = get_object_or_404(
            Fournisseur, pk=edit_id, erp_client__isnull=True)

    if request.method == 'POST':
        _exiger_gestion(request.user)
        action = request.POST.get('action', '')
        if action == 'delete':
            fournisseur = get_object_or_404(
                Fournisseur, pk=request.POST.get('fournisseur_id'),
                erp_client__isnull=True)
            if fournisseur.produit_set.exists():
                messages.error(
                    request,
                    "Impossible de supprimer « %s » : des produits "
                    "l'utilisent encore." % fournisseur.nom)
            else:
                fournisseur.delete()
                messages.success(request, "Fournisseur supprimé.")
            return redirect('admin_fournisseurs')
        if action == 'update':
            if edit_fournisseur is None:
                messages.error(request, "Fournisseur introuvable.")
                return redirect('admin_fournisseurs')
            form = FournisseurForm(request.POST, instance=edit_fournisseur)
            if form.is_valid():
                fournisseur = form.save(commit=False)
                fournisseur.erp_client = None
                fournisseur.save()
                messages.success(request, "Fournisseur mis à jour.")
                return redirect('admin_fournisseurs')
        else:
            form = FournisseurForm(request.POST)
            if form.is_valid():
                fournisseur = form.save(commit=False)
                fournisseur.erp_client = None
                fournisseur.save()
                messages.success(request, "Fournisseur créé.")
                return redirect('admin_fournisseurs')
    else:
        form = FournisseurForm(instance=edit_fournisseur)

    qs = site.annotate(
        nb_produits=Count(
            'produit', filter=Q(produit__erp_client__isnull=True))
    ).order_by('nom')
    q = (request.GET.get('q') or '').strip()
    if q:
        qs = qs.filter(
            Q(nom__icontains=q) | Q(contact__icontains=q) |
            Q(email__icontains=q) | Q(telephone__icontains=q))
    fournisseurs, pager = _paginate(qs, 'page', request, 20)
    utilisees = site.filter(
        produit__erp_client__isnull=True).distinct().count()
    total = site.count()
    return render(request, 'studio/admin_fournisseurs.html', {
        'fournisseurs': fournisseurs,
        'pager': pager,
        'q': q,
        'form': form,
        'edit_fournisseur': edit_fournisseur,
        'peut_gerer': peut_gerer,
        'stats': {
            'total': total,
            'utilises': utilisees,
            'vides': max(0, total - utilisees),
        },
    })
