import pytest
from tests.generators import transaction_descriptions

def test_transaction_descriptions():
    transactions = [
        {'amount': 100, 'currency': 'USD'},
        {'amount': 200, 'currency': 'EUR'},
        {'amount': 300, 'currency': 'USD'},
        {'amount': 400, 'currency': 'JPY'}
    ]
    descriptions = [
        'Транзакция на сумму 100 в валюте USD.',
        'Транзакция на сумму 200 в валюте EUR.',
        'Транзакция на сумму 300 в валюте USD.',
        'Транзакция на сумму 400 в валюте JPY.'
    ]
    assert list(transaction_descriptions(transactions)) == descriptions