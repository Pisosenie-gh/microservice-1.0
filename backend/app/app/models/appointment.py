from email.policy import default
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .internal_employee import InternalEmployee
    from .staff_unit import StaffUnit



class Appointment(Base):
    __tablename__ = "appointment"
    id = Column(Integer, primary_key=True, index=True)
    decreeId = Column(Integer)
    startDate = Column(Date)
    endDate = Column(Date)
    isFRP = Column(Boolean)
    isTemporary = Column(Boolean)
    isActive = Column(Integer, default=1)

    employeeId = Column(Integer, ForeignKey('internal_employee.id'), nullable=True)
    staffUnitId = Column(Integer, ForeignKey('staff_unit.id'), nullable=True)

  
    employee = relationship("InternalEmployee", backref="employee")
    staffUnit = relationship("StaffUnit", backref="staff_unit")