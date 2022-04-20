from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class MilitaryServiceAttitudeBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class MilitaryServiceAttitudeCreate(MilitaryServiceAttitudeBase):
    pass


# Properties to receive on item update
class MilitaryServiceAttitudeUpdate(MilitaryServiceAttitudeBase):
    pass


# Properties shared by models stored in DB
class MilitaryServiceAttitudeInDBBase(MilitaryServiceAttitudeBase):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class MilitaryServiceAttitude(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    isActive: int
    class Config:
        orm_mode = True

# Properties properties stored in DB
class MilitaryServiceAttitudeInDB(MilitaryServiceAttitudeInDBBase):
    pass

