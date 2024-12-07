# Generated by Django 5.1.3 on 2024-12-07 17:47

import fontawesome_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_alter_practicearea_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicearea',
            name='icon',
            field=fontawesome_5.fields.IconField(blank=True, help_text='Clase de Font Awesome', max_length=60, verbose_name='icono'),
        ),
    ]
