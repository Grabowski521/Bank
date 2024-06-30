from datetime import datetime
from src.masks.date import convert_date

def test_convert_date_valid(date_strings):
    assert convert_date(date_strings['valid']) == '11.07.2018'

def test_convert_date_invalid(date_strings):
    assert convert_date(date_strings['invalid']) == 'invalid'