from typing import Optional

from pydantic import BaseModel, Field
from datetime import date
from .nationality_sap import NationalitySap
# Shared properties
class NationalityBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class NationalityCreate(NationalityBase):

    nationalitySAPId: int


# Properties to receive on item update
class NationalityUpdate(NationalityBase):
    nationalitySAPId: int

# Properties shared by models stored in DB
class NationalityInDBBase(NationalityBase):
    id: int
    nameRu: str
    nameKz: str
    nationalitySAPId: int
    class Config:
        orm_mode = True


# Properties to return to client
class Nationality(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    isActive: int    
    nationalitySAP: NationalitySap
    class Config:
        orm_mode = True

# Properties properties stored in DB
class NationalityInDB(NationalityInDBBase):
    pass

