# -*- coding: utf-8 -*-
"""
Vistas de la aplicación globales
"""

# Librerias Django
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# Librerias de terceros
import requests

# Librerias en carpetas locales
from .forms import AvatarForm, PerfilForm, PersonaCreationForm
from .models import Persona
from .tokens import account_activation_token


def registro(request):
    """Función de registro con reCAPTCHA de ggogle y envio de correo de
    confirmación de registro"""

    contexto = {}
    if request.method == 'POST':
        contexto['form'] = PersonaCreationForm(request.POST)
        if contexto['form'].is_valid():

            # === Begin reCAPTCHA validation ===#
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = requests.get(url, params=values, verify=True)
            result = data.json()
            # ===End reCAPTCHA validation ===#
            if result['success']:

                user = contexto['form'].save(commit=False)
                user.save()

                current_site = get_current_site(request)
                subject = 'Activa tú cuenta en el {{ settings.NOMBRE_APP }}'
                contexto = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
                    'token': account_activation_token.make_token(user),
                }
                message = render_to_string('registro_correo.html', contexto)
                user.email_user(subject, message)

                return render(request, 'registro_enviado.html', contexto)
            else:
                contexto['reCAPTCHA_error'] = 'reCAPTCHA invalido. Por favor \
                    vuelva a intentar su registro.'
    else:
        contexto['form'] = PersonaCreationForm()

    return render(request, 'registro_usuario.html', contexto)


def activar(request, uidb64, token):
    """Esta función activa a la persona cuando confirma el link enviado desde
    su correo
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Persona.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Persona.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('cuenta:perfil')

    return render(request, 'registro_invalido.html')


def perfil(request):
    """Función del perfil del usuraio
    """
    contexto = {}  # Diccionario de contexto para la plantilla

    usuario = Persona.objects.get(pk=request.user.pk)

    if request.method == 'POST':
        contexto['form'] = PerfilForm(request.POST, request.FILES, instance=usuario)
        if contexto['form'].is_valid():
            contexto['form'].save()
            messages.success(request, '¡La actualización de los datos de su perfil se proceso exitosamente!')
    else:
        # Para formatear la fecha en el formulario
        if usuario.fecha_nacimiento is not None:
            usuario.fecha_nacimiento = usuario.fecha_nacimiento.strftime('%d/%m/%Y')

        contexto['form'] = PerfilForm(instance=usuario)
        contexto['form_avatar'] = AvatarForm(instance=usuario)
    return render(request, 'perfil_usuario.html', contexto)


def cambio_clave(request):
    """Esta función es para el cambio de clave del usuario
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante!
            messages.success(request, '¡Su cambio de clave se proceso exitosamente!')
            return redirect('cuenta:perfil')
        else:
            messages.error(request, 'Su intento de cambio de clave tiene \
                errores. Por favor corrijalos.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'perfil_cambio_clave.html', {'form': form})


def avatar(request):
    """Función para actualizar el avatar
    """

    usuario = Persona.objects.get(pk=request.user.pk)

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()

    return redirect('cuenta:perfil')


# ========================================================================== #
def error_404(request, exception):
    """Gestion de errores html 404
    """

    data = {}
    return render(request, '404.html', data)


# ========================================================================== #
def error_500(request):
    """Gestion de errores html 500
    """

    data = {}
    return render(request, '500.html', data)
