from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

from .position import Position
from .staff_unit_type import StaffUnitType
from .staff_category import StaffCategory
# Shared properties
class StaffUnitBase(BaseModel):

    organizationUnitId: int
    rate: float



# Properties to receive on item creation
class StaffUnitCreate(StaffUnitBase):
    positionId: int
    typeId: int
    staffCategoryId: int


# Properties to receive on item update
class StaffUnitUpdate(StaffUnitBase):
    positionId: int
    typeId: int
    staffCategoryId: int



# Properties shared by models stored in DB
class StaffUnitInDBBase(StaffUnitBase):
    id: int
    positionId: int
    typeId: int
    staffCategoryId: int
    position: Position
    type: StaffUnitType
    staffCategory: StaffCategory
    isActive: int
    class Config:
        orm_mode = True


# Properties to return to client
class StaffUnit(BaseModel):
    id: int
    organizationUnitId: int
    rate: float
    isActive: int
    position: Position
    type: StaffUnitType
    staffCategory: StaffCategory

    class Config:
        orm_mode = True

# Properties properties stored in DB
class StaffUnitInDB(StaffUnitInDBBase):
    pass

