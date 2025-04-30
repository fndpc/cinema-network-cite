from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.DecimalField(decimal_places=1, max_digits=3, validators=[MaxValueValidator(10.0)])
    description = models.TextField()
    duration = models.CharField(max_length=8)
    filmmaker = models.CharField(max_length=100)
    actors = models.CharField(max_length=255)
    country = models.CharField(max_length=30)
    image = models.ImageField(upload_to='movies_images/')
    slug = models.SlugField(unique=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"movie_slug": self.slug})
    

    class Meta:
        verbose_name_plural = 'Фильмы'