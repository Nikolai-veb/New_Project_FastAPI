
from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List

class Ganre(BaseModel):
    name: str



class Author(BaseModel):
    first_name: str=Field(..., min_length=3, max_length=30)
    last_name: str
    age: int=Field(..., gt=20, le=100, description="Возрастт должен быть не меньше 20")

#    @validator('age')
#    def check_age(cls, v):
#        if v < 20:
#            raise ValueError("Возрастт должен быть не меньше 20")
#        return v


class Book(BaseModel):
    title: str
    writer: str
    deration: str
    date: date
    summary: str
    genres: List[Ganre]
    page: int

