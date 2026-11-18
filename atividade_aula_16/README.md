# Atividade Aula 16 — API Django

Esta pasta contém somente as respostas e a documentação da atividade. O projeto Django existente permanece em `..\controlenotas`; ele não foi copiado para cá.

## Arquivos

- `respostas_atividade.md`: respostas teóricas, comandos, cenários de erro e resumo de verificação.

## Executar o projeto

Na raiz `BACKEND`, abra o PowerShell e execute:

```powershell
cd .\controlenotas
.\venv\Scripts\Activate.ps1
python manage.py check
python manage.py runserver
```

O projeto usa PostgreSQL e carrega suas configurações de conexão do arquivo `.env` do projeto. Mantenha esse arquivo local e não compartilhe credenciais. Não é necessário executar migrations para iniciar a atividade.

## Localizar a atividade

Volte à pasta `atividade_aula_16` e abra `respostas_atividade.md`. O resumo separa o que já existia, as alterações feitas, as verificações confirmadas e os testes manuais ainda pendentes no Postman/Insomnia.
