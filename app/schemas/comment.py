from pydantic import BaseModel, EmailStr


class CommentUser(BaseModel):
    id_user: int
    email_user: EmailStr
    comment: str
    likes: int | None = None


