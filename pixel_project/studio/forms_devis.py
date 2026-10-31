"""Formulaires de l'espace admin : devis, ventes et préfactures."""
from django import forms
from django.forms import inlineformset_factory

from .models import (
    Devis, DevisLigne, PreFacture, PreFactureLigne, Produit, Vente,
)

INPUT = {'class': 'pxadmin-input'}
SELECT = {'class': 'pxadmin-select'}
TEXTAREA = {'class': 'pxadmin-input', 'rows': 3}


class DevisForm(forms.ModelForm):
    class Meta:
        model = Devis
        fields = [
            'client_nom', 'client_email', 'client_tel', 'client_adresse',
            'sujet', 'message', 'statut', 'tva', 'notes',
        ]
        widgets = {
            'client_nom': forms.TextInput(attrs=INPUT),
            'client_email': forms.EmailInput(attrs=INPUT),
            'client_tel': forms.TextInput(attrs=INPUT),
            'client_adresse': forms.Textarea(attrs={**TEXTAREA, 'rows': 2}),
            'sujet': forms.TextInput(attrs=INPUT),
            'message': forms.Textarea(attrs={**TEXTAREA, 'rows': 4}),
            'statut': forms.Select(attrs=SELECT),
            'tva': forms.NumberInput(attrs={**INPUT, 'step': '0.01',
                                            'min': '0', 'max': '100',
                                            'data-tva': '1'}),
            'notes': forms.Textarea(attrs={**TEXTAREA, 'rows': 3}),
        }


class DevisLigneForm(forms.ModelForm):
    class Meta:
        model = DevisLigne
        fields = ['produit', 'designation', 'quantite', 'prix_unitaire', 'remise']
        widgets = {
            'produit': forms.Select(attrs={
                **SELECT, 'data-produit-select': '1'}),
            'designation': forms.TextInput(attrs={
                **INPUT, 'data-designation': '1'}),
            'quantite': forms.NumberInput(attrs={
                **INPUT, 'min': '1', 'step': '1',
                'data-quantite': '1'}),
            'prix_unitaire': forms.NumberInput(attrs={
                **INPUT, 'min': '0', 'step': '0.01',
                'data-prix': '1'}),
            'remise': forms.NumberInput(attrs={
                **INPUT, 'min': '0', 'max': '100', 'step': '0.01',
                'data-remise': '1'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produit'].queryset = Produit.objects.filter(
            actif=True, erp_client__isnull=True).order_by('nom')
        self.fields['produit'].empty_label = '— Produit du catalogue —'

    def clean(self):
        cleaned = super().clean()
        if not self.has_changed() or cleaned.get('DELETE'):
            return cleaned
        produit = cleaned.get('produit')
        designation = (cleaned.get('designation') or '').strip()
        if not produit and not designation:
            raise forms.ValidationError(
                "Choisissez un produit du catalogue ou saisissez une désignation.")
        if produit:
            if not designation:
                cleaned['designation'] = produit.nom
            if not cleaned.get('prix_unitaire'):
                cleaned['prix_unitaire'] = produit.prix_vente
        if not cleaned.get('prix_unitaire'):
            cleaned['prix_unitaire'] = 0
        if not cleaned.get('quantite'):
            cleaned['quantite'] = 1
        if cleaned.get('remise') is None:
            cleaned['remise'] = 0
        return cleaned


DevisLigneFormSet = inlineformset_factory(
    Devis, DevisLigne, form=DevisLigneForm, extra=2, can_delete=True,
    min_num=0, validate_min=False,
)


class PreFactureForm(forms.ModelForm):
    class Meta:
        model = PreFacture
        fields = [
            'client_nom', 'client_email', 'client_adresse', 'date_validite',
            'statut', 'tva', 'notes',
        ]
        widgets = {
            'client_nom': forms.TextInput(attrs=INPUT),
            'client_email': forms.EmailInput(attrs=INPUT),
            'client_adresse': forms.Textarea(attrs={**TEXTAREA, 'rows': 2}),
            'date_validite': forms.DateInput(attrs={
                **INPUT, 'type': 'date'}),
            'statut': forms.Select(attrs=SELECT),
            'tva': forms.NumberInput(attrs={**INPUT, 'step': '0.01',
                                            'min': '0', 'max': '100',
                                            'data-tva': '1'}),
            'notes': forms.Textarea(attrs={**TEXTAREA, 'rows': 3}),
        }


class PreFactureLigneForm(forms.ModelForm):
    class Meta:
        model = PreFactureLigne
        fields = ['produit', 'designation', 'quantite', 'prix_unitaire', 'remise']
        widgets = {
            'produit': forms.Select(attrs={
                **SELECT, 'data-produit-select': '1'}),
            'designation': forms.TextInput(attrs={
                **INPUT, 'data-designation': '1'}),
            'quantite': forms.NumberInput(attrs={
                **INPUT, 'min': '1', 'step': '1',
                'data-quantite': '1'}),
            'prix_unitaire': forms.NumberInput(attrs={
                **INPUT, 'min': '0', 'step': '0.01',
                'data-prix': '1'}),
            'remise': forms.NumberInput(attrs={
                **INPUT, 'min': '0', 'max': '100', 'step': '0.01',
                'data-remise': '1'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produit'].queryset = Produit.objects.filter(
            actif=True, erp_client__isnull=True).order_by('nom')
        self.fields['produit'].empty_label = '— Produit du catalogue —'

    def clean(self):
        cleaned = super().clean()
        if not self.has_changed() or cleaned.get('DELETE'):
            return cleaned
        produit = cleaned.get('produit')
        designation = (cleaned.get('designation') or '').strip()
        if not produit and not designation:
            raise forms.ValidationError(
                "Choisissez un produit du catalogue ou saisissez une désignation.")
        if produit:
            if not designation:
                cleaned['designation'] = produit.nom
            if not cleaned.get('prix_unitaire'):
                cleaned['prix_unitaire'] = produit.prix_vente
        if not cleaned.get('prix_unitaire'):
            cleaned['prix_unitaire'] = 0
        if not cleaned.get('quantite'):
            cleaned['quantite'] = 1
        if cleaned.get('remise') is None:
            cleaned['remise'] = 0
        return cleaned


PreFactureLigneFormSet = inlineformset_factory(
    PreFacture, PreFactureLigne, form=PreFactureLigneForm, extra=2,
    can_delete=True, min_num=0, validate_min=False,
)


class VenteForm(forms.Form):
    produit = forms.ModelChoiceField(
        queryset=Produit.objects.none(), label="Produit")
    quantite = forms.IntegerField(min_value=1, initial=1, label="Quantité")
    prix_unitaire = forms.DecimalField(
        max_digits=10, decimal_places=2, required=False, min_value=0,
        label="Prix unitaire (TND)")
    client_nom = forms.CharField(
        max_length=100, required=False, label="Client")
    devis = forms.ModelChoiceField(
        queryset=Devis.objects.none(), required=False, label="Devis lié")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produit'].queryset = Produit.objects.filter(
            actif=True, erp_client__isnull=True).order_by('nom')
        self.fields['produit'].widget.attrs.update(SELECT)
        for name in ('quantite', 'prix_unitaire', 'client_nom', 'devis'):
            widget = self.fields[name].widget
            widget.attrs.update(
                SELECT if name == 'devis' else INPUT)
        self.fields['devis'].queryset = Devis.objects.exclude(
            statut__in=['converti', 'refuse']).order_by('-date_creation')
