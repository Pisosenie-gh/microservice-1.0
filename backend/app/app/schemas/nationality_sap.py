from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class NationalitySapBase(BaseModel):
    name: str
    code: str


# Properties to receive on item creation
class NationalitySapCreate(NationalitySapBase):
    pass


# Properties to receive on item update
class NationalitySapUpdate(NationalitySapBase):
    pass




# Properties shared by models stored in DB
class NationalitySapInDBBase(NationalitySapBase):
    id: int
    name: str
    code: str
    class Config:
        orm_mode = True


# Properties to return to client
class NationalitySap(BaseModel):
    id: int
    name: str
    code: str
    isActive: int  
    class Config:
        orm_mode = True

# Properties properties stored in DB
class NationalitySapInDB(NationalitySapInDBBase):
    pass

