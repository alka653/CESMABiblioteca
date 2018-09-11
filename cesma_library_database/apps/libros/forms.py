from django.forms import *
from django import forms
from .models import *

class LibroSearchForm(forms.Form):
	buscar_por = forms.CharField(label = 'Buscar por:', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Digite palabra a buscar'}))

	def __init__(self, *args, **kwargs):
		buscar_por = kwargs.pop('buscar_por', None)
		super(LibroSearchForm, self).__init__(*args, **kwargs)
		if buscar_por: self.fields['buscar_por'].initial = buscar_por