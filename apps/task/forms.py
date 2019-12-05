"""Clases formularios para la gestión del modulo de Tareas
"""

# Django Libraries
# Librerias Django
from django.forms import CheckboxInput, ModelForm, TextInput

# Local Folders Libraries
# Librerias desarrolladas por mi
from .models import Task


# ========================================================================== #
class TaskForm(ModelForm):
    """Clase para la gestión del formulario de tareas
    """
    class Meta:
        model = Task
        fields = [
            'task',
        ]
        widgets = {
            'task': TextInput(
                attrs={
                    'class': 'form-control',
                },
            )
        }


# ========================================================================== #
class TaskCheckForm(ModelForm):
    """Clase para la gestión de la formulario de tareas
    """
    class Meta:
        model = Task
        fields = [
            'task',
            'solve',
        ]
        widgets = {
            'task': TextInput(
                attrs={
                    'class': 'form-control',
                    'readonly': '',
                },
            ),
            'solve': CheckboxInput()
        }
