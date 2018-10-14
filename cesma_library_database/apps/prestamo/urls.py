from django.contrib.auth.decorators import login_required
from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('cesma_library_database.apps.prestamo.views',
     #url(r'^$', login_required(PrestamoListLibro.as_view()), name = 'prestamo_libro'),
	url(r'^$', PrestamoListLibro.as_view(), name = 'prestamo_libro'),
	url(r'^prestar/(?P<libro_isbn>[-\w]+)/$', login_required(PrestarLibro.as_view()), name = 'prestar_libro'),
	url(r'^prestar/(?P<pk>\d+)/devolver/$', login_required(PrestarLibroDevolver), name = 'prestamo_devolver'),
)