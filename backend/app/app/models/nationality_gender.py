
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .nationality import Nationality

if TYPE_CHECKING:
    from .gender import Gender


class NationalityGender(Base):
    __tablename__ = 'nationality-gender'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)
    isActive = Column(Integer, default=1)
    nationalityId = Column(Integer, ForeignKey('nationality.id'))
    genderId = Column(Integer, ForeignKey('gender.id'))
    nationality = relationship("Nationality", backref="init", viewonly=True)
    gender = relationship("Gender", backref="init", viewonly=True)
