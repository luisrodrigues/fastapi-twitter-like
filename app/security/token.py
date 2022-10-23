from fastapi import HTTPException
from datetime import datetime, timedelta

from jose import JWTError, jwt

from app.schemas.token_schema import TokenData
from app.core.config import Settings

app_settings = Settings()

ALGORITHM = "HS256"


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=app_settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, app_settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception: HTTPException):
    try:
        payload = jwt.decode(token, app_settings.SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        return TokenData(email=email)
    except JWTError:
        raise credentials_exception
