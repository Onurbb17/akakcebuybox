from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- Kullanıcı Lisans Modeli ---
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_start = models.DateField(auto_now_add=True)
    license_months = models.IntegerField(default=1)

    @property
    def license_end(self):
        return self.license_start + timedelta(days=30 * self.license_months)

    @property
    def days_left(self):
        return (self.license_end - date.today()).days

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# --- Kategori ve Eşleşme Modelleri ---

class Kategori(models.Model):
    isim = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kategoriler')

    def __str__(self):
        return self.isim

class Eslesme(models.Model):
    kategori = models.ForeignKey(Kategori, related_name='eslesmeler', on_delete=models.CASCADE)
    akakce_link = models.URLField("Akakçe Linki")
    site_link = models.URLField("Sitenizdeki Link", blank=True, null=True)
    eklenme_zamani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kategori.isim} - {self.akakce_link[:40]}..."

# --- Bildirim Modeli ---
class Bildirim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bildirimler')
    mesaj = models.CharField(max_length=255)
    olusturma_zamani = models.DateTimeField(auto_now_add=True)
    okundu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}: {self.mesaj[:40]}"