from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class StaffUnitRoleBase(BaseModel):
    employeeFuncRoleSpecId: int
    nameRu: str
    nameKz: str
    


# Properties to receive on item creation
class StaffUnitRoleCreate(StaffUnitRoleBase):
    pass


# Properties to receive on item update
class StaffUnitRoleUpdate(StaffUnitRoleBase):
    pass


# Properties shared by models stored in DB
class StaffUnitRoleInDBBase(StaffUnitRoleBase):
    id: int
    nameRu: str
    nameKz: str
    employeeFuncRoleSpecId: int
    isActive: int
    class Config:
        orm_mode = True


# Properties to return to client
class StaffUnitRole(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    employeeFuncRoleSpecId: int
    isActive: int
    class Config:
        orm_mode = True

# Properties properties stored in DB
class StaffUnitRoleInDB(StaffUnitRoleInDBBase):
    pass

