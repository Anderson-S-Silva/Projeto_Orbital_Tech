# 💻 api-contatos: API de Gerenciamento de Contatos (Teste de Programação)

Este repositório contém a solução para o Teste de Programação, focado no desenvolvimento de uma API RESTful simples para gerenciamento de contatos, utilizando Python e o framework FastAPI.

O projeto foi desenvolvido com foco em **organização de código, clareza e boas práticas de programação**, conforme solicitado nas observações gerais do teste.

## 🚀 Tecnologias Utilizadas

*   **Linguagem:** Python 3.11+
*   **Framework Web:** [FastAPI](https://fastapi.tiangolo.com/) (para alta performance e documentação automática)
*   **Validação de Dados:** [Pydantic](https://docs.pydantic.dev/) (para tipagem e validação de schemas)
*   **Servidor:** [Uvicorn](https://www.uvicorn.org/) (servidor ASGI)
*   **Banco de Dados:** Simulação em memória (lista Python) para simplificar e focar na lógica da API.

## 📁 Estrutura do Projeto

```
api-contatos/
├── main.py             # Implementação da API (FastAPI, Schemas, Endpoints)
├── logica_programacao.py # Soluções para as Questões 08 e 09
├── README.md           # Este arquivo
└── venv/               # Ambiente virtual (ignorado pelo .gitignore)
```

## ⚙️ Instalação e Execução

### Pré-requisitos

Certifique-se de ter o Python 3.11 ou superior instalado.

### 1. Clonar o Repositório

```bash
git clone https://github.com/Anderson-S-Silva/Projeto_Orbital_Tech.git
cd Projeto_Orbital_Tech
```

### 2. Configurar o Ambiente Virtual

É altamente recomendado o uso de um ambiente virtual para isolar as dependências do projeto.

```bash
# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install fastapi uvicorn pydantic email-validator
```

### 4. Iniciar a API

Execute o servidor Uvicorn:

```bash
uvicorn main:app --reload
```

A API estará acessível em `http://127.0.0.1:8000`.

### 5. Acessar a Documentação

A documentação interativa (Swagger UI) estará disponível em:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

## 🌐 Endpoints da API (Questão 10)

A API implementa as operações CRUD (Create, Read, Update, Delete) para o gerenciamento de contatos.

| Método | Path | Descrição | Status Code |
| :--- | :--- | :--- | :--- |
| `POST` | `/contatos` | Cadastra um novo contato. | `201 Created` |
| `GET` | `/contatos` | Lista todos os contatos, ordenados por `nome_completo` e incluindo a `idade` calculada. | `200 OK` |
| `PUT` | `/contatos/{contato_id}` | Atualiza um contato existente pelo ID. | `200 OK` ou `404 Not Found` |
| `DELETE` | `/contatos/{contato_id}` | Remove um contato pelo ID. | `204 No Content` ou `404 Not Found` |

### Exemplo de Uso (cURL)

**1. Cadastro de Contato (POST)**
```bash
curl -X POST "http://127.0.0.1:8000/contatos" \
-H "Content-Type: application/json" \
-d '{
  "nome_completo": "Alice Silva",
  "data_nascimento": "1990-05-15",
  "email": "alice.silva@teste.com",
  "telefone": "11987654321",
  "endereco": "Rua A, 123"
}'
```

**2. Listagem de Contatos (GET)**
```bash
curl -X GET "http://127.0.0.1:8000/contatos"
```

## 🧠 Soluções de Lógica de Programação

As soluções para as questões 08 e 09 estão implementadas no arquivo `logica_programacao.py`.

### Questão 08: Cálculo de Imposto

Função que calcula o imposto com base no valor do produto:

```python
def calcular_imposto(valor_produto: float) -> float:
    if valor_produto >= 3000:
        aliquota = 0.18
    elif valor_produto >= 2000:
        aliquota = 0.15
    elif valor_produto >= 1000:
        aliquota = 0.12
    else:
        aliquota = 0.0
    
    return valor_produto * aliquota
```

### Questão 09: Relatório de Notas

Função que gera um relatório estatístico a partir de uma lista de notas:

```python
def gerar_relatorio_notas(notas: List[Union[int, float]]) -> Dict[str, Union[float, int, List[Union[int, float]]]]:
    # ... (Implementação completa no arquivo logica_programacao.py)
    # ...
    pass
```

## 📝 Relatório Final

O arquivo `resultado_teste_programacao.json` contém todas as respostas compiladas no formato JSON, incluindo as soluções de Lógica Matemática (Questões 01 a 06) e Raciocínio Lógico (Questão 07).

---
*Desenvolvido por Manus AI*
