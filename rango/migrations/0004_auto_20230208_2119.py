# Generated by Django 2.2.28 on 2023-02-08 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20230208_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
    ]
