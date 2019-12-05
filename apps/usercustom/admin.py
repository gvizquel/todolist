"""
Sección administrativa del modelo usercustom
"""
# Django Libraries
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin

# Local Folders Libraries
from .forms import PersonaChangeForm, PersonaCreationForm
from .models import UserCustom  # , Archivo


class PersonaAdmin(UserAdmin):
    """ Admin para usuarios
    """
    form = PersonaChangeForm
    add_form = PersonaCreationForm
    # fieldsets = (
    #     ('Usuario', {
    #         'fields': ('username',
    #                    'email')
    #     }),
    #     ('Información personal', {
    #         'classes': ('collapse',),
    #         'fields': (
    #             'first_name',
    #             'last_name',
    #             'email',
    #         ),
    #     }),
    #     ('Permisos', {
    #         'classes': ('collapse',),
    #         'fields': ('is_superuser',
    #                    'is_staff',
    #                    'is_active',
    #                    'password',
    #                    'groups',
    #                    'user_permissions'),
    #     }),
    #     ('Auditoria', {
    #         'classes': ('collapse',),
    #         'fields': (
    #             'last_login',
    #             'date_joined',),
    #     }),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username',
    #                    'email',
    #                    'password1',
    #                    'password2',)}
    #      ),
    # )

    search_fields = ('email',)
    list_filter = ('is_staff', 'is_superuser')
    list_display = ('__str__', 'username', 'email',)
    # list_select_related = ()
    show_full_result_count = False
    actions_selection_counter = False
    ordering = ('id',)

    # def get_search_results(self, request, queryset, search_term):
    #   queryset, use_distinct = super(PersonaAdmin, self).get_search_results(
    #         request, queryset, search_term)
    #     try:
    #         search_term_as_int = int(search_term)
    #     except ValueError:
    #         pass
    #     else:
    #         queryset = self.model.objects.filter(
    #             cedulaidentidad=search_term_as_int)
    #     return queryset, use_distinct

admin.site.register(UserCustom, PersonaAdmin)


admin.site.register(LogEntry)
