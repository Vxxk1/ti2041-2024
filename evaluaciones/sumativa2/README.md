
Evaluación Sumativa 3

Esta aplicación web, desarrollada en Django, está diseñada para gestionar productos, marcas, categorías y características. Ofrece funcionalidades como registro, filtrado y validación de productos, con medidas de seguridad integradas para garantizar una experiencia confiable.

Requisitos
Python 3.11 o superior
Django 5.1

Guía de Instalación

Instalar dependencias necesarias
bash
Copiar código
pip install django


Aplicar migraciones

python manage.py migrate


Ejecutar el servidor de desarrollo

python manage.py runserver


Acceder a la aplicación en el navegador:

Inicio de sesión: http://127.0.0.1:8000/login/
Lista de productos: http://127.0.0.1:8000/productos/

Principales Funcionalidades

Listado de productos
Presenta un listado con opciones para filtrar por marca, categoría o características.

Registro de productos
Permite añadir nuevos productos, validando que no existan duplicados.

Mensajes de operación
Informa si el registro de un producto fue exitoso o si ocurrió algún error.

Autenticación y cierre de sesión
Gestión de acceso a través de un sistema de login y logout.

Panel de administración
Administración avanzada de datos mediante el panel integrado de Django.

Medidas de Seguridad

Acceso autenticado
Descripción: Las vistas principales, como listar_productos y registro_producto, requieren autenticación.

Implementación:

from django.contrib.auth.decorators import login_required

@login_required
def listar_productos(request):

Restringe el acceso a usuarios no autenticados.

Protección CSRF
Descripción: Los formularios incluyen un token CSRF para validar solicitudes POST.

Implementación:

<form method="POST">
    {% csrf_token %}
</form>

Bloquea intentos de falsificación de solicitudes entre sitios.

Variables de sesión
Descripción: Durante el inicio de sesión, se almacenan datos clave en la sesión, como el nombre del usuario y su pertenencia al grupo ADMIN_PRODUCTS.

Implementación:

request.session['username'] = user.username
request.session['is_admin_products'] = user.groups.filter(name='ADMIN_PRODUCTS').exists()

Controla el acceso a funciones administrativas según roles.
