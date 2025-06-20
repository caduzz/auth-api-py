from typing import Union
from fastapi import FastAPI
from controllers import user_router

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Servidor rodando"}

app.include_router(user_router)