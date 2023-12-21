from fastapi import APIRouter
from converter import converter

router = APIRouter()


@router.get("/converter/{from_currency}")
def converter_end(from_currency: str, to_currency: str, amount: float):
    results = {}
    to_currency = to_currency.upper().split(",")
    for currency in to_currency:
        results[f"{from_currency}_to_{currency}"] = converter(from_currency, currency, amount)
    return results
