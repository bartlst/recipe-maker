from fastapi.routing import APIRouter
from .auth import auth_router

base_router = APIRouter()
base_router.include_router(auth_router)