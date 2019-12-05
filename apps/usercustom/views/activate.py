# -*- coding: utf-8 -*-
"""
Vistas de la aplicación main
"""

# Django Libraries
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView

# Thirdparty Libraries
from apps.usercustom.tokens import ACCOUNT_ACTIVATION_TOKEN

# Local Folders Libraries
from ..models import UserCustom


# ========================================================================== #
class ActivateView(RedirectView):
    """Esta clase activa a la persona cuando confirma el link enviado desde
    su correo
    """
    url = 'usercustom:login'

    def get(self, request, *args, **kwargs):
        uidb64 = self.kwargs['uidb64']
        token = self.kwargs['token']
        url = self.get_redirect_url(*args, **kwargs)
        uid = force_text(urlsafe_base64_decode(uidb64))

        try:
            user = UserCustom.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserCustom.DoesNotExist):
            user = None

        token_valid = ACCOUNT_ACTIVATION_TOKEN.check_token(user, token)

        if user is not None and token_valid:
            user.is_active = True
            user.save()
            messages.success(
                self.request,
                _('Welcome, your account has been successfully activated. Please log in using your credentials.')
            )
        else:
            messages.error(
                self.request,
                _('The sign up confirm link is invalid. If your account is not yet active, use the password recovery link.')
            )

        return HttpResponseRedirect(reverse_lazy(url))
