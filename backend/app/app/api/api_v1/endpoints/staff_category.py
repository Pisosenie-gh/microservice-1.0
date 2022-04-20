from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.StaffCategory])
def read_staff_category(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника категории персонала
    """

    staff_category = crud.staff_category.get_multi(db, skip=skip, limit=limit)


    return staff_category

@router.get("/{id}", response_model=schemas.StaffCategory)
def read_staff_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника категории персонала по id
    """
    staff_category = crud.staff_category.get(db=db, id=id)
    if not staff_category:
        raise HTTPException(status_code=404, detail="staff_category {id} not found ".format(id=id))

    return staff_category

