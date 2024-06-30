from datetime import datetime
from src.masks.main import mask_card_number, mask_account_number

# Тестируем функцию mask_card_number
def test_mask_card_number_valid(card_and_account_numbers):
    card_type, card_number = card_and_account_numbers['card_valid']
    assert mask_card_number(card_type, card_number) == 'Visa: 1234 56** **** 3456'

def test_mask_card_number_invalid(card_and_account_numbers):
    card_type, card_number = card_and_account_numbers['card_invalid']
    assert mask_card_number(card_type, card_number) == 'Неверный формат номера карты'

# Тестируем функцию mask_account_number с использованием фикстуры
def test_mask_account_number_valid(card_and_account_numbers):
    account_number = card_and_account_numbers['account_valid']
    assert mask_account_number(account_number) == 'Счёт: ****3456'

def test_mask_account_number_invalid(card_and_account_numbers):
    account_number = card_and_account_numbers['account_invalid']
    assert mask_account_number(account_number) == 'Неверный формат номера счета'