from django.contrib import admin
from . models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['showtime', 'user', 'qr',]