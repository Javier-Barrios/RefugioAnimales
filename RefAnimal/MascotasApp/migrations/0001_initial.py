# Generated by Django 4.0.3 on 2022-04-17 00:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'sexo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Type2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'type2',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mascota', models.CharField(max_length=50000, unique=True, verbose_name='id_mascota')),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='nombre')),
                ('edad', models.PositiveIntegerField(default=0)),
                ('fecha_rescate', models.DateField(default=datetime.datetime.now, verbose_name='fecha_rescate')),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotomascota/%Y/%M/%D')),
                ('foto2', models.ImageField(blank=True, null=True, upload_to='fotomascota/%Y/%M/%D')),
                ('foto3', models.ImageField(blank=True, null=True, upload_to='fotomascota/%Y/%M/%D')),
                ('enfermedad', models.CharField(max_length=150, unique=True, verbose_name='enfermedad')),
                ('Type2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MascotasApp.type2')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MascotasApp.sexo')),
            ],
            options={
                'verbose_name': 'mascota',
                'verbose_name_plural': 'mascotas',
                'db_table': 'mascotas',
                'ordering': ['id'],
            },
        ),
    ]