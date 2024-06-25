from typing import List, Dict, Any
from datetime import datetime


def sort_by_state(records: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей, оставляя только те, у которых ключ 'state' соответствует заданному значению.

    :param records: Список словарей, каждый из которых представляет запись с ключами 'id', 'state', 'date'.
    :param state: Состояние, по которому производится фильтрация (по умолчанию 'EXECUTED').
    :return: Новый список словарей, отфильтрованный по заданному состоянию.
    """
    return [record for record in records if record.get('state') == state]


def sort_by_date(records: List[Dict[str, Any]], order: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате в заданном порядке.

    :param records: Список словарей, каждый из которых представляет запись с ключами 'id', 'state', 'date'.
    :param order: Булевый параметр, определяющий порядок сортировки. True для сортировки по убыванию (по умолчанию),
     False для сортировки по возрастанию.
    :return: Новый список словарей, отсортированный по дате в заданном порядке.
    """
    return sorted(records, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=order)

# Пример использования функций
records = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Вызов функций
executed_records = sort_by_state(records)
sorted_records_desc = sort_by_date(records)
sorted_records_asc = sort_by_date(records, order=False)

print(executed_records)
print(sorted_records_desc)
print(sorted_records_asc)