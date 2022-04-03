
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

class LoginData(BaseModel):
    senha : str 
    telefone : str    

class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str
 
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
    # consertei o nome da column que eu coloquei errado com esse codigo no SQL 
    # ALTER TABLE pedido RENAME COLUMN local_estrega TO local_entrega
    tipo_entrega : str
    # endereco: str
    observacao : Optional[str] = "Sem observacao"

    usuario_id: Optional[int]
    produto_id: Optional[int]

    usuario: Optional[UsuarioSimples]
    produto: Optional[ProdutoSimples]

    class Config:
        orm_mode = True