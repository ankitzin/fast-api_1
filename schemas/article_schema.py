from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    description: str


class DisplayArticle(ArticleBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
