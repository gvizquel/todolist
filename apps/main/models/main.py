# -*- coding: utf-8
"""
Modelo de datos de la app main
"""
# Django Libraries
from django.db import models


class MainModel(models.Model):
    active = models.BooleanField(default=True, blank=True, null=True)
    fc = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fm = models.DateTimeField(auto_now=True, blank=True, null=True)
    uc = models.ForeignKey(
        'usercustom.UserCustom',
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_uc",
        db_column="uc",
        null=True,
        blank=True
    )
    um = models.ForeignKey(
        'usercustom.UserCustom',
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_um",
        db_column="um",
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
