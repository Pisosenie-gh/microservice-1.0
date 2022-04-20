from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Grade])
def read_grades(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей грейдов
    """

    grade = crud.grade.get_multi(db, skip=skip, limit=limit)


    return grade


@router.post("/", response_model=schemas.Grade)
def create_grade(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.GradeCreate,

) -> Any:
    """
    Добавление записи грейдов
    """
    grade = crud.grade.create(db=db, obj_in=grade_in)
    return grade


@router.put("/{id}", response_model=schemas.Grade)
def update_grade(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.GradeUpdate,
) -> Any:
    """
    Обновление записи грейдов
    """
    grade = crud.grade.get(db=db, id=id)
    if not grade:
        raise HTTPException(status_code=404,  detail="grade {id} not found ".format(id=id))

    grade = crud.grade.update(db=db, db_obj=grade, obj_in=grade_in)
    return grade


@router.get("/{id}", response_model=schemas.Grade)
def read_grade(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись грейдов по id
    """
    grade = crud.grade.get(db=db, id=id)
    if not grade:
        raise HTTPException(status_code=404,  detail="grade {id} not found ".format(id=id))

    return grade


@router.patch("/{id}", response_model=schemas.Grade)
def patch_grade(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    grade = crud.grade.get(db=db, id=id)
    if not grade:
        raise HTTPException(status_code=404, detail="grade {id} not found ".format(id=id))

    grade = crud.grade.patch(db=db, db_obj=grade, obj_in=grade_in)
    return grade