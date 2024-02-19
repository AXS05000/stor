# forms.py

from django import forms
from django.core.exceptions import ValidationError
from .models import DocumentoColaborador


class DocumentoColaboradorForm(forms.ModelForm):
    class Meta:
        model = DocumentoColaborador
        fields = [
            "nome",
            "rg_frente",
            "rg_costas",
            "cpf",
            "certidao_nascimento",
            "cnh_frente",
            "cnh_costas",
            "carteira_de_trabalho_pag_1",
            "carteira_de_trabalho_pag_2",
            "carteira_de_vascinacao",
            "comprovante_de_escolaridade",
            "comprovante_de_residencia",
            "curriculo",
            "exame_admissional",
            "formulario_odonto",
            "formulario_vt",
            "formulario_plano_de_saude",
            "reservista",
            "titulo_de_eleitor_frente",
            "titulo_de_eleitor_costas",
            "sus_frente",
            "sus_costas",
            "conta_bancaria",
            "pis",
        ]

    def clean(self):
        cleaned_data = super().clean()
        for field in [
            "rg_frente",
            "rg_costas",
            "cpf",
            "certidao_nascimento",
            "cnh_frente",
            "cnh_costas",
            "carteira_de_trabalho_pag_1",
            "carteira_de_trabalho_pag_2",
            "carteira_de_vascinacao",
            "comprovante_de_escolaridade",
            "comprovante_de_residencia",
            "curriculo",
            "exame_admissional",
            "formulario_odonto",
            "formulario_vt",
            "formulario_plano_de_saude",
            "reservista",
            "titulo_de_eleitor_frente",
            "titulo_de_eleitor_costas",
            "sus_frente",
            "sus_costas",
            "conta_bancaria",
            "pis",
        ]:
            documento = cleaned_data.get(field)
            if documento:
                if not documento.name.lower().endswith(".pdf"):
                    self.add_error(field, "Apenas arquivos PDF são permitidos.")
        return cleaned_data
