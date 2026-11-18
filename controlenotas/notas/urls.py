from django.urls import path
from . import views

urlpatterns = [
    path('contato/', views.cadastro_contato, name='cadastro_contato'),
]