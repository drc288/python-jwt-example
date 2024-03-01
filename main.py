from fastapi import FastAPI, Request
from app.api.api import api_router
from app.config.logger import log
from starlette.middleware.base import BaseHTTPMiddleware
from app.middleware.logging import log_request


app = FastAPI(
    title="FastAPI JWT Auth",
    description="A simple JWT authentication implementation with FastAPI"
)

app.add_middleware(BaseHTTPMiddleware, dispatch=log_request)
app.include_router(api_router, prefix="/api")
