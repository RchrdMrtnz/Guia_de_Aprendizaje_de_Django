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

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new and self.role:
            from django.contrib.auth.models import Group
            # Usamos filter().first() para evitar crash si el grupo no existe aún (ej: bootstrapping)
            group = Group.objects.filter(name=self.role).first()
            if group:
                self.groups.add(group)
