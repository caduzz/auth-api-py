from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
import jwt
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

class JWTBearer(HTTPBearer):
  def __init__(self, auto_error: bool = True):
    super(JWTBearer, self).__init__(auto_error=auto_error)

  async def __call__(self, request: Request):
    credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
    if credentials:
      if not self.verify_jwt(credentials.credentials):
        raise HTTPException(status_code=403, detail="Token inválido ou expirado")
      return credentials.credentials
    else:
      raise HTTPException(status_code=403, detail="Credenciais inválidas")

  def verify_jwt(self, token: str) -> bool:
    try:
      payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
      return True
    except jwt.ExpiredSignatureError:
      raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
      return False
