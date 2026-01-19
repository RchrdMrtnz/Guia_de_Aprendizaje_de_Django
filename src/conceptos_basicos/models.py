from django.db import models
from django.utils.text import slugify
from django.utils import timezone
import datetime

class Curso(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    # Slug es una versión URL-friendly del título (ej: "curso-de-django")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Slug URL")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        """
        Sobrescribimos el método save para generar el slug automáticamente
        si no se ha proporcionado uno.
        """
        if not self.slug:
            self.slug = slugify(self.titulo)
            # Manejo básico de colisiones (en producción se requeriría algo más robusto)
            # Aquí confiamos en que el usuario pondrá títulos distintos o editará el slug si falla
        super().save(*args, **kwargs)

    @property
    def es_reciente(self):
        """Retorna True si el curso se creó en los últimos 30 días."""
        return self.creado_en >= timezone.now() - datetime.timedelta(days=30)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-fecha_inicio'] # Ordenar por defecto por fecha de inicio descendente

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    cursos = models.ManyToManyField(Curso, related_name="estudiantes", verbose_name="Cursos Inscritos")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
