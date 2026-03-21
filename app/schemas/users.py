from pydantic import BaseModel, EmailStr


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
