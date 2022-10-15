from typing import Optional
from fastapi import FastAPI, status, Response
from enum import Enum

app = FastAPI()


@app.get("/hello")
def index():
    return "hello world"


# @app.get("/blog/all")
# def get_all_blogs():
#     return {"message":"this is all message"}

@app.get("/blog/all",
         tags=['blog'],
         summary="Get all blogs",
         description="Getting all Blogs with this Request.")
def get_all_blogs(page=3, page_size: Optional[int] = None):
    return {"message": f"all {page_size} on page {page}."}


@app.get('/blog/{blog_id}/comments/{comment_id}', tags=['blog','comment'])
def get_comment(blog_id:int, comment_id:int, valid: bool = True, username: Optional[str] = None):
    """
    - **blog_id**: Mandatory Parameter
    - **comment_id**: Mandatory Parameter
    - **valid**: Optional Parameter
    - **username**: Optional Parameter <br><br>
    ```return: the info about the comment on Blog with respect to blog_id.```
    """
    return {
        "message": f"{blog_id} for username {username}, {valid} comment."
    }


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get("/blog/type/{blog_type}", tags=['blog'])
def get_blog_type(blog_type: BlogType):
    return {
        "message": f"Blog type is {blog_type}"
    }


@app.get("/blog/{blog_id}", status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(blog_id: int, response: Response):
    if blog_id > 5:
        response.status_code= status.HTTP_404_NOT_FOUND
        return {"message": f"this {blog_id} not found."}

    return {"message": f"this is {blog_id}"}

