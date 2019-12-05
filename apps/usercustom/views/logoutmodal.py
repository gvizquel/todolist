"""Sub Vista logout modaldel módulo erp
"""
# Django Libraries
from django.views.generic import TemplateView


# ========================================================================== #
class LogOutModalView(TemplateView):
    """Lista de las ordenes de venta
    """
    template_name = 'usercustom/logoutmodal.html'
