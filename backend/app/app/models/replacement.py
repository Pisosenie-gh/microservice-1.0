
from email.policy import default
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from .internal_employee import InternalEmployee
    from .replacement_type import ReplacementType


class Replacement(Base):
    __tablename__ = 'replacement'

    id = Column(Integer, primary_key=True, index=True)
    startDate = Column(Date)
    endDate = Column(Date)
    isActive = Column(Integer, default=1)
    typeId = Column(Integer, ForeignKey('replacement_type.id'))
    replacedId = Column(Integer, ForeignKey('internal_employee.id'), nullable=True)
    replacerId = Column(Integer, ForeignKey('internal_employee.id'), nullable=True)
    


    type = relationship("ReplacementType", backref="type",  foreign_keys='Replacement.typeId')
    replaced = relationship("InternalEmployee", backref="replaced",  foreign_keys='Replacement.replacedId')
    replacer = relationship("InternalEmployee", backref="replacer",  foreign_keys='Replacement.replacerId')