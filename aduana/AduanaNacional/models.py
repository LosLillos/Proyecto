from django.db import models

class Zona(models.Model):
	nombre = models.CharField(max_length=50)
	municipio = models.CharField(max_length=50)
	departamento = models.CharField(max_length=20)
	administracion = models.CharField(max_length=20)

class Objeto(models.Model):
	origen = models.CharField(max_length=100)
	fecha = models.DateField()
	descripcion = models.CharField(max_length=200)
	propietario = models.CharField(max_length=50)
	foto = models.ImageField(upload_to='AduanaNacional/objetos/')
	zona = models.CharField(max_length=50)