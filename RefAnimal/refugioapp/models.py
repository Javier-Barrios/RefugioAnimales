from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Type(models.Model):

    nombre = models.CharField(max_length=150, verbose_name='nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        db_table='type'
        ordering=['id']

class empleado(models.Model):

    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=150, verbose_name='nombre')
    email = models.CharField(max_length=150, verbose_name='email')
    numero= models.PositiveIntegerField(default=0)
    dpi = models.CharField(max_length=10, unique=True, verbose_name='dpi')
    fecha_registro = models.DateField(default=datetime.now, verbose_name='fecha_registro')
    fecha_creacion =  models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    edad= models.PositiveIntegerField(default=0)
    salario= models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    foto= models.ImageField(upload_to='foto/%Y/%M/%D', null=True, blank=True)

    def __str__(self):
        return self.nombre

 
    @property
    def get_photo_url(self):
        if self.foto  and hasattr(self.foto , 'url'):
            return self.foto.url
        else:
            return "/static/img/not_available.png"

    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table='empleado'
        ordering=['id']







