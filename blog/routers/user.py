from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..hashing import Hash
from ..repository import user

get_db = database.get_db
router = APIRouter(tags=['user'])


@router.post('/user', response_model=schemas.Showuser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)



@router.get('/user/{id}', status_code=200, response_model=schemas.Showuser)
def show(id, db: Session = Depends(get_db)):
    return user.get_one(id, db)
