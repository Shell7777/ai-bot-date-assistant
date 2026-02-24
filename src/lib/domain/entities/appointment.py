from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

@dataclass
class Appointment:
    business_id: str
    appointment_id: str
    client_name: str
    service_name: str
    start_time: datetime
    status: str
