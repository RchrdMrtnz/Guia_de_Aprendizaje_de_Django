from django.contrib.auth.mixins import PermissionRequiredMixin

class TeacherRequiredMixin(PermissionRequiredMixin):
    """
    Mixin para asegurar que el usuario tenga permisos de profesor.
    Verifica explícitamente el permiso 'add_curso' en lugar de comparar el rol.
    """
    permission_required = 'conceptos_basicos.add_curso'
    # raise_exception = False (Default):
    # - Si no está logueado -> Redirige a Login
    # - Si está logueado sin permisos -> 403 Forbidden
