"""Formulaires de gestion du catalogue du site.

Les produits, catégories et fournisseurs sont ceux du site (sans entreprise
GestiActiv). Les listes déroulantes sont donc filtrées sur
``erp_client__isnull=True`` pour ne jamais exposer les référentiels d'un
tenant.
"""
from django import forms

from .models import Categorie, Fournisseur, MouvementStock, Produit

INPUT = {'class': 'pxadmin-input'}
SELECT = {'class': 'pxadmin-select'}
TEXTAREA = {'class': 'pxadmin-input', 'rows': 3}
CHECKBOX = {'class': 'pxadmin-checkbox'}


class ProduitForm(forms.ModelForm):
    stock_initial = forms.IntegerField(
        label="Stock initial", min_value=0, max_value=1000000,
        initial=0, required=False,
        widget=forms.NumberInput(attrs={
            **INPUT, 'min': '0', 'step': '1'}))

    class Meta:
        model = Produit
        fields = [
            'nom', 'categorie', 'fournisseur', 'prix_achat', 'prix_vente',
            'stock_minimum', 'code_barre', 'est_service', 'actif',
        ]
        widgets = {
            'nom': forms.TextInput(attrs=INPUT),
            'categorie': forms.Select(attrs=SELECT),
            'fournisseur': forms.Select(attrs=SELECT),
            'prix_achat': forms.NumberInput(attrs={
                **INPUT, 'min': '0', 'step': '0.01'}),
            'prix_vente': forms.NumberInput(attrs={
                **INPUT, 'min': '0', 'step': '0.01'}),
            'stock_minimum': forms.NumberInput(attrs={
                **INPUT, 'min': '0', 'step': '1'}),
            'est_service': forms.CheckboxInput(attrs=CHECKBOX),
            'code_barre': forms.TextInput(attrs=INPUT),
            'actif': forms.CheckboxInput(attrs=CHECKBOX),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categorie'].required = False
        self.fields['fournisseur'].required = False
        self.fields['categorie'].queryset = Categorie.objects.filter(
            erp_client__isnull=True).order_by('nom')
        self.fields['fournisseur'].queryset = Fournisseur.objects.filter(
            erp_client__isnull=True).order_by('nom')
        if not self.instance.pk:
            self.fields['actif'].initial = True
            self.fields['stock_minimum'].initial = 5

    def clean_nom(self):
        nom = (self.cleaned_data.get('nom') or '').strip()
        if not nom:
            raise forms.ValidationError("Le nom du produit est obligatoire.")
        return nom

    def clean_code_barre(self):
        code = (self.cleaned_data.get('code_barre') or '').strip()
        if code:
            qs = Produit.objects.filter(
                erp_client__isnull=True, code_barre__iexact=code)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError(
                    "Ce code-barres est déjà utilisé par un autre produit.")
        return code

    def clean_prix_achat(self):
        valeur = self.cleaned_data.get('prix_achat')
        if valeur is not None and valeur < 0:
            raise forms.ValidationError("Le prix d'achat ne peut pas être négatif.")
        return valeur

    def clean_prix_vente(self):
        valeur = self.cleaned_data.get('prix_vente')
        if valeur is not None and valeur < 0:
            raise forms.ValidationError("Le prix de vente ne peut pas être négatif.")
        return valeur

    def clean_stock_minimum(self):
        valeur = self.cleaned_data.get('stock_minimum')
        if valeur is not None and valeur < 0:
            raise forms.ValidationError("Le stock minimum ne peut pas être négatif.")
        return valeur


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs=INPUT),
            'description': forms.Textarea(attrs={**TEXTAREA, 'rows': 3}),
        }

    def clean_nom(self):
        nom = (self.cleaned_data.get('nom') or '').strip()
        if not nom:
            raise forms.ValidationError("Le nom est obligatoire.")
        qs = Categorie.objects.filter(
            erp_client__isnull=True, nom__iexact=nom)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                "Une catégorie porte déjà ce nom.")
        return nom


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'contact', 'telephone', 'email', 'adresse']
        widgets = {
            'nom': forms.TextInput(attrs=INPUT),
            'contact': forms.TextInput(attrs=INPUT),
            'telephone': forms.TextInput(attrs=INPUT),
            'email': forms.EmailInput(attrs=INPUT),
            'adresse': forms.Textarea(attrs={**TEXTAREA, 'rows': 3}),
        }

    def clean_nom(self):
        nom = (self.cleaned_data.get('nom') or '').strip()
        if not nom:
            raise forms.ValidationError("Le nom est obligatoire.")
        qs = Fournisseur.objects.filter(
            erp_client__isnull=True, nom__iexact=nom)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                "Un fournisseur porte déjà ce nom.")
        return nom


class MouvementStockForm(forms.Form):
    type = forms.ChoiceField(
        choices=MouvementStock.TYPES, label="Type de mouvement",
        widget=forms.Select(attrs=SELECT))
    quantite = forms.IntegerField(
        min_value=0, max_value=1000000, label="Quantité",
        help_text="Pour un ajustement, indiquez le nouveau stock.",
        widget=forms.NumberInput(attrs={
            **INPUT, 'min': '0', 'step': '1'}))
    reference = forms.CharField(
        required=False, max_length=100, label="Référence du bon",
        widget=forms.TextInput(attrs=INPUT))
    notes = forms.CharField(
        required=False, label="Notes",
        widget=forms.Textarea(attrs={**TEXTAREA, 'rows': 2}))

    def clean(self):
        cleaned = super().clean()
        type_mouvement = cleaned.get('type')
        quantite = cleaned.get('quantite')
        if type_mouvement and type_mouvement != 'ajustement' and not quantite:
            self.add_error(
                'quantite', "La quantité doit être supérieure à zéro.")
        return cleaned
