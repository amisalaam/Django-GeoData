from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class District(BaseModel):
    id: int
    name: str
    state_id: Optional[int] = None
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
