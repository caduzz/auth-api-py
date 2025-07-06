from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.auth_routes import router as auth_router

app = FastAPI()

@app.get("/")
async def root():
    return {"status": 200, "message": "API is running"}

app.include_router(user_router)
app.include_router(auth_router)