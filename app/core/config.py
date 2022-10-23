import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    # API
    API_TITLE: str = "Tweeddr API"
    # JWT
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    LOGIN_ENDPOINT: str = "/login"
    # DB
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./posts.db"
