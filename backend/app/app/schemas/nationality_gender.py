from typing import Optional

from pydantic import BaseModel, Field
from datetime import date
from .nationality import Nationality
from .gender import Gender


# Shared properties
class NationalityGenderBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class NationalityGenderCreate(NationalityGenderBase):
    nationalityId: int
    genderId: int

# Properties to receive on item update
class NationalityGenderUpdate(NationalityGenderBase):
    nationalityId: int
    genderId: int



# Properties shared by models stored in DB
class NationalityGenderInDBBase(NationalityGenderBase):
    id: int
    nameRu: str
    nameKz: str


    class Config:
        orm_mode = True


# Properties to return to client
class NationalityGender(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    isActive: int  
    nationality: Nationality
    gender: Gender

    class Config:
        orm_mode = True


# Properties properties stored in DB
class NationalityGenderInDB(NationalityGenderInDBBase):
    pass

