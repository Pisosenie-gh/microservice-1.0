from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/{id}/staff-unit-role/", response_model=List[schemas.StaffUnitRole])
def read_staff_unit_role(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    id: int = 0

) -> Any:
    """
    Роль штатной единицы: Возвращает массив записей
    """

    staff_unit_role = crud.staff_unit_role.get_multi(db, skip=skip, limit=limit)


    return staff_unit_role



@router.post("/{id}/staff-unit-role/", response_model=schemas.StaffUnitRole)
def create_staff_unit_role(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.StaffUnitRoleCreate,

) -> Any:
    """
    Роль штатной единицы: Добавление записи
    """
    staff_unit_role = crud.staff_unit_role.create(db=db, obj_in=grade_in)
    return staff_unit_role


@router.put("/staff-unit-role/{id}", response_model=schemas.StaffUnitRole)
def update_staff_unit_role(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.StaffUnitRoleUpdate,
) -> Any:
    """
    Роль штатной единицы: Обновление записи
    """
    staff_unit_role = crud.staff_unit_role.get(db=db, id=id)
    if not staff_unit_role:
        raise HTTPException(status_code=404, detail="staff_unit_role {id} not found ".format(id=id))

    staff_unit_role = crud.staff_unit_role.update(db=db, db_obj=staff_unit_role, obj_in=grade_in)
    return staff_unit_role


@router.get("/staff-unit-role/{id}", response_model=schemas.StaffUnitRole)
def read_staff_unit_role(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Роль штатной единицы: Возвращает запись
    """
    staff_unit_role = crud.staff_unit_role.get(db=db, id=id)
    if not staff_unit_role:
        raise HTTPException(status_code=404, detail="staff_unit_role {id} not found ".format(id=id))

    return staff_unit_role


@router.patch("/staff-unit-role/{id}", response_model=schemas.StaffUnitRole)
def patch_staff_unit_role(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    staff_unit_role_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    staff_unit_role = crud.staff_unit_role.get(db=db, id=id)
    if not staff_unit_role:
        raise HTTPException(status_code=404, detail="staff_unit_role {id} not found ".format(id=id))

    staff_unit_role = crud.staff_unit_role.patch(db=db, db_obj=staff_unit_role, obj_in=staff_unit_role_in)
    return staff_unit_role