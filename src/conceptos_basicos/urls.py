from django.urls import path
from . import views

urlpatterns = [
    # FBV URLs
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),

    # CBV URLs
    path('cbv/cursos/', views.CursoListView.as_view(), name='curso_list_cbv'),
    path('cbv/cursos/nuevo/', views.CursoCreateView.as_view(), name='curso_create_cbv'),
    path('cbv/cursos/<slug:slug>/', views.CursoDetailView.as_view(), name='curso_detail_cbv'),

    # Registro
    path('registro/', views.RegistroView.as_view(), name='registro'),
]
