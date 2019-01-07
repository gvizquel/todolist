# Django: Aplicación de auto gestión de usuarios #

## A modo de introducción ##

___
Django Admin es un sistema de gestión en backend para los modelos escritos en Django. Incluso para la gestión de **Usuarios**, **Grupos** y **Permisos**, es simplemente increible. Pero cuando se trata de darle a los ususarios la autogestión de sus perfiles el tema ya deja de ser ser simple. Por eso me tomé la molestia de escribir una modesta aplicación para la auto gestión de los usuarios en tu sistema. Para darle un aire de backend, siendo un frintend, he utilazado las plantillas de AdminLTE.
___

Para trabajar en equipo, desarrollando en cualquier lenguaje de programación, se debe convenir en como escribir el código. Ya existen estándares definidos por lacomunidad como los PSRx para PHP y el PEPx para python. Les recomiendo (POR FAVOR) revisarlos y ponerlos en practica, tanto para codificar como para documentar el código.

## 1- Funcionalidades ##

* Registro y/o creación de cuentas con validación de anti robot reCaptcha de google. Envío automático de correo electronico con las credenciales para activación de la cuenta. Las credenciales expiran a los dos (2) días de ser emitidas.
* Visualización y posibilidad de actualizar el perfil del usuario.
* Cambio de clave del usuario.
* Reinicio de clave del usuario. Envió automático de correo electronico con las credenciales para el acceso al formulario de reinicio de la clave. Las credenciales expiran a los dos (2) días de ser emitidas.

## 2.- Instalación ##

* Copiar la carpeta cuenta en la raiz de su proyecto.
* Crear las credenciales de reCaptcha en google.(https://www.google.com/recaptcha/admin#list)
* Agregar la siguiente configuración al archivo settings.py:

```console
INSTALLED_APPS = [
    ...
    'cuenta',
    ...
]
GOOGLE_RECAPTCHA_SECRET_KEY = 'LaClaveDeGoogleReCaptcha'

PASSWORD_RESET_TIMEOUT_DAYS = 2

AUTH_USER_MODEL = 'cuenta.Persona'

######################## ENVIO DE CORREO EN PRODUCCIÓN ########################
EMAIL_HOST = 'IP ó nombre de dominio del servidor de envío de correos'
EMAIL_PORT = El puerto de envio de correos del servidor
EMAIL_HOST_USER = 'ElUsuarioQueEnviaLosCorreos'
EMAIL_HOST_PASSWORD = 'LaClaveDelUsuarioQueEnviaCorreos'
EMAIL_USE_TLS = True ó False dependiendo de la configuración de tu servidor de correo

######################## ENVIO DE CORREO EN DESARROLLO ########################
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
