# Generated by Django 4.0.3 on 2022-05-11 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdopcionApp', '0006_rename_usuario_adopcion_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adopcion',
            name='fecha_rescate',
            field=models.DateField(default=datetime.datetime.now, verbose_name='fecha_rescate'),
        ),
    ]
