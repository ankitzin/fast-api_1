from fastapi import FastAPI
from routers import blog_get, blog_post, users_route
from db.database import engine
from db import models

app = FastAPI()
app.include_router(users_route.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return "hello world"


models.Base.metadata.create_all(engine)
