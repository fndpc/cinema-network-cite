from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid



class CustomUser(AbstractUser):
    telegram_chat_id = models.CharField(max_length=20, verbose_name="Чат ID", null=True, unique=True, blank=True)
    token = models.CharField(max_length=100, verbose_name="Токен", unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = str(uuid.uuid4())
        super().save(*args, **kwargs)