from src.generators import transaction_descriptions


def test_transaction_descriptions():
    transactions = [
        {'description': 'Перевод на счет', 'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}},
        {'description': 'Оплата услуг', 'operationAmount': {'amount': 200, 'currency': {'code': 'EUR'}}},
        {'description': 'Покупка в интернет-магазине', 'operationAmount': {'amount': 300, 'currency': {'code': 'USD'}}},
        {'description': 'Платная подписка', 'operationAmount': {'amount': 400, 'currency': {'code': 'JPY'}}}
    ]

    descriptions = [
        'Перевод на счет - 100 USD',
        'Оплата услуг - 200 EUR',
        'Покупка в интернет-магазине - 300 USD',
        'Платная подписка - 400 JPY'
    ]

    assert list(transaction_descriptions(transactions)) == descriptions