from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import User, ShowUser
from app.api.dependencies import get_db
from app.services import users_service

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    # create a user
    return users_service.create_user(request, db)


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=ShowUser)
def read_user(user_id: int, db: Session = Depends(get_db)):
    # fetch user by id
    return users_service.get_user_by_id(user_id, db)
