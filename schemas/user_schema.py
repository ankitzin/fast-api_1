from typing import List

from pydantic import BaseModel

from schemas.article_schema import DisplayArticle


class User(BaseModel):
    name: str
    email: str
    password: str


class DisplayUser(BaseModel):
    name: str
    email: str
    articles: List[DisplayArticle] = []

    class Config:
        orm_mode = True
