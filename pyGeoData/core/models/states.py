from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class State(BaseModel):
    id: int
    name: str
    country_id: Optional[int] = None
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
