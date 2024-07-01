from typing import List, Dict, Any
from datetime import datetime
from src.masks.processing import sort_by_state, sort_by_date

def test_sort_by_state(records):
    expected = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-06-30T12:00:00.000000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-06-30T14:00:00.000000'}
    ]
    assert sort_by_state(records) == expected

def test_sort_by_date_desc(records):
    expected = [
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-06-30T14:00:00.000000'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-06-30T13:00:00.000000'},
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-06-30T12:00:00.000000'}
    ]
    assert sort_by_date(records) == expected

def test_sort_by_date_asc(records):
    expected = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-06-30T12:00:00.000000'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-06-30T13:00:00.000000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-06-30T14:00:00.000000'}
    ]
    assert sort_by_date(records, order=False) == expected