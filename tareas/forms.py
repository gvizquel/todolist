"""Clases formularios para la gestión del modulo de Tareas
"""

# Librerias Django
from django.forms import ModelForm, TextInput, CheckboxInput


# Librerias desarrolladas por mi
from tareas.models import Tarea


# ========================================================================== #
class TareaForm(ModelForm):
    """Clase para la gestión del formulario de tareas
    """
    class Meta:
        model = Tarea
        fields = [
            'tarea',
        ]
        widgets = {
            'tarea': TextInput(attrs={'class': 'form-control'},)
        }


# ========================================================================== #
class MarcarTareaForm(ModelForm):
    """Clase para la gestión de la formulario de tareas
    """
    class Meta:
        model = Tarea
        fields = [
            'tarea',
            'resuelta',
        ]
        widgets = {
            'tarea': TextInput(attrs={
                'class': 'form-control',
                'style': 'background-color:#00a65a; color: white; border: 1px solid white;',
                'readonly': ''},),
            'resuelta': CheckboxInput()
        }
