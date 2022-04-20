from typing import List, Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.replacement_type import ReplacementType


class CRUDReplacementType(CRUDBase[ReplacementType, None, None]):
    pass

replacement_type = CRUDReplacementType(ReplacementType)


