# -*- coding: utf-8 -*-
"""
Vistas de la aplicación main
"""

# Django Libraries
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _

# Thirdparty Libraries
import requests
from apps.usercustom.forms import PasswordRecoveryForm, PasswordSetForm
from apps.usercustom.tokens import PASSWORD_RECOVERY_TOKEN

# Local Folders Libraries
from ..models import UserCustom


# ========================================================================== #
class PasswordRecoveryView(PasswordResetView):
    """Esta Clase tiene dos funciones:
    1.- Envía un coreo al uuario con instrucciones para recuperar su
    contraseña
    2.- Despliega un formulario para recuperar la contraseña
    """
    success_url = 'usercustom:login'
    template_name = 'usercustom/password_reset_form.html'
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'uidb64' in self.kwargs and 'token' in self.kwargs:
            # Formulario para escribir la nueva contraseña
            context['form'] = PasswordSetForm()
            context['url_action'] = reverse_lazy(
                'usercustom:password-set',
                kwargs={
                    'uidb64': self.kwargs['uidb64'],
                    'token': self.kwargs['token']
                }
            )
        else:
            # Fromulario para solicitar el link de recuperación de contraseña
            context['form'] = PasswordRecoveryForm()
            context['url_action'] = reverse_lazy('usercustom:password-recovery')

        return context

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        form = self.get_form()
        if 'uidb64' in self.kwargs and 'token' in self.kwargs:
            form = PasswordSetForm(request.POST)
        else:
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = requests.get(url, params=values, verify=True)
            result = data.json()

            if result['success']:
                self.extra_context['reCAPTCHA_error'] = ''
            else:
                self.extra_context['reCAPTCHA_error'] = _('Invalid reCAPTCHA')
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        if 'uidb64' in self.kwargs and 'token' in self.kwargs:
            uidb64 = self.kwargs['uidb64']
            token = self.kwargs['token']
            uid = force_text(urlsafe_base64_decode(uidb64))

            try:
                user = UserCustom.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, UserCustom.DoesNotExist):
                user = None

            token_valid = PASSWORD_RECOVERY_TOKEN.check_token(user, token)

            if user is not None and token_valid:
                user.set_password(form.cleaned_data['password1'])
                user.is_active = True
                user.save()
                messages.success(
                    self.request,
                    _('Welcome back, your password has been successfully modified. Please log in using your credentials.')
                )
            else:
                messages.error(
                    self.request,
                    _('The password recovery link is invalid or has already been used.')
                )

            return HttpResponseRedirect(reverse_lazy(self.get_success_url()))
        else:
            email = form.cleaned_data['email']
            try:
                user = UserCustom.objects.get(email=email)
            except (TypeError, ValueError, OverflowError, UserCustom.DoesNotExist):
                user = None
            if user is not None:
                current_site = get_current_site(self.request)
                subject = _('%(proj_name)s password recovery') % {
                    'proj_name': settings.PROJECT_NAME
                }

                url = reverse_lazy(
                    'usercustom:password-set',
                    kwargs={
                        'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': PASSWORD_RECOVERY_TOKEN.make_token(user)
                    }
                )

                message_body = _('You received this email because you requested that your password be reset to "%(proj_name)s".\n\nPlease go to the following link to recover your password:\n\nhttp://%(domain)s%(url)s\n\nThe credentials of this link last for one (1) day.\n\nBest regards.\n\nThe %(proj_name)s team.') % {'proj_name': settings.PROJECT_NAME, 'user': user.username, 'domain': 'localhost:8000', 'url': url}
                message_body = message_body.replace("  ", "")

                user.email_user(subject, message_body)

                messages.success(
                    self.request,
                    _('Instructions to recover your password in %(proj_name)s were sent to the email account %(email)s') % {'proj_name': settings.PROJECT_NAME, 'email': email}
                )

                return HttpResponseRedirect(reverse_lazy(self.get_success_url()))

            else:
                messages.error(
                    self.request,
                    _('The email provided is not registered in %(proj_name)s') % {
                        'proj_name': settings.PROJECT_NAME
                    }
                )

                return HttpResponseRedirect(
                    reverse_lazy('usercustom:password-recovery')
                )
