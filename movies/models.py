from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.DecimalField(decimal_places=1, max_digits=3, validators=[MaxValueValidator(5.0)])
    description = models.TextField()
    duration = models.CharField(max_length=8)
    filmmaker = models.CharField(max_length=100)
    actors = models.CharField(max_length=255)
    country = models.CharField(max_length=30)
    image = models.ImageField(upload_to='movies_images/')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Movies'