from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from conceptos_basicos.models import Curso, Categoria
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.test.utils import CaptureQueriesContext
from django.db import connection

User = get_user_model()


class CursoAPIPerformanceTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.categoria = Categoria.objects.create(
            nombre="Test Categoria", slug="test-cat"
        )
        # Create multiple courses to make N+1 more apparent
        for i in range(10):
            Curso.objects.create(
                titulo=f"Curso {i}",
                descripcion=f"Desc {i}",
                categoria=self.categoria,
                nivel="BASICO",
                precio=20.00,
                publicado=True,
                fecha_inicio=timezone.now().date()
            )

    def test_list_cursos_query_count(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('curso-list')

        with CaptureQueriesContext(connection) as queries:
            response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

        print(f"\nNumber of queries: {len(queries)}")
        for i, query in enumerate(queries):
            print(f"Query {i+1}: {query['sql']}\n")
