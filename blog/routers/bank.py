from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, models


get_db = database.get_db
router = APIRouter(prefix='/bank', tags=['bank'])



@router.post('/')
def create_bank(bank: schemas.Bank, db: Session = Depends(get_db)):
    new_bank = models.Bank(surname=bank.surname, name=bank.name, balance=bank.balance*4)
    db.add(new_bank)
    db.commit()
    db.refresh(new_bank)
    return new_bank
