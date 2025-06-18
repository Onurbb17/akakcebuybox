from django.apps import AppConfig

class FiyatCekmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fiyat_cekme'

    def ready(self):
        import fiyat_cekme.signals