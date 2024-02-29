from fastapi import APIRouter, Body
from app.auth.jwt_handler import signJWT
from app.models.user import UserLoginSchema, UserRegisterSchema

router = APIRouter()

users = []

# Sign up
@router.post("/signup", tags=["auth"])
def sign_up(user: UserRegisterSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

# Log in
@router.post("/login", tags=["auth"])
def log_in(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    return {"error": "Invalid credentials"}
