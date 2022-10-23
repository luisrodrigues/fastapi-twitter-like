from pydantic.main import BaseModel

from app.schemas.user_schema import ShowUser


class PostBase(BaseModel):
    title: str
    body: str


class Post(PostBase):
    class Config:
        orm_mode = True


class ShowPost(Post):
    creator: ShowUser

    class Config:
        orm_mode = True
