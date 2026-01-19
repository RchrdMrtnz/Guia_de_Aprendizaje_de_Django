# 7. Administración Profesional

El panel de administración de Django es una de sus "killer features". Con muy poca configuración, obtienes una interfaz CRUD completa y gestionable.

## Personalización con `ModelAdmin`
Para ir más allá del registro básico, usamos clases que heredan de `admin.ModelAdmin`.

### Configuración Común
*   `list_display`: Qué columnas mostrar en la lista de objetos.
*   `list_filter`: Filtros laterales (por fecha, booleano, relación).
*   `search_fields`: Barra de búsqueda (busca en los campos indicados).
*   `prepopulated_fields`: Rellena campos automáticamente (ideal para slugs).
*   `filter_horizontal`: Widget de doble caja para selección múltiple (ManyToMany).

### Ejemplo (ver `src/conceptos_basicos/admin.py`)

```python
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_inicio', 'es_reciente')
    list_filter = ('fecha_inicio',)
    search_fields = ('titulo', 'descripcion')
    prepopulated_fields = {'slug': ('titulo',)}
```

## Campos Calculados en el Admin
Puedes añadir columnas que no existen en la base de datos pero que son calculadas por métodos del modelo o del Admin.

```python
    @admin.display(boolean=True, description='¿Es reciente?')
    def es_reciente_display(self, obj):
        return obj.es_reciente
```

## Acciones Personalizadas
Puedes agregar acciones al desplegable "Action" para procesar lotes de objetos.

```python
    actions = ['marcar_como_archivado']

    def marcar_como_archivado(self, request, queryset):
        count = queryset.update(activo=False)
        self.message_user(request, f"{count} cursos archivados.")
```

---
[Siguiente: Temas Avanzados y Optimización](./08_avanzado.md)
