from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship('User', back_populates='blog')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blog = relationship('Blog', back_populates='creator')


class Bank(Base):
        __tablename__ = 'banks'

        id = Column(Integer, primary_key=True, index=True)
        surname = Column(String)
        name = Column(String)
        balance = Column(Integer)
