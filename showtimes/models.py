from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from cinemas.models import Cinemas, Hall
from movies.models import Movies


class Showtimes(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    time = models.DateTimeField()
    price = models.IntegerField()

    def clean(self):
        if self.time <= timezone.now():
            raise ValidationError('Время должно быть больше текущего времени.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

