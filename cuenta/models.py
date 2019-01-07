# -*- coding: utf-8
"""
Modelo de datos de la app globales
"""
# Librerias Future
from __future__ import unicode_literals

# Librerias Standard
import os

# Librerias Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Librerias en carpetas locales
from .libSobreEscribirImagen import SobreEscribirAvatar


def image_path(instance, filename):
    """Define la ruta de las imgenes
    """
    return os.path.join(
        'avatar',
        str(instance.pk) + '.' + filename.rsplit('.', 1)[1]
    )


##############################################################################
class Persona(AbstractUser):
    """Modelo abstracto de la clase User
    """
    SEXO_CHOICES = (
        ('F', 'FEMENINO'),
        ('M', 'MASCULINO'),
    )
    LETRACEDULA_CHOICES = (
        ('V', 'V'),
        ('E', 'E'),
    )
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True, db_index=True)
    first_name = models.CharField(max_length=30, db_index=True)
    last_name = models.CharField(max_length=30, db_index=True)
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    email_secundario = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        db_index=True,
        unique=True
    )
    letra_cedula_identidad = models.CharField(
        max_length=1,
        choices=LETRACEDULA_CHOICES,
        default=LETRACEDULA_CHOICES[0][0]
    )
    cedula_identidad = models.IntegerField(
        blank=True,
        null=True,
        db_index=True
    )
    otros_nombres = models.CharField(
        max_length=90,
        null=True,
        blank=True,
        db_index=True
    )
    otros_apellidos = models.CharField(
        max_length=255, null=True, blank=True, db_index=True)
    telefono = models.CharField(max_length=19, blank=True, null=True)
    celular = models.CharField(max_length=19, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        max_length=255,
        storage=SobreEscribirAvatar(),
        upload_to=image_path,
        default='avatar/default_avatar.png'
    )

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        return '%s %s %s %s' % (
            self.first_name,
            self.otros_nombres,
            self.last_name,
            self.otros_apellidos
        )

    def get_short_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = ('Persona')
        verbose_name_plural = ('Personas')
        db_table = 'auth_user'
