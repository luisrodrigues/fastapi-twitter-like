from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import Settings

app_settings = Settings()
app = FastAPI(title=app_settings.API_TITLE)
app.include_router(api_router)
