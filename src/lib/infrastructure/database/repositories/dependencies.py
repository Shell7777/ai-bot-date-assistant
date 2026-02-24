from src.lib.application.use_cases.create_appointment_use_case import CreateAppointmentUseCase
from src.lib.infrastructure.database.repositories.dynamodb_appoitment_repository import DynamoAppointmentRepository

def get_appointment_repository():
    return DynamoAppointmentRepository()

def get_create_appointment_use_case():
    repo = get_appointment_repository
    return CreateAppointmentUseCase(repo)
