from django.db import models

class Estudiantes (models.Model):
	nombre_y_apellido = models.CharField(max_length=90)
	grado = models.CharField(max_length=20)
	codigo = models.CharField(max_length=10)

	def __str__(self):
		return 'Nombre: '+self.nombre_y_apellido+' - Grado: '+self.grado+' - codigo:'+self.codigo

	def __unicode__(self):
		return 'Nombre: '+self.nombre_y_apellido+' - Grado: '+self.grado+' - codigo:'+self.codigo
