from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.auth.jwt_handler import decodeJWT

class jwtBearer(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token")
            return credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")

    def verify_jwt(self, jwt_token: str):
        isTokenValid : bool = False
        payload = decodeJWT(jwt_token)
        if payload:
            isTokenValid = True
        return isTokenValid