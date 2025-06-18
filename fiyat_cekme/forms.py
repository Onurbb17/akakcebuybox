from django import forms
from .models import Kategori, Eslesme

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['isim']

class EslesmeForm(forms.ModelForm):
    class Meta:
        model = Eslesme
        fields = ['akakce_link', 'site_link']
        widgets = {
            'akakce_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Akakçe ürün linki'}),
            'site_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Sitenizdeki ürün linki'}),
        }