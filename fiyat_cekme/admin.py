from django.contrib import admin
from .models import UserProfile, Kategori, Eslesme

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "license_start", "license_end", "days_left")
    search_fields = ("user__username", "user__email")
    list_filter = ("license_start",)
    ordering = ("user",)  # <-- Burayı var olan bir field ile değiştir!
    readonly_fields = ("days_left",)

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ("isim", "user")
    search_fields = ("isim", "user__username")
    list_filter = ("user",)
    ordering = ("isim",)

@admin.register(Eslesme)
class EslesmeAdmin(admin.ModelAdmin):
    list_display = ("kategori", "akakce_link", "site_link", "eklenme_zamani")
    search_fields = ("akakce_link", "site_link", "kategori__isim")
    list_filter = ("kategori",)
    ordering = ("-eklenme_zamani",)
    date_hierarchy = "eklenme_zamani"
    actions = ["kopyala_linkleri"]

    def kopyala_linkleri(self, request, queryset):
        self.message_user(request, f"{queryset.count()} eşleşmenin linkleri kopyalandı!")
    kopyala_linkleri.short_description = "Seçilen eşleşmelerin linklerini kopyala"