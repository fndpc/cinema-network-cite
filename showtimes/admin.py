from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Showtimes)
class ShowtimesAdmin(admin.ModelAdmin):
    list_display = ['id', 'cinema', 'hall', 'movie', 'time', 'price']