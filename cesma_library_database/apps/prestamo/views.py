from cesma_library_database.apps.libros.models import Libros
from django.views.generic import ListView, FormView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
import datetime

template_dir = 'prestamo/'

class PrestamoListLibro(ListView):
	model = Prestamos
	template_name = template_dir+'list_prestamo.html'

class PrestarLibro(FormView):
	form_class = SelectAlumnoForm
	template_name = template_dir+'prestar_libro.html'

	def get_context_data(self, **kwargs):
		context = super(PrestarLibro, self).get_context_data(**kwargs)
		context['title'] = 'Bienvenido'
		context['libro'] = Libros.objects.filter(ISBN = self.kwargs['libro_isbn']).first()
		return context

	def form_valid(self, form):
		form.prestamo(self.kwargs['libro_isbn'])
		return super(PrestarLibro, self).form_valid(form)

	def get_success_url(self):
		return reverse('prestamo_libro')

def PrestarLibroDevolver(request, pk):
	Prestamos.objects.filter(pk = pk).update(fecha_devolucion = datetime.datetime.now())
	return HttpResponseRedirect(reverse('prestamo_libro'))