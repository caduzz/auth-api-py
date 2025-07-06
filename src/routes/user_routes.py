from fastapi import APIRouter, Body
from controllers.user_controller import UserController

router = APIRouter(prefix="/users", tags=["Users"])
controller = UserController()

@router.get("/{user_id}")
async def get_user(user_id: int):
  return {"user": controller.get_user(user_id)}

@router.get("/")
async def get_users():
  return {"users": controller.get_all_users()}

@router.post("/")
async def create_user(user: dict = Body(...)):
  return {"message": "User created", "user": controller.create_user(user)}