# -*- coding: utf-8 -*-
"""
Formularios para la app main
"""
# Django Libraries
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, TextInput

# Own Libraries
from main.models import Persona


class PersonaCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserCustom
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder':'Primer nombre'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder':'Primer apellido'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder':'Usuario'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder':'Coreo electrónico'}),
        }
