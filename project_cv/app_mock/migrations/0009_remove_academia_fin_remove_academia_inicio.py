# Generated by Django 4.2 on 2025-02-23 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mock', '0008_academia_carrera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academia',
            name='fin',
        ),
        migrations.RemoveField(
            model_name='academia',
            name='inicio',
        ),
    ]
