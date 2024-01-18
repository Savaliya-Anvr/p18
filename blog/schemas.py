from pydantic import BaseModel
from typing import Optional


class First(BaseModel):
    title: str = 'that is all'
    price: int = 78
    author: Optional[bool] = None
