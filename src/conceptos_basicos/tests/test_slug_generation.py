from django.test import TestCase
from django.utils.text import slugify
from conceptos_basicos.models import Curso
import datetime


class CursoSlugTest(TestCase):
    def test_basic_slug_generation(self):
        """Checks that a normal title generates the expected slug."""
        curso = Curso.objects.create(
            titulo="Django Básico",
            descripcion="Test",
            fecha_inicio=datetime.date.today()
        )
        self.assertEqual(curso.slug, "django-basico")

    def test_special_characters_slug(self):
        """Checks slug generation with special characters."""
        curso = Curso.objects.create(
            titulo="Django & Python: ¡Increíble!",
            descripcion="Test",
            fecha_inicio=datetime.date.today()
        )
        # slugify removes & and ! and converts : to nothing or handles it
        self.assertEqual(curso.slug, "django-python-increible")

    def test_accented_characters_slug(self):
        """Checks slug generation with accented characters."""
        curso = Curso.objects.create(
            titulo="Programación Avanzada en Ñandú",
            descripcion="Test",
            fecha_inicio=datetime.date.today()
        )
        self.assertEqual(curso.slug, "programacion-avanzada-en-nandu")

    def test_manual_slug_override(self):
        """Checks that a manually provided slug is not overwritten."""
        curso = Curso.objects.create(
            titulo="Título Original",
            slug="slug-manual-personalizado",
            descripcion="Test",
            fecha_inicio=datetime.date.today()
        )
        self.assertEqual(curso.slug, "slug-manual-personalizado")

    def test_slug_stability_on_update(self):
        """Checks that changing the title does not change an existing slug."""
        curso = Curso.objects.create(
            titulo="Título Inicial",
            descripcion="Test",
            fecha_inicio=datetime.date.today()
        )
        original_slug = curso.slug

        curso.titulo = "Título Modificado"
        curso.save()

        self.assertEqual(curso.slug, original_slug)
        self.assertNotEqual(slugify(curso.titulo), original_slug)

    def test_empty_result_slug(self):
        """Checks behavior when title would result in an empty slug (only symbols)."""
        curso = Curso.objects.create(
            titulo="!!!",
            descripcion="Test",
            fecha_inicio=datetime.date.today()
        )
        # slugify("!!!") is ""
        self.assertEqual(curso.slug, "")
