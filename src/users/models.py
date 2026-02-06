from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Administrador')
        TEACHER = 'TEACHER', _('Profesor')
        STUDENT = 'STUDENT', _('Estudiante')

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.STUDENT,
        verbose_name=_('Rol')
    )
