

from fastapi import FastAPI
from app.controllers.user_controller import router as user_router
from app.database import database



app = FastAPI()


app.include_router(user_router)
@app.get("/")
def home():
    return {"message": "User Service is running"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()