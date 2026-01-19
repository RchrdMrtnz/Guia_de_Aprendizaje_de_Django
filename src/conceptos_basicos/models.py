from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

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
