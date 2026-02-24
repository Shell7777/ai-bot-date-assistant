from http.client import responses
from fastapi import HTTPException, Depends

from src.lib.domain.entities.appointment import Appointment
from src.lib.infrastructure.database.repositories.dependencies import get_appointment_repository

class AppointmentHandler:
    # FastAPI inyectará el repositorio en cada llamada
    async def get_all(self, repo = Depends(get_appointment_repository)):
        response = repo.get_all()
        return {"message": "Appointments found", "response": response}

    async def save(self, appointment: Appointment, repo = Depends(get_appointment_repository)):
        response = repo.save(appointment)
        return {"message": "Appointment saved", "response": response}

    async def get_by_id(self, business_id: str, appointment_id: str, repo = Depends(get_appointment_repository)):
        response = repo.get_by_id(business_id, appointment_id)
        if not response:
            raise HTTPException(status_code=404, detail="Appointment not found")
        return {"message": "Appointment found", "response": response}