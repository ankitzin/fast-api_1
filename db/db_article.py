from sqlalchemy.orm import Session

from db.models import DbArticle
from schemas.article_schema import ArticleBase


def create_article(request: ArticleBase, db:Session, user_id: int):
    db_item = DbArticle(
        title=request.title,
        description=request.description,
        user_id=user_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def get_article(db:Session, skip: int = 0, limit: int = 100):
    db_item = db.query(DbArticle).offset(skip).limit(limit).all()

    return db_item

