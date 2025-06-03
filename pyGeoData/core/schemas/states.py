from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class StateBase(BaseModel):
    name: str
    country_id: Optional[int]

class StateCreate(StateBase):
    pass

class State(StateBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
