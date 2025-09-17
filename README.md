# 📊 Projeto: Leitor e Analisador de Planilhas Excel com Flask

## 📌 Descrição
Este projeto é uma aplicação web simples feita com **Flask** e **Pandas** que permite:

- Fazer upload de uma planilha Excel (`.xlsx`).
- Exibir as **primeiras linhas da planilha**.
- Detectar **colunas numéricas**.
- Calcular estatísticas automáticas (**soma, média, mínimo e máximo**).
- Mostrar os resultados em uma página web estilizada com **Bootstrap**.

---

## 📂 Estrutura de Pastas

automacao_planilhas/\
│ ├── app.py # código Flask (rotas e interface web)\
│ ├── analise.py # funções de análise de dados com pandas\
│ └── templates/\
│ └── index.html # página HTML (interface do usuário)


---

## ⚙️ Dependências
Antes de rodar o projeto, instale as bibliotecas necessárias:

```bash
pip install flask pandas openpyxl

```

---

## 🚀 Como rodar o projeto

- Rode o servidor Flask:

```bash
python app.py

```


- Abra no navegador:

👉 http://127.0.0.1:5000

- Para encerrar o programa, aperte Ctrl+c

