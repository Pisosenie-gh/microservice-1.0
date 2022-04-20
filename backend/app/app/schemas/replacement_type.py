from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class ReplacementTypeBase(BaseModel):
    id: int
    nameRu: str
    nameKz: str




# Properties shared by models stored in DB
class ReplacementTypeInDBBase(ReplacementTypeBase):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class ReplacementType(ReplacementTypeBase):
    id: int
    class Config:
        orm_mode = True

# Properties properties stored in DB
class ReplacementTypeInDB(ReplacementTypeInDBBase):
    pass

