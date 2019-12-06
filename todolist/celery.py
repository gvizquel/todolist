"""
Celery config for todolist project.
"""
# Standard Libraries
import os

# Thirdparty Libraries
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')

celery_app = Celery('todolist')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
