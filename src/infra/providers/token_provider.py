from datetime import datetime , timedelta
from jose import jwt

SECRET_KEY = "06394AF259DB19355CCF0B668C77EC0FDD9B8D5AA388D848E1BB5959E80E2A24"
ALGORITHMY = "HS256"
EXPIRES_IN_MIN = 3000

def criar_access_token(data: dict):
    dados  = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    
    dados.update({"exp":expiracao})

    token_jwt = jwt.encode(dados,SECRET_KEY,algorithm = ALGORITHMY)
    return token_jwt


def verificar_acess_token(token:str):
    carga  = jwt.decode(token,SECRET_KEY,algorithm = ALGORITHMY)
    return carga.get("sub")