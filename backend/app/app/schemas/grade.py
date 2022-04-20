from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class GradeBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class GradeCreate(GradeBase):
    pass


# Properties to receive on item update
class GradeUpdate(GradeBase):
    pass


# Properties shared by models stored in DB
class GradeInDBBase(GradeBase):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class Grade(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    isActive: int
    class Config: 
        orm_mode = True

# Properties properties stored in DB
class GradeInDB(GradeInDBBase):
    pass

