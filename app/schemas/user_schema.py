from typing import List

from pydantic.main import BaseModel


class UserPost(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    posts: List[UserPost] = []

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str
