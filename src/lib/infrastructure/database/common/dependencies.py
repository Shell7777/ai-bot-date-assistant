from src.lib.application.use_cases.appointment.use_case import AppointmentUseCase
from src.lib.application.use_cases.llm.ChatMinifyUseCase import ChatMinifyUseCase
from src.lib.infrastructure.database.repositories.dynamodb_appoitment_repository import DynamoAppointmentRepository
from src.lib.infrastructure.llm.gemini import GeminiClient

repository =  DynamoAppointmentRepository()
client_llm = GeminiClient()

## Dependency Injection functions
'''appointment use case'''
def get_appointment_use_case():
    return AppointmentUseCase(repository)


'''appointment llm use case'''
def llm_chat_minify():
    return ChatMinifyUseCase(llm_port=client_llm)