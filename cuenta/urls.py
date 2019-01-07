"""
    Definición de las URI's para la aplicación globales
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetConfirmView, PasswordResetDoneView,
    PasswordResetView)
from django.urls import path, reverse_lazy

# Librerias en carpetas locales
from .views import (activar, avatar, cambio_clave, perfil, registro)

app_name = 'cuenta'

urlpatterns = [
    # ========================= Ristro de Usuarios ========================= #
    path('registro', registro, name='registro'),
    path('activar/<uidb64>/<token>', activar, name='activar'),

    # =========================== Login - Logout =========================== #
    path(
        'login/',
        LoginView.as_view(
            template_name='perfil_login.html',
            redirect_field_name='next',
        ),
        name='login'
    ),
    path('salir', LogoutView.as_view(next_page='cuenta:login'), name='logout'),

    # =========================== Cambio de Clave ========================== #
    path('perfil', login_required(perfil), name='perfil'),
    path('cambiar-clave', login_required(cambio_clave), name='cambiar-clave'),

    # =========================== Reinicio Clave =========================== #
    path(
        'reiniciar-clave-enviado',
        PasswordResetDoneView.as_view(
            template_name='reinicio_enviado.html'
        ),
        name='reiniciar-enviado'
    ),
    path(
        'reiniciar-clave',
        PasswordResetView.as_view(
            template_name='reinicio_clave.html',
            email_template_name='reinicio_correo.html',
            success_url=reverse_lazy('cuenta:reiniciar-enviado')
        ),
        name='reiniciar-clave'
    ),
    path(
        'nueva-clave/<uidb64>/<token>',
        PasswordResetConfirmView.as_view(
            template_name='reinicio_nueva_clave.html',
            success_url=reverse_lazy('cuenta:perfil'),
            post_reset_login=True,
        ),
        name='nueva-clave'
    ),
    path(
        'avatar',
        login_required(avatar),
        name='avatar'),
]
