from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ResponseLogin(BaseModel):
    id_user: int
    email: EmailStr
    message: str


class MessageConfirme(BaseModel):
    message: str = 'Confirmo deletar minha conta'

class FilterUsers(BaseModel):
    init: int = Field(ge=0, default=0)
    end: int = Field(ge=-1, default=-1)
