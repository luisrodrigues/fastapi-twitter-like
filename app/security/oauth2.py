from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.core.config import Settings
from app.security.token import verify_token

app_settings = Settings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=app_settings.LOGIN_ENDPOINT)


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)

