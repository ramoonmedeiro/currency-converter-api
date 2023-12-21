import requests
from dotenv import load_dotenv, find_dotenv
from fastapi import HTTPException
import os
load_dotenv(find_dotenv())

alphavantage_apikey = os.getenv("ALPHA_VANTAGE_APIKEY")


def converter(from_currency: str, to_currency: str, amount: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={alphavantage_apikey}'
    try:
        r = requests.get(url)
        data = r.json()
        exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        converted_amount = amount * exchange_rate
        return round(converted_amount, 3)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
