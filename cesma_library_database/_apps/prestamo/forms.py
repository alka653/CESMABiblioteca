from cesma_library_database.apps.estudiantes.models import Estudiantes
from cesma_library_database.apps.libros.models import Libros
from django.forms import *
from django import forms
from .models import *

class SelectAlumnoForm(forms.Form):
	estudiante = forms.ModelChoiceField(Estudiantes.objects.all(), label = 'Estudiante', widget = forms.Select(attrs = {'class': 'form-control', 'id': 'id_estudiante', 'required': False}))

	def prestamo(self, libro):
		prestamo = Prestamos(
			libro = Libros.objects.filter(ISBN = libro).first(),
			estudiante = self.cleaned_data['estudiante']
		)
		prestamo.save()