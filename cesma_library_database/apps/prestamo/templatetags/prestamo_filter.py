# -*- encoding: utf-8 -*-
from cesma_library_database.apps.prestamo.models import *
from datetime import datetime,timedelta
from django import template

register = template.Library()

@register.simple_tag
def show_prestamo():
	now = datetime.now() + timedelta(days = 12)
	return Prestamos.objects.filter(fecha_devolucion__isnull = True, fecha_prestamo__gte = now).count()