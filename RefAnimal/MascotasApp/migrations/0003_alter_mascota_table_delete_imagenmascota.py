# Generated by Django 4.0.3 on 2022-04-17 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MascotasApp', '0002_imagenmascota'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='mascota',
            table='mascota',
        ),
        migrations.DeleteModel(
            name='ImagenMascota',
        ),
    ]
