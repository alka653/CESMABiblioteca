from cesma_library_database.apps.estudiantes.models import Estudiantes
from cesma_library_database.apps.libros.models import Libros
from django.db import models

class Prestamos(models.Model):
	estudiante= models.ForeignKey(Estudiantes)
	libro=models.ForeignKey(Libros)
	fecha_prestamo=models.DateTimeField(auto_now=True)
	fecha_devolucion=models.DateTimeField(blank = True, null = True)