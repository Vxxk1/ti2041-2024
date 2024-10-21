## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

evaluaciones/ │ └───sumativa1/ │ └───biblioteca/ # Proyecto Django │ └───bib1/ # Aplicación dentro del proyecto

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes requisitos:

1. **Python**: Se requiere tener Python instalado. Puedes descargarlo desde [python.org](https://www.python.org/).
2. **pip**: El gestor de paquetes de Python (`pip`) también debe estar instalado.
3. **Django**: Instala Django ejecutando el siguiente comando: pip install django

## Instrucciones para Ejecutar el Proyecto

1. Clona el proyecto utilizando Git: git clone <repositorio-url>
2. Navega a la carpeta del proyecto
3. Inicia el servidor de desarrollo de Django: python manage.py runserver
4. Abre tu navegador web y navega a http://localhost:8000 para ver el proyecto en ejecución.

Funcionalidades
Listar productos: Muestra una lista de todos los productos registrados.
Registrar producto: Permite registrar nuevos productos con validación de datos.
Validación de producto: Asegura que el nombre, precio y descripción sean proporcionados antes de registrar el producto.
Estructura del proyecto
La estructura del proyecto es la siguiente:

productos/: Contiene la lógica principal de la aplicación, incluidas vistas y modelos.
static/: Archivos estáticos, como el CSS personalizado.
templates/: Contiene los templates HTML para listar, registrar, y mostrar resultados.
manage.py: Script para gestionar el proyecto Django.



