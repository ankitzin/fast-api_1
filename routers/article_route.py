from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database
from db import db_article
from auth.oauth2 import oauth_schema
from schemas.article_schema import DisplayArticle, ArticleBase

router = APIRouter(
    tags=['article'],
    prefix='/article'
)


@router.get('/', response_model=List[DisplayArticle])
def get_articles_all(skip: int = 0, limit:int = 0, db: Session = Depends(database.get_db), token: str = Depends(oauth_schema)):
    articles = db_article.get_article(db, skip, limit)
    return articles


@router.post("/users/{user_id}/items/", response_model=DisplayArticle)
def create_item_for_user(user_id: int, article: ArticleBase, db: Session = Depends(database.get_db), token: str = Depends(oauth_schema)):
    return db_article.create_article(article, db=db, user_id=user_id)