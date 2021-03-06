from fastapi import APIRouter,status,Depends,HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Usuario,UsuarioSimples,LoginData,LoginSucesso
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provider,token_provider
from src.routers.auth_utils import obter_usuario_logado

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

@router.post("/token",response_model=LoginSucesso)
def login(login_data:LoginData,session:Session =Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="TELEFONE OU SENHA ESTAO INCORRETOS!!!")
    
    senha_valida = hash_provider.verificar_hash(senha,usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="TELEFONE OU SENHA ESTAO INCORRETOS!!!")

    # GERAR TOKEN
    token = token_provider.criar_access_token({"sub":usuario.telefone})
    return LoginSucesso(usuario=usuario,access_token = token)

@router.get("/me",response_model=UsuarioSimples)
# ajyste
def me(usuario: Usuario = Depends(obter_usuario_logado)):
    return usuario





    

# @router.get("/usuarios",response_model=List[Usuario])
# def listar_usuarios(session:Session = Depends(get_db)):
#     usuarios = RepositorioUsuario(session).listar()
#     return usuarios