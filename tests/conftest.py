import pytest
from datetime import datetime

@pytest.fixture
def records():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-06-30T12:00:00.000000'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-06-30T13:00:00.000000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-06-30T14:00:00.000000'},
    ]



@pytest.fixture
def date_strings():
    return {
        'valid': '2018-07-11T02:26:18.671407',
        'invalid': 'invalid_date_string'
    }

@pytest.fixture
def card_and_account_numbers():
    return {
        'card_valid': ('Visa', '1234567890123456'),
        'card_invalid': ('Visa', '12345'),
        'account_valid': '1234567890123456',
        'account_invalid': '123'
    }