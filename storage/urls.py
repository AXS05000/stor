# urls.py

from django.urls import path
from .views import (
    listar_documentos,
    upload_documento,
    download_documentos_colaborador,
    HomeListarDocumentosView,
)

urlpatterns = [
    path("listagem/", listar_documentos, name="listar_documentos"),
    path("home/", HomeListarDocumentosView.as_view(), name="home_listar_documentos"),
    path("upload_documentos/", upload_documento, name="upload_documento"),
    path(
        "download/documentos/<int:colaborador_id>/",
        download_documentos_colaborador,
        name="download_documentos_colaborador",
    ),
]
