from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from conceptos_basicos.models import Curso, Categoria
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class CursoAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.categoria = Categoria.objects.create(nombre="Test Categoria", slug="test-cat")
        self.curso_data = {
            "titulo": "Curso API Test",
            "descripcion": "Descripcion de prueba",
            "categoria": self.categoria.id,
            "nivel": "BASICO",
            "precio": "10.00",
            "publicado": True,
            "fecha_inicio": timezone.now().date(),
        }
        self.curso = Curso.objects.create(
            titulo="Curso Existente",
            descripcion="Desc",
            categoria=self.categoria,
            nivel="BASICO",
            precio=20.00,
            publicado=True,
            fecha_inicio=timezone.now().date()
        )

    def test_list_cursos(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('curso-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_curso(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('curso-list')
        response = self.client.post(url, self.curso_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Curso.objects.count(), 2)
        self.assertEqual(Curso.objects.get(titulo="Curso API Test").categoria, self.categoria)

    def test_unauthenticated_access_denied(self):
        url = reverse('curso-list')
        # Probar GET
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Probar POST
        response = self.client.post(url, self.curso_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
