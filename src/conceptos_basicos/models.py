from django.db import models
from django.db.models import Case, When, Value, BooleanField
from django.utils.text import slugify
from django.utils import timezone
import datetime

class CursoQuerySet(models.QuerySet):
    def with_es_reciente(self):
        """Annotates the queryset with _es_reciente boolean."""
        threshold = timezone.now() - datetime.timedelta(days=30)
        return self.annotate(
            _es_reciente=Case(
                When(creado_en__gte=threshold, then=Value(True)),
                default=Value(False),
                output_field=BooleanField()
            )
        )

class CursoManager(models.Manager):
    def get_queryset(self):
        return CursoQuerySet(self.model, using=self._db)

    def with_es_reciente(self):
        return self.get_queryset().with_es_reciente()

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    NIVEL_CHOICES = [
        ('BASICO', 'Básico'),
        ('INTERMEDIO', 'Intermedio'),
        ('AVANZADO', 'Avanzado'),
    ]

    objects = CursoManager()

    titulo = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Slug URL")
    descripcion = models.TextField(verbose_name="Descripción")

    # Nuevo Campo: Relación Uno a Muchos
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name="cursos", verbose_name="Categoría")

    # Nuevos Campos: Tipos de datos variados
    nivel = models.CharField(max_length=10, choices=NIVEL_CHOICES, default='BASICO', verbose_name="Nivel")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Precio")
    publicado = models.BooleanField(default=False, verbose_name="¿Publicado?")

    fecha_inicio = models.DateField(db_index=True, verbose_name="Fecha de Inicio")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-fecha_inicio']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    @property
    def es_reciente(self):
        # Optimización: si ya viene anotado de la BD, usamos ese valor
        if hasattr(self, '_es_reciente'):
            return self._es_reciente
        # Fallback para casos donde no se usó with_es_reciente()
        return self.creado_en >= timezone.now() - datetime.timedelta(days=30)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    # Relación Muchos a Muchos
    cursos = models.ManyToManyField(Curso, related_name="estudiantes", verbose_name="Cursos Inscritos")

    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return self.nombre

class PerfilEstudiante(models.Model):
    # Relación Uno a Uno
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, related_name="perfil")
    bio = models.TextField(blank=True, verbose_name="Biografía")
    website = models.URLField(blank=True, verbose_name="Sitio Web")

    class Meta:
        verbose_name = "Perfil de Estudiante"
        verbose_name_plural = "Perfiles de Estudiante"

    def __str__(self):
        return f"Perfil de {self.estudiante.nombre}"
