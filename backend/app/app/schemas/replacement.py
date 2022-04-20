from typing import Optional, List

from pydantic import BaseModel, Field
from datetime import date

from .internal_employee import InternalEmployee
from .replacement_type import ReplacementType

# Shared properties
class ReplacementBase(BaseModel):
    
    startDate: date
    endDate: date

# Properties to receive on item creation
class ReplacementCreate(ReplacementBase):
    typeId: int
    replacerId: int



# Properties to receive on item update
class ReplacementUpdate(ReplacementBase):
    typeId: int
    replacedId: int
    replacerId: int

# Properties shared by models stored in DB
class ReplacementInDBBase(ReplacementBase):
    id: int
    typeId: int
    replacedId: int
    replacerId: int
    isActive: int
    type: ReplacementType
    replaced: InternalEmployee
    replacer: InternalEmployee

    class Config:
        orm_mode = True


class ReplacementPatch(BaseModel):
    endDate: date
    isActive: int

# Properties to return to client
class Replacement(BaseModel):
    id: int
    startDate: date
    endDate: date
    type: ReplacementType
    replaced: InternalEmployee
    replacer: InternalEmployee

    class Config:
        orm_mode = True


# Properties properties stored in DB
class ReplacementInDB(ReplacementInDBBase):
    pass

