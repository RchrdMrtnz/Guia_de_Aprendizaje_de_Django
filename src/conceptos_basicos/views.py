from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.html import format_html
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from users.mixins import TeacherRequiredMixin
from users.forms import CustomUserCreationForm
from .models import Curso
from .forms import CursoForm
from .serializers import CursoSerializer

# --- FUNCTION BASED VIEWS (FBV) ---

def lista_cursos(request):
    cursos = Curso.objects.with_es_reciente().all()
    # Versión simple sin templates (para demos)
    return HttpResponse(format_html("<h1>Listado de Cursos (FBV)</h1><p>Cursos encontrados: {}</p>", cursos.count()))

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    return HttpResponse(format_html("<h1>{} (FBV)</h1><p>{}</p>", curso.titulo, curso.descripcion))


# --- CLASS BASED VIEWS (CBV) ---

class CursoListView(ListView):
    model = Curso
    template_name = "conceptos_basicos/curso_list.html"
    context_object_name = "cursos"

    def get_queryset(self):
        # Ejemplo de filtro personalizado: solo cursos recientes o todos
        return Curso.objects.with_es_reciente().all()

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
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


# --- DRF VIEWSETS ---

class CursoViewSet(viewsets.ModelViewSet):
    serializer_class = CursoSerializer

    def get_queryset(self):
        return Curso.objects.with_es_reciente().all()
