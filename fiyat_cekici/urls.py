"""
URL configuration for fiyat_cekici project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fiyat_cekme.views import home_view, register, login_view, logout_view, fiyat_cek, profile,settings_view
from django.contrib.auth import views as auth_views
from fiyat_cekme.views import bildirim_merkezi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('register/', register, name='register'),
    path('bildirimler/', bildirim_merkezi, name='bildirimler'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('fiyat-cek/', fiyat_cek, name='fiyat_cek'),
    path('ayarlar/', settings_view, name='settings'),
    path('profile/', profile, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]