from django.db import models
from django.core.validators import MaxValueValidator




class Hall(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    cinema = models.ForeignKey('Cinemas', related_name='halls', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
class Cinemas(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    rating = models.DecimalField(decimal_places=1, max_digits=3, validators=[MaxValueValidator(5.0)])
    description = models.TextField()
    image = models.ImageField(upload_to='cinema_images/')

    

    def __str__(self):
        return self.name