# Librerias Django
from django.contrib.messages.views import SuccessMessageMixin
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView)


# Librerias desarrolladas por mi
from tareas.forms import TareaForm, MarcarTareaForm
from tareas.models import Tarea


##############################################################################
class ListarTarea(ListView):
    """Con esta clase se puede listar las tareas que pertenecen a una persona
    """

    model = Tarea
    template_name = 'tarea_listar.html'

    def get_queryset(self):
        # Selecciono las tareas del propietario
        queryset = Tarea.objects.filter(
            persona=self.request.user
        )

        return queryset


##############################################################################
class AgregarTarea(SuccessMessageMixin, CreateView):
    """Esta clase sirve para agregar las tareas de las personas
    """

    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_formulario.html'
    success_url = reverse_lazy('tarea:listar')
    success_message = '¡La tarea se agregó de manera exitosa!'

    def get_context_data(self, **kwargs):
        contexto = super(AgregarTarea, self).get_context_data(**kwargs)
        contexto['agregar'] = True

        return contexto

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.persona = self.request.user
        self.object.save()

        return super().form_valid(form)


##############################################################################
class EditarTarea(SuccessMessageMixin, UpdateView):
    """Esta clase sirve para editar las tareas de las personas
    """

    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_formulario.html'
    success_url = reverse_lazy('tarea:listar')
    success_message = '¡La tarea se actualizó de manera exitosa!'

    def get_context_data(self, **kwargs):
        contexto = super(EditarTarea, self).get_context_data(**kwargs)
        contexto['editar'] = False

        return contexto

    def get_object(self, queryset=None):
        tarea = self.kwargs.get(self.pk_url_kwarg)
        queryset = get_object_or_404(Tarea, persona=self.request.user, pk=tarea)

        return queryset


##############################################################################
class DetalleTarea(DetailView):
    """Con esta clase se puede ver el detalle de un tarea
    """

    model = Tarea
    template_name = 'tarea_detalle.html'

    def get_object(self, queryset=None):
        tarea = self.kwargs.get(self.pk_url_kwarg)
        queryset = get_object_or_404(Tarea, persona=self.request.user, pk=tarea)

        return queryset


##############################################################################
class EliminarTarea(DeleteView):
    """Con esta clase se pueden eliminar las tareas de las personas
    """

    model = Tarea
    template_name = 'tarea_eliminar.html'
    success_url = reverse_lazy('tarea:listar')
    success_message = '¡La tarea se eliminó de manera exitosa!'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        if not self.object.resuelta:
            messages.success(self.request, self.success_message)
            self.object.delete()

        return HttpResponseRedirect(success_url)

    def get_queryset(self):
        tarea = self.kwargs.get(self.pk_url_kwarg)
        queryset = Tarea.objects.filter(persona=self.request.user, pk=tarea)

        return queryset


##############################################################################
class MarcarTarea(SuccessMessageMixin, UpdateView):
    """Esta clase sirve para editar las tareas de las personas
    """

    model = Tarea
    form_class = MarcarTareaForm
    template_name = 'tarea_formulario.html'
    success_url = reverse_lazy('tarea:listar')
    success_message = '¡La tarea se marco como resuelta de manera exitosa!'

    def get_context_data(self, **kwargs):
        contexto = super(MarcarTarea, self).get_context_data(**kwargs)
        contexto['marcar'] = True

        return contexto

    def get_object(self, queryset=None):
        tarea = self.kwargs.get(self.pk_url_kwarg)
        queryset = get_object_or_404(Tarea, persona=self.request.user, pk=tarea)

        return queryset