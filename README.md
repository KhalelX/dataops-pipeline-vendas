# Pipeline de Dados Automatizado + Dashboard Power BI

Projeto completo simulando um fluxo real de **Engenharia de Dados até Business Intelligence**, automatizando o caminho do dado bruto até a visualização final.

---

## Objetivo

Construir um pipeline de dados que:

✔️ Recebe arquivos brutos (CSV/Excel)  
✔️ Realiza tratamento e padronização  
✔️ Carrega os dados em um banco SQLite  
✔️ Executa o fluxo automaticamente  
✔️ Disponibiliza os dados para análise no Power BI  

Este projeto demonstra na prática o ciclo completo do dado:  
**Dado Bruto → Tratamento → Banco → Dashboard**

---

## Arquitetura do Projeto


---

## ⚙️ Tecnologias Utilizadas

| Ferramenta | Finalidade |
|------------|------------|
| **Python** | Orquestração da pipeline |
| **Pandas** | Manipulação e tratamento de dados |
| **SQLAlchemy** | Conexão com banco de dados |
| **SQLite** | Armazenamento dos dados tratados |
| **Power BI** | Visualização e criação de dashboard |

---

## 🔄 Etapas da Pipeline

### 🟢 1. Ingestão (`ingestao.py`)
- Lê arquivos CSV e Excel da pasta `data_bruto`
- Consolida todos os dados em um único arquivo

### 🟡 2. Tratamento (`tratamento.py`)
- Padroniza nomes das colunas
- Remove linhas vazias
- Converte tipos de dados (ex: datas)
- Gera o arquivo `dados_tratados.csv`

### 🔵 3. Carga no Banco (`carga_banco.py`)
- Lê o arquivo tratado
- Insere os dados no banco SQLite
- Atualiza a tabela `fato_operacao`

### 🟣 4. Orquestração (`pipeline.py`)
Executa automaticamente todas as etapas na ordem correta.

---

## ▶️ Como Executar o Projeto

### 1️⃣ Ativar o ambiente virtual

```bash
.\.venv\Scripts\activate
