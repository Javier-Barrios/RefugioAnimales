# Generated by Django 4.0.3 on 2022-04-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MascotasApp', '0003_alter_mascota_table_delete_imagenmascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='enfermedad',
            field=models.CharField(max_length=150, verbose_name='enfermedad'),
        ),
    ]
