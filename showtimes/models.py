from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from cinemas.models import Cinemas, Hall
from movies.models import Movies


class Showtimes(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE, verbose_name='Кинотеатр')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name='Зал')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name='Фильм')
    time = models.DateTimeField(verbose_name='Время')
    price = models.IntegerField(verbose_name='Цена')

    def clean(self):
        if self.time <= timezone.now():
            raise ValidationError('Время должно быть больше текущего времени.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.movie.title} в {self.cinema.name} в {self.time.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name_plural = 'Расписание'

    