from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"status": "ok", "message": "Welcome to auth api in python"}

@app.get("/item/{item_id}")
def read_item(item_id: Union[int, str]):
  return {"item_id": item_id, "message": "Item retrieved successfully"}