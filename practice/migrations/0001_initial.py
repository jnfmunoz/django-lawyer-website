# Generated by Django 5.1.3 on 2024-11-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.CharField(max_length=200, verbose_name='Descripción')),
                ('icon', models.CharField(help_text='Clase de Font Awesome', max_length=255, verbose_name='icono')),
            ],
            options={
                'verbose_name': 'Área de Práctica',
                'verbose_name_plural': 'Área de Prácticas',
                'ordering': ['id'],
            },
        ),
    ]
