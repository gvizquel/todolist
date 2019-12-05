
# Standard Libraries
import os

# Django Libraries
from django.utils.translation import ugettext_lazy as _
from celery.schedules import crontab

# Thirdparty Libraries
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='foo')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]

INTERNAL_IPS = ('localhost', '127.0.0.1',)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',

    # Local Apps
    'apps.usercustom',
    'apps.main',
    'apps.task',

    # # Third-Party Apps
    'apps.rosetta',
    'bootstrap_datepicker_plus',
    'bootstrap4',
    'django_extensions',
    'django_celery_beat',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ========================================================================== #
""" Esta es la clave para el recaptcha de google, hay que busca una para el
proyecto
"""
GOOGLE_RECAPTCHA_SECRET_KEY = '6LevF1gUAAAAAPn3z8EswCgIk1S_jLKYdf4s62B9'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'todo.sqlite3'),
    }
}

ROOT_URLCONF = 'todolist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'loaders': [
                # 'app_namespace.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.csrf',

            ],
        },
    },
]

WSGI_APPLICATION = 'todolist.wsgi.application'


# ========================================================================== #
""" EL tempo de validez de los token de activación de la cuenta del usuario y
recuperacion de contraseña del usuario.
"""
PASSWORD_RESET_TIMEOUT_DAYS = 1


# ========================================================================== #
""" Esta configuración define el modelo personalizado para auth.user. Tambien
establece las rutas para algunas funciones.
"""
AUTH_USER_MODEL = 'usercustom.UserCustom'
LOGIN_URL = 'usercustom:login'
LOGOUT_REDIRECT_URL = 'usercustom:login'
LOGIN_REDIRECT_URL = 'usercustom:profile'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ========================================================================== #
""" Este bloque contiene toda la configuración para la loclización
"""
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# def gettext(cadena):
#     '''  "dummy" gettext() function
#     '''
#     return cadena

LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/Caracas'
# Restricts languages
# Al usar lenguages del tipo en-us. es-ve, fr-ca no funciona la traducción
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French'))
]
# Where Django looks for translation files
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
USE_I18N = True
USE_L10N = True
USE_TZ = True

ROSETTA_EXCLUDED_APPLICATIONS = (
    'dal_select2',
    'django_extensions',
)


# ========================================================================== #
""" Este bloque es para la configuración de los estaticos y los archivos de
imagens
"""
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'


# ========================================================================== #
""" En este bloque se debe configurar el servidor de correo que utilizará
Django para enviar correos.
"""
# During development only
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# ========================================================================== #
""" Esta configuración hace disponible todas esta variables en cualquier
plantilla
"""
PROJECT_NAME = 'ToDoList'
SLOGAN = 'Software de gestión de lista de tareas'
PREFIX = 'ToDo'
SUFIX = 'List'
VERSION = '1.0'
INITIAL_A = 'T'
INITIAL_B = 'L'

SETTINGS_EXPORT = [
    'PROJECT_NAME',
    'SLOGAN',
    'PREFIX',
    'SUFIX',
    'VERSION',
    'INITIAL_A',
    'INITIAL_B'
]


# celery
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Caracas'

# Let's make things happen
# CELERY_BEAT_SCHEDULE = {
#     'solve-task-in-todo-list': {
#         'task': 'apps.task.tasks.check_task',
#         'schedule': 30.0,
#     },
# }
