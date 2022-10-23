from fastapi import APIRouter

from app.routers import posts_router, users_router, auth_router

api_router = APIRouter()
api_router.include_router(auth_router.router, tags=["Authentication"])
api_router.include_router(users_router.router, prefix="/users", tags=["Users"])
api_router.include_router(posts_router.router, prefix="/posts", tags=["Posts"])
