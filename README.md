<div align="center">

# 🚀 B2B SaaS Tech Platform & Lead Engine

**Plataforma de Alta Performance para Serviços B2B em Nuvem, IA Agêntica e Engenharia de Dados**

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38BDF8?style=for-the-badge&logo=tailwind-css&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📌 Sobre o Projeto

Uma **Landing Page B2B High-Tech** completa, integrada a uma API backend moderna para captação, validação, persistência relacional de leads e envio instantâneo de notificações por e-mail.

O projeto foi projetado seguindo as melhores práticas de arquitetura **Cloud-Native**, utilizando um ecossistema conteinerizado em **Docker & Docker Compose** com **Django 5** e **PostgreSQL**.

### 🌟 Diferenciais
* 🎨 **Interface Dark/SaaS High-Tech:** Construída com Tailwind CSS, ícones FontAwesome e componentes em estilo Glassmorphism.
* 🤖 **Demonstração de Stack Enterprise:** Apresenta conceitos de Engenharia de Dados (Arquitetura Medallion), Agentes de IA via Protocolo MCP e Backend em .NET/Python.
* 🧮 **Simulador/Calculadora de ROI Interativa:** Widget dinâmico em JavaScript para estimativa de economia em Cloud e ganho de eficiência operacional.
* ⚡ **API REST Assíncrona:** Endpoint `/api/leads/` pronto para consumo JSON via `POST`.
* 📧 **Serviço de Notificação SMTP:** Envio automático de e-mails detalhados a cada nova submissão de formulário.
* 🛡️ **Painel Administrativo Nativo:** Gestão e auditoria dos leads cadastrados via Django Admin.

---

## 🛠️ Arquitetura do Sistema

```
                        ┌────────────────────────────────────────┐
                        │      Landing Page (HTML5 + JS + CSS)   │
                        └───────────────────┬────────────────────┘
                                            │ POST /api/leads/
                                            ▼
                        ┌────────────────────────────────────────┐
                        │      Django Web Server (Gunicorn/Dev)  │
                        └─────────┬────────────────────┬─────────┘
                                  │                    │
          ┌───────────────────────▼──┐              ┌──▼────────────────────────┐
          │  PostgreSQL Database     │              │  SMTP Email Service       │
          │  (Persistência dos Leads)│              │  (Notificação Instantânea)│
          └──────────────────────────┘              └───────────────────────────┘
```

---

## 🧰 Stack Tecnológica

* **Frontend:** HTML5, JavaScript (ES6+ Async/Await), Tailwind CSS (CDN), FontAwesome 6.
* **Backend:** Python 3.11, Django 5.0, Django REST Framework / JSON Endpoints.
* **Gerenciador de Pacotes Python:** `uv` (Fast Python Package Installer) / `pip`.
* **Banco de Dados:** PostgreSQL 15 Alpine.
* **Infraestrutura e DevOps:** Docker & Docker Compose.

---

## 🗂️ Estrutura de Diretórios

```text
├── core/                   # Configurações globais do Django (settings, urls, wsgi)
├── leads/                  # App Django para captura e gerenciamento de leads
│   ├── admin.py            # Customização do painel Django Admin
│   ├── models.py           # Modelo Lead (nome, email, empresa, telefone, mensagem)
│   ├── views.py            # Controller para ingestão e disparo de e-mails
│   └── urls.py             # Rota do endpoint /api/leads/
├── templates/              # Arquivos HTML/Templates da aplicação
│   └── index.html          # Landing Page Principal
├── static/                 # Arquivos Estáticos (CSS, JS, Imagens)
│   └── js/
│       └── main.js         # Lógica do formulário e fetch assíncrono
├── .env.example            # Exemplo de variáveis de ambiente
├── Dockerfile              # Imagem do servidor de aplicação
├── docker-compose.yml      # Orquestração do Django + PostgreSQL
├── manage.py               # Utilitário CLI do Django
└── requirements.txt        # Dependências do projeto
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados na máquina.

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com base no modelo a seguir:

```env
SECRET_KEY=sua-chave-secreta-django
DEBUG=1

# Configurações do Banco PostgreSQL
DB_NAME=landingpage_db
DB_USER=landing_user
DB_PASSWORD=landing_password
DB_HOST=db
DB_PORT=5432

# Configurações de E-mail (SMTP)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=sua-senha-de-app
EMAIL_RECEIVER=seu-email-notificacao@empresa.com
```

### 3. Subir os Contêineres
Suba o ambiente em segundo plano:
```bash
docker compose up --build -d
```

### 4. Executar Migrações e Criar Superusuário
```bash
# Executar as migrações do banco de dados
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate

# Criar usuário de acesso ao Django Admin
docker compose exec web python manage.py createsuperuser
```

---

## 🌐 Endpoints e Acessos

| Serviço | URL | Descrição |
| :--- | :--- | :--- |
| **Landing Page** | `http://localhost:8000/` | Interface visual principal |
| **API Leads** | `http://localhost:8000/api/leads/` | Endpoint `POST` para recepção de novos leads |
| **Django Admin** | `http://localhost:8000/admin/` | Painel de controle e visualização do banco |

---

## 🧪 Testando a Ingestão de Leads via CLI

Você pode testar a API enviando uma requisição `POST` diretamente via `curl`:

```bash
curl -X POST http://localhost:8000/api/leads/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Executivo Teste",
    "email": "executivo@empresa.com",
    "company": "Tech Corp",
    "phone": "(11) 99999-9999",
    "service_interest": "Agentes de IA e MCP",
    "message": "Gostaria de agendar uma reunião técnica de diagnóstico."
  }'
```

---

## 📄 Licença

Este projeto está sob a licença [MIT](./LICENSE). Sinta-se livre para utilizar, modificar e distribuir.

---

<div align="center">

Desenvolvido por **[Seu Nome / Sua Empresa]** 🚀

</div>