from fastapi import FastAPI
from routes.user_routes import router as user_router

app = FastAPI()

@app.get("/")
async def root():
    return {"status": 200, "message": "API is running"}

app.include_router(user_router)