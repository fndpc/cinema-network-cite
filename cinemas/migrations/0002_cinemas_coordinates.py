# Generated by Django 5.2 on 2025-04-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemas',
            name='coordinates',
            field=models.JSONField(default=[0, 0]),
            preserve_default=False,
        ),
    ]
