from rest_framework import serializers

from .models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            "id",
            "nome",
            "matricula",
            "nota",
            "aprovado",
            "data_nascimento",
            "turma",
        ]
        read_only_fields = ["id"]
