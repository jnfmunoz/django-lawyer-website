# Generated by Django 5.1.3 on 2024-12-15 04:42

import fontawesome_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Descripción')),
                ('icon', fontawesome_5.fields.IconField(blank=True, help_text='Clase de Font Awesome', max_length=60, verbose_name='Icono')),
                ('link', models.URLField(blank=True, help_text='URL Red Social', null=True, verbose_name='Enlace')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
                'ordering': ['id'],
            },
        ),
    ]
