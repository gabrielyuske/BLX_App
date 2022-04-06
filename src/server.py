from email import message
from fastapi import FastAPI,Request,BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_Produtos,rotas_Pedidos,rotas_Auth
from src.jobs.write_moification import write_notfy

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

# ROTAS SEGURANCA
app.include_router( rotas_Auth.router,prefix="/auth" )

# ROTAS PEDIDOS
app.include_router( rotas_Pedidos.router )

#Middlewares

# ESCREVE EM  JAVASCRIPT
@app.middleware("http")
async def processar_tempo_requisicao(request:Request,next):
    print("INTECEPTOU CHEGADA...")

    response = await next(request)

    print("interceptou volta...")
    return response

@app.post("/send_email/{email}")
def send_email(email:str,background:BackgroundTasks):
    background.add_task(write_notfy,email,message="Alguma notificacao")
    return {"message" : "Notificacao concluida no background"}