from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class DashboardTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='password123'
        )
        self.url = reverse('dashboard')

    def test_dashboard_redirects_anonymous(self):
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_dashboard_accessible_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proyectos_reales/dashboard.html')
        self.assertTemplateUsed(response, 'proyectos_reales/base_dashboard.html')
