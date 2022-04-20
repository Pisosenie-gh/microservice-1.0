
from sqlalchemy import Column, Integer, String

from app.db.base_class import Base




class EmployeeStatus(Base):
    __tablename__ = 'employee-status'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)
