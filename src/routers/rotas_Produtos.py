from fastapi import APIRouter,status,Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from typing import List
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.schemas.schemas import Produto,ProdutoSimples


router = APIRouter()

# ROTAS PRODUTOS

#                     status_code=201
@router.post("/produtos",status_code=status.HTTP_201_CREATED,response_model=ProdutoSimples)
def criar_produto(produto:Produto,db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@router.get("/produtos",response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@router.put("/produtos/{id}",response_model=ProdutoSimples)
def atualizar_produto(id:int,produto:Produto,session:Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto
        # ,{"message": "PRODUTO ATUALIZADO"}

@router.delete("/produtos/{id}")
def remover_produto(id:int,session:Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return {"msg":"DELETADO COM SUCESSO"}

