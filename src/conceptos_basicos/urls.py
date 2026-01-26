from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cursos', views.CursoViewSet)

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),

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
