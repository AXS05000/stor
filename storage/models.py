from django.db import models
from django.utils.text import slugify
import os


def documento_colaborador_directory_path(instance, filename, doc_type):
    # Obter a extensão do arquivo original
    ext = filename.split(".")[-1]
    # Definir o novo nome do arquivo com base no tipo de documento
    new_filename = f"{doc_type}.{ext}"
    # Definir o caminho do diretório onde o arquivo será salvo
    return os.path.join(
        "uploads",
        "documentos",
        instance.nome.replace(" ", "_"),
        new_filename,
    )


def rg_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "rg")


def rg_frente_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "rg_frente")


def rg_costas_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "rg_costas")


def cpf_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "cpf")


def certidao_nascimento_directory_path(instance, filename):
    return documento_colaborador_directory_path(
        instance, filename, "certidao_nascimento"
    )


def cnh_frente_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "cnh_frente")


def cnh_costas_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "cnh_costas")


def carteira_de_trabalho_pag_1_directory_path(instance, filename):
    return documento_colaborador_directory_path(
        instance, filename, "carteira_de_trabalho_pag_1"
    )


def carteira_de_trabalho_pag_2_directory_path(instance, filename):
    return documento_colaborador_directory_path(
        instance, filename, "carteira_de_trabalho_pag_2"
    )


def carteira_de_vascinacao_directory_path(instance, filename):
    return documento_colaborador_directory_path(
        instance, filename, "carteira_de_vascinacao"
    )


def comprovante_de_escolaridade_directory_path(instance, filename):
    return documento_colaborador_directory_path(
        instance, filename, "comprovante_de_escolaridade"
    )


def comprovante_de_residencia_directory_path(instance, filename):
    return documento_colaborador_directory_path(
        instance, filename, "comprovante_de_residencia"
    )


def curriculo_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "curriculo")


def exame_admissional_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "exame_admissional")


def formulario_odonto_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "formulario_odonto")


def formulario_vt_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "formulario_vt")


def formulario_plano_de_saude_directory_path(instance, filename):
    return documento_colaborador_directory_path(
        instance, filename, "formulario_plano_de_saude"
    )


def reservista_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "reservista")


def titulo_de_eleitor_frente_directory_path(instance, filename):
    return documento_colaborador_directory_path(
        instance, filename, "titulo_de_eleitor_frente"
    )


def titulo_de_eleitor_costas_directory_path(instance, filename):
    return documento_colaborador_directory_path(
        instance, filename, "titulo_de_eleitor_costas"
    )


def sus_frente_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "sus_frente")


def sus_costas_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "sus_costas")


def conta_bancaria_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "conta_bancaria")


def pis_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "pis")


class DocumentoColaborador(models.Model):
    nome = models.CharField(max_length=100)
    rg_frente = models.FileField(
        upload_to=rg_frente_directory_path, blank=True, null=True
    )
    rg_costas = models.FileField(
        upload_to=rg_costas_directory_path, blank=True, null=True
    )
    cpf = models.FileField(upload_to=cpf_directory_path, blank=True, null=True)
    certidao_nascimento = models.FileField(
        upload_to=certidao_nascimento_directory_path, blank=True, null=True
    )
    cnh_frente = models.FileField(
        upload_to=cnh_frente_directory_path, blank=True, null=True
    )
    cnh_costas = models.FileField(
        upload_to=cnh_costas_directory_path, blank=True, null=True
    )
    carteira_de_trabalho_pag_1 = models.FileField(
        upload_to=carteira_de_trabalho_pag_1_directory_path, blank=True, null=True
    )
    carteira_de_trabalho_pag_2 = models.FileField(
        upload_to=carteira_de_trabalho_pag_2_directory_path, blank=True, null=True
    )
    carteira_de_vascinacao = models.FileField(
        upload_to=carteira_de_vascinacao_directory_path, blank=True, null=True
    )
    comprovante_de_escolaridade = models.FileField(
        upload_to=comprovante_de_escolaridade_directory_path, blank=True, null=True
    )
    comprovante_de_residencia = models.FileField(
        upload_to=comprovante_de_residencia_directory_path, blank=True, null=True
    )
    curriculo = models.FileField(
        upload_to=curriculo_directory_path, blank=True, null=True
    )
    exame_admissional = models.FileField(
        upload_to=exame_admissional_directory_path, blank=True, null=True
    )
    formulario_odonto = models.FileField(
        upload_to=formulario_odonto_directory_path, blank=True, null=True
    )
    formulario_vt = models.FileField(
        upload_to=formulario_vt_directory_path, blank=True, null=True
    )
    formulario_plano_de_saude = models.FileField(
        upload_to=formulario_plano_de_saude_directory_path, blank=True, null=True
    )
    reservista = models.FileField(
        upload_to=reservista_directory_path, blank=True, null=True
    )
    titulo_de_eleitor_frente = models.FileField(
        upload_to=titulo_de_eleitor_frente_directory_path, blank=True, null=True
    )
    titulo_de_eleitor_costas = models.FileField(
        upload_to=titulo_de_eleitor_costas_directory_path, blank=True, null=True
    )

    sus_frente = models.FileField(
        upload_to=sus_frente_directory_path, blank=True, null=True
    )
    sus_costas = models.FileField(
        upload_to=sus_costas_directory_path, blank=True, null=True
    )
    conta_bancaria = models.FileField(
        upload_to=conta_bancaria_directory_path, blank=True, null=True
    )
    pis = models.FileField(upload_to=pis_directory_path, blank=True, null=True)

    def __str__(self):
        return self.nome
