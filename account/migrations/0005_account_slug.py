# Generated by Django 4.2 on 2024-10-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_profileimage_background_image_backgroundimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
