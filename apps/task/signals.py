""" Task signals
"""
# Django Libraries
from django.db.models.signals import post_save
from django.dispatch import receiver

# Local Folders Libraries
from .models import Task
from .tasks import send_task_alert


@receiver(post_save, sender=Task)
def send_mail(sender, instance, created, **kwargs):
    if created:
        send_task_alert.delay(instance.person.pk)
