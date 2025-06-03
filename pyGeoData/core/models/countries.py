from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Country(BaseModel):
    id: int
    name: str
    code: str
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
