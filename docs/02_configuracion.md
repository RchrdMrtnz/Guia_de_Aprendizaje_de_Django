# 2. Configuración del Entorno

## Prerrequisitos
*   Python 3.8 o superior instalado.
*   pip (gestor de paquetes de Python).

## Paso 1: Crear un Entorno Virtual
Es recomendable usar entornos virtuales para aislar las dependencias de tu proyecto.

```bash
# En Linux/macOS
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

## Paso 2: Instalar Django
Con el entorno virtual activado:

```bash
pip install django
```

## Paso 3: Crear un Proyecto
Django ofrece un comando para generar la estructura inicial.

```bash
django-admin startproject mi_proyecto
cd mi_proyecto
```

## Estructura generada
*   `manage.py`: Una utilidad de línea de comandos para interactuar con el proyecto.
*   `mi_proyecto/settings.py`: Configuración global (base de datos, apps instaladas, etc).
*   `mi_proyecto/urls.py`: Declaración de rutas (URL dispatcher).
*   `mi_proyecto/wsgi.py` y `asgi.py`: Puntos de entrada para servidores web.

## Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```
Visita `http://127.0.0.1:8000/` para ver tu web funcionando.

---
[Siguiente: Modelos y Bases de Datos](./03_modelos.md)
