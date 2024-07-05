def filter_by_currency(transactions, currency):
    """
    Фильтрует транзакции по заданной валюте, указанной внутри 'operationAmount'.
    """
    return (transaction for transaction in transactions if transaction['operationAmount']['currency'] == currency)

transactions = [
    {'operationAmount': {'amount': 100, 'currency': 'USD'}},
    {'operationAmount': {'amount': 200, 'currency': 'EUR'}},
    {'operationAmount': {'amount': 300, 'currency': 'USD'}},
    {'operationAmount': {'amount': 400, 'currency': 'JPY'}}
]

usd_transactions = filter_by_currency(transactions, 'USD')
for transaction in usd_transactions:
    print(transaction)

#############################

def transaction_descriptions(transactions):
    """
    Генерирует описание каждой транзакции в списке.

    """
    for transaction in transactions:
            yield f"Транзакция на сумму {transaction['amount']} в валюте {transaction['currency']}."

transactions = [
    {'amount': 100, 'currency': 'USD'},
    {'amount': 200, 'currency': 'EUR'},
    {'amount': 300, 'currency': 'USD'},
    {'amount': 400, 'currency': 'JPY'}
]

for description in transaction_descriptions(transactions):
    print(description)

#############################

def card_number_generator(start, end):
    """
    Генератор номеров банковских карт в формате 'XXXX XXXX XXXX XXXX'.

    """
    start_num = int(start.replace(' ', ''))
    end_num = int(end.replace(' ', ''))

    for number in range(start_num, end_num + 1):
        str_number = str(number).zfill(16)
        yield f"{str_number[:4]} {str_number[4:8]} {str_number[8:12]} {str_number[12:]}"


start_card_number = '0000 0000 0000 0001'
end_card_number = '0000 0000 0000 0099' #Тут должно быть 9999 9999 9999 9999, но на тестах это долго, поэтому вариант попроще

for card_number in card_number_generator(start_card_number, end_card_number):
    print(card_number)