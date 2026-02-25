from datetime import datetime
from pydantic import BaseModel

class AppointmentRequest(BaseModel):
    business_id: str
    client_name: str
    service_name: str
    start_time: datetime     