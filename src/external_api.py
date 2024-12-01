import os
from dotenv import load_dotenv
import requests

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')


def convert_currency(transaction):
    amount = transaction.get('operationAmount', {}).get('amount')
    currency_code = transaction.get('operationAmount', {}).get('currency', {}).get('code')

    if amount is None or currency_code is None:
        raise ValueError("Недостаточно данных для конвертации")

    if currency_code == "RUB":
        return amount

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"

    headers = {
        "apikey": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе к API: {response.status_code} - {response.text}")

    result = response.json().get('result')

    if result is None:
        raise Exception("Не удалось получить результат конвертации из ответа API")

    return result


try:
    amount = float(input("Введите сумму для конвертации: "))
    currency_code = input("Введите код валюты (например, USD): ").strip().upper()

    transaction = {
        "operationAmount": {
            "amount": amount,
            "currency": {
                "code": currency_code
            }
        }
    }

    converted_amount = convert_currency(transaction)
    print(f"Конвертированная сумма: {converted_amount} RUB")
except ValueError as ve:
    print(f"Ошибка ввода: {ve}")
except Exception as e:
    print(f"Произошла ошибка: {e}")