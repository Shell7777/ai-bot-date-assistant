from src.lib.application.use_cases.appointment.use_case import AppointmentUseCase
from src.lib.infrastructure.database.repositories.dynamodb_appoitment_repository import DynamoAppointmentRepository

repository =  DynamoAppointmentRepository()
def get_appointment_use_case():
    return AppointmentUseCase(repository)
