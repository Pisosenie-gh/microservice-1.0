

from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class StaffUnitType(Base):
    __tablename__ = 'staff-unit-type'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)



