from typing import List, Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.gender import Gender


class CRUDGender(CRUDBase[Gender, None, None]):
    pass

gender = CRUDGender(Gender)


