from src.generators import filter_by_currency


def test_filter_by_currency():
    transactions = [
        {'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}},
        {'operationAmount': {'amount': 200, 'currency': {'code': 'EUR'}}},
        {'operationAmount': {'amount': 300, 'currency': {'code': 'USD'}}},
        {'operationAmount': {'amount': 400, 'currency': {'code': 'JPY'}}}
    ]

    # Проверяем фильтрацию по USD
    usd_transactions = list(filter_by_currency(transactions, 'USD'))
    assert usd_transactions == [
        {'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}},
        {'operationAmount': {'amount': 300, 'currency': {'code': 'USD'}}}
    ]

    # Проверяем фильтрацию по EUR
    eur_transactions = list(filter_by_currency(transactions, 'EUR'))
    assert eur_transactions == [
        {'operationAmount': {'amount': 200, 'currency': {'code': 'EUR'}}},
    ]