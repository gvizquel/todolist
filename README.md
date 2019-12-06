# To Do List

Una mini aplicación web para manejar un "TODO list" con Django 2

## Funcionalidad

- Gestión de usuario: auto registro, recuperar y cambiar claves, perfil.
- Agregar tareas al TODO list.
- Marcar una tarea como resuelta.
- Obtener la lista de tareas y su estado actual.

## Consideraciones

- Se utilizo pipenv para la gestión del entorno virtual y las librerias.
- Para instalar todas las librerias puede usar el metodo tradicional (pip install -r requirements.txt) o pipenv install
- Se utilizo Python 3.7.2
- Se utilizaron las plantillas provistas por AdminLTE 3 Control Panel Template basadas en bootstrap 4
- El desarrollo funcional se realizo utilizando el paradigma de vistas basadas en clases de Django (Class-Based Views).
- Se utilizó el motor de plantillas django-template.
- La aplicación permite el auto registro de los usuarios, modificación y recuperación de clave, actualización de datos del perfil de usuario. Para el auto registro se requiere un servidor de correo. Para efectos de este proyecto se utiliza el 'django.core.mail.backends.console.EmailBackend' que envia el correo a los log de la consola del servidor de pruebas. Para validadar el registro y evitar la creación de cuentas "bots" junto con la validación del registro vía correo electronico se utilizó google recaptcha. Tambien se puede hacer gestión de usuarios por el admin <http://127.0.0.1:8000/admin>
- DBMS es sqlite3.
- Una vez iniciado el servidor de pruebas (./manage.py runserver) la ruta de acceso a la aplicación es <http://http://127.0.0.1:8000>
- Las tareas se deben redactar con hasta un maximo de 255 caracacteres alfa númericos.
- La aplicación es multi idioma y se pre configuro para ingles (base), español y franses, se utilizó django-rosetta para apoyar la traducción. La opción de administración de la traducción solo es visible en el menú lateral para los usuarios admin.
- Se configuró una tarea programada con Celery y Redis para que cada 30 segundos las tareas que no sen resuelto se resuelvan de forma automatica.
- Para la gestión de tareas programadas con celery  se uso la libreria django-celery-beat.
- Cada vez que se crea una tare se envia un correo al usario que la crea desde el background de Celery.
- El comando para ejecutar las tareas programadas es: celery -A todolist worker -B --loglevel=debug

## PENDIENTES

- Pruebas unitarias.
