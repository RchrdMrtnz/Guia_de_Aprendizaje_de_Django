# 3. Modelos y Bases de Datos: Profundización

Los modelos son la fuente única y definitiva de información sobre tus datos. Contienen los campos y comportamientos esenciales de los datos que estás almacenando. Django sigue el principio DRY (Don't Repeat Yourself).

## Definición Avanzada de Modelos
Además de los campos básicos, los modelos pueden contener metadatos, métodos personalizados y lógica de negocio.

### Ejemplo Completo (ver `src/conceptos_basicos/models.py`)

```python
from django.db import models
from django.utils.text import slugify

class Curso(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    # Slug: Cadena URL-friendly (ej: "curso-django-avanzado")
    slug = models.SlugField(unique=True, blank=True, null=True)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()

    # Campos de auditoría (timestamps)
    creado_en = models.DateTimeField(auto_now_add=True) # Se fija al crear
    actualizado_en = models.DateTimeField(auto_now=True) # Se actualiza al guardar

    # CLASE META: Opciones de configuración del modelo
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-fecha_inicio'] # Ordenar por defecto por fecha descendente

    # MÉTODOS MÁGICOS
    def __str__(self):
        return self.titulo

    # SOBRESCRIBIR SAVE: Lógica automática antes de guardar
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    # PROPIEDADES: Campos calculados que no se guardan en BD
    @property
    def es_reciente(self):
        from django.utils import timezone
        import datetime
        return self.creado_en >= timezone.now() - datetime.timedelta(days=30)
```

## Conceptos Clave

### 1. Clase Meta
Dentro de un modelo, la clase `Meta` se usa para definir opciones que no son campos.
*   `ordering`: Define el orden por defecto al hacer consultas (`Curso.objects.all()`).
*   `verbose_name` / `verbose_name_plural`: Nombres legibles para el panel de administración.
*   `indexes`: Para crear índices de base de datos y mejorar rendimiento.

### 2. Sobrescritura de `save()`
Es común sobrescribir `save()` para ejecutar lógica cada vez que un objeto se crea o modifica.
*   **Caso de uso:** Generar slugs, redimensionar imágenes, calcular totales.
*   **Importante:** Siempre llamar a `super().save()` al final para que Django guarde realmente el objeto.

### 3. Propiedades (`@property`)
Permiten añadir atributos al objeto que se calculan en tiempo de ejecución.
*   Ejemplo: `nombre_completo` uniendo `nombre` y `apellido`.
*   No se pueden usar directamente en filtros de base de datos (`filter()`), pero son muy útiles en templates y vistas.

### 4. Slugs
Un `Slug` es una etiqueta corta para algo, que contiene solo letras, números, guiones bajos o guiones. Generalmente se usan en URLs.
*   Ejemplo: `www.misitio.com/cursos/aprende-django-facil/` (donde `aprende-django-facil` es el slug).

---
[Siguiente: Vistas y URLs Avanzadas](./04_vistas_urls.md)
