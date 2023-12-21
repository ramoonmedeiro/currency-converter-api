from fastapi import APIRouter, Path, Query
from converter import converter
from schemas import ConverterInputBody

router = APIRouter()


@router.get("/api/v1/converter/{from_currency}")
def converter_v1(
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"),
    to_currency: str = Query(max_length=50, regex="^[A-Z]{3}(,[A-Z]{3})*$"),
    amount: float = Query(gt=0)
):
    results = {}
    to_currency = to_currency.upper().split(",")
    for currency in to_currency:
        results[f"{from_currency}_to_{currency}"] = converter(
            from_currency=from_currency,
            to_currency=currency,
            amount=amount
            )

    return results


@router.post("/api/v2/converter/{from_currency}")
def converter_v2(
    body: ConverterInputBody,
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$")
):
    to_currency = body.to_currency
    amount = body.amount

    results = {
        f"{from_currency}_to_{currency}": converter(
            from_currency,
            currency,
            amount
        ) for currency in to_currency
    }

    return results
