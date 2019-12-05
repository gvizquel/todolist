"""Celery test
"""
from celery import task
from celery import shared_task
from .models import Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def check_task():
    logger.info("Solving tasks")
    not_solve = Task.objects.filter(solve=False)
    for itask in not_solve:
        itask.solve = True
        itask.save()
    return None
