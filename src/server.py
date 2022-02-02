from fastapi import FastAPI,Depends,status
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_bd, get_db
from src.schemas.schemas import Produto,ProdutoSimples
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

# criar_bd()

app = FastAPI()
#                     status_code=201
@app.post("/produtos",status_code=status.HTTP_201_CREATED,response_model=ProdutoSimples)
def criar_produto(produto:Produto,db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get("/produtos",status_code=status.HTTP_200_OK,response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos




