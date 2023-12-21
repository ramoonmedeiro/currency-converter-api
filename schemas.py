from pydantic import BaseModel, validator, Field
from typing import List
import re


class ConverterInputBody(BaseModel):
    to_currency: List[str]
    amount: float = Field(gt=0)

    @validator('to_currency')
    def validate_to_currency(cls, value):
        for currency in value:
            if not re.match("^[A-Z]{3}$", currency):
                raise ValueError(f'Invalid to_currency: {currency}')
        return value
