# Django Libraries
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TasksConfig(AppConfig):
    name = 'apps.task'
    verbose_name = _('Tasks')

    def ready(self):
        import apps.task.signals  # noqa
