# Projeto Docker Compose: 5 Backends + 1 Frontend 🐳

Este repositório contém o resultado de uma atividade prática (Estudo Dirigido) focada em conteinerização e orquestração de microsserviços. O objetivo principal do projeto foi criar um ambiente completo, com múltiplas APIs independentes conversando com uma interface web, utilizando **Docker** e **Docker Compose**.

---

## 🏗️ Arquitetura do Projeto

O ecossistema é composto por **6 serviços** rodando em containers isolados, conectados através da rede interna do Docker Compose:

| Serviço | Descrição |
|---|---|
| **Frontend** | Painel em HTML/JavaScript servido pelo Nginx |
| **Backend 1 — API de Usuários** | Retorna status e lê variáveis de ambiente |
| **Backend 2 — API de Produtos** | Retorna uma lista de dados mockados (produtos e preços) |
| **Backend 3 — API de Pedidos** | Retorna o status do serviço |
| **Backend 4 — API de Pagamentos** | Retorna o status do serviço |
| **Backend 5 — API de Relatórios** | Retorna o status do serviço |

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11** + **Flask** — Backends
- **HTML, CSS e Vanilla JavaScript** — Frontend
- **Nginx:alpine** — Servidor Web do Frontend
- **Docker** — Criação de Imagens e Containers
- **Docker Compose** — Orquestração e Rede

---

## 🎯 Desafios Concluídos

Durante o desenvolvimento, os seguintes desafios práticos foram implementados com sucesso:

- [x] Criação de mensagens personalizadas para cada serviço backend
- [x] Implementação de uma rota de verificação de integridade (`/health`) em todas as APIs
- [x] Modificação do Backend 2 para retornar uma lista de dados estruturados (mock de produtos)
- [x] Implementação de carregamento automático (auto-load) no Frontend, consumindo as APIs assim que a página é aberta
- [x] Injeção de Variáveis de Ambiente (`AMBIENTE=Desenvolvimento`) no Backend 1 via `docker-compose.yml`

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados
- Git para clonar o repositório

### Passo a passo

**1. Clone este repositório:**

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```

**2. Acesse a pasta do projeto:**

```bash
cd NOME_DO_REPOSITORIO
```

**3. Construa as imagens e suba os containers:**

```bash
docker compose up --build
```

**4. Acesse a aplicação no seu navegador:**

```
http://localhost:8080
```

---

## 🔌 Mapeamento de Portas

Caso queira testar as APIs individualmente, elas estão mapeadas nas seguintes portas do host:

| Serviço | Porta Host | Porta Container | Rota Principal | Rota de Health |
|---|---|---|---|---|
| Frontend | `8080` | `80` | http://localhost:8080/ | — |
| Backend 1 | `5001` | `5000` | http://localhost:5001/ | http://localhost:5001/health |
| Backend 2 | `5002` | `5000` | http://localhost:5002/ | http://localhost:5002/health |
| Backend 3 | `5003` | `5000` | http://localhost:5003/ | http://localhost:5003/health |
| Backend 4 | `5004` | `5000` | http://localhost:5004/ | http://localhost:5004/health |
| Backend 5 | `5005` | `5000` | http://localhost:5005/ | http://localhost:5005/health |

---

> Projeto desenvolvido para fins acadêmicos e estudo de DevOps/Conteinerização.
> 
> Aluno: Vinicius Gussoni Vellosa  R.A. 05222-031
> 
> Engenharia da Computação - Uniara - 2026
