""" Modelos de la aplicacion tareas
"""
from django.db import models
from django.utils import timezone

# Create your models here.


# ========================================================================== #
class Tarea(models.Model):
    """
    Gestiona las tareas de las personas
    """
    persona = models.ForeignKey('cuenta.Persona', on_delete=models.PROTECT)
    tarea = models.CharField(max_length=255)
    resuelta = models.BooleanField(default=False)
    fecha_resolucion = models.DateTimeField(editable=False, blank=True, null=True)

    def __str__(self):
        return self.tarea

    def save(self, *args, **kwargs):
        """ On save, update timestamps
        """
        if self.resuelta:
            self.fecha_resolucion = timezone.now()

        return super(Tarea, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
