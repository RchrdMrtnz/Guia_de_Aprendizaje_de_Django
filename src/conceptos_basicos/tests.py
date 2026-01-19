from django.test import TestCase
from django.urls import reverse
from .models import Curso, Estudiante
from django.utils import timezone
import datetime

class CursoModelTest(TestCase):
    def test_crear_curso(self):
        """Prueba que se puede crear un curso correctamente."""
        curso = Curso.objects.create(
            titulo="Django Básico",
            descripcion="Curso de introducción",
            fecha_inicio=datetime.date.today()
        )
        self.assertEqual(curso.titulo, "Django Básico")
        self.assertTrue(isinstance(curso, Curso))
        self.assertEqual(str(curso), "Django Básico")

class EstudianteModelTest(TestCase):
    def test_crear_estudiante(self):
        """Prueba que se puede crear un estudiante y asignarle cursos."""
        curso = Curso.objects.create(
            titulo="Python 101",
            descripcion="Intro a Python",
            fecha_inicio=datetime.date.today()
        )
        estudiante = Estudiante.objects.create(
            nombre="Juan Perez",
            email="juan@example.com"
        )
        estudiante.cursos.add(curso)

        self.assertEqual(estudiante.cursos.count(), 1)
        self.assertEqual(estudiante.cursos.first(), curso)

class VistasTest(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            titulo="Curso de Prueba",
            descripcion="Descripcion de prueba",
            fecha_inicio=datetime.date.today()
        )

    def test_lista_cursos_view(self):
        """Prueba que la vista de lista devuelve 200 y contiene el curso."""
        url = reverse('lista_cursos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Curso de Prueba")

    def test_detalle_curso_view(self):
        """Prueba que la vista de detalle devuelve 200 y el contenido correcto."""
        url = reverse('detalle_curso', args=[self.curso.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Curso de Prueba")
        self.assertContains(response, "Descripcion de prueba")
