# -*- coding: utf-8 -*-
"""
Vistas de la aplicación main
"""

# Django Libraries
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import UpdateView

# Thirdparty Libraries
from apps.usercustom.forms import AvatarForm, PerfilForm

# Local Folders Libraries
from ..models import UserCustom


# ========================================================================== #
class ProfileView(SuccessMessageMixin, UpdateView):
    """Vista para editarar las sale
    """
    model = UserCustom
    form_class = PerfilForm
    template_name = 'usercustom/profile.html'
    success_message = _('Your profile was updated successfully')
    success_url = reverse_lazy('usercustom:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_avatar'] = AvatarForm(instance=self.request.user)

        return context

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
