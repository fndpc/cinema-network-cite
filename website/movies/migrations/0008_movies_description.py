# Generated by Django 5.2 on 2025-07-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_remove_movies_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='description',
            field=models.TextField(default='desc'),
            preserve_default=False,
        ),
    ]
