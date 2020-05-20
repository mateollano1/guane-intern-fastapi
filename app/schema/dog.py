from datetime import datetime
from typing import List

from pydantic import BaseModel


class DogBase(BaseModel):
    name: str
    picture: str
    create_date = datetime.now()
    is_adopted = False


class DogCreate(DogBase):
    pass


class Dog(DogBase):
    id: int

    class Config:
        orm_mode = True
