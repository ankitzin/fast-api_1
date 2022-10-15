from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/hello")
def index():
    return "hello world"


# @app.get("/blog/all")
# def get_all_blogs():
#     return {"message":"this is all message"}

@app.get("/blog/all")
def get_all_blogs(page=3, page_size: Optional[int] = None):
    return {"message": f"all {page_size} on page {page}."}


@app.get('/blog/{blog_id}/comments/{comment_id}')
def get_comment(blog_id:int, comment_id:int, valid: bool = True, username: Optional[str] = None):
    return {
        "message": f"{blog_id} for username {username}, {valid} comment."
    }


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get("/blog/type/{blog_type}")
def get_blog_type(blog_type: BlogType):
    return {
        "message": f"Blog type is {blog_type}"
    }


@app.get("/blog/{blog_id}")
def get_blog(blog_id: int):
    return {"message": f"this is {blog_id}"}

