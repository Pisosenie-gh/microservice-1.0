from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Gender])
def read_gender(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Пол: Возвращает массив записей
    """

    gender = crud.gender.get_multi(db, skip=skip, limit=limit)


    return gender

@router.get("/{id}", response_model=schemas.Gender)
def read_gender(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Пол: возвращает запись
    """
    gender = crud.gender.get(db=db, id=id)
    if not gender:
        raise HTTPException(status_code=404, detail="gender {id} not found ".format(id=id))

    return gender

