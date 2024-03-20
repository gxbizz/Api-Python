import os
from fastapi import FastAPI, HTTPException

app = FastAPI()

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
        
