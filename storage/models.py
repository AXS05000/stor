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
        instance.nome_colaborador.replace(" ", "_"),
        new_filename,
    )


def rg_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "rg")


def cpf_directory_path(instance, filename):
    return documento_colaborador_directory_path(instance, filename, "cpf")


def certidao_nascimento_directory_path(instance, filename):
    return documento_colaborador_directory_path(
        instance, filename, "certidao_nascimento"
    )


class DocumentoColaborador(models.Model):
    nome_colaborador = models.CharField(max_length=100)
    rg = models.FileField(upload_to=rg_directory_path, blank=True, null=True)
    cpf = models.FileField(upload_to=cpf_directory_path, blank=True, null=True)
    certidao_nascimento = models.FileField(
        upload_to=certidao_nascimento_directory_path, blank=True, null=True
    )

    def __str__(self):
        return self.nome_colaborador
