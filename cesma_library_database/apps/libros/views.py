from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q
from .models import *
from .forms import *

template_dir = 'libro/'

class ListLibro(FormMixin, ListView):
	model = Libros
	paginate_by = 15
	form_class = LibroSearchForm
	template_name = template_dir+'list_libro.html'

	def get_context_data(self, **kwargs):
		context = super(ListLibro, self).get_context_data(**kwargs)
		context['title'] = 'Lista de libros'
		return context

	def get_form_kwargs(self):
		kwargs = super(ListLibro, self).get_form_kwargs()
		kwargs['buscar_por'] = self.request.GET.get('buscar_por')
		return kwargs

	def get_queryset(self):
		queryset = super(ListLibro, self).get_queryset()
		if self.request.GET.get('buscar_por') is not None:
			find_by = self.request.GET.get('buscar_por')
			queryset = queryset.filter(Q(nombre__icontains = find_by) | Q(codigo__icontains = find_by) | Q(editorial__icontains = find_by) | Q(autor__icontains = find_by) | Q(ISBN__icontains = find_by))
		return queryset