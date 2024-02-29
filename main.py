from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI(
    title="FastAPI JWT Auth",
    description="A simple JWT authentication implementation with FastAPI"
)

app.include_router(api_router, prefix="/api")
