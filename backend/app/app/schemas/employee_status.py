from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class EmployeeStatusBase(BaseModel):
    id: int
    nameRu: str
    nameKz: str




# Properties shared by models stored in DB
class EmployeeStatusInDBBase(EmployeeStatusBase):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class EmployeeStatus(EmployeeStatusBase):
    id: int
    class Config:
        orm_mode = True

# Properties properties stored in DB
class EmployeeStatusInDB(EmployeeStatusInDBBase):
    pass

