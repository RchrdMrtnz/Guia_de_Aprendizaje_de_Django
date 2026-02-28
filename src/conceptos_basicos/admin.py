from django.contrib import admin
from .models import Curso, Estudiante


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_inicio', 'creado_en', 'es_reciente_display')
    list_filter = ('fecha_inicio', 'creado_en')
    search_fields = ('titulo', 'descripcion')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha_inicio'
    actions = ['marcar_como_archivado']

    def get_queryset(self, request):
        return super().get_queryset(request).with_es_reciente()

    @admin.display(boolean=True, description='¿Es reciente?')
    def es_reciente_display(self, obj):
        return obj.es_reciente

    def marcar_como_archivado(self, request, queryset):
        # Ejemplo de acción personalizada (aunque no tenemos campo 'archivado',
        # es demostrativo)
        self.message_user(
            request, f"{queryset.count()} cursos seleccionados para archivar."
        )
    marcar_como_archivado.short_description = (
        "Marcar cursos seleccionados como archivados"
    )


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_registro')
    search_fields = ('nombre', 'email')
    filter_horizontal = ('cursos',)  # Widget mejorado para ManyToMany
