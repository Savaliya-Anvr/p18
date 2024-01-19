from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title: str
    body: str
    price: int


class Shown(BaseModel):
    title: str
    price: int
    # class Config():
    #     orm_mode = True
    #


class Bank(BaseModel):
    surname: str
    name: str
    balance: int


class User(BaseModel):
    name: str
    email: str
    password: str

class Showuser(BaseModel):
    name:str
    email:str

