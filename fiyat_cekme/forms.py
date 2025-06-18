from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField

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

class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "captcha"]
