from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DistrictBase(BaseModel):
    name: str
    state_id: Optional[int]

class DistrictCreate(DistrictBase):
    pass

class District(DistrictBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
