# -*- encoding: utf-8 -*-
from cesma_library_database.apps.prestamo.models import *
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date
from django import template

register = template.Library()

@register.simple_tag
def show_prestamo():
	now = datetime.now() + timedelta(days = 12)
	return Prestamos.objects.filter(fecha_devolucion__isnull = True, fecha_prestamo__lte = now).count()

@register.simple_tag
def diff_date(date):
	diff = (date.now().date() - datetime.strptime(date.strftime("%Y/%m/%d %I:%M:%S %p"), '%Y/%m/%d %I:%M:%S %p').date()).days
	return 'Tiene '+str(diff)+' días de retraso' if diff > 0 else ''