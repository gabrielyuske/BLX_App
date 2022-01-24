from typing import Optional
from pydantic import BaseModel
from typing import Optional,List

class User(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List[Order]
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]


class Product(BaseModel):
    id:Optional[str] = None
    usuario: User 
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

class Order(BaseModel):
    id:Optional[str] = None
    usuario : User
    produto : Product
    entrega : bool = True
    endereco: str
    observacao : Optional[str] = "Sem observacao"

