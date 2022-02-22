from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_Produtos,rotas_Usuarios,rotas_Pedidos

app = FastAPI()

# CORS
origins = ["http://localhost:3000"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

# ROTAS PRODUTOS
app.include_router( rotas_Produtos.router )

# ROTAS USUARIOS
app.include_router( rotas_Usuarios.router )

# ROTAS PEDIDOS
app.include_router( rotas_Pedidos.router )

