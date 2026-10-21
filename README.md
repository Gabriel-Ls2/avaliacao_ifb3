# API de Filmes

API REST para consultar e gerenciar filmes e gêneros, desenvolvida com Django e Django REST Framework. O projeto utiliza Django-Filter para filtros de pesquisa e SQLite para armazenar os dados. Também conta com autenticação por token e uma interface administrativa para gerenciar os registros.

**Repositório:** [avaliacao_ifb3](https://github.com/Gabriel-Ls2/avaliacao_ifb3)

## Tecnologias utilizadas

- Python 3.12 ou superior
- Django
- Django REST Framework
- Django-Filter
- SQLite
- Git

## Estrutura dos dados

O projeto possui dois recursos principais:

- **Gêneros:** nome.
- **Filmes:** título, descrição, ano de lançamento, gênero e duração.

Cada filme está associado a um gênero por meio de uma chave estrangeira.

## Requisitos

- Python 3.12 ou superior
- Git

## Clonar e iniciar

### Windows — PowerShell

Execute os seguintes comandos no terminal:

```powershell
git clone https://github.com/Gabriel-Ls2/avaliacao_ifb3.git
cd projeto_avaliativo

python -m venv venv
.\venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Se o PowerShell bloquear a ativação do ambiente virtual, consulte a [documentação sobre políticas de execução do PowerShell](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_execution_policies/) ou utilize o CMD.

### Windows — CMD

```bat
git clone https://github.com/Gabriel-Ls2/avaliacao_ifb3.git
cd projeto_avaliativo

python -m venv venv
venv\Scripts\activate

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Linux ou macOS

```bash
git clone https://github.com/Gabriel-Ls2/avaliacao_ifb3.git
cd projeto_avaliativo

python3 -m venv venv
source venv/bin/activate

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Após iniciar o servidor, a aplicação estará disponível em:

http://127.0.0.1:8000/

## Banco de dados

O projeto utiliza SQLite para armazenar os dados. Após clonar o repositório, execute as migrações para criar as tabelas do banco de dados local.

```bash
python manage.py migrate
```

### Importação de dados iniciais (opcional)

Execute o comando abaixo para importar os dados:

```bash
python importarDados.py
```

Execute a importação apenas uma vez por banco de dados, pois o script pode inserir registros duplicados.

## Endpoints

A API disponibiliza os seguintes endpoints:

| Recurso | Endpoint |
|---|---|
| API | `http://127.0.0.1:8000/api/` |
| Gêneros | `http://127.0.0.1:8000/api/generos/` |
| Filmes | `http://127.0.0.1:8000/api/filmes/` |
| Administração Django | `http://127.0.0.1:8000/admin/` |

Os endpoints de filmes e gêneros permitem operações CRUD:

- **GET:** listar e consultar registros.
- **POST:** cadastrar novos registros.
- **PUT/PATCH:** atualizar registros existentes.
- **DELETE:** excluir registros.

## Filtros de pesquisa

A listagem de filmes pode aceitar filtros de acordo com os campos configurados no projeto.

Exemplos de consulta:

```text
http://127.0.0.1:8000/api/filmes/?titulo=Interestelar
http://127.0.0.1:8000/api/filmes/?ano_lancamento=2014
http://127.0.0.1:8000/api/filmes/?genero=1
```

Os filtros disponíveis dependem da configuração realizada no `views.py`.

## Autenticação

A API utiliza autenticação por token e autenticação por sessão. Conforme as permissões configuradas, as consultas de leitura podem ser realizadas sem autenticação, enquanto as operações de escrita exigem autenticação.

## Criar usuário administrador

Para acessar a interface administrativa do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

Siga as instruções do terminal para definir as credenciais. Depois, acesse:

http://127.0.0.1:8000/admin/

