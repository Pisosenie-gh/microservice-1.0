
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from .gender import Gender


class MaritalStatus(Base):
    __tablename__ = 'marital_status'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)
    genderId = Column(Integer, ForeignKey('gender.id'))
    gender = relationship("Gender", backref="marital_status", viewonly=True)
    isActive = Column(Integer, default=1)
    