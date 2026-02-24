from fastapi import APIRouter
from src.lib.infrastructure.api.appointment_handler import AppointmentHandler

# Definimos el prefijo específico para este grupo de rutas
router = APIRouter(prefix="/appointments", tags=["Appointments"])
handler = AppointmentHandler()

router.add_api_route("/", endpoint=handler.get_all, methods=["GET"])
router.add_api_route("/{business_id}/{appointment_id}", endpoint=handler.get_all, methods=["GET"])
router.add_api_route("/", endpoint=handler.save, methods=["POST"])