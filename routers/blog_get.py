from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

# @router.get("/blog/all")
# def get_all_blogs():
#     return {"message":"this is all message"}


@router.get("/all", summary="Get all blogs", description="Getting all Blogs with this Request.",
            response_description="all blogs is here.")
def get_all_blogs(page=3, page_size: Optional[int] = None):
    return {"message": f"all {page_size} on page {page}."}


@router.get('/{blog_id}/comments/{comment_id}', tags=['comment'])
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


@router.get("/type/{blog_type}")
def get_blog_type(blog_type: BlogType):
    return {
        "message": f"Blog type is {blog_type}"
    }


@router.get("/{blog_id}", status_code=status.HTTP_200_OK)
def get_blog(blog_id: int, response: Response):
    if blog_id > 5:
        response.status_code= status.HTTP_404_NOT_FOUND
        return {"message": f"this {blog_id} not found."}

    return {"message": f"this is {blog_id}"}