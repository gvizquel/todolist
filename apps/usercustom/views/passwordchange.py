# -*- coding: utf-8 -*-
"""
Vistas de la aplicación main
"""

# Django Libraries
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy as _


# ========================================================================== #
def cambio_clave(request):
    """Esta función es para el cambio de clave del usuario
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante!
            messages.success(request, _('Your password change was successfully \
                processed'))
            return redirect('usercustom:profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(
        request,
        'usercustom/password_change_form.html',
        {'form': form}
    )
