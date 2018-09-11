from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('cesma_library_database.apps.libros.views',
	url(r'^$', ListLibro.as_view(), name = 'lista_libro')
)