from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .. import models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_one(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    return blog


def create(request, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, price=request.price, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(id: int, request, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    blog.update(request.model_dump())
    db.commit()
    return 'Updated'


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not there to delete")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'
