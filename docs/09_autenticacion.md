# 9. Autenticación y Autorización

Django viene con un sistema de autenticación de usuario robusto que maneja cuentas de usuario, grupos, permisos y sesiones basadas en cookies.

## Configuración Básica

Para usar la autenticación predeterminada, incluye `django.contrib.auth.urls` en tu `urls.py`.

```python
# urls.py
path("accounts/", include("django.contrib.auth.urls")),
```

Esto habilita rutas como:
*   `/accounts/login/`
*   `/accounts/logout/`
*   `/accounts/password_change/`

## Vistas de Login y Logout
Por defecto, Django busca las plantillas en `registration/login.html`.

### Ejemplo `registration/login.html`

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Entrar</button>
</form>
```

Debes configurar hacia dónde redirigir tras el login en `settings.py`:

```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

## Registro de Usuarios
Django provee `UserCreationForm` para crear nuevos usuarios fácilmente.

```python
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

class RegistroView(CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = "registration/signup.html"
```

## Restringir Acceso (Autorización)
Para proteger vistas y asegurar que solo usuarios logueados accedan:

### En Vistas Basadas en Funciones (FBV)
Usa el decorador `@login_required`.

```python
from django.contrib.auth.decorators import login_required

@login_required
def mi_vista_protegida(request):
    ...
```

### En Vistas Basadas en Clases (CBV)
Usa el mixin `LoginRequiredMixin`.

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MiVistaProtegida(LoginRequiredMixin, ListView):
    ...
```

## Acceso en Plantillas
La variable `user` está disponible automáticamente en los templates.

```html
{% if user.is_authenticated %}
    <p>Hola, {{ user.username }}</p>
    <form action="{% url 'logout' %}" method="post">{% csrf_token %}<button>Salir</button></form>
{% else %}
    <a href="{% url 'login' %}">Entrar</a>
{% endif %}
```

---
[Volver al índice](index.md)
