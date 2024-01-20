from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models
from typing import List
from ..repository import blog

get_db = database.get_db
router = APIRouter(prefix='/blog', tags=['blog'])


@router.get('/', response_model=List[schemas.Shown])
def show_all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.post('/')
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.Shown)
def show(id, db: Session = Depends(get_db)):
    return blog.get_one(id,db)
