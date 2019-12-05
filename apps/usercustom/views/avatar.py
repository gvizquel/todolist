# -*- coding: utf-8 -*-
"""
Vistas de la aplicación main
"""
# Django Libraries
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

# Local Folders Libraries
from ..forms import AvatarForm
from ..models import UserCustom


# ========================================================================== #
class AvatarUpdateView(UpdateView):
    """Vista para editarar las sale
    """
    model = UserCustom
    form_class = AvatarForm
    success_url = reverse_lazy('usercustom:profile')

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        # pk = self.kwargs.get(self.pk_url_kwarg)
        pk = self.request.user.pk
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query") %
                {'verbose_name': queryset.model._meta.verbose_name}
            )
        return obj

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        usuario = UserCustom.objects.get(pk=self.request.user.pk)

        if request.method == 'POST':
            form = AvatarForm(self.request.POST, self.request.FILES, instance=usuario)
            if form.is_valid():
                form.save()

        return redirect('usercustom:profile')


# ========================================================================== #
# def avatar(request):
#     """Función para actualizar el avatar
#     """

#     usuario = UserCustom.objects.get(pk=request.user.pk)

#     if request.method == 'POST':
#         form = AvatarForm(request.POST, request.FILES, instance=usuario)
#         if form.is_valid():
#             form.save()

    # return redirect('usercustom:profile')
