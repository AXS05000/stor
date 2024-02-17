# urls.py

from django.urls import path
from .views import (
    listar_documentos,
    upload_documento,
    download_documentos_colaborador,
    home_listar_documentos,
)

urlpatterns = [
    path("listagem/", listar_documentos, name="listar_documentos"),
    path("home/", home_listar_documentos, name="home_listar_documentos"),
    path("upload_documentos/", upload_documento, name="upload_documento"),
    path(
        "download/documentos/<int:colaborador_id>/",
        download_documentos_colaborador,
        name="download_documentos_colaborador",
    ),
]
