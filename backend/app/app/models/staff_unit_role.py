

from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class StaffUnitRole(Base):
    __tablename__ = 'staff-unit-role'

    id = Column(Integer, primary_key=True, index=True)
    employeeFuncRoleSpecId = Column(Integer)
    nameRu = Column(String)
    nameKz = Column(String)
    isActive = Column(Integer, default=1)


