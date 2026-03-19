# 📊 Sistema de Análise de Vendas

Dashboard web para gerenciar e analisar vendas de produtos, construído com **Python/Flask** e um frontend moderno.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| **Dashboard com métricas** | Cards exibindo total de vendas, quantidade, produto mais vendido e mais lucrativo |
| **Cadastro de vendas** | Formulário para adicionar novas vendas (produto, valor, data) |
| **Listagem de vendas** | Tabela com todas as vendas registradas |
| **Filtro por valor** | Filtrar vendas acima de um valor mínimo |
| **Análise automática** | Produto mais vendido, mais lucrativo e média de vendas por dia |

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

```bash
# Clone o repositório ou navegue até a pasta do projeto
cd vendas

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py
```

Acesse **http://localhost:5000** no navegador.

---

## 📁 Estrutura do Projeto

```
vendas/
├── app.py               # Servidor Flask + classes de negócio
├── requirements.txt     # Dependências Python
├── README.md            # Documentação
└── templates/
    └── index.html       # Frontend (HTML/CSS/JS)
```

---

## 🔌 API REST

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Página principal (dashboard) |
| `GET` | `/api/vendas` | Lista todas as vendas |
| `POST` | `/api/vendas` | Adiciona uma nova venda |
| `GET` | `/api/vendas/filtro?valor_minimo=X` | Filtra vendas acima do valor |
| `GET` | `/api/analise` | Retorna métricas e análises |

### Exemplo — Adicionar Venda

```bash
curl -X POST http://localhost:5000/api/vendas \
  -H "Content-Type: application/json" \
  -d '{"produto": "Mouse", "valor": 150.00, "data_venda": "2025-03-01"}'
```

---

## 🛠️ Tecnologias

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3 (vanilla), JavaScript (vanilla) — *Desenvolvido por IA*
- **Tipografia:** Google Fonts (Inter)
- **Design:** Dark theme, gradientes, micro-animações

---

## 📝 Classes Principais

### `Venda`
Representa uma venda individual com produto, valor e data.

### `AnaliseVendas`
Gerencia a lista de vendas e oferece métodos de análise:

- `adicionar_venda(venda)` — Adiciona uma venda à lista
- `vendas_acima_de(valor_minimo)` — Filtra vendas acima de um valor
- `total_vendas()` — Soma total de todas as vendas
- `total_vendas_periodo(inicio, fim)` — Total em um período específico
- `produto_mais_vendido()` — Produto com maior quantidade de vendas
- `produto_mais_lucrativo()` — Produto com maior receita total
- `media_vendas_por_dia()` — Média de valores vendidos por dia

---

# 📊 Sales Analysis System

Web dashboard to manage and analyze product sales, built with **Python/Flask** and a modern frontend.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)

---

## ✨ Features

| Feature | Description |
|---|---|
| **Dashboard with metrics** | Cards displaying total sales, quantity, best-selling product, and most profitable product |
| **Sales Registration** | Form to add new sales (product, value, date) |
| **Sales Listing** | Table with all registered sales |
| **Filter by Value** | Filter sales above a minimum value |
| **Automatic Analysis** | Best-selling product, most profitable product, and average sales per day |

---

## 🚀 How to Run

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository or navigate to the project folder
cd vendas

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Access **http://localhost:5000** in your browser.

---

## 📁 Project Structure

```
vendas/
├── app.py               # Flask server + business classes
├── requirements.txt     # Python dependencies
├── README.md            # Documentation
└── templates/
    └── index.html       # Frontend (HTML/CSS/JS)
```

---

## 🔌 REST API

| Method | Endpoint | Description |
|--------|----------|-----------|
| `GET` | `/` | Main page (dashboard) |
| `GET` | `/api/vendas` | Lists all sales |
| `POST` | `/api/vendas` | Adds a new sale |
| `GET` | `/api/vendas/filtro?valor_minimo=X` | Filters sales above the value |
| `GET` | `/api/analise` | Returns metrics and analysis |

### Example — Add Sale

```bash
curl -X POST http://localhost:5000/api/vendas \
  -H "Content-Type: application/json" \
  -d '{"produto": "Mouse", "valor": 150.00, "data_venda": "2025-03-01"}'
```

---

## 🛠️ Technologies

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3 (vanilla), JavaScript (vanilla) — *Developed by AI*
- **Typography:** Google Fonts (Inter)
- **Design:** Dark theme, gradients, micro-animations

---

## 📝 Main Classes

### `Venda`
Represents an individual sale with product, value, and date.

### `AnaliseVendas`
Manages the sales list and offers analysis methods:

- `adicionar_venda(venda)` — Adds a sale to the list
- `vendas_acima_de(valor_minimo)` — Filters sales above a value
- `total_vendas()` — Total sum of all sales
- `total_vendas_periodo(inicio, fim)` — Total in a specific period
- `produto_mais_vendido()` — Product with the highest quantity of sales
- `produto_mais_lucrativo()` — Product with the highest total revenue
- `media_vendas_por_dia()` — Average sales value per day
