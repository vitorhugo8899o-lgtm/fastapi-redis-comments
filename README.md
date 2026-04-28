# 🚀 FastAPI Redis Comments - Social Network CLI Simulator

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135.1-009485)](https://fastapi.tiangolo.com/)
[![Redis](https://img.shields.io/badge/Redis-7.3.0-DC382D)](https://redis.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📋 Sobre o Projeto

**FastAPI Redis Comments** é um simulador de rede social desenvolvido em **linha de comando (CLI)** que demonstra a integração prática do **Redis** com aplicações **Python** e **FastAPI**.

O projeto permite criar usuários, publicar comentários e gerenciar interações em tempo real, com toda a velocidade e eficiência que o Redis oferece.

### 🎯 Objetivo Principal
Explorar conceitos avançados em desenvolvimento Python, incluindo:
- Integração com Redis para armazenamento em memória
- Desenvolvimento assíncrono com FastAPI
- Gerenciamento de lifespan (contexto) de aplicações
- Boas práticas em testes automatizados
- CLI interativa para interação com dados

---

## ✨ Funcionalidades Principais

### 👥 **CRUD de Usuários**
- ✅ Criar novos usuários
- ✅ Listar todos os usuários ativos
- ✅ Atualizar informações de usuários
- ✅ Remover usuários

### 💬 **Gerenciamento de Comentários**
- ✅ Criar e publicar comentários
- ✅ Listar todos os comentários disponíveis
- ✅ Deletar comentários (autenticação futura)
- ✅ Vincular comentários a usuários específicos

### 👍 **Interações Sociais**
- ✅ Curtir/descurtir comentários
- ✅ Rastrear número de curtidas por comentário
- ✅ Visualizar estatísticas de engajamento

### 📊 **Listagens e Visualizações**
- ✅ Dashboard com todos os usuários
- ✅ Feed de comentários em tempo real
- ✅ Estatísticas de atividade (melhorias visuais com Rich)

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
| :--- | :--- | :--- |
| **Python** | 3.13+ | Linguagem de programação |
| **FastAPI** | 0.135.1+ | Framework web assíncrono de alta performance |
| **Redis** | 7.3.0+ | Banco de dados em memória para armazenamento rápido |
| **redis-py** | 7.3.0+ | Cliente Python para integração com Redis |
| **httpx** | 0.28.1+ | Cliente HTTP assíncrono para requisições |
| **Rich** | 14.3.3+ | Formatação avançada de output no terminal |
| **asgi-lifespan** | 2.1.0+ | Gerenciamento de contexto de aplicação ASGI |
| **Pydantic** | 2.12.5+ | Validação de dados com type hints |
| **pytest** | 9.0.2+ | Framework de testes automatizados |
| **pytest-asyncio** | 1.3.0+ | Suporte assíncrono para pytest |
| **Docker/Compose** | Latest | Containerização e orquestração |
| **Ruff** | 0.15.7+ | Linter e formatador ultrarrápido |

---

## 📁 Estrutura do Projeto

```
fastapi-redis-comments/
├── app/                          # Aplicação principal FastAPI
│   ├── main.py                  # Ponto de entrada da API
│   ├── models/                  # Modelos Pydantic
│   ├── routes/                  # Endpoints da API
│   ├── services/                # Lógica de negócio
│   └── redis_client.py          # Configuração Redis
│
├── CLI/                          # Interface de linha de comando
│   └── script.py                # Script principal CLI
│
├── tests/                        # Suite de testes
│   ├── test_users.py            # Testes de usuários
│   ├── test_comments.py         # Testes de comentários
│   └── test_interactions.py      # Testes de interações
│
├── docker-compose.yml           # Configuração Docker
├── pyproject.toml               # Configuração Poetry
├── requirements.txt             # Dependências pip
├── poetry.lock                  # Lock file Poetry
└── README.md                    # Este arquivo
```

---

## 🚀 Como Executar o Projeto

### 📋 Pré-requisitos

Certifique-se de ter instalado:
- **Python 3.13+** ([Download](https://www.python.org/downloads/))
- **Docker** ([Download](https://www.docker.com/get-started))
- **Docker Compose** (incluído com Docker Desktop)

Opcionalmente:
- **Poetry** ([Download](https://python-poetry.org/)) - Gerenciador de dependências alternativo

### 📝 Passo a Passo

#### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/vitorhugo8899o-lgtm/fastapi-redis-comments.git
cd fastapi-redis-comments
```

#### 2️⃣ Inicie o Redis com Docker
```bash
docker-compose up -d
```

Verifique se o Redis está rodando:
```bash
docker-compose ps
```

#### 3️⃣ Instale as Dependências

**Opção A: Com Poetry (Recomendado)**
```bash
poetry install
poetry shell
```

**Opção B: Com pip**
```bash
pip install -r requirements.txt
```

#### 4️⃣ Execute a Aplicação

**Rodando o CLI (Simulador de Rede Social)**
```bash
python -m CLI.script
```

**Rodando a API FastAPI em desenvolvimento**
```bash
poetry run run
# ou
fastapi dev app/main.py
```

A API estará disponível em: `http://localhost:8000`
Documentação interativa (Swagger): `http://localhost:8000/docs`

---

## 🧪 Testes

### Executar Todos os Testes
```bash
poetry run test
# ou
pytest -s -x --cov=app -vv
```

### Executar com Coverage
```bash
poetry run test
# Relatório HTML será gerado em: htmlcov/index.html
```

### Executar Testes Específicos
```bash
pytest tests/test_users.py -v
pytest tests/test_comments.py -v
```

---

## 🔍 Linting e Formatação

### Verificar Código (Ruff)
```bash
poetry run lint
# ou
ruff check .
```

### Formatar Código Automaticamente
```bash
poetry run format
# ou
ruff format .
```

---

## 💡 Aprendizados e Considerações

### 🎓 Principais Aprendizados
- **FastAPI Lifespan**: Exploração de conceitos avançados de contexto de aplicação (apresentou desafios inicialmente)
- **Performance do Redis**: Observou-se performance excepcional operando em memória, resultando em requisições extremamente rápidas
- **Async/Await**: Implementação completa com suporte assíncrono nativo
- **Validação com Pydantic**: Type hints e validação automática de dados

### 🔮 Próximas Melhorias

| Feature | Descrição | Prioridade |
|---------|-----------|-----------|
| **Autenticação JWT** | Implementar tokens JWT para segurança | 🔴 Alta |
| **Autorização** | Controle granular de acesso a recursos | 🟠 Média |
| **Persistência** | Integrar banco de dados relacional (PostgreSQL) | 🟠 Média |
| **Rate Limiting** | Limitar requisições por usuário | 🟠 Média |
| **Logging Estruturado** | Adicionar logging centralizado | 🟡 Baixa |
| **CI/CD** | Pipeline GitHub Actions | 🟡 Baixa |
| **Documentação API** | Expandir documentação de endpoints | 🟡 Baixa |

### ⚠️ Considerações Importantes

> ⚠️ **Nota sobre Redis**: Embora o Redis não seja tradicionalmente utilizado como banco de dados principal, neste projeto foi utilizado especificamente para fins de aprendizagem e demonstração de integração. Para produção com persistência de dados, considere uma solução de banco de dados relacional ou noSQL apropriada.

---

## 📚 Exemplos de Uso

### Criar um Usuário
```python
POST /api/users
{
  "name": "João Silva",
  "email": "joao@example.com"
}
```

### Publicar um Comentário
```python
POST /api/comments
{
  "user_id": "user_123",
  "content": "Olá, mundo! 🚀"
}
```

### Curtir um Comentário
```python
POST /api/comments/{comment_id}/like
{
  "user_id": "user_456"
}
```

### Listar Comentários
```python
GET /api/comments?limit=20&offset=0
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para:
- 🐛 Abrir issues para reportar bugs
- 💡 Sugerir novas funcionalidades
- 🍴 Fazer um fork e criar pull requests
- 📝 Melhorar a documentação
- 🔐 Implementar autenticação e segurança

### Processo de Contribuição
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Add: MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📧 Contato

- **Autor**: Vítor Hugo
- **Email**: [vitorhugo8899o@gmail.com](mailto:vitorhugo8899o@gmail.com)
- **GitHub**: [@vitorhugo8899o-lgtm](https://github.com/vitorhugo8899o-lgtm)

---

## 🔗 Recursos Úteis

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Redis Documentation](https://redis.io/documentation)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python Async/Await](https://docs.python.org/3/library/asyncio.html)
- [Docker Documentation](https://docs.docker.com/)

---

**Desenvolvido com ❤️ em Python**

⭐ Se este projeto foi útil, considere dar uma estrela!
