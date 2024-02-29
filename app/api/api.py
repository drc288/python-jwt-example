from fastapi import APIRouter
from app.api.endpoints import posts, login


api_router = APIRouter()

api_router.include_router(posts.router, tags=["posts"], prefix="/posts")
api_router.include_router(login.router, tags=["auth"], prefix="/auth")