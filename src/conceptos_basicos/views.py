from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from users.mixins import TeacherRequiredMixin
from .models import Curso
from .forms import CursoForm
from .serializers import CursoSerializer

# --- FUNCTION BASED VIEWS (FBV) ---

def lista_cursos(request):
    cursos = Curso.objects.with_es_reciente().all()
    # Versión simple sin templates (para demos)
    return HttpResponse(f"<h1>Listado de Cursos (FBV)</h1><p>Cursos encontrados: {cursos.count()}</p>")

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    return HttpResponse(f"<h1>{curso.titulo} (FBV)</h1><p>{curso.descripcion}</p>")


# --- CLASS BASED VIEWS (CBV) ---

class CursoListView(ListView):
    model = Curso
    template_name = "conceptos_basicos/curso_list.html"
    context_object_name = "cursos"

    def get_queryset(self):
        # Ejemplo de filtro personalizado: solo cursos recientes o todos
        return Curso.objects.select_related('categoria').with_es_reciente().all()

class CursoDetailView(DetailView):
    model = Curso
    template_name = "conceptos_basicos/curso_detail.html"
    context_object_name = "curso"

class CursoCreateView(TeacherRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = "conceptos_basicos/curso_form.html"
    success_url = reverse_lazy('curso_list_cbv')

class RegistroView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


# --- DRF VIEWSETS ---

class CursoViewSet(viewsets.ModelViewSet):
    serializer_class = CursoSerializer

    def get_queryset(self):
        return Curso.objects.with_es_reciente().all()
