from django.test import TestCase
from django.utils import timezone
from conceptos_basicos.models import Curso
import datetime


class CursoEsRecienteTest(TestCase):
    def setUp(self):
        self.ahora = timezone.now()

    def test_es_reciente_fallback_nuevo(self):
        """Prueba el fallback de es_reciente para un curso recién creado."""
        curso = Curso.objects.create(
            titulo="Curso Reciente",
            descripcion="Prueba",
            fecha_inicio=self.ahora.date()
        )
        # No usamos with_es_reciente(), así que debería usar el fallback
        self.assertFalse(hasattr(curso, '_es_reciente'))
        self.assertTrue(curso.es_reciente)

    def test_es_reciente_fallback_antiguo(self):
        """Prueba el fallback de es_reciente para un curso antiguo."""
        curso = Curso.objects.create(
            titulo="Curso Antiguo",
            descripcion="Prueba",
            fecha_inicio=self.ahora.date()
        )
        # Forzamos una fecha de creación antigua en la DB
        antiguedad = self.ahora - datetime.timedelta(days=31)
        Curso.objects.filter(id=curso.id).update(creado_en=antiguedad)

        curso.refresh_from_db()
        self.assertFalse(hasattr(curso, '_es_reciente'))
        self.assertFalse(curso.es_reciente)

    def test_es_reciente_anotado(self):
        """Prueba que es_reciente use el atributo anotado de la base de datos."""
        # 1. Curso reciente
        Curso.objects.create(
            titulo="Reciente",
            descripcion="Prueba",
            fecha_inicio=self.ahora.date()
        )

        # 2. Curso antiguo
        curso_antiguo = Curso.objects.create(
            titulo="Antiguo",
            descripcion="Prueba",
            fecha_inicio=self.ahora.date()
        )
        antiguedad = self.ahora - datetime.timedelta(days=31)
        Curso.objects.filter(id=curso_antiguo.id).update(creado_en=antiguedad)

        # Consultamos usando with_es_reciente()
        queryset = Curso.objects.with_es_reciente()

        curso_reciente_anotado = queryset.get(titulo="Reciente")
        curso_antiguo_anotado = queryset.get(titulo="Antiguo")

        # Verificamos que tengan el atributo de anotación
        self.assertTrue(hasattr(curso_reciente_anotado, '_es_reciente'))
        self.assertTrue(hasattr(curso_antiguo_anotado, '_es_reciente'))

        # Verificamos que la propiedad use ese atributo
        self.assertTrue(curso_reciente_anotado.es_reciente)
        self.assertFalse(curso_antiguo_anotado.es_reciente)
