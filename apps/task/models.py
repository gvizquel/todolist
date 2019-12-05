""" Modelos de la aplicacion tareas
"""
# Django Libraries
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Thirdparty Libraries
from apps.main.models import MainModel


# ========================================================================== #
class Task(MainModel):
    """
    Gestiona las tareas de las personas
    """
    person = models.ForeignKey(
        'usercustom.UserCustom',
        on_delete=models.PROTECT,
        verbose_name=_('User'),
        related_name='users'
    )
    task = models.CharField(max_length=255, verbose_name=_('Task'))
    solve = models.BooleanField(default=False, verbose_name=_('Solve'))
    solve_date = models.DateTimeField(
        editable=False, blank=True, null=True, verbose_name=_('Solve date'))

    def __str__(self):
        return self.task

    def save(self, *args, **kwargs):
        """ On save, update timestamps
        """
        if self.solve:
            self.solve_date = timezone.now()

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        detail_fields = (
            'person',
            'task',
            'solve',
            'solve_date'
        )
        for field in self._meta.get_fields():
            fname = field.name
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_' + fname + '_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if value and field.name in detail_fields:
                if field.many_to_many:
                    value = ''
                    partners = eval('self.{}.all()'.format(field.name))
                    for partner in partners:
                        value += str(partner) + '<br>'
                fields.append(
                    {
                        'label': field.verbose_name,
                        'name': field.name,
                        'value': value,
                    }
                )
        return fields
