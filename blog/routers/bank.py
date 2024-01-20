from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models


get_db = database.get_db
router = APIRouter(prefix='/bank', tags=['bank'])


@router.get('/{id}', status_code=200,response_model=schemas.showbank)
def show_bank(id, db:Session = Depends(get_db)):
    banks = db.query(models.Bank).filter(models.Bank.id == id).first()
    if not banks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Bank User with the id {id} is not available')
    return banks


@router.post('/')
def create_bank(bank: schemas.Bank, db: Session = Depends(get_db)):
    new_bank = models.Bank(surname=bank.surname, name=bank.name, balance=bank.balance*4)
    db.add(new_bank)
    db.commit()
    db.refresh(new_bank)
    return new_bank
