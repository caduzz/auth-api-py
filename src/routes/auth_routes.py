from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.user_model import User
from utils.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])
user_model = User()

class LoginInput(BaseModel):
  email: str
  password: str

@router.post("/login")
def login(user: LoginInput):
  db_user = user_model.get_user_by_email(user.email)

  if not db_user or db_user[3] != user.password:  # senha na posição 3
    raise HTTPException(status_code=401, detail="Email ou senha inválidos")

  token = create_access_token(str(db_user[0]))  # id na posição 0
  return {
    "access_token": token,
    "token_type": "bearer",
    "user": {
      "id": db_user[0],
      "name": db_user[1],
      "email": db_user[2]
    }
  }
