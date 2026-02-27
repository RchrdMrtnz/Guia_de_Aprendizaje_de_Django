from django import forms
from .models import Curso
from django.core.exceptions import ValidationError


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descripcion', 'fecha_inicio']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
        help_texts = {
            'titulo': 'El nombre del curso debe ser descriptivo.',
        }

    def clean_titulo(self):
        """Validación personalizada: Evitar títulos todo en mayúsculas."""
        titulo = self.cleaned_data.get('titulo')
        if titulo.isupper():
            raise ValidationError(
                "El título no puede estar escrito completamente en mayúsculas."
            )
        return titulo
