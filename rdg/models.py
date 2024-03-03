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
