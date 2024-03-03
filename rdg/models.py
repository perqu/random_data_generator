from typing import Optional
from datetime import datetime,timedelta
from pydantic import BaseModel, validator

class IntData(BaseModel):
    range_from: int = 0
    range_to: int = 100
    amount: Optional[int] = 1

    @validator("range_to")
    def range_to_greater_than_range_from(cls, v, values):
        if v <= values["range_from"]:
            raise ValueError("range_to must be greater than range_from")
        return v
    
class FloatData(BaseModel):
    range_from: float = 0
    range_to: float = 100
    decimal_places: int = 2
    amount: Optional[int] = 1

    @validator("range_to")
    def range_to_greater_than_range_from(cls, v, values):
        if v <= values["range_from"]:
            raise ValueError("range_to must be greater than range_from")
        return v
    
class DateData(BaseModel):
    range_from: datetime = datetime.now() - timedelta(days=365)
    range_to: datetime = datetime.now()
    amount: Optional[int] = 1

class EmailData(BaseModel):
    length: int = 7
    domain: str = '@gmail.com'
    amount: Optional[int] = 1

    @validator('length')
    def length_min_max(cls, v):
        if v < 6 or v > 64:
            raise ValueError('length must be between 6 and 64 characters')
        return v
    
    @validator('domain')
    def domain_max_length(cls, v):
        if len(v) > 255:
            raise ValueError('Domain length cannot exceed 255')
        return v