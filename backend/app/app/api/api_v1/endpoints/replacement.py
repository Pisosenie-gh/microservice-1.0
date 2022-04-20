from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/{id}/replacement/", response_model=List[schemas.Replacement])
def read_replacement(
    db: Session = Depends(deps.get_db),
    id: int = None,
    skip: int = 0,
    limit: int = 100,
    

) -> Any:
    """
    Возвращает массив записей замещений сотрудника<br>
    Поддерживается ограничение результатов выдачи при помощи параметров <b>skip</b> и <b>limit</b>
    """

    replacement = crud.replacement.get_multi(db, skip=skip, limit=limit, id=id)


    return replacement


@router.post("/{id}/replacement/", response_model=schemas.Replacement)
def create_replacement(
    *,
    db: Session = Depends(deps.get_db),
    replacement_in: schemas.ReplacementCreate,
    id: int

) -> Any:
    """
    Добавление записи замещения
    """
    replacement = crud.replacement.create(db=db, obj_in=replacement_in, id=id)
    return replacement


@router.put("/replacement/{id}", response_model=schemas.Replacement)
def update_replacement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    replacement_in: schemas.ReplacementUpdate,
) -> Any:
    """
    Обновление записи замещения
    """
    replacement = crud.replacement.get(db=db, id=id)
    if not replacement:
        raise HTTPException(status_code=404, detail="replacement {id} not found ".format(id=id))

    replacement = crud.replacement.update(db=db, db_obj=replacement, obj_in=replacement_in)
    return replacement


@router.get("/replacement/{id}", response_model=schemas.Replacement)
def read_replacement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись замещения по его id
    """
    replacement = crud.replacement.get(db=db, id=id)
    if not replacement:
        raise HTTPException(status_code=404, detail="replacement {id} not found ".format(id=id))

    return replacement


@router.patch("/replacement/{id}", response_model=schemas.Replacement)
def patch_replacement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    replacement_in: schemas.ReplacementPatch,
) -> Any:
    """
    Корректировка записи назначения
    """
    replacement = crud.replacement.get(db=db, id=id)
    if not replacement:
        raise HTTPException(status_code=404, detail="replacement {id} not found ".format(id=id))

    replacement = crud.replacement.patch(db=db, db_obj=replacement, obj_in=replacement_in)
    return replacement