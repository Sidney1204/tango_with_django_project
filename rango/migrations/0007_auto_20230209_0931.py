# Generated by Django 2.2.28 on 2023-02-09 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
