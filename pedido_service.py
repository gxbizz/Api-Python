import os
from random import randint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:5500"  # porta- front-end 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
file_path = os.path.abspath("services_caches/pedido.txt")  

@app.post("/pedido/{user_id}/add")
async def criar_pedido(user_id: int):
   with open(file_path, "a") as file:
      order_id = randint(0, 32123)
      dados = str({"user_id": user_id})
      file.write(f"{order_id}: {dados} \n")
      return {"status": "sucesso", "mensagem": "Pedido feito com sucesso"}

@app.get("/pedidos/{user_id}")
async def get_pedidos(user_id: int):
   with open(file_path, "r") as file:
      pedidos = []
      for line in file:
         order_id, dados = line.strip().split(":", 1)
         dados = eval(dados)
         id_user = dados["user_id"]
         if(id_user == user_id):
            dados["order_id"] = order_id
            pedidos.append(dados)
         
      return pedidos
   
@app.get("/pedido/{order_id}")
async def get_pedido(order_id: str):
   with open(file_path, "r") as file:
     for line in file:
         order, dados = line.strip().split(":", 1)
         if(order_id == order):
               return eval(dados)
   return {"status": "erro", "mensagem": "Nenhum pedido encontrado"}