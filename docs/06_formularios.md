# 6. Formularios y Validación

Django facilita enormemente el manejo de formularios, encargándose de la renderización HTML, la validación de datos y la conversión a objetos Python.

## Tipos de Formularios
1.  **Form:** Formularios genéricos que no están directamente vinculados a un modelo.
2.  **ModelForm:** Formularios que se crean automáticamente a partir de un modelo existente.

## Creando un ModelForm
Definimos nuestros formularios en `forms.py`.

```python
from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descripcion', 'fecha_inicio']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
        }
```

## Validación Personalizada
Podemos añadir reglas de validación específicas sobrescribiendo el método `clean_<campo>`.

```python
from django.core.exceptions import ValidationError

def clean_titulo(self):
    titulo = self.cleaned_data.get('titulo')
    if titulo.isupper():
        raise ValidationError("El título no puede estar todo en mayúsculas.")
    return titulo
```

## Usando Formularios en Vistas (CreateView)
Las CBVs como `CreateView` y `UpdateView` se integran perfectamente con los formularios.

```python
class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = "curso_form.html"
    success_url = '/cursos/'
```

## Renderizado en Plantillas
Django ofrece métodos rápidos para renderizar formularios:
*   `{{ form.as_p }}`: Cada campo en un párrafo `<p>`.
*   `{{ form.as_table }}`: Como filas de tabla `<tr>`.
*   `{{ form.as_ul }}`: Como lista `<li>`.

Para mayor control, puedes iterar sobre los campos:
```html
{% for field in form %}
    <label>{{ field.label }}</label>
    {{ field }}
    {{ field.errors }}
{% endfor %}
```

---
[Siguiente: Administración Avanzada](./07_admin.md)
