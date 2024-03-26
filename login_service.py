import os
from fastapi import FastAPI, HTTPException
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
file_path = os.path.abspath("services_caches/login.txt")  

@app.post("/cadastrar")
async def cadastrar(username: str, password: str):
    with open(file_path, "a") as file:
        file.write(str({"username": username, "password": password}) + "\n")
    return {"status": "sucesso", "mensagem": "Usuário criado com sucesso"}


@app.post("/login")
async def login(username: str, password: str):
    with open(file_path, "r") as file:
        for line in file:
            user = eval(line)
            if user["username"] == username:
                if user["password"] == password:
                    return {"status": "sucesso", "mensagem": "Usuário autenticado com sucesso"}
                else:
                    return {"status": "sucesso", "mensagem": "Senha incorreta"}
        return {"status": "erro", "mensagem": "Nenhum usuário encontrado"}
        
