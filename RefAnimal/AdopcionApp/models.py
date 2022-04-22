from django.db import models
from MascotasApp.models import *




class adopcion(models.Model):

    nombre = models.CharField(max_length=150, verbose_name='nombre')
    apellido = models.CharField(max_length=150, verbose_name='apellido')
    edad= models.PositiveIntegerField(default=0)
    email = models.CharField(max_length=150, verbose_name='email')
    numero= models.PositiveIntegerField(default=0)
    domicilio = models.CharField(max_length=500, verbose_name='domicilio')
    mascota = models.CharField(max_length=150, verbose_name='mascota')
    razon_para_adoptar = models.CharField(max_length=100000, verbose_name='razon_para_adoptar')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='adopcion'
        verbose_name_plural='adopciones'
        db_table='adopcion'
        ordering=['id']
