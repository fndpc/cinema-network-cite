from django.contrib import admin
from . models import Hall, Cinemas


# Register your models here.
admin.site.register(Cinemas)

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'capacity', 'cinema']