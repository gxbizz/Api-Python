import os
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

file_path = os.path.abspath("services_caches/produtos.txt")  

@app.post("/produto")
async def cadastrar_produto(id: int, nome: str, preco: float):
    with open(file_path, "a") as file:
        dados = str({"nome": nome, "preco": preco})
        file.write(f"{id}: {dados} \n")
        return {"status": "sucesso", "mensagem": "Produto adicionado com sucesso"}



@app.get("/produtos")
async def listar_produtos():
    with open(file_path, "r") as file:
        produtos = []
        for line in file:
            id, dados = line.strip().split(":", 1)
            dados = eval(dados)
            dados["id"] = id
            produtos.append(dados)
        return produtos
    
@app.get("/produto/{id}")
async def get_produto(id: str):
    with open(file_path, "r") as file:
        for line in file:
            id_produto, dados = line.strip().split(":", 1)
            if(id == id_produto):
                return eval(dados)
    return {"status": "erro", "mensagem": "Nenhum produto encontrado"}