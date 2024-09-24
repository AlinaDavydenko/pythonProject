import os
from typing import Any

import requests
from dotenv import load_dotenv

# получаем ключ Api и настройки
load_dotenv()


def sum_of_transactions(transaction: dict) -> Any:
    """ Функцию принимает json файл и возвращает сумму транзакций в рублях """
    api_key = os.getenv('API_KEY')
    currency_code = transaction['operationAmount']['currency']['code']
    amount = float(transaction['operationAmount']['amount'])
    if currency_code == 'RUB':
        return amount
    elif currency_code in ['EUR', 'USD']:
        headers = {
            "apikey": api_key
        }
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        response = requests.get(url, headers=headers)
        result = response.json()
        return result['result']
    else:
        return f'Недопустимый код валюты {currency_code}'
