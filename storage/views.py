from django.shortcuts import render, redirect
from .forms import DocumentoColaboradorForm
from .models import DocumentoColaborador
from django.utils.text import slugify
import zipfile
from django.http import HttpResponse
from django.core.files.base import ContentFile
from io import BytesIO


def listar_documentos(request):
    documentos = DocumentoColaborador.objects.all()
    return render(request, "listar_documentos.html", {"documentos": documentos})


def upload_documento(request):
    if request.method == "POST":
        form = DocumentoColaboradorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listar_documentos")
    else:
        form = DocumentoColaboradorForm()
    return render(request, "upload_documento.html", {"form": form})


def download_documentos_colaborador(request, colaborador_id):
    colaborador = DocumentoColaborador.objects.get(id=colaborador_id)
    documentos = [
        colaborador.rg,
        colaborador.cpf,
        colaborador.certidao_nascimento,
    ]  # ajuste conforme necessário

    response = HttpResponse(content_type="application/zip")
    zip_file = BytesIO()
    with zipfile.ZipFile(zip_file, "w") as zf:
        for documento in documentos:
            if documento:
                nome_arquivo = documento.name.split("/")[-1]
                arquivo_em_memoria = documento.read()
                zf.writestr(nome_arquivo, arquivo_em_memoria)

    response["Content-Disposition"] = (
        f"attachment; filename={colaborador.nome_colaborador}.zip"
    )
    zip_file.seek(0)
    response.write(zip_file.read())
    return response
