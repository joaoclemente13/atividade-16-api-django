from django.contrib import admin
from .models import Aluno


class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "matricula",
        "nota",
        "aprovado",
    )

    search_fields = ("nome", "matricula")
    list_filter = ("aprovado",) 
    list_editable = ("aprovado",)

    actions = ["aprovar_alunos"]

    def aprovar_alunos(self, request, queryset):
        queryset.update(aprovado=True)

    aprovar_alunos.short_description = "Aprovar alunos selecionados"


admin.site.register(Aluno, AlunoAdmin)