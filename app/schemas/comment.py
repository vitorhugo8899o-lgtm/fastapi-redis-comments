from pydantic import BaseModel, EmailStr, PrivateAttr


class CommentUser(BaseModel):
    _id_comment: int = PrivateAttr()
    _id_user: int = PrivateAttr()
    _email_user: EmailStr = PrivateAttr()
    comment: str

