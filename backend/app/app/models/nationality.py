
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .nationality_sap import NationalitySap  # noqa: F401

class Nationality(Base):
    __tablename__ = 'nationality'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)
    isActive = Column(Integer, default=1)

    nationalitySAPId = Column(Integer, ForeignKey('nationality-sap.id'))
    nationalitySAP = relationship("NationalitySap", backref="init", viewonly=True)

