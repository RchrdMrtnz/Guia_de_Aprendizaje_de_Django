from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser
from django.contrib.auth.models import Group


class PermissionTests(TestCase):
    def setUp(self):
        # Create users
        # The save() method of CustomUser + Data Migration ensures groups are assigned
        self.teacher = CustomUser.objects.create_user(
            username='teacher', password='password', role='TEACHER'
        )
        self.student = CustomUser.objects.create_user(
            username='student', password='password', role='STUDENT'
        )
        self.url = reverse('curso_create_cbv')

    def test_group_assignment(self):
        """Verifica que el grupo se asigna automáticamente al guardar el usuario."""
        teacher_group = Group.objects.get(name='TEACHER')
        student_group = Group.objects.get(name='STUDENT')

        self.assertIn(teacher_group, self.teacher.groups.all())
        self.assertIn(student_group, self.student.groups.all())

    def test_teacher_permissions(self):
        """Verifica que el profesor tiene el permiso add_curso."""
        # Esto confirma que la migración asignó el permiso al grupo
        self.assertTrue(self.teacher.has_perm('conceptos_basicos.add_curso'))

    def test_teacher_can_access_view(self):
        """El profesor debe poder acceder a la vista de crear curso."""
        self.client.force_login(self.teacher)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_student_cannot_access_view(self):
        """El estudiante debe recibir Forbidden (403)."""
        self.client.force_login(self.student)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
