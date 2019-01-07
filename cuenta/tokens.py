"""Generador del tokens para el registro de usuarios
"""
# Librerias Django
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class ActivacionCuentaTokenGenerator(PasswordResetTokenGenerator):
    """Esta clase genera un token que se envía en correo para validadar el \
    registro del usuario
    """
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

account_activation_token = ActivacionCuentaTokenGenerator()
