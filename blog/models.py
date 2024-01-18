from sqlalchemy import Column, Integer, String
from .database import Base


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    price = Column(Integer)


class Bank(Base):
    __tablename__ = 'banks'

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String)
    name = Column(String)
    balance = Column(Integer)