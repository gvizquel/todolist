# Librerias Django
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('cuenta/', include('cuenta.urls')),
    path('tarea/', include('tareas.urls')),
    path('admin/', admin.site.urls),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT, }),
]

handler404 = 'cuenta.views.error_404'
handler500 = 'cuenta.views.error_500'