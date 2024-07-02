from datetime import datetime
import pytest
from src.masks.main import mask_card_number, mask_account_number


# Параметризация для теста функции mask_card_number
@pytest.mark.parametrize("card_type, card_number, expected", [
    ('Visa', '1234567890123456', 'Visa: 1234 56** **** 3456'),
    ('Visa', '12345', 'Неверный формат номера карты')
])
def test_mask_card_number(card_type, card_number, expected):
    assert mask_card_number(card_type, card_number) == expected

# Параметризация для теста функции mask_account_number
@pytest.mark.parametrize("account_number, expected", [
    ('1234567890123456', 'Счёт: ****3456'),
    ('123', 'Неверный формат номера счета')
])
def test_mask_account_number(account_number, expected):
    assert mask_account_number(account_number) == expected