from models.user_model import User
from fastapi import HTTPException

class UserController:
  def __init__(self):
    self.model = User()

  def get_user(self, user_id: int):
    user = self.model.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

  def get_all_users(self):
    return self.model.get_all()

  def create_user(self, user_data: dict):
    name = user_data.get("name")
    email = user_data.get("email")
    if not name or not email:
        raise HTTPException(status_code=400, detail="Name and email are required")
    return self.model.create(name, email)