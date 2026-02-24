from fastapi import APIRouter
from src.lib.infrastructure.api.routes.appointment_routes import router as appointment_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(appointment_router)
