# Django Libraries
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

# Thirdparty Libraries
from apps.main.views import (
    MainCreateView,
    MainDeleteView,
    MainDetailView,
    MainListView,
    MainUpdateView
)

# Local Folders Libraries
from .forms import TaskCheckForm, TaskForm
from .models import Task

OBJECT_LIST_FIELDS = [
    {'string': _('Person'), 'field': 'person'},
    {'string': _('task'), 'field': 'task'},
    {'string': _('Solve'), 'field': 'solve'},
    {'string': _('Solve date'), 'field': 'solve_date'},
]


# ========================================================================== #
class ListTask(LoginRequiredMixin, MainListView):
    """Con esta clase se puede listar las farms que pertenecen a un usuario
    """
    model = Task
    template_name = 'main/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_partner'] = 'Partner:create'
        return context

    def get_queryset(self):
        # Selecciono las tareas del propietario
        queryset = Task.objects.filter(
            person=self.request.user
        )

        return queryset


##############################################################################
class TaskCreate(LoginRequiredMixin, MainCreateView):
    """Esta clase sirve para agregar las tareas de las personas
    """
    model = Task
    form_class = TaskForm
    template_name = 'main/form_modal.html'
    success_url = reverse_lazy('Task:list')

    def form_valid(self, form):
        create_object = form.save(commit=False)
        create_object.person = self.request.user
        create_object.save()

        return super().form_valid(form)


##############################################################################
class TaskUpdate(LoginRequiredMixin, MainUpdateView):
    """Esta clase sirve para editar las tareas de las personas
    """
    model = Task
    form_class = TaskForm
    template_name = 'main/form_modal.html'
    success_url = reverse_lazy('Task:list')

    def get_object(self, queryset=None):
        task = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(Task, person=self.request.user, pk=task)


##############################################################################
class DetailTask(LoginRequiredMixin, MainDetailView):
    """Con esta clase se puede ver el detalle de un tarea
    """

    model = Task
    template_name = 'main/detail_modal.html'

    def get_object(self, queryset=None):
        tarea = self.kwargs.get(self.pk_url_kwarg)
        queryset = get_object_or_404(
            Task, person=self.request.user, pk=tarea)

        return queryset


##############################################################################
class TaskDelete(LoginRequiredMixin, MainDeleteView):
    """Con esta clase se pueden eliminar las tareas de las personas
    """

    model = Task
    template_name = 'main/delete_modal.html'
    success_url = reverse_lazy('Task:list')
    success_message = '¡La tarea se eliminó de manera exitosa!'

    def get_context_data(self, **kwargs):
        verbose_name = self.model._meta.verbose_name
        context = super().get_context_data(**kwargs)
        task = self.get_object()

        if not task.solve:
            context['del_mesage_1'] = _('Are you sure to delete this %(object)s?') % {
                'object': verbose_name}
            context['del_mesage_2'] = _(
                "Press the \"<b>Accept</b>\" button to delete this %(object)s. Remember that this action is irreversible.") % {'object': verbose_name}
            context['del_mesage_3'] = _(
                "Press the \"<b>Cancel</b>\" button to avoid this action.")
            context['removable'] = True
        else:
            context['del_mesage_1'] = _("This %(object)s is solved, so you cannot delete it.") % {
                'object': verbose_name}
            context['del_mesage_3'] = _(
                "Press the \"<b>Cancel</b>\" button to return.")
            context['removable'] = False
        return context

    def delete(self, request, *args, **kwargs):
        delete_object = self.get_object()
        if not delete_object.solve:
            delete_object.delete()
            messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.success_url)

    def get_object(self, queryset=None):
        task = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(Task, person=self.request.user, pk=task)


##############################################################################
class TaskCheck(LoginRequiredMixin, MainUpdateView):
    """Esta clase sirve para editar las tareas de las personas
    """
    model = Task
    form_class = TaskCheckForm
    template_name = 'main/form_modal.html'
    success_url = reverse_lazy('Task:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_name = self.model._meta.verbose_name
        context['action_url'] = reverse_lazy(
            '{}:check'.format(verbose_name), args=[self.object.pk])
        return context

    def get_object(self, queryset=None):
        task = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(Task, person=self.request.user, pk=task, solve=False)
