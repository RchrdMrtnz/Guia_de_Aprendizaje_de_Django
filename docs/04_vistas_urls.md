# 4. Vistas y URLs: Profundización

## Class-Based Views (CBVs)
Las Vistas Basadas en Clases son una forma poderosa de escribir vistas en Django, permitiendo reutilizar código y organizar la lógica de manera orientada a objetos.

### Ventajas de las CBVs
*   **Reutilización de código:** A través de la herencia y Mixins.
*   **Vistas Genéricas:** Django incluye vistas para tareas comunes (listar, ver detalle, crear, editar, borrar).

### Vistas Genéricas Comunes
1.  **ListView:** Muestra una lista de objetos.
2.  **DetailView:** Muestra los detalles de un solo objeto.
3.  **CreateView / UpdateView / DeleteView:** Manejan formularios para editar datos.

### Ejemplo de Implementación (ver `src/conceptos_basicos/views.py`)

```python
from django.views.generic import ListView, DetailView
from .models import Curso

class CursoListView(ListView):
    model = Curso
    template_name = "conceptos_basicos/curso_list.html" # Plantilla a usar
    context_object_name = "cursos" # Nombre de la variable en el template

    def get_queryset(self):
        """Podemos sobrescribir este método para filtrar datos."""
        return Curso.objects.filter(fecha_inicio__year=2023)

class CursoDetailView(DetailView):
    model = Curso
    # Busca por 'pk' o 'slug' automáticamente
```

## Configuración de URLs para CBVs

Para usar una CBV en `urls.py`, debemos llamar al método `.as_view()`.

```python
# urls.py
from .views import CursoListView, CursoDetailView

urlpatterns = [
    path('cursos/', CursoListView.as_view(), name='curso_list'),
    path('curso/<slug:slug>/', CursoDetailView.as_view(), name='curso_detail'),
]
```

### Resultado Visual
Así se ve la lista de cursos generada con nuestras Vistas Basadas en Clases y plantillas:

![Listado de Cursos](img/lista_cursos.png)

Y el detalle de un curso:

![Detalle de Curso](img/detalle_curso.png)

## Mixins
Los Mixins son clases que aportan funcionalidad extra a una vista.
*   `LoginRequiredMixin`: Requiere que el usuario esté logueado.
*   `PermissionRequiredMixin`: Requiere permisos específicos.

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    fields = ['titulo', 'descripcion']
```

---
[Siguiente: Plantillas y Archivos Estáticos](./05_plantillas.md)
