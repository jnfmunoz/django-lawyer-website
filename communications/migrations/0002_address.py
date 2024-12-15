# Generated by Django 5.1.3 on 2024-12-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200, verbose_name='Calle')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('commune', models.CharField(max_length=200, verbose_name='Comuna')),
                ('country', models.CharField(max_length=200, verbose_name='País')),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Dirección',
                'ordering': ['id'],
            },
        ),
    ]
