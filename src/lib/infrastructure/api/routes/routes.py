from fastapi import APIRouter
from src.lib.infrastructure.api.routes.webhook_routes import router as webhook_routes
from src.lib.infrastructure.api.routes.appointment_routes import router as appointment_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(appointment_router)
api_router.include_router(webhook_routes)

