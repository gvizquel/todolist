"""Celery test
"""
# Thirdparty Libraries
from .models import Task
from celery import shared_task
from celery.utils.log import get_task_logger
from django.contrib.auth import get_user_model
User = get_user_model()

# Local Folders Libraries

logger = get_task_logger(__name__)


@shared_task
def check_task():
    """Esta tarea se ejecuta recurrentemente cada 60 segundos
    """
    logger.debug("Solving tasks")
    not_solve = Task.objects.filter(solve=False)
    for itask in not_solve:
        itask.solve = True
        itask.save()


@shared_task
def send_task_alert(id):
    """Se envia un aviso al correo del dueño de la tarea cada vez que se crea
    una nueva tarea.
    """
    destinatary = User.objects.get(pk=id)
    subject = "Advise"
    message_body = "Se creo una nueva tarea"
    return destinatary.email_user(subject, message_body)
