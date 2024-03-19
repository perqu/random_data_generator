from typing import Optional
from datetime import datetime,timedelta
from pydantic import BaseModel, validator, field_validator, ValidationInfo
from rdg.data import phones

class IntData(BaseModel):
    range_from: int = 0
    range_to: int = 100
    amount: Optional[int] = 1

    @field_validator("range_to")
    def range_to_greater_than_range_from(cls, v, info: ValidationInfo):
        if v <= info.data.get('range_from'):
            raise ValueError("range_to must be greater than range_from")
        return v
    
class FloatData(BaseModel):
    range_from: float = 0
    range_to: float = 100
    decimal_places: int = 2
    amount: Optional[int] = 1

    @field_validator("range_to")
    def range_to_greater_than_range_from(cls, v, info: ValidationInfo):
        if v <= info.data.get("range_from"):
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

    @field_validator('length')
    def length_min_max(cls, v):
        if v < 6 or v > 64:
            raise ValueError('length must be between 6 and 64 characters')
        return v
    
    @field_validator('domain')
    def domain_max_length(cls, v):
        if len(v) > 255:
            raise ValueError('Domain length cannot exceed 255')
        return v
    
class PhoneData(BaseModel):
    country: str = 'poland'
    amount: Optional[int] = 1

    @field_validator('country')
    def country_exists(cls, v):
        if v.lower() not in phones:
            raise ValueError('There is no country like that')
        return v.lower()
    
class TableData(BaseModel):
    code: str