from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

from .gender import Gender


# Shared properties
class MaritalStatusBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class MaritalStatusCreate(MaritalStatusBase):
    genderId: int

# Properties to receive on item update
class MaritalStatusUpdate(MaritalStatusBase):
    genderId: int


# Properties shared by models stored in DB
class MaritalStatusInDBBase(MaritalStatusBase):
    id: int
    nameRu: str
    nameKz: str


    class Config:
        orm_mode = True


# Properties to return to client
class MaritalStatus(BaseModel):
    id: int
    gender: Gender
    nameRu: str
    nameKz: str
    isActive: int

    class Config:
        orm_mode = True


# Properties properties stored in DB
class MaritalStatusInDB(MaritalStatusInDBBase):
    pass

