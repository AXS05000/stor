# urls.py

from django.urls import path
from .views import (
    listar_documentos,
    upload_documento,
    download_documentos_colaborador,
    HomeListarDocumentosView,
    FormsView,
)

urlpatterns = [
    path("", HomeListarDocumentosView.as_view(), name="index"),
    path("listagem/", listar_documentos, name="listar_documentos"),
    path("forms/", FormsView.as_view(), name="forms"),
    path("upload_documentos/", upload_documento, name="upload_documento"),
    path(
        "download/documentos/<int:colaborador_id>/",
        download_documentos_colaborador,
        name="download_documentos_colaborador",
    ),
]
