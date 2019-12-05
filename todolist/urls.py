# Librerias Django
# Django Libraries
from django.conf import settings
from django.conf.urls import handler404, handler500, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.views.static import serve

# Thirdparty Libraries
from apps.usercustom.views import ActivateLanguageView

urlpatterns = [
    path('', include('apps.usercustom.urls')),
    path('translate/', include('rosetta.urls')),
    path('task/', include('apps.task.urls')),
    path('admin/', admin.site.urls),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<path:path>', serve,
         {'document_root': settings.STATIC_ROOT, }),
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path(
        '<language_code>/language/activate/',
        ActivateLanguageView.as_view(),
        name='activate_language'
    ),
)

handler404 = 'apps.usercustom.views.error_404'
handler500 = 'apps.usercustom.views.error_500'
