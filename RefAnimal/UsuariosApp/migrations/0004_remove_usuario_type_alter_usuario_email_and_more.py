# Generated by Django 4.0.3 on 2022-04-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsuariosApp', '0003_alter_usuario_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='type',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
