from django.shortcuts import render, redirect
from .forms import DocumentoColaboradorForm
from .models import DocumentoColaborador
from django.utils.text import slugify
import zipfile
from django.http import HttpResponse
from django.core.files.base import ContentFile
from io import BytesIO
from django.views.generic import ListView
from django.db.models import Sum


def listar_documentos(request):
    documentos = DocumentoColaborador.objects.all()
    for documento in documentos:
        tamanho_total = 0
        if documento.rg:
            tamanho_total += documento.rg.size
        if documento.cpf:
            tamanho_total += documento.cpf.size
        if documento.certidao_nascimento:
            tamanho_total += documento.certidao_nascimento.size
        # Convertendo bytes para megabytes
        documento.tamanho_mb = tamanho_total / (1024 * 1024)
    return render(request, "listar_documentos.html", {"documentos": documentos})


class HomeListarDocumentosView(ListView):
    model = DocumentoColaborador
    template_name = "home.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documentos = context["object_list"]  # Aqui estamos utilizando a paginação
        incompletos = 0
        tamanho_total_bytes = 0

        for documento in documentos:
            tamanho_documento_bytes = 0
            if documento.rg:
                tamanho_documento_bytes += documento.rg.size
            if documento.cpf:
                tamanho_documento_bytes += documento.cpf.size
            if documento.certidao_nascimento:
                tamanho_documento_bytes += documento.certidao_nascimento.size

            tamanho_total_bytes += tamanho_documento_bytes

            # Aqui calculamos o tamanho em MB de cada documento e adicionamos como atributo do objeto
            documento.tamanho_mb = tamanho_documento_bytes / (1024 * 1024)

            if not (documento.rg and documento.cpf and documento.certidao_nascimento):
                incompletos += 1

        tamanho_total_mb = tamanho_total_bytes / (1024 * 1024)
        if tamanho_total_mb >= 1024:
            context["espaco_utilizado"] = f"{tamanho_total_mb / 1024:.2f} GB"
        else:
            context["espaco_utilizado"] = f"{tamanho_total_mb:.2f} MB"

        context["incompletos"] = incompletos

        return context


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
