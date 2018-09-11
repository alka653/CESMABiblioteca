from django.db import models

class Libros(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=10)
	editorial = models.CharField(max_length=60)
	autor = models.CharField(max_length=90)
	ISBN = models.CharField(max_length=20)
	portada = models.ImageField(upload_to = 'img/libros/', blank = True, null = True)

	def __str__(self):
		return 'Nombre: '+self.nombre+' - Codigo: '+self.codigo+' - Editorial:'+self.editorial+' - Autor: '+self.autor+' - ISBN: '+self.ISBN

	def __unicode__(self):
		return 'Nombre: '+self.nombre+' - Codigo: '+self.codigo+' - Editorial:'+self.editorial+' - Autor: '+self.autor+' - ISBN: '+self.ISBN

	def get_portada(self):
		if self.portada and hasattr(self.portada, 'url'):
			return self.portada.url
		else:
			return '/static/img/libros/none.png'