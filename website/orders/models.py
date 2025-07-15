from django.db import models
from showtimes.models import Showtimes
from users.models import CustomUser
# from django.contrib.auth.models import User
# Create your models here.
class Orders(models.Model):
    showtime = models.ForeignKey(Showtimes, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    qr = models.ImageField(verbose_name="QR код", upload_to="orders_qr/", blank=True)

    class Meta:
        verbose_name_plural = 'Закакзы'

    