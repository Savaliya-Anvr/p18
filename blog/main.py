from fastapi import FastAPI, Depends, Response, status, HTTPException
import uvicorn
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import schemas, models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog')
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, price=request.price)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.post('/bank')
def createbank(bank: schemas.Bank, db: Session = Depends(get_db)):
    new_bank = models.Bank(surname=bank.surname, name=bank.name, balance=bank.balance*4)
    db.add(new_bank)
    db.commit()
    db.refresh(new_bank)
    return new_bank

@app.delete('/blog/{id}', status_code=200)
def destroy(id,db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session = False)
    db.commit()
    return 'done'

@app.get('/blog/{id}', status_code=200)
def show(id, response:Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')

    return blogs


@app.get('/blog')
def show(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()

    return blogs


if __name__ == '__main__':
    uvicorn.run(app)
