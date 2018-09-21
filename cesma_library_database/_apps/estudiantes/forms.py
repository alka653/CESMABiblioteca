from django import forms

from models import Estudiantes

class EstudiantesForm(forms.ModelForm):

	class Meta:
		model = Estudiantes 

		fields = [
		'nombre_y_apellido', 
		'grado',
		'código',
		]

		labels = [
		'nombre_y_apellido': 'Nombre_y_Apellido',
		'grado': 'Grado',
		'código': 'Código',
		]
