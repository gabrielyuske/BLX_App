from datetime import datetime , timedelta
from jose import jwt

SECRET_KEY = "5d41402abc4b2a76b9719d911017c592"
ALGORITHMY = "HS256"
EXPIRES_IN_MIN = 3000

def criar_access_token(data: dict):
    dados  = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    
    dados.update({"exp":expiracao})

    token_jwt = jwt.encode(dados,SECRET_KEY,algorithm = ALGORITHMY)
    return token_jwt


def verificar_access_token(token:str):
    carga  = jwt.decode(token,SECRET_KEY,algorithms = [ALGORITHMY])
    return carga.get("sub")