from fastapi.routing import APIRouter

from .day import day_router

api_router = APIRouter()
api_router.include_router(day_router)
