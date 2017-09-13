from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cliente(models.Model):
#	image = models.FileField(null=True, blank=True)
	nombres = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	cedula_identidad = models.CharField(max_length=13)
	direccion = models.CharField(max_length=500)
	telefono = models.CharField(max_length=14)
	estado = models.BooleanField()


	def __str__(self):
		return self.nombres


class Producto(models.Model):

	 nombre =models.CharField(max_length= 200)
	 precio =models.CharField(max_length=30)
	 medidas =models.CharField(max_length=30)
	 tipo_producto =models.CharField(max_length=30)

	 

	 def __str__(self):
		return self.nombre


class Perfil(User):
	edad= models.IntegerField()

	def __str__(seft):
		return seft.edad


