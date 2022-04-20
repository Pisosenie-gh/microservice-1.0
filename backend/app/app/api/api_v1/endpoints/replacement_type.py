from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ReplacementType])
def read_replacement_type(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Тип замещения: Возвращает массив записей
    """

    replacement_type = crud.replacement_type.get_multi(db, skip=skip, limit=limit)


    return replacement_type

@router.get("/{id}", response_model=schemas.ReplacementType)
def read_replacement_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Тип замещения: возвращает запись
    """
    replacement_type = crud.replacement_type.get(db=db, id=id)
    if not replacement_type:
        raise HTTPException(status_code=404, detail="replacement_type {id} not found ".format(id=id))

    return replacement_type

