# Generated by Django 4.0.3 on 2022-04-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsuariosApp', '0002_alter_usuario_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
    ]
