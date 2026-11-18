from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from notas import views as notas_views

router = DefaultRouter()
router.register("alunos", notas_views.AlunoViewSet, basename="aluno")

urlpatterns = [
    path("", lambda request: redirect("/admin/")),
    path("admin/", admin.site.urls),
    path("api/exemplo/alunos/", notas_views.alunos_json, name="exemplo_alunos_json"),
    path("alunos/", notas_views.AlunoListCreateView.as_view(), name="aluno-list-create"),
    path("alunos/<int:pk>/", notas_views.AlunoDetailView.as_view(), name="aluno-detail"),
    path("api/login/", obtain_auth_token, name="api-token-auth"),
    path("api/", include(router.urls)),
    path("notas/", include("notas.urls")),
]