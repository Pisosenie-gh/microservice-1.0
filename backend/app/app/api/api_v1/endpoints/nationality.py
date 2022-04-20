from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Nationality])
def read_nationality(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника национальности
    """

    nationality = crud.nationality.get_multi(db, skip=skip, limit=limit)


    return nationality


@router.post("/", response_model=schemas.Nationality)
def create_nationality(
    *,
    db: Session = Depends(deps.get_db),
    nationality_in: schemas.NationalityCreate,

) -> Any:
    """
    Добавление записи справочника национальности
    """
    nationality = crud.nationality.create(db=db, obj_in=nationality_in)
    return nationality


@router.put("/{id}", response_model=schemas.Nationality)
def update_nationality(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    nationality_in: schemas.NationalityUpdate,
) -> Any:
    """
    Обновление записи справочника национальности
    """
    nationality = crud.nationality.get(db=db, id=id)
    if not nationality:
        raise HTTPException(status_code=404, detail="nationality {id} not found ".format(id=id))

    nationality = crud.nationality.update(db=db, db_obj=nationality, obj_in=nationality_in)
    return nationality


@router.get("/{id}", response_model=schemas.Nationality)
def read_nationality(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника национальности
    """
    nationality = crud.nationality.get(db=db, id=id)
    if not nationality:
        raise HTTPException(status_code=404, detail="nationality {id} not found ".format(id=id))

    return nationality


@router.patch("/{id}", response_model=schemas.Nationality)
def patch_nationality(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    nationality_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    nationality = crud.nationality.get(db=db, id=id)
    if not nationality:
        raise HTTPException(status_code=404, detail="nationality {id} not found ".format(id=id))

    nationality = crud.nationality.patch(db=db, db_obj=nationality, obj_in=nationality_in)
    return nationality