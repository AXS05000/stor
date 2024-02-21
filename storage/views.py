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
from django.utils import timezone
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def listar_documentos(request):
    documentos = DocumentoColaborador.objects.all()
    for documento in documentos:
        tamanho_total_bytes = 0
        campos_documentos = [
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
            # Adicione outros campos conforme necessário
        ]

        for campo in campos_documentos:
            arquivo = getattr(documento, campo, None)
            if arquivo:
                tamanho_total_bytes += arquivo.size

        # Convertendo bytes para megabytes e atribuindo ao objeto documento para acesso no template
        documento.tamanho_mb = tamanho_total_bytes / (1024 * 1024)

    return render(request, "listar_documentos.html", {"documentos": documentos})


class HomeListarDocumentosView(ListView):
    model = DocumentoColaborador
    template_name = "index.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        order_by = self.request.GET.get("order_by", "-id")
        if query:
            return DocumentoColaborador.objects.filter(
                Q(nome__icontains=query)
            ).order_by(order_by)
        return DocumentoColaborador.objects.all().order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoje = timezone.now().date()
        cadastros_hoje = DocumentoColaborador.objects.filter(
            data_de_criacao=hoje
        ).count()
        documentos = context["object_list"]
        incompletos = 0
        tamanho_total_bytes = 0

        campos_documentos = [
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

        for documento in documentos:
            tamanho_documento_bytes = sum(
                getattr(documento, campo).size if getattr(documento, campo) else 0
                for campo in campos_documentos
            )
            tamanho_total_bytes += tamanho_documento_bytes
            documento.tamanho_mb = tamanho_documento_bytes / (1024 * 1024)
            if not all(getattr(documento, campo) for campo in campos_documentos[:3]):
                incompletos += 1

        tamanho_total_mb = tamanho_total_bytes / (1024 * 1024)
        total_colaboradores = DocumentoColaborador.objects.count()
        if tamanho_total_mb >= 1024:
            context["espaco_utilizado"] = f"{tamanho_total_mb / 1024:.2f} GB"
        else:
            context["espaco_utilizado"] = f"{tamanho_total_mb:.2f} MB"

        context["incompletos"] = incompletos
        context["total_colaboradores"] = total_colaboradores
        context["cadastros_hoje"] = (
            cadastros_hoje  # Adiciona a contagem de cadastros de hoje ao contexto
        )

        return context


def upload_documento(request):
    if request.method == "POST":
        form = DocumentoColaboradorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = DocumentoColaboradorForm()
    return render(request, "upload_documento.html", {"form": form})


def download_documentos_colaborador(request, colaborador_id):
    colaborador = DocumentoColaborador.objects.get(id=colaborador_id)
    documentos = [
        colaborador.rg_frente,
        colaborador.rg_costas,
        colaborador.cpf,
        colaborador.certidao_nascimento,
        colaborador.cnh_frente,
        colaborador.cnh_costas,
        colaborador.carteira_de_trabalho_pag_1,
        colaborador.carteira_de_trabalho_pag_2,
        colaborador.carteira_de_vascinacao,
        colaborador.comprovante_de_escolaridade,
        colaborador.comprovante_de_residencia,
        colaborador.curriculo,
        colaborador.exame_admissional,
        colaborador.formulario_odonto,
        colaborador.formulario_vt,
        colaborador.formulario_plano_de_saude,
        colaborador.reservista,
        colaborador.titulo_de_eleitor_frente,
        colaborador.titulo_de_eleitor_costas,
        colaborador.sus_frente,
        colaborador.sus_costas,
        colaborador.conta_bancaria,
        colaborador.pis,
        # Inclua outros campos conforme necessário
    ]

    response = HttpResponse(content_type="application/zip")
    zip_file = BytesIO()
    with zipfile.ZipFile(zip_file, "w") as zf:
        for documento in documentos:
            if documento and hasattr(documento, "read"):
                nome_arquivo = documento.name.split("/")[-1]
                arquivo_em_memoria = documento.read()
                zf.writestr(nome_arquivo, arquivo_em_memoria)

    response["Content-Disposition"] = (
        f"attachment; filename={colaborador.nome.replace(' ', '_')}.zip"
    )
    zip_file.seek(0)
    response.write(zip_file.read())
    return response


def forms(request, exception):
    return render(request, "forms.html")


class FormsView(CreateView):
    model = DocumentoColaborador
    form_class = DocumentoColaboradorForm
    template_name = "forms.html"
    success_url = reverse_lazy("index")
