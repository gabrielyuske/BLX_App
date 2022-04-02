from http.client import HTTPException
from logging import exception
from fastapi import status
from jose import JWTError
from sqlalchemy.orm import Session
from infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider

from fastapi.security import OAuth2PasswordBearer


oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

def obter_usuario_logado(token:str = Depends(oauth2_schema),session:Session = Depends(get_db)):
    
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,detail="Token INVALIDO")

    try:
        telefone = token_provider.verificar_acess_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="token INVALIDO")

    
    if not telefone:
        raise exception

    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)
    
    if not usuario:
        raise exception
    
    return usuario

    