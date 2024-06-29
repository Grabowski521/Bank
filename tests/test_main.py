from src.masks.main import mask_card_number, mask_account_number

# Тестируем функцию mask_card_number
def test_mask_card_number_valid():
    assert mask_card_number('Visa', '1234567890123456') == 'Visa: 1234 56** **** 3456'

def test_mask_card_number_invalid():
    assert mask_card_number('Visa', '12345') == 'Неверный формат номера карты'

# Тестируем функцию mask_account_number
def test_mask_account_number_valid():
    assert mask_account_number('1234567890123456') == 'Счёт: ****3456'

def test_mask_account_number_invalid():
    assert mask_account_number('123') == 'Неверный формат номера счета'