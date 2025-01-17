from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn 


app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool=True, sort:Optional[str]=None):
    return published
    if published == True:
        return {'data':f'{limit} published blogs from database'}
    else:
        return {'data':f"{limit} blogs from database"}


@app.get("/blog/unpublished")
def unpublished():
    return {'data':'all unpublished blog'}


@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id
    return {'data':id}


@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    # fetch comment of blog id = id
    return limit
    return {'data': {'comments': {1,2}}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(request: Blog):
    return {'data': f'Blog is created with title {request.title}'}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)