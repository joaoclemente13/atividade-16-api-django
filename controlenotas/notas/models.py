from django.db import models


class Turma(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)

    nota = models.DecimalField(
        max_digits=4,
        decimal_places=1
    )

    aprovado = models.BooleanField(default=False)

    data_nascimento = models.DateField(
        null=True,
        blank=True
    )

    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome