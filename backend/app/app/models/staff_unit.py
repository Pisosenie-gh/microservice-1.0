
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .position import Position
    from .staff_unit_type import StaffUnitType
    from .staff_category import StaffCategory



class StaffUnit(Base):
    __tablename__ = 'staff_unit'

    id = Column(Integer, primary_key=True, index=True)
    organizationUnitId = Column(Integer)
    rate = Column(Integer)
    isActive = Column(Integer, default=1)

    positionId = Column(Integer, ForeignKey('position.id'))
    typeId = Column(Integer, ForeignKey('staff_unit_type.id'))
    staffCategoryId = Column(Integer, ForeignKey('staff_category.id'))

    position = relationship("Position", backref="position", viewonly=True)
    type = relationship("StaffUnitType", backref="type", viewonly=True)
    staffCategory = relationship("StaffCategory", backref="category", viewonly=True)
