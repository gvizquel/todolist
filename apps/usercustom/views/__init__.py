# -*- coding: utf-8 -*-
"""
Vistas de la aplicación main
"""
from django.shortcuts import redirect, render

from ..forms import AvatarForm
from ..models import UserCustom
from .activate import ActivateView
from .activatelanguage import ActivateLanguageView
from .avatar import AvatarUpdateView
from .logoutmodal import LogOutModalView
from .passwordchange import cambio_clave
from .passwordreset import PasswordRecoveryView
from .profile import ProfileView
from .signup import SignUpView

ChangePasswordView = cambio_clave
