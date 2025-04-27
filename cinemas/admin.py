from django.contrib import admin
from . models import Hall, Cinemas


# Register your models here.


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'capacity', 'cinema']

@admin.register(Cinemas)
class CinemasAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'rating']