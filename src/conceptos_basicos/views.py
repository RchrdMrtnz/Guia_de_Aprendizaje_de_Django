from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Curso

# Function Based View (FBV)
def lista_cursos(request):
    cursos = Curso.objects.all()
    # En un caso real usaríamos render() con un template, pero aquí usamos HttpResponse para simplificar
    # o podríamos armar un string simple.
    response_content = "<h1>Listado de Cursos</h1><ul>"
    for curso in cursos:
        response_content += f"<li>{curso.titulo} - {curso.fecha_inicio}</li>"
    response_content += "</ul>"
    return HttpResponse(response_content)

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    return HttpResponse(f"<h1>{curso.titulo}</h1><p>{curso.descripcion}</p>")
