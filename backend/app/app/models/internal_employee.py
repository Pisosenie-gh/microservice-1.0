from email.policy import default
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .employee_status import EmployeeStatus
    from .grade import Grade
    from .marital_status import MaritalStatus
    from .military_service_attitude import MilitaryServiceAttitude
    from .nationality_gender import NationalityGender
    from .ldap_login import LdapLogin


class InternalEmployee(Base):
    __tablename__ = "internal-employee"
    id = Column(Integer, primary_key=True, index=True)
    individualId = Column(Integer)
    legalOrganizationlId = Column(Integer)
    fullnameDeclinationId = Column(Integer)
    financialAccountId = Column(Integer)
    iin = Column(String)
    personnelNumber = Column(String)
    lastName = Column(String)
    firstName = Column(String)
    middleName = Column(String)
    birthDate = Column(Date)
    workStartDate = Column(Date)
    isReserveMember  = Column(Boolean)
    isInsider = Column(Boolean)
    isActive = Column(String, default=1)
    gender = Column(String)
    statusId = Column(Integer, ForeignKey('employee-status.id'), nullable=True)
    gradeId = Column(Integer, ForeignKey('grade.id'), nullable=True)
    maritalStatusId = Column(Integer, ForeignKey('marital-status.id'), nullable=True)
    militaryServiceAttitudeId = Column(Integer, ForeignKey('military-service-attitude.id'), nullable=True)
    nationalityGenderId = Column(Integer, ForeignKey('nationality-gender.id'), nullable=True)
    ldapLoginId = Column(Integer, ForeignKey('ldap-login.id'), nullable=True)

    status = relationship("EmployeeStatus", backref="employee-status")
    grade = relationship("Grade", backref="grade")
    marital_status = relationship("MaritalStatus", backref="marital-status")
    militaryServiceAttitude = relationship("MilitaryServiceAttitude", backref="military-service-attitude")
    nationalityGender = relationship("NationalityGender", backref="nationality-gender")
    ldapLogin = relationship("LdapLogin", backref="ldap-login")