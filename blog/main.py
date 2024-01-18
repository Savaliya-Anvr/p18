from fastapi import FastAPI
import uvicorn
from .database import SessionLocal, engine
from . import schemas, models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.post('/blog')
def create_blog(blog: schemas.First):
    return {f'Title of the blog is { blog.title} and price is {blog.price}'}



if __name__ == '__main__':
    uvicorn.run(app)
