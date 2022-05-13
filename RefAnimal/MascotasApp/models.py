from operator import mod
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class sexo(models.Model):

    nombre = models.CharField(max_length=20, verbose_name='nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        db_table='sexo'
        ordering=['id']


class Type2(models.Model):

    nombre = models.CharField(max_length=20, verbose_name='nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        db_table='type2'
        ordering=['id']



class adoptado(models.Model):

    nombre = models.CharField(max_length=20, verbose_name='nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        db_table='adoptado'
        ordering=['id']



class mascota(models.Model):

    Type2 = models.ForeignKey(Type2, on_delete=models.CASCADE)
    adoptado = models.ForeignKey(adoptado, on_delete=models.CASCADE)
    
    nombre = models.CharField(max_length=150, unique=True, verbose_name='nombre')
    sexo = models.ForeignKey(sexo, on_delete=models.CASCADE)
    edad= models.PositiveIntegerField(default=0)
    fecha_rescate = models.DateField(default=datetime.now, verbose_name='fecha_rescate')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    foto= models.ImageField(upload_to='fotomascota/%Y/%M/%D', null=True, blank=True)
    foto2= models.ImageField(upload_to='fotomascota/%Y/%M/%D', null=True, blank=True)
    foto3= models.ImageField(upload_to='fotomascota/%Y/%M/%D', null=True, blank=True)
    vacunas = models.CharField(max_length=20, verbose_name='vacuna')
    raza = models.CharField(max_length=20, verbose_name='raza')
    enfermedad = models.CharField(max_length=150, verbose_name='enfermedad')
    alimentacion = models.CharField(max_length=150, verbose_name='alimentacion')
    descripcion = models.CharField(max_length=150, unique=True, verbose_name='descripcion')
    
    


    def __str__(self):
        return self.nombre

 
    @property
    def get_photo_url(self):
        if self.foto  and hasattr(self.foto , 'url'):
            return self.foto.url
        else:
            return "/static/img/not_available.png"

    def get_photo2_url(self):
        if self.foto2  and hasattr(self.foto2 , 'url'):
            return self.foto2.url
        else:
            return "/static/img/not_available.png"

    def get_photo3_url(self):
        if self.foto3  and hasattr(self.foto3 , 'url'):
            return self.foto3.url
        else:
            return "/static/img/not_available.png"

    class Meta:
        verbose_name='mascota'
        verbose_name_plural='mascotas'
        db_table='mascota'
        ordering=['id']

#class ImagenMascota(models.Model):
#    imagen = models.ImageField(upload_to='fotomascota/%Y/%M/%D')
#    animal = models.ForeignKey(mascota, on_delete=models.CASCADE)






