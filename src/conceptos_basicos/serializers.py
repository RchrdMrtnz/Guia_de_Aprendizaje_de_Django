from rest_framework import serializers
from .models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = [
            'id', 'titulo', 'slug', 'descripcion', 'categoria',
            'nivel', 'precio', 'publicado', 'fecha_inicio',
            'creado_en', 'actualizado_en'
        ]
        read_only_fields = ['id', 'creado_en', 'actualizado_en']
