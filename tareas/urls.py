"""Rutas de nuestra aplicación Tareas
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Librerias de tercero
from tareas.views import (
    AgregarTarea, DetalleTarea, EditarTarea,
    EliminarTarea, ListarTarea, MarcarTarea)

# from .routers import router

app_name = 'tarea'

urlpatterns = [
    path(
        'listar',
        login_required()(ListarTarea.as_view()),
        name='listar'),
    path(
        'detalle/<int:pk>',
        login_required()(DetalleTarea.as_view()),
        name='detalle'),
    path(
        'agregar',
        login_required()(AgregarTarea.as_view()),
        name='agregar'),
    path(
        'editar/<int:pk>',
        login_required()(EditarTarea.as_view()),
        name='editar'),
    path(
        'marcar/<int:pk>',
        login_required()(MarcarTarea.as_view()),
        name='marcar'),
    path(
        'eliminar/<int:pk>',
        login_required()(EliminarTarea.as_view()),
        name='eliminar'),
]
