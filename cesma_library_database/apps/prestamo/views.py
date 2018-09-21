from cesma_library_database.apps.libros.models import Libros
from django.views.generic import ListView, FormView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from .models import *
from .forms import *
import datetime
from cesma_library_database.apps.libros.forms import LibroSearchForm

template_dir = 'prestamo/'

class PrestamoListLibro (FormMixin, ListView):
	model = Prestamos
	paginate_by = 15
	form_class = LibroSearchForm
	template_name = template_dir+'list_prestamo.html'

	def get_form_kwargs(self):
		kwargs = super(PrestamoListLibro, self).get_form_kwargs()
		kwargs['buscar_por'] = self.request.GET.get('buscar_por')
		return kwargs

	def get_queryset(self):
		queryset = super(PrestamoListLibro, self).get_queryset()
		if self.request.GET.get('buscar_por') is not None:
			find_by = self.request.GET.get('buscar_por')
			queryset = queryset.filter(Q(estudiante__nombre_y_apellido__icontains = find_by) | Q(libro__nombre__icontains = find_by) | Q(libro__editorial__icontains = find_by) | Q(libro__autor__icontains = find_by) | Q(libro__ISBN__icontains = find_by))
		return queryset

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