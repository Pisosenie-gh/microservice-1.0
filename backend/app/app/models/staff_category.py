

from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class StaffCategory(Base):
    __tablename__ = 'staff-category'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)



