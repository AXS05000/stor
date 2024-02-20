from django.urls import include, path

from . import views

urlpatterns = [
    path("usuario/", include("django.contrib.auth.urls")),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
