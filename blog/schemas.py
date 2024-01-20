from pydantic import BaseModel
from typing import Optional, List


class Blog(BaseModel):
    title: str
    body: str
    price: int


class Showuser(BaseModel):
    name: str
    email: str
    blog: List[Blog]


class Shown(BaseModel):
    title: str
    price: int
    creator: Showuser


class User(BaseModel):
    name: str
    email: str
    password: str


class Bank(BaseModel):
    surname: str
    name: str
    balance: int


class showbank(BaseModel):
    name: str
    balance: int

