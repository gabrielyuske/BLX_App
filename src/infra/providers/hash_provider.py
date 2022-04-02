from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def geras_hash(texto):
    # gerar hash
    return pwd_context.hash(texto)

def verificar_hash(texto,hash):
    return pwd_context.verify(texto,hash)