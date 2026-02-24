from fastapi import APIRouter, Depends
from src.lib.application.use_cases.appointment.use_case import AppointmentUseCase
from src.lib.domain.entities.appointment import Appointment
from src.lib.infrastructure.api.dto.appointment_request import AppointmentRequest
from src.lib.infrastructure.database.repositories.dependencies import get_appointment_use_case

router = APIRouter(prefix="/appointments", tags=["Appointments"],redirect_slashes=False)

@router.get("")
def get_all(use_case: AppointmentUseCase = Depends(get_appointment_use_case)):
    print("Getting all appointments")
    return use_case.get_all()

@router.get("{business_id}/{appointment_id}")
def get_by_id(
    business_id: str, 
    appointment_id: str, 
    use_case: AppointmentUseCase = Depends(get_appointment_use_case)
):
    return use_case.get_by_id(business_id, appointment_id)

@router.post("")
def save(
   appointment_data: AppointmentRequest,
    use_case: AppointmentUseCase = Depends(get_appointment_use_case)
):
    return use_case.save(
        business_id=appointment_data.business_id,
        client_name=appointment_data.client_name,
        service_name=appointment_data.service_name,
        start_time=appointment_data.start_time
    )