from typing import Optional, List

from pydantic import BaseModel, Field
from datetime import date

from .internal_employee import InternalEmployee
from .staff_unit import StaffUnit



# Shared properties
class AppointmentBase(BaseModel):
    decreeId: int
    startDate: date
    endDate: date
    isFRP: bool
    isTemporary: bool


# Properties to receive on item creation
class AppointmentCreate(AppointmentBase):
    decreeId: int
    startDate: date
    endDate: date
    isFRP: bool
    isTemporary: bool
    staffUnitId: int




# Properties to receive on item update
class AppointmentUpdate(AppointmentBase):
    decreeId: int
    startDate: date
    endDate: date
    isFRP: bool
    isTemporary: bool
    staffUnitId: int
    employeeId: int
    
# Properties shared by models stored in DB
class AppointmentInDBBase(AppointmentBase):
    id: int
    decreeId: int
    startDate: date
    endDate: date
    isFRP: bool
    isTemporary: bool
    staffUnitId: int
    employeeId: int
    isActive: int
    employee: InternalEmployee
    staffUnit: StaffUnit
    class Config:
        orm_mode = True

class AppointmentPatch(BaseModel):
    endDate: date
    isActive: int
    
# Properties to return to client
class Appointment(AppointmentBase):
    id: int
    decreeId: int
    startDate: date
    endDate: date
    isFRP: bool
    isTemporary: bool
    isActive: int
    employee: InternalEmployee
    staffUnit: StaffUnit


    class Config:
        orm_mode = True


# Properties properties stored in DB
class AppointmentInDB(AppointmentInDBBase):
    pass

