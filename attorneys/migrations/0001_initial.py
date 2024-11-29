# Generated by Django 5.1.3 on 2024-11-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attorney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Primer nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('practice_area', models.CharField(max_length=100, verbose_name='Área de Práctica')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='LinkedIn')),
            ],
            options={
                'verbose_name': 'Abogado',
                'verbose_name_plural': 'Abogados',
                'ordering': ['id'],
            },
        ),
    ]
