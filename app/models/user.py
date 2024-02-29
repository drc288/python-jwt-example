from pydantic import BaseModel, Field, EmailStr, SecretStr

class UserRegisterSchema(BaseModel):
    name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: SecretStr = Field(default=None)

    class config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "pepito",
                "password": "password"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: SecretStr = Field(default=None)

    class config:
        schema_extra = {
            "example": {
                "email": "pepito",
                "password": "password"
            }
        }