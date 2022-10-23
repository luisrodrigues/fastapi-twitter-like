from sqlalchemy.orm import Session

from app.schemas import user_schema
from app.models import user_model
from app.security import hashing


def create_user(request: user_schema.User, db: Session):
    hashed_password = hashing.bcrypt(request.password)
    # create a user
    new_user = user_model.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_id(user_id: int, db: Session):
    # fetch user by id
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    return user


def get_user_by_email(email: str, db: Session):
    # fetch user by email
    user = db.query(user_model.User).filter(user_model.User.email == email).first()
    return user
