
from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    # produtos: List[produtos] = []
    # meus_produtos: List[produtos] = []
    # minhas_vendas: List[Pedido]
    # meus_pedidos: List[Pedido]


class Produto(BaseModel):
    id:Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        orm_mode = True

class ProdutoSimples(BaseModel):
    id:Optional[str] = None
    nome: str
    preco: float

    class Config:
        orm_mode = True
        

class Pedido(BaseModel):
    id:Optional[str] = None
    usuario : User
    # produto : Produto
    entrega : bool = True
    endereco: str
    observacao : Optional[str] = "Sem observacao"

