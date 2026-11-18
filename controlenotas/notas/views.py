from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .forms import ContatoForm
from .models import Aluno
from .serializers import AlunoSerializer


def cadastro_contato(request):
    form = ContatoForm()
    return render(
        request, "notas/contato.html", {"form": form}
    )


def alunos_json(request):
    alunos = list(Aluno.objects.values("id"))
    return JsonResponse(alunos, safe=False)


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class AlunoListCreateView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class AlunoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]