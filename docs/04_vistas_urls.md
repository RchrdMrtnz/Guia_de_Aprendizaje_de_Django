# 4. Vistas y URLs

## Vistas (Views)
Una vista es una función de Python (o una clase) que recibe una petición web (`HttpRequest`) y devuelve una respuesta (`HttpResponse`).

### Tipos de Vistas
1.  **Function-Based Views (FBV):** Vistas escritas como funciones. Son simples y explícitas.
2.  **Class-Based Views (CBV):** Vistas escritas como clases. Permiten reutilizar código mediante herencia.

### Ejemplo (ver `src/conceptos_basicos/views.py`)

```python
from django.http import HttpResponse
from .models import Curso

def lista_cursos(request):
    cursos = Curso.objects.all()
    # Lógica simple para mostrar datos
    response_content = "<h1>Listado de Cursos</h1>"
    for curso in cursos:
        response_content += f"<p>{curso.titulo}</p>"
    return HttpResponse(response_content)
```

## URLs (Routing)
Para que una vista sea accesible, debe estar vinculada a una URL. Django usa un sistema de configuración de URLs (`URLconf`) elegante y potente.

### Configuración
1.  **App URLs (`src/conceptos_basicos/urls.py`):** Define las rutas específicas de la aplicación.
2.  **Project URLs (`src/curso_django/urls.py`):** Incluye las rutas de las aplicaciones.

### Path Converters
Puedes capturar valores de la URL para pasarlos como argumentos a tus vistas.

```python
# urls.py
path('cursos/<int:curso_id>/', views.detalle_curso)
```

*   `int`: Coincide con cero o más enteros.
*   `slug`: Coincide con una cadena slug (letras, números, guiones, guiones bajos).
*   `str`: Coincide con cualquier cadena no vacía (por defecto).

---
[Volver al índice](../README.md)
