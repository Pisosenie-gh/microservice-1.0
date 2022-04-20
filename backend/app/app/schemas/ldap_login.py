from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class LdapLoginBase(BaseModel):
    login: str



# Properties to receive on item creation
class LdapLoginCreate(LdapLoginBase):
    pass


# Properties to receive on item update
class LdapLoginUpdate(LdapLoginBase):
    pass


# Properties shared by models stored in DB
class LdapLoginInDBBase(LdapLoginBase):
    id: int
    login: str
    class Config:
        orm_mode = True


# Properties to return to client
class LdapLogin(BaseModel):
    id: int
    login: str
    isActive: int
    class Config: 
        orm_mode = True

# Properties properties stored in DB
class LdapLoginInDB(LdapLoginInDBBase):
    pass

