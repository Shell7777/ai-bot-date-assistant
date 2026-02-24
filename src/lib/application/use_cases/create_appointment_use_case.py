from src.lib.domain.entities.appointment import Appointment
import uuid

class CreateAppointmentUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, business_id, client_name, service_name, start_time):
        new_appointment = Appointment(
            business_id=business_id,
            appointment_id=str(uuid.uuid4()),
            client_name=client_name,
            service_name=service_name,
            start_time=start_time
        )
        self.repository.save(new_appointment)
        return new_appointment