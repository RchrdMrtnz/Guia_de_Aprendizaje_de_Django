# 5. Plantillas y Archivos Estáticos

Django usa un potente motor de plantillas para generar HTML dinámicamente. Además, facilita el manejo de archivos estáticos (CSS, JS, imágenes).

## Herencia de Plantillas
Una de las características más potentes es la herencia. Permite crear un template base (`base.html`) con la estructura común (header, footer, navegación) y que otros templates rellenen bloques específicos.

### Ejemplo: `base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mi Sitio{% endblock %}</title>
</head>
<body>
    <nav>...</nav>

    <div class="content">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
```

### Ejemplo: `hijo.html`

```html
{% extends "base.html" %}

{% block title %}Página de Inicio{% endblock %}

{% block content %}
    <h1>Bienvenido</h1>
    <p>Este es el contenido específico.</p>
{% endblock %}
```

## Django Template Language (DTL)
Sintaxis básica:
*   `{{ variable }}`: Imprime una variable.
*   `{% tag %}`: Lógica de control (for, if, block).
*   `{{ variable|filtro }}`: Modifica la variable (ej: `date`, `upper`, `truncatewords`).

### Tags Comunes
*   `{% for item in lista %} ... {% endfor %}`
*   `{% if condicion %} ... {% else %} ... {% endif %}`
*   `{% url 'nombre_ruta' arg1 %}`: Genera URLs dinámicas.
*   `{% static 'path/to/file' %}`: Genera la URL de un archivo estático.

## Archivos Estáticos
Para servir CSS, JS e imágenes, Django usa la app `django.contrib.staticfiles`.

1.  Configura `STATIC_URL` en `settings.py`.
2.  Crea una carpeta `static/` en tu app o en la raíz (configurando `STATICFILES_DIRS`).
3.  Carga el tag en el template: `{% load static %}`.
4.  Usa el tag: `<link href="{% static 'css/style.css' %}">`.

---
[Siguiente: Formularios y Validaciones](./06_formularios.md)
