from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class First(BaseModel):
    title : str
    price : int
    author : Optional[bool] = None

@app.post('/blog')
def create_blog(blog:First):
    return {'data':f'Title of the blog is { blog.title} and price is {blog.price}'}

@app.get('/')
def root(id:int):
    return {'data':f'{id} is your personal ID'}

if __name__ == '__main__':
    uvicorn.run(app)


