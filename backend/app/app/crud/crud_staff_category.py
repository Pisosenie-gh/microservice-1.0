from typing import List, Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.staff_category import StaffCategory


class CRUDStaffCategory(CRUDBase[StaffCategory, None, None]):
    pass

staff_category = CRUDStaffCategory(StaffCategory)


