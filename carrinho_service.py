from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"  # porta- front-end 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

file_path = os.path.abspath("services_caches/carrinho.txt")  

@app.post("/carrinho/{user_id}/add")
async def add_carrinho(user_id: int, produto_id: int, quantidade: int):
    with open(file_path, "a") as file:
        dados = str({"produto_id": produto_id, "quantidade": quantidade})
        file.write(f"{user_id}: {dados} \n")
        return {"status": "sucesso", "mensagem": "Carrinho adicionado com sucesso"}
   
@app.get("/carrinho/{user_id}")
async def get_carrinho(user_id: str):
    with open(file_path, "r") as file:
        for line in file:
            id_user, dados = line.strip().split(":", 1)
            if(user_id is id_user):
                return eval(dados)
    return {"status": "erro", "mensagem": "Nenhum carrinho adicionado encontrado"}