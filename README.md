# Redis-social-network

---

##  Descrição do Projeto
O **Redis-social-network** é uma ferramenta de linha de comando (CLI) que simula uma rede social simples.  
Com ela, é possível criar usuários, publicar comentários e interagir com postagens por meio de curtidas.

O projeto tem como foco principal demonstrar, na prática, a integração do Redis com aplicações Python.

---

##  Funcionalidades Principais

-  **CRUD de Usuários**  
  Criação, leitura, atualização e remoção de usuários.

-  **Gerenciamento de Comentários**  
  Criação, listagem e exclusão de comentários.

-  **Interações**  
  Possibilidade de curtir comentários.

-  **Listagens**  
  Visualização de todos os usuários ativos e comentários disponíveis.

---

##  Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| **FastAPI** | Framework para construção da API |
| **redis-py** | Cliente Python para integração com Redis |
| **httpx** | Biblioteca para requisições HTTP assíncronas |
| **rich** | Formatação de saída no terminal e melhorias visuais |
| **pytest / pytest-asyncio** | Testes automatizados com suporte assíncrono |
| **Docker / Docker Compose** | Containerização do Redis |

---

<br/>

## Intuito do Projeto

Este projeto foi desenvolvido com o objetivo de aprofundar conhecimentos no uso do Redis em conjunto com Python.
Embora o Redis não seja tradicionalmente utilizado como banco de dados principal, nesse projeto utilizei ele apenas para fins de aprendizagem.


## Considerações

- **Autenticação e Segurança**: A implementação de autenticação baseada em tokens (ex: JWT) é uma melhoria futura.
- **Performance do Redis**:  A alta performace do redis foi muito notavel, operando em mémoria ele deixava as requisões estremamente rápidas
- **Aprendizados com FastAPI**: Foram explorados conceitos mais avançados como lifespan, que inicialmente apresentou desafios, mas trouxe grande aprendizado.

<br/>

---

## Contribuição
Sinta-se à vontade para abrir uma issue, sugerir melhorias, fazer um fork do projeto ou implementar novas funcionalidades (como autenticação)

---
<br/>

##  Como Executar o Projeto


### Pré-requisitos
- Python 3.10+
- Docker 

### Passos:

#### Clone o repositório
```
  git clone https://github.com/vitorhugo8899o-lgtm/fastapi-redis-comments.git
```


#### Mude para a pasta do dirétorio
```
  cd fastapi-redis-comments
```

#### Suba o container do Redis
```
  docker-compose up -d
```

#### Instale as dependências
```
  poetry install  # caso utilize o poetry
  pip install -r requirements.txt
```

#### Execute a aplicação
```
  python -m CLI.script
```
