from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class StaffUnitTypeBase(BaseModel):
    id: int
    nameRu: str
    nameKz: str




# Properties shared by models stored in DB
class StaffUnitTypeInDBBase(StaffUnitTypeBase):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class StaffUnitType(StaffUnitTypeBase):
    id: int
    class Config:
        orm_mode = True

# Properties properties stored in DB
class StaffUnitTypeInDB(StaffUnitTypeInDBBase):
    pass

