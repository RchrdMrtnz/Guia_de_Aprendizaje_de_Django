from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistroViewTest(TestCase):
    def test_registro_page_loads(self):
        """Prueba que se puede acceder a la página de registro (GET)."""
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        # Verificar que el formulario está en el contexto y es del tipo correcto
        from users.forms import CustomUserCreationForm
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

    def test_registro_form_submission_success(self):
        """Prueba que un usuario puede registrarse exitosamente con datos válidos."""
        datos = {
            'username': 'nuevousuario',
            'password1': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(reverse('registro'), datos)

        # Debe redirigir al login tras el éxito (302)
        self.assertRedirects(response, reverse('login'))

        # Verificar que el usuario se creó en la base de datos
        self.assertTrue(User.objects.filter(username='nuevousuario').exists())

        # Verificar que el usuario tiene el rol por defecto (STUDENT)
        user = User.objects.get(username='nuevousuario')
        self.assertEqual(user.role, 'STUDENT')

    def test_registro_form_submission_error(self):
        """Prueba que el registro falla si las contraseñas no coinciden."""
        datos = {
            'username': 'errorusuario',
            'password1': 'password123',
            'password2': 'diferente456',
        }
        response = self.client.post(reverse('registro'), datos)

        # No debe redirigir, debe volver a mostrar el formulario (200)
        self.assertEqual(response.status_code, 200)

        # Verificar que el usuario NO se creó
        self.assertFalse(User.objects.filter(username='errorusuario').exists())

        # Verificar que hay errores en el formulario
        form = response.context['form']
        self.assertTrue(form.errors)
        # UserCreationForm pone el error de coincidencia en __all__ o en password2 dependiendo de la versión
        # Pero podemos verificar que el form no es válido.
        self.assertFalse(form.is_valid())
