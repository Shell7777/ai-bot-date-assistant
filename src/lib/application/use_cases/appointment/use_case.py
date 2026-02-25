from abc import ABC

from src.lib.domain.entities.appointment import Appointment
import uuid

class AppointmentUseCase(ABC):
    def __init__(self, repository):
        self.repository = repository

    def save(self, business_id, client_name, service_name, start_time):
        new_appointment = Appointment(
            business_id=business_id,
            appointment_id=str(uuid.uuid4()),
            client_name=client_name,
            service_name=service_name,
            start_time=start_time,
            status="scheduled"
        )
        self.repository.save(new_appointment)
        return new_appointment
    
    def get_all(self): 
        return self.repository.get_all()
    
    def get_by_id(self, business_id, appointment_id):
        return self.repository.get_by_id(business_id, appointment_id)
    