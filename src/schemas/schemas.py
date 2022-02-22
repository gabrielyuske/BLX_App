
from pydantic import BaseModel
from typing import Optional, List


class ProdutoSimples( BaseModel ):
    id: Optional[str] = None
    nome: str
    preco: float

    class Config:
        orm_mode = True


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimples] = []

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True

class Produto(BaseModel):
    id:Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional [int]
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id:Optional[int] = None
    quantidade: int
    local_entrega : Optional[str]
    tipo_entrega : str
    endereco: str
    observacao : Optional[str] = "Sem observacao"

    usuario_id: Optional[int]
    produto_id: Optional[int]

    usuario: Optional[UsuarioSimples]
    produto: Optional[ProdutoSimples]

