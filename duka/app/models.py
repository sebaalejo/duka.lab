from django.db import models

# Create your models here.


class Producto(models.Model):
    tipo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()

class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mensaje=models.CharField(max_length=300)

class Producto_Terceros(models.Model):
    tipo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()