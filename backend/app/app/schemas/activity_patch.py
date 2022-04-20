from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class ActivityPatch(BaseModel):
    isActive: int


    class Config:
        orm_mode = True


