# Generated by Django 5.0.1 on 2024-01-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_houses', '0006_property_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='bedrooms',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]