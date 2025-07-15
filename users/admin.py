from django.contrib import admin
from . models import CustomUser

@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'first_name', 'token', 'telegram_chat_id', ]