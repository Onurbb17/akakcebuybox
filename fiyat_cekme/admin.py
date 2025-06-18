from django.contrib import admin
from .models import UserProfile, Kategori, Eslesme

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_start', 'license_end', 'days_left')
    search_fields = ('user__username', 'user__email')
    list_filter = ('license_start',)

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('isim', 'user')
    search_fields = ('isim', 'user__username')
    list_filter = ('user',)

@admin.register(Eslesme)
class EslesmeAdmin(admin.ModelAdmin):
    list_display = ('kategori', 'akakce_link', 'site_link', 'eklenme_zamani')
    search_fields = ('akakce_link', 'site_link', 'kategori__isim')
    list_filter = ('kategori',)