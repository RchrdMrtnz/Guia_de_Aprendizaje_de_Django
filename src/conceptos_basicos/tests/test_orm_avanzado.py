from django.test import TestCase
from django.db.models import Q, Avg, Count, F
from conceptos_basicos.models import Curso, Categoria, Estudiante, PerfilEstudiante
from django.utils import timezone
import datetime


class ORMAvanzadoTest(TestCase):
    def setUp(self):
        # Setup Data
        self.cat_web = Categoria.objects.create(
            nombre="Desarrollo Web", slug="desarrollo-web"
        )
        self.cat_data = Categoria.objects.create(
            nombre="Data Science", slug="data-science"
        )

        self.curso_django = Curso.objects.create(
            titulo="Django Experto",
            categoria=self.cat_web,
            nivel="AVANZADO",
            precio=99.99,
            publicado=True,
            fecha_inicio=timezone.now().date()
        )
        self.curso_python = Curso.objects.create(
            titulo="Python Básico",
            categoria=self.cat_data,
            nivel="BASICO",
            precio=0.00,
            publicado=True,
            fecha_inicio=timezone.now().date() - datetime.timedelta(days=10)
        )
        self.curso_draft = Curso.objects.create(
            titulo="Borrador Secreto",
            categoria=self.cat_web,
            nivel="INTERMEDIO",
            precio=50.00,
            publicado=False,
            fecha_inicio=timezone.now().date() + datetime.timedelta(days=30)
        )

        self.est1 = Estudiante.objects.create(nombre="Juan", email="juan@example.com")
        self.est2 = Estudiante.objects.create(nombre="Maria", email="maria@example.com")

        # Relaciones
        self.est1.cursos.add(self.curso_django, self.curso_python)
        self.est2.cursos.add(self.curso_python)

        PerfilEstudiante.objects.create(
            estudiante=self.est1, bio="Pythonista", website="http://juan.dev"
        )

    def test_filtrado_basico(self):
        """Demuestra filter, exclude y get"""
        # Filter
        publicados = Curso.objects.filter(publicado=True)
        self.assertEqual(publicados.count(), 2)

        # Exclude
        gratuitos = Curso.objects.exclude(precio__gt=0)
        self.assertEqual(gratuitos.count(), 1)
        self.assertEqual(gratuitos.first(), self.curso_python)

        # Get
        curso = Curso.objects.get(slug="django-experto")
        self.assertEqual(curso.titulo, "Django Experto")

    def test_busquedas_avanzadas(self):
        """Demuestra lookups: __icontains, __gte, etc"""
        # Case-insensitive contain
        web_courses = Curso.objects.filter(titulo__icontains="django")
        self.assertTrue(web_courses.exists())

        # Relación inversa y spanning (buscando cursos de una categoria por
        # nombre de categoria)
        cursos_web = Curso.objects.filter(categoria__nombre="Desarrollo Web")
        self.assertEqual(cursos_web.count(), 2)  # Django + Borrador

    def test_consultas_complejas_Q(self):
        """Demuestra uso de Q objects para OR"""
        # Cursos que son GRATIS O son NIVEL AVANZADO
        query = Curso.objects.filter(Q(precio=0) | Q(nivel="AVANZADO"))
        self.assertEqual(query.count(), 2)  # Python (Gratis) + Django (Avanzado)

    def test_agregacion(self):
        """Demuestra Avg, Count"""
        # Precio promedio de cursos publicados
        promedio = Curso.objects.filter(publicado=True).aggregate(Avg('precio'))
        # (99.99 + 0) / 2 = 49.995
        self.assertAlmostEqual(float(promedio['precio__avg']), 49.995, places=2)

        # Anotación: Contar estudiantes por curso
        cursos_con_conteo = Curso.objects.annotate(num_estudiantes=Count('estudiantes'))
        c_python = cursos_con_conteo.get(titulo="Python Básico")
        self.assertEqual(c_python.num_estudiantes, 2)  # Juan y Maria

    def test_actualizacion_F(self):
        """Demuestra expresiones F para updates atómicos"""
        # Aumentar precio de todos los cursos web en un 10%
        Curso.objects.filter(categoria=self.cat_web).update(precio=F('precio') * 1.1)

        self.curso_django.refresh_from_db()
        # 99.99 * 1.1 = 109.989
        self.assertTrue(self.curso_django.precio > 100)
