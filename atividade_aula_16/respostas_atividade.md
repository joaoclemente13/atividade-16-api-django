# Atividade 16 — Projeto API Django

## Parte 1 — Questões teóricas

1. **`render()` e `JsonResponse()`:** `render()` combina uma requisição com um template e retorna uma página HTML, normalmente com contexto. `JsonResponse()` serializa dados para JSON e retorna uma resposta adequada para uma API.
2. **`safe=False`:** por padrão, `JsonResponse` aceita um dicionário como objeto JSON de nível superior. Use `safe=False` quando o valor de nível superior for outro tipo, como uma lista. Isso permite a resposta; não valida nem protege os dados.
3. **`ModelForm` e `ModelSerializer`:** `ModelForm` cria/valida formulários HTML vinculados a um model. `ModelSerializer` do DRF converte instâncias e dados em representações para API, valida a entrada e facilita operações de criação e atualização.
4. **Views genéricas:** `ListCreateAPIView` fornece listagem (`GET`) e criação (`POST`). `RetrieveUpdateDestroyAPIView` fornece consulta de um registro (`GET`), atualização completa (`PUT`), atualização parcial (`PATCH`) e remoção (`DELETE`).
5. **Token e Stateless:** o cliente envia o token em cada requisição, normalmente no cabeçalho `Authorization: Token <chave>`. Assim, a API não depende de uma sessão de navegador entre requisições. A implementação padrão de TokenAuthentication do DRF consulta tokens armazenados no servidor; portanto, ela não é totalmente sem estado no sentido de não manter qualquer estado no servidor.

## Parte 2 — Complete o comando

1. Instalação do pacote: `pip install djangorestframework`.
2. Ativação no projeto: incluir `'rest_framework'` em `INSTALLED_APPS`.
3. Serializer associado a um model: criar uma classe que herde de `serializers.ModelSerializer` e declarar o model e os campos em `Meta`.
4. View genérica para listar e criar: `generics.ListCreateAPIView`.
5. View genérica para consultar, atualizar e excluir um item: `generics.RetrieveUpdateDestroyAPIView`.
6. Registro e resposta: adicionar as views em `urlpatterns` com `path()`. Quando um `POST` cria um recurso com sucesso, o código HTTP apropriado é **201 Created**.

## Parte 3 — Encontre o erro

### Cenário A — Lista retornada como JSON

**Erro:** `JsonResponse(alunos)` usa o padrão `safe=True`, que espera um dicionário. Para uma lista no nível superior, ocorre `TypeError`.

**Correção:**

```python
return JsonResponse(alunos, safe=False)
```

Uma alternativa é envolver a lista em um dicionário, por exemplo `JsonResponse({"alunos": alunos})`.

### Cenário B — API sem autenticação e permissões

**Problema:** sem classes de autenticação e permissão, endpoints podem ficar acessíveis a clientes não autenticados, dependendo da configuração global do DRF.

**Correção:** exigir autenticação por token e usuário autenticado nas views protegidas:

```python
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

authentication_classes = [TokenAuthentication]
permission_classes = [IsAuthenticated]
```

O cliente deve enviar `Authorization: Token <chave>`. O endpoint de obtenção do token é a exceção: ele precisa aceitar as credenciais para emitir o token.

## Verificação do projeto

- **Já existia:** `AlunoSerializer`, `alunos_json` com `safe=False`, DRF e `rest_framework.authtoken` em `INSTALLED_APPS`, e CRUD por `AlunoViewSet` registrado em `DefaultRouter` sob `/api/alunos/`. O `ModelViewSet` já exige `TokenAuthentication` e `IsAuthenticated`. O CRUD foi preservado; conforme informado na atividade, já havia sido implementado e testado.
- **Implementado nesta atividade:** `AlunoListCreateView` em `/alunos/`, `AlunoDetailView` em `/alunos/<int:pk>/` e obtenção de token em `/api/login/`. As duas views genéricas também exigem autenticação por token e usuário autenticado.
- **Confirmado por comando:** `manage.py check` terminou com `System check identified no issues (0 silenced)`. A inspeção do URL resolver confirmou as rotas do roteador `/api/alunos/` e `/api/alunos/<pk>/`, as novas rotas genéricas e `/api/login/`. Chamadas sem token às duas views genéricas retornaram HTTP 401.
- **Pendente no Postman/Insomnia:** exercitar emissão de token com credenciais válidas e operações autenticadas de criação, leitura, atualização e exclusão. O CRUD não foi reexecutado nesta etapa. Nenhum aluno foi criado, alterado ou excluído durante esta verificação.

### Desafio extra — `ModelViewSet` + `DefaultRouter`

O projeto já registra `AlunoViewSet` em um `DefaultRouter` com o prefixo `alunos`. Isso oferece as rotas REST sob `/api/alunos/` sem declarar cada ação individualmente: coleção para listar/criar e item identificado pela chave primária para consultar/atualizar/excluir. O viewset usa o `AlunoSerializer` e restringe o acesso a usuários autenticados por token. A implementação foi preservada, sem recriação.
