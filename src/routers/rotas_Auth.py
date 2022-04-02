from fastapi import APIRouter,status,Depends,HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provider

router = APIRouter()

# ROTAS USUARIOS

@router.post("/signup",status_code=status.HTTP_201_CREATED,response_model=Usuario)
def signup(usuario:Usuario,session:Session = Depends(get_db)):
    usuaro_localizado =RepositorioUsuario(session).obter_por_telefone(usuario.telefone)

    if usuaro_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="JA EXISTE U USUARIO PRA ESTE TELEFONE") 
    # CRIAR NOVO USUARIO
    usuario.senha = hash_provider.geras_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

# @router.get("/usuarios",response_model=List[Usuario])
# def listar_usuarios(session:Session = Depends(get_db)):
#     usuarios = RepositorioUsuario(session).listar()
#     return usuarios