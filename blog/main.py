from fastapi import FastAPI
import uvicorn
from typing import Optional
from . import schemas

app = FastAPI()


@app.post('/blog')
def create_blog(blog: schemas.First):
    # return {f'Title of the blog is { blog.title} and price is {blog.price}'}
    return blog


@app.get('/')
def root(id: int):
    return {'data': f'{id} is your personal ID'}


if __name__ == '__main__':
    uvicorn.run(app)
