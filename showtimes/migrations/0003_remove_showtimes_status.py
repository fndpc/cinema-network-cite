# Generated by Django 5.2 on 2025-04-18 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showtimes', '0002_showtimes_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtimes',
            name='status',
        ),
    ]
