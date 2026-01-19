# 8. Temas Avanzados y Optimización

Para llevar tus habilidades de Django al nivel profesional, es crucial entender cómo optimizar tus consultas y cómo exponer tu aplicación al mundo a través de APIs.

## Optimización de Consultas (Database Performance)
El problema "N+1" es el asesino de rendimiento más común en Django. Ocurre cuando accedes a datos relacionados dentro de un bucle.

### `select_related`
Úsalo para relaciones "Uno a Uno" o "Muchos a Uno" (ForeignKey). Realiza un SQL JOIN.

```python
# Malo: N+1 consultas
libros = Libro.objects.all()
for libro in libros:
    print(libro.autor.nombre) # ¡Hace una consulta extra por cada libro!

# Bueno: 1 consulta única
libros = Libro.objects.select_related('autor').all()
for libro in libros:
    print(libro.autor.nombre) # Los datos ya están en memoria
```

### `prefetch_related`
Úsalo para relaciones "Muchos a Muchos" o "Inversas". Hace dos consultas y une los resultados en Python.

```python
# Traer todos los estudiantes y sus cursos eficientemente
estudiantes = Estudiante.objects.prefetch_related('cursos').all()
```

## Django REST Framework (DRF)
Hoy en día, es común que el backend sirva datos JSON para un frontend en React/Vue o una App Móvil. DRF es el estándar para esto.

### Serializers
Convierten tus modelos a JSON.

```python
from rest_framework import serializers

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
```

### ViewSets
Manejan la lógica CRUD automáticamente.

```python
from rest_framework import viewsets

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
```

## Recursos para Profundizar
*   [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/): Herramienta indispensable para ver las consultas SQL que hace tu vista.
*   [Celery](https://docs.celeryproject.org/): Para tareas en segundo plano (emails, procesamiento de imágenes).
*   [Channels](https://channels.readthedocs.io/): Para WebSockets y tiempo real.

---
[Volver al índice](index.md)
