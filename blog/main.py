from fastapi import FastAPI, Depends, Response, status, HTTPException
import uvicorn
from typing import List
from passlib.context import CryptContext
from .database import get_db, engine
from sqlalchemy.orm import Session
from . import schemas, models
from .hashing import Hash
from .routers import blog, user, bank, authentication

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(bank.router)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.get('/blog', response_model=List[schemas.Shown], tags=['blog'])
# def show_all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

#
# @app.post('/blog', tags=['blog'])
# def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, price=request.price, user_id = 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog
#
#
# @app.post('/bank', tags=['bank'])
# def create_bank(bank: schemas.Bank, db: Session = Depends(get_db)):
#     new_bank = models.Bank(surname=bank.surname, name=bank.name, balance=bank.balance*4)
#     db.add(new_bank)
#     db.commit()
#     db.refresh(new_bank)
#     return new_bank
#
#
# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blog'])
# def destroy(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'Blog with id {id} is not found')
#
#     blog.delete(synchronize_session = False)
#     db.commit()
#     return 'done'
#
#
# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blog'])
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
#     blog.update(request.model_dump())
#     db.commit()
#     return 'Updated'
#
#
# @app.get('/blog/{id}', status_code=200, response_model=schemas.Shown, tags=['blog'])
# def show(id, response:Response, db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blogs:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'Blog with the id {id} is not available')
#
#     return blogs


# pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


# @app.post('/user',response_model=schemas.Showuser, tags=['user'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#
#     new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
#
# @app.get('/user/{id}', status_code=200, response_model=schemas.Showuser, tags=['user'])
# def show(id, db: Session = Depends(get_db)):
#     users = db.query(models.User).filter(models.User.id == id).first()
#     if not users:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'User with the id {id} is not available')
#     return users

