import pytest
from tests.generators import filter_by_currency

def test_filter_by_currency():
    transactions = [
        {'amount': 100, 'currency': 'USD'},
        {'amount': 200, 'currency': 'EUR'},
        {'amount': 300, 'currency': 'USD'},
        {'amount': 400, 'currency': 'JPY'}
    ]
    expected = [
        {'amount': 100, 'currency': 'USD'},
        {'amount': 300, 'currency': 'USD'}
    ]
    assert list(filter_by_currency(transactions, 'USD')) == expected