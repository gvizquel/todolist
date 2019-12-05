# -*- coding: utf-8 -*-
"""
Vistas de la aplicación main
"""

# Django Libraries
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView

# Thirdparty Libraries
import requests
from apps.usercustom.forms import PersonaCreationForm
from apps.usercustom.tokens import ACCOUNT_ACTIVATION_TOKEN

# Local Folders Libraries
from ..models import UserCustom


# ========================================================================== #
class SignUpView(CreateView):
    """Esta clase sirve registrar a los usuarios en el sistema
    """
    model = UserCustom
    form_class = PersonaCreationForm
    template_name = 'usercustom/signup.html'
    extra_context = {}
    success_url = 'usercustom:login'
    success_message = _(
        'Your account was created successfully. A link was sent to your email that you must sign in to confirm your sign up.')

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        form = self.get_form()
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = requests.get(url, params=values, verify=True)
        result = data.json()

        if form.is_valid() and result['success']:
            self.extra_context['reCAPTCHA_error'] = ''
            return self.form_valid(form)
        else:
            if not result['success']:
                messages.error(self.request, _('Invalid reCAPTCHA'))
                self.extra_context['reCAPTCHA_error'] = _('Invalid reCAPTCHA')
            return self.form_invalid(form)

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        self.object = form.save()
        current_site = get_current_site(self.request)
        subject = _('%(proj_name)s sign up') % {
            'proj_name': settings.PROJECT_NAME}

        url = reverse_lazy(
            'usercustom:activar',
            kwargs={
                'uidb64': urlsafe_base64_encode(force_bytes(self.object.pk)),
                'token': ACCOUNT_ACTIVATION_TOKEN.make_token(self.object)
            }
        )

        message_body = _('Thank you for registering in %(proj_name)s, your username is: %(user)s.\n\nPlease go to the following link to confirm your registration and activate your account:\n\nhttp://%(domain)s%(url)s\n\nThe credentials of this link last for one (1) day.\n\nBest regards.\n\nThe %(proj_name)s team.') % {
            'proj_name': settings.PROJECT_NAME, 'user': self.object.username, 'domain': 'localhost:8000', 'url': url}
        message_body = message_body.replace("  ", "")

        self.object.email_user(subject, message_body)

        messages.success(
            self.request,
            _('Your account has been created successfully. Open the link that was sent to your email, to confirm your registration and activate your account.')
        )

        return HttpResponseRedirect(reverse_lazy(self.get_success_url()))
