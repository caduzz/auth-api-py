import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def create_access_token(user_id: str):
  payload = {
    "sub": user_id,
    "exp": datetime.utcnow() + timedelta(hours=1),
    "iat": datetime.utcnow()
  }
  token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
  return token