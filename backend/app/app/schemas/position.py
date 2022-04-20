from typing import Optional, List

from pydantic import BaseModel, Field
from datetime import date



# Shared properties
class PositionBase(BaseModel):
    eGovPositionId: int
    nameRu: str
    nameKz: str
    declinationId: int

# Properties to receive on item creation
class PositionCreate(PositionBase):
    pass

# Properties to receive on item update
class PositionUpdate(PositionBase):
    pass

# Properties shared by models stored in DB
class PositionInDBBase(PositionBase):
    id: int
    eGovPositionId: int
    nameRu: str
    nameKz: str
    declinationId: int

    class Config:
        orm_mode = True


# Properties to return to client
class Position(BaseModel):
    id: int
    eGovPositionId: int
    nameRu: str
    nameKz: str
    declinationId: int
    isActive: int

    class Config:
        orm_mode = True


# Properties properties stored in DB
class PositionInDB(PositionInDBBase):
    pass

