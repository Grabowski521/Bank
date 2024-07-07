from src.generators import card_number_generator


def test_card_number_generator():
    start_card_number = '0000 0000 0000 0001'
    end_card_number = '0000 0000 0000 0002'
    generated_numbers = list(card_number_generator(start_card_number, end_card_number))
    expected_numbers = ['0000 0000 0000 0001', '0000 0000 0000 0002']
    assert generated_numbers == expected_numbers
