# -*- coding: utf-8 -*-
"""
Vistas de la aplicación main
"""

# Standard Libraries
from urllib.parse import urlparse

# Django Libraries
from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.utils import translation
from django.views.generic.base import View


# ========================================================================== #
class ActivateLanguageView(View):
    ''' Clase para la activación de un lenguaje
    '''
    language_code = ''
    redirect_from = ''
    redirect_to = ''
    match = ''

    def get(self, request, *args, **kwargs):
        ''' Metodo para hacer switch en idiomas
        '''
        self.redirect_from = request.META.get('HTTP_REFERER', None) or '/'
        self.match = resolve(urlparse(self.redirect_from)[2])
        self.language_code = kwargs.get('language_code')
        if self.match.namespace:
            self.redirect_to = self.match.namespace + ':'
        self.redirect_to += self.match.url_name
        print(self.language_code)
        translation.activate(self.language_code)
        request.session[translation.LANGUAGE_SESSION_KEY] = self.language_code

        return redirect(reverse(self.redirect_to, kwargs=self.match.kwargs))
