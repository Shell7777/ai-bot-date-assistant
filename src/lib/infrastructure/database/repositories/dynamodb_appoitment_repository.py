from src.lib.infrastructure.database.dynamo_client import get_dynamodb
from src.lib.domain.entities.appointment import Appointment

class DynamoAppointmentRepository:

    def __init__(self):
        self.table = get_dynamodb().Table("appointments")

    def save(self, appointment: Appointment):
        self.table.put_item(
            Item={
                "PK": f"BUSINESS#{appointment.business_id}",
                "SK": f"APPOINTMENT#{appointment.appointment_id}",
                "client_name": appointment.client_name,
                "service_name": appointment.service_name,
                "start_time": appointment.start_time.isoformat(),
                "status": appointment.status
            }
        )

    def get_all(self):
        response = self.table.scan()
        items = response.get("Items",[])
        appointments = []
        for item in items:
            appointment = Appointment(
                business_id=item.get("PK"),
                appointment_id=item.get("SK"),
                client_name=item.get("client_name"),
                service_name=item.get("service_name"),
                start_time=item.get("start_time"),
                status=item.get("status")
            )
            appointments.append(appointment)
        return appointments

    def get_by_id(self, business_id :str, appointment_id : str):
        response = self.table.get_item(Key = {
            "PK": f"BUSINESS#{business_id}",
            "SK": f"APPOINTMENT#{appointment_id}"
        })
        print(response)
        return response.get("Item")