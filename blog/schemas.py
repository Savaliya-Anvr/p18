from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title: str
    body: str
    price: int


class Bank(BaseModel):
    surname: str
    name: str
    balance: int

