from datetime import datetime
from pydantic import BaseModel

class WebhookRequest(BaseModel):
    phone: str
    message: str
    business_id: str
    timestamp: datetime     