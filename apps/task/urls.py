"""Rutas de nuestra aplicación Tareas
"""
# Django Libraries
from django.urls import path

# Local Folders Libraries
from .views import (
    DetailTask,
    ListTask,
    TaskCheck,
    TaskCreate,
    TaskDelete,
    TaskUpdate
)

# from .routers import router

app_name = 'Task'

urlpatterns = [
    path('list', ListTask.as_view(), name='list'),
    path('detail/<int:pk>', DetailTask.as_view(), name='detail'),
    path('create', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='delete'),
    path('check/<int:pk>', TaskCheck.as_view(), name='check'),
]
