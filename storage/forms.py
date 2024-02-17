# forms.py

from django import forms
from django.core.exceptions import ValidationError
from .models import DocumentoColaborador

class DocumentoColaboradorForm(forms.ModelForm):
    class Meta:
        model = DocumentoColaborador
        fields = ['nome_colaborador', 'rg', 'cpf', 'certidao_nascimento']

    def clean(self):
        cleaned_data = super().clean()
        for field in ['rg', 'cpf', 'certidao_nascimento']:
            documento = cleaned_data.get(field)
            if documento:
                if not documento.name.lower().endswith('.pdf'):
                    self.add_error(field, 'Apenas arquivos PDF são permitidos.')
        return cleaned_data
