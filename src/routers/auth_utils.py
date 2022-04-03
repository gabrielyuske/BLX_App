from http.client import HTTPException
from pydantic import ValidationError
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from fastapi import status,Depends,HTTPException
from jose import JWTError
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider


from fastapi.security import OAuth2PasswordBearer


oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

def obter_usuario_logado(token: str = Depends(oauth2_schema),session:Session = Depends(get_db)):
    
    # exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token INVALIDO')
    exception = HTTPException(status_code=401, detail='Token INVALIDO')

    try:
        telefone :str = token_provider.verificar_access_token(token)
    except (JWTError,ValidationError):
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="Token INVALIDO")
    if not telefone:
        raise exception
    
    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)
    
    if not usuario:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,detail ="Token INVALIDO")
    
    return usuario

    