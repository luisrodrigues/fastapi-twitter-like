from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.config import Settings
from app.models.user_model import User
from app.api.dependencies import get_db
from app.security.token import create_access_token
from app.security import hashing

app_settings = Settings()
router = APIRouter()


@router.post(app_settings.LOGIN_ENDPOINT)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {request.username} was not found")

    if not hashing.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Invalid credentials for {request.username}")

    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
