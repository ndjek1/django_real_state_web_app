# Generated by Django 5.0.1 on 2024-01-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.IntegerField(),
        ),
    ]
