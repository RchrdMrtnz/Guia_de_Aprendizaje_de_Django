from django.test import TestCase
from django.urls import reverse
from conceptos_basicos.models import Curso, Estudiante
from django.contrib.auth import get_user_model
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
        # Verificar generación automática de slug
        self.assertEqual(curso.slug, "django-basico")

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
        # Crear usuario para pruebas de autenticación
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_lista_cursos_view(self):
        """Prueba que la vista de lista devuelve 200 y contiene el conteo de cursos."""
        url = reverse('lista_cursos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cursos encontrados")

    def test_detalle_curso_view(self):
        """Prueba que la vista de detalle devuelve 200 y el contenido correcto."""
        url = reverse('detalle_curso', args=[self.curso.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Curso de Prueba")
        self.assertContains(response, "Descripcion de prueba")

    def test_lista_cursos_cbv(self):
        """Prueba la Class Based View de lista con template."""
        url = reverse('curso_list_cbv')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "conceptos_basicos/curso_list.html")
        self.assertContains(response, "Nuestros Cursos")

    def test_detalle_curso_cbv(self):
        """Prueba la Class Based View de detalle con template y slug."""
        url = reverse('curso_detail_cbv', args=[self.curso.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "conceptos_basicos/curso_detail.html")
        self.assertContains(response, self.curso.titulo)

    def test_crear_curso_requiere_login(self):
        """Prueba que crear curso redirige al login si no estás autenticado."""
        url = reverse('curso_create_cbv')
        response = self.client.get(url)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_crear_curso_view(self):
        """Prueba que se puede acceder al formulario y crear un curso (logeado)."""
        self.client.login(username='testuser', password='password123')
        url = reverse('curso_create_cbv')

        # GET request
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "conceptos_basicos/curso_form.html")

        # POST request (Crear)
        datos = {
            'titulo': 'Nuevo Curso Django',
            'descripcion': 'Descripción del nuevo curso',
            'fecha_inicio': datetime.date.today()
        }
        response = self.client.post(url, datos)
        # Debería redirigir tras el éxito
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Curso.objects.filter(titulo='Nuevo Curso Django').exists())

    def test_validacion_curso_form(self):
        """Prueba la validación personalizada del formulario (titulo mayúsculas)."""
        self.client.login(username='testuser', password='password123')
        url = reverse('curso_create_cbv')
        datos = {
            'titulo': 'TITULO EN MAYUSCULAS', # Esto debería fallar
            'descripcion': 'Test',
            'fecha_inicio': datetime.date.today()
        }
        response = self.client.post(url, datos)
        self.assertEqual(response.status_code, 200) # Se queda en la misma página (form invalido)

        # Verificar manualmente el error en el formulario del contexto
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('titulo', form.errors)
        self.assertEqual(form.errors['titulo'][0], "El título no puede estar escrito completamente en mayúsculas.")
