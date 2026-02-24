from dataclasses import dataclass 
from datetime import datetime

@dataclass
class Appointment:
    business_id: str
    appointment_id: str
    client_name: str
    service_name: str
    start_time: datetime
    status: str
