from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Kategori, Eslesme
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

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
    email = forms.EmailField(required=True, label="E-posta")
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user