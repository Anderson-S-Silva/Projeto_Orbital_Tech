from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import date, datetime
from uuid import UUID, uuid4

# --- 1. Modelos Pydantic (Schemas) ---

# Schema base para criação e atualização
class ContatoBase(BaseModel):
    nome_completo: str = Field(..., min_length=1, description="Nome completo do contato.")
    data_nascimento: date = Field(..., description="Data de nascimento no formato YYYY-MM-DD.")
    email: EmailStr = Field(..., description="Endereço de e-mail válido.")
    telefone: Optional[str] = Field(None, description="Número de telefone.")
    endereco: Optional[str] = Field(None, description="Endereço completo.")

# Schema para criação (herda de ContatoBase)
class ContatoCreate(ContatoBase):
    pass

# Schema para resposta (inclui ID e idade calculada)
class ContatoResponse(ContatoBase):
    id: UUID = Field(..., description="Identificador único do contato (UUID).")
    idade: int = Field(..., description="Idade calculada a partir da data de nascimento.")

    class Config:
        # Permite que o Pydantic mapeie de objetos que não são dicionários (como o nosso ContactoInDB)
        from_attributes = True

# --- 2. Modelo de Dados (Simulação de Banco de Dados) ---

class ContatoInDB(ContatoBase):
    """Modelo interno que representa o contato no 'banco de dados'."""
    id: UUID = Field(default_factory=uuid4)

    def calcular_idade(self) -> int:
        """Calcula a idade com base na data de nascimento."""
        today = date.today()
        return today.year - self.data_nascimento.year - (
            (today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )

# Simulação de um banco de dados em memória (lista de contatos)
db: List[ContatoInDB] = []

# --- 3. Funções de Repositório (CRUD Básico) ---

def get_contato_by_id(contato_id: UUID) -> Optional[ContatoInDB]:
    """Busca um contato pelo ID."""
    return next((c for c in db if c.id == contato_id), None)

def get_all_contatos() -> List[ContatoInDB]:
    """Retorna todos os contatos ordenados por nome."""
    # Requisito 3.c: Retornar todos os contatos, ordenados alfabeticamente pelo Nome Completo
    return sorted(db, key=lambda c: c.nome_completo)

def create_contato(contato_data: ContatoCreate) -> ContatoInDB:
    """Cria e adiciona um novo contato ao 'banco de dados'."""
    novo_contato = ContatoInDB(**contato_data.model_dump())
    db.append(novo_contato)
    return novo_contato

def update_contato(contato_id: UUID, contato_data: ContatoCreate) -> Optional[ContatoInDB]:
    """Atualiza um contato existente."""
    contato = get_contato_by_id(contato_id)
    if contato:
        # Atualiza os campos do modelo InDB com os dados do ContatoCreate
        update_data = contato_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(contato, key, value)
        return contato
    return None

def delete_contato(contato_id: UUID) -> bool:
    """Remove um contato pelo ID."""
    global db
    initial_len = len(db)
    db = [c for c in db if c.id != contato_id]
    return len(db) < initial_len

# --- 4. Inicialização da Aplicação FastAPI ---

app = FastAPI(
    title="API Contatos - Teste de Programação",
    description="API RESTful simples para gerenciamento de contatos.",
    version="1.0.0"
)

# --- 5. Endpoints da API ---

@app.post("/contatos", response_model=ContatoResponse, status_code=status.HTTP_201_CREATED, tags=["Contatos"])
def cadastrar_contato(contato: ContatoCreate):
    """
    1. Cadastro de Contato (POST /contatos)
    Criação de um novo contato. Retorna HTTP Status 201 Created em caso de sucesso.
    """
    novo_contato = create_contato(contato)
    return ContatoResponse(
        **novo_contato.model_dump(),
        idade=novo_contato.calcular_idade()
    )

@app.put("/contatos/{contato_id}", response_model=ContatoResponse, tags=["Contatos"])
def atualizar_contato(contato_id: UUID, contato: ContatoCreate):
    """
    2. Atualização de Contato (PUT /contatos/:contatoid)
    Atualização de informações de um contato existente.
    Campos obrigatórios: Nome Completo, Data de Nascimento e Email (garantido pelo ContatoCreate).
    Caso o ID não exista, retorna HTTP 404 Not Found.
    """
    contato_atualizado = update_contato(contato_id, contato)
    if not contato_atualizado:
        # Requisito 2.d: Caso o ID não exista, retornar HTTP 404 Not Found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contato não encontrado")
    
    return ContatoResponse(
        **contato_atualizado.model_dump(),
        idade=contato_atualizado.calcular_idade()
    )

@app.get("/contatos", response_model=List[ContatoResponse], tags=["Contatos"])
def listar_contatos():
    """
    3. Listagem de Contatos (GET /contatos)
    Retorna todos os contatos, ordenados alfabeticamente pelo Nome Completo.
    Cada contato retorna a idade calculada.
    """
    contatos_db = get_all_contatos()
    
    # Mapeia os modelos internos para os modelos de resposta, calculando a idade
    return [
        ContatoResponse(**c.model_dump(), idade=c.calcular_idade())
        for c in contatos_db
    ]

@app.delete("/contatos/{contato_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Contatos"])
def excluir_contato(contato_id: UUID):
    """
    4. Exclusão de Contato por ID (DELETE /contatos/:contatoId)
    Remove contato pelo ID (UUID).
    Caso o ID não exista, retorna HTTP 404 Not Found.
    """
    if not delete_contato(contato_id):
        # Requisito 4.c: Caso o ID não exista, retornar HTTP 404 Not Found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contato não encontrado")
    
    # Retorna 204 No Content em caso de sucesso (padrão para DELETE sem corpo de resposta)
    return
