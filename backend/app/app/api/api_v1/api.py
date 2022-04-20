from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, gender, replacement_type, staff_unit_type,\
    staff_category, employee_status, nationality_gender, nationality, nationality_sap, grade, military_service_attitude,\
        marital_status, position, staff_unit_role, staff_unit, ldap_login, internal_employee, appointment, replacement


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(gender.router, prefix="/core/gender", tags=["gender"])
api_router.include_router(replacement_type.router, prefix="/core/replacement-type", tags=["replacement-type"])
api_router.include_router(staff_unit_type.router, prefix="/core/staff-unit-type", tags=["staff-unit-type"])
api_router.include_router(staff_category.router, prefix="/core/staff-category", tags=["staff-category"])
api_router.include_router(employee_status.router, prefix="/core/employee-status", tags=["employee-status"])
api_router.include_router(nationality_sap.router, prefix="/core/nationality-sap", tags=["nationality-sap"])
api_router.include_router(nationality.router, prefix="/core/nationality", tags=["nationality"])
api_router.include_router(nationality_gender.router, prefix="/core/nationality-gender", tags=["nationality-gender"])
api_router.include_router(grade.router, prefix="/core/grader", tags=["grade"])
api_router.include_router(military_service_attitude.router, prefix="/core/military-service-attitude", tags=["military-service-attitude"])
api_router.include_router(marital_status.router, prefix="/core/marital-status", tags=["marital-status"])
api_router.include_router(position.router, prefix="/core/position", tags=["position"])
api_router.include_router(staff_unit_role.router, prefix="/staff-unit", tags=["staff_unit_role"])
api_router.include_router(staff_unit.router, prefix="/organization-unit", tags=["staff_unit"])
api_router.include_router(ldap_login.router, prefix="/employee", tags=["ldap-login"])
api_router.include_router(internal_employee.router, prefix="/internal-employee", tags=["internal-employee"])
api_router.include_router(appointment.router, prefix="/employee", tags=["appointment"])
api_router.include_router(replacement.router, prefix="/employee", tags=["replacement"])



