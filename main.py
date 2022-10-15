from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def index():
    return "hello world"


@app.get("/blog/all")
def get_all_blogs():
    return {"message":"this is all message"}


@app.get("/blog/{blog_id}")
def get_blog(blog_id: int):
    return f"The id is {blog_id}"


