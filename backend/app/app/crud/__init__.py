import imp
from re import I
from .crud_item import item
from .crud_user import user
from .crud_gender import gender
from .crud_replacement_type import replacement_type
from .crud_staff_unit_type import staff_unit_type
from .crud_staff_category import staff_category
from .crud_employee_status import employee_status
from .crud_nationality import nationality
from .crud_nationality_sap import nationality_sap
from .crud_nationality_gender import nationality_gender
from .crud_grade import grade
from .crud_military_service_attitude import military_service_attitude
from .crud_marital_status import marital_status
from .crud_position import position
from .crud_staff_unit_role import staff_unit_role
from .crud_staff_unit import staff_unit
from .crud_ldap_login import ldap_login
from .crud_internal_employee import internal_employee
from .crud_appointment import appointment
from .crud_replacement import replacement
# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
