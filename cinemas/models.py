from django.db import models
from django.core.validators import MaxValueValidator




class Hall(models.Model):
    name = models.CharField(max_length=255, verbose_name='Номер зала')
    capacity = models.IntegerField(verbose_name = 'Вместимость')
    cinema = models.ForeignKey('Cinemas', related_name='halls',
    on_delete=models.CASCADE, verbose_name='Кинотеатр')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Залы'

# Create your models here.
class Cinemas(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название кинотеатра')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    rating = models.DecimalField(decimal_places=1, max_digits=3,
    verbose_name='Рейтинг', validators=[MaxValueValidator(5.0)])
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='cinema_images/', verbose_name='Изображение кинотеатра')

    

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Кинотеатры'