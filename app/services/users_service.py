from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user_schema import User
from app.repositories import users_repository


def check_user_exists(user: User):
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User was not found")


def create_user(request: User, db: Session):
    return users_repository.create_user(request, db)


def get_user_by_id(user_id: int, db: Session):
    # fetch user by id
    user = users_repository.get_user_by_id(user_id, db)
    check_user_exists(user)
    return user


def get_user_by_email(email: str, db: Session):
    # fetch user by email
    user = users_repository.get_user_by_email(email, db)
    check_user_exists(user)
    return user
