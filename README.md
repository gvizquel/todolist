# To Do List

Una mini aplicación web para manejar un "TODO list" con Django 2.1

## Funcionalidad

- Registrar un usuario.
- Agregar tareas al TODO list.
- Marcar una tarea como resuelta.
- Obtener la lista de tareas y su estado actual.

## Consideraciones

- Revisar el archivo requeriments.txt para las dependencias y versiones del las aplicaciones de soporte al desarrollo utilizadas
- Se utilizo Python 3.7.2
- Se utilizaron las plantillas provistas por AdminLTE Control Panel Template basadas en bootstrap 3
- El desarrollo funcional se realizo utilizando el paradigma de vistas basadas en clases de Django (Class-Based Views).
- Se utilizó el motor de plantillas Jinja2 por ser hast 20% mas rapido en el renderizado del html. El admin se mantiene con el motor de plantillas django-template.
- La aplicación permite el auto registro de los usuarios(<http://127.0.0.1:8000/cuenta/registro>), modificación y recuperación de clave, actualización de datos del perfil de usuario. Para el auto registro se requiere un servidor de correo. Para efectos de este proyecto se utiliza el 'django.core.mail.backends.console.EmailBackend' que envia el correo a los log de la consola del servidor de pruebas. Para validadar el registro y evitar la creación de cuentas "bots" junto con la validación del registro vía correo electronico se utilizó google recaptcha. Tambien se puede hacer gestión de usuarios por el admin <http://127.0.0.1:8000/admin>
- Se crearon dos ususarios de prueba: el usuario <b>admin</b> con la clave <b>t0d0l1st</b> y el usuario <b>usuario</b> con la misma clave.
- DBMS es sqlite3.
- Una vez iniciado el servidor de pruebas (./manage.py runserver) la ruta de acceso a la aplicación es <http://http://127.0.0.1:8000/cuenta/login>
- Las tareas se deben redactar con hasta un maximo de 255 caracacteres alfa númericos.
