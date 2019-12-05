"""Generador del tokens para el registro de usuarios
"""
# Django Libraries
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# Thirdparty Libraries
import six


class AccountActivacionTokenGenerator(PasswordResetTokenGenerator):
    """Esta clase genera un token que se envía en correo para validadar el
    registro del usuario
    """

    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


ACCOUNT_ACTIVATION_TOKEN = AccountActivacionTokenGenerator()


class PasswordRecoveryTokenGenerator(PasswordResetTokenGenerator):
    """Esta clase genera un token que se envía en correo para recuperar la
    contraseña del usuario
    """

    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.password)
        )


PASSWORD_RECOVERY_TOKEN = PasswordRecoveryTokenGenerator()
