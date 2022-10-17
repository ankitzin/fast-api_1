from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    tags=['blog'],
    prefix='/blog'
)


class BlogModel(BaseModel):
    title: str
    name: str
    content: str
    comment_number: int
    published: Optional[bool]


@router.post('/new/{blog_id}')
def blog_create(blog: BlogModel, blog_id: int, version: int=1):
    return {
        "data": blog,
        "blog_id": blog_id,
        "version": version
    }
