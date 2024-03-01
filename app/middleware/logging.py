from fastapi import Request
from app.config.logger import log

async def log_request(request: Request, call_next):
    payload = {
        'url': request.url,
        'method': request.method,
        'public_ip': request.client.host if request.client else None,
    }
    log.info(payload)
    response = await call_next(request)
    return response