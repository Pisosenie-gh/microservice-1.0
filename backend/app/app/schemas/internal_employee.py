from typing import Optional, List

from pydantic import BaseModel, Field
from datetime import date

from .employee_status import EmployeeStatus
from .ldap_login import LdapLogin
from .grade import Grade
from .marital_status import MaritalStatus
from .military_service_attitude import MilitaryServiceAttitude
from .nationality_gender import NationalityGender


# Shared properties
class InternalEmployeeBase(BaseModel):
    individualId: int
    legalOrganizationlId: int
    fullnameDeclinationId: int
    financialAccountId: int
    iin: str
    personnelNumber: str
    lastName: str
    firstName: str
    middleName: str
    birthDate: date
    workStartDate: date
    gender: str
    isReserveMember: bool
    isInsider: bool

# Properties to receive on item creation
class InternalEmployeeCreate(InternalEmployeeBase):
    individualId: int
    legalOrganizationlId: int
    fullnameDeclinationId: int
    financialAccountId: int
    iin: str
    personnelNumber: str
    lastName: str
    firstName: str
    middleName: str
    birthDate: date
    workStartDate: date
    gender: str
    isReserveMember: bool
    isInsider: bool
    statusId: int
    gradeId: int
    maritalStatusId: int
    militaryServiceAttitudeId: int
    nationalityGenderId: int




# Properties to receive on item update
class InternalEmployeeUpdate(InternalEmployeeBase):
    individualId: int
    legalOrganizationlId: int
    fullnameDeclinationId: int
    financialAccountId: int
    iin: str
    personnelNumber: str
    lastName: str
    firstName: str
    middleName: str
    birthDate: date
    workStartDate: date
    gender: str
    isReserveMember: bool
    isInsider: bool
    statusId: int
    gradeId: int
    maritalStatusId: int
    militaryServiceAttitudeId: int
    
# Properties shared by models stored in DB
class InternalEmployeeInDBBase(InternalEmployeeBase):
    id: int
    individualId: int
    legalOrganizationlId: int
    fullnameDeclinationId: int
    financialAccountId: int
    iin: str
    personnelNumber: str
    lastName: str
    firstName: str
    middleName: str
    birthDate: date
    workStartDate: date
    gender: str
    isReserveMember: bool
    isInsider: bool
    isActive: int
    statusId: int
    gradeId: int
    maritalStatusId: int
    militaryServiceAttitudeId: int
    status: EmployeeStatus
    grade: Grade
    marital_status: MaritalStatus
    militaryServiceAttitude: MilitaryServiceAttitude
    nationalityGender: NationalityGender

    class Config:
        orm_mode = True

class InternalEmployeePatch(BaseModel):
    personnelNumber: str
    statusId: int
    isReserveMember: bool
    isInsider: bool
    isActive: int

class InternalEmployeeAddLdap(BaseModel):
    ldapLoginId: int

# Properties to return to client
class InternalEmployee(InternalEmployeeBase):
    id: int
    individualId: int
    legalOrganizationlId: int
    fullnameDeclinationId: int
    financialAccountId: int
    iin: str
    personnelNumber: str
    lastName: str
    firstName: str
    middleName: str
    birthDate: date
    workStartDate: date
    isReserveMember: bool
    isInsider: bool
    gender: str
    isActive: int
    status: EmployeeStatus
    ldapLogin: Optional[LdapLogin] 
    grade: Grade
    marital_status: MaritalStatus
    militaryServiceAttitude: MilitaryServiceAttitude
    nationalityGender: NationalityGender


    class Config:
        orm_mode = True



    class Config:
        orm_mode = True


# Properties properties stored in DB
class InternalEmployeeInDB(InternalEmployeeInDBBase):
    pass

