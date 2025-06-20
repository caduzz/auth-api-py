import sqlite3

from fastapi import (
  APIRouter,
  HTTPException
)

cursor = sqlite3.connect('meu_banco.db').cursor()

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{user_id}")
async def get_user(*, user_id: int):
  user = cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
  if user:
    return {"user": user}

  raise HTTPException(status_code=404, detail="User not found")

@router.get("/")
async def get_users():
  return {"users": cursor.execute("SELECT * FROM users").fetchall()}

@router.post("/")
async def create_user(user: dict):
  cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user["name"], user["email"]))
  cursor.connection.commit()  
  return {"message": "User created", "user": user}