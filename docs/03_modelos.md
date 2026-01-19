# 3. Modelos y Bases de Datos

Los modelos son la fuente única y definitiva de información sobre tus datos. Contienen los campos y comportamientos esenciales de los datos que estás almacenando. Django sigue el principio DRY (Don't Repeat Yourself).

## Definición de Modelos
Los modelos se definen en el archivo `models.py` de tu aplicación. Cada modelo es una clase que hereda de `django.db.models.Model`.

### Ejemplo (ver `src/conceptos_basicos/models.py`)

En este repositorio, hemos creado dos modelos: `Curso` y `Estudiante`.

```python
from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    # Campos de auditoría automática
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
```

## Tipos de Campos Comunes
*   `CharField`: Para cadenas de texto cortas.
*   `TextField`: Para textos largos.
*   `DateField` / `DateTimeField`: Para fechas y horas.
*   `IntegerField`: Para números enteros.
*   `EmailField`: Valida que el texto sea un email.

## Relaciones
Django soporta los tres tipos de relaciones de bases de datos más comunes:

1.  **Muchos a Uno (Many-to-One):** Se define con `ForeignKey`.
2.  **Muchos a Muchos (Many-to-Many):** Se define con `ManyToManyField`.
3.  **Uno a Uno (One-to-One):** Se define con `OneToOneField`.

En nuestro ejemplo, un estudiante puede estar en muchos cursos y un curso puede tener muchos estudiantes:

```python
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    # Relación M2M
    cursos = models.ManyToManyField(Curso, related_name="estudiantes")
```

## Migraciones
Las migraciones son la forma en que Django propaga los cambios que haces en tus modelos (agregar un campo, borrar un modelo, etc.) a tu esquema de base de datos.

```bash
# Crear migraciones basadas en cambios en models.py
python manage.py makemigrations

# Aplicar las migraciones a la base de datos
python manage.py migrate
```

---
[Siguiente: Vistas y URLs](./04_vistas_urls.md)
