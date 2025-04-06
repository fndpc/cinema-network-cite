from django.db import models
from showtimes.models import Showtimes
from django.contrib.auth.models import User

# Create your models here.
class Orders(models.Model):
    showtime = models.ForeignKey(Showtimes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Orders'