# Generated by Django 5.2 on 2025-04-06 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movies_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name_plural': 'Movies'},
        ),
    ]
