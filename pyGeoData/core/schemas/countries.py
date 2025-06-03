from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CountryBase(BaseModel):
    name: str
    code: str

class CountryCreate(CountryBase):
    pass

class Country(CountryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
