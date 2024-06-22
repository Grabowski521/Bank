from datetime import datetime

def sort_dicts_by_date(dicts_list, order='descending'):
    # Функция преобразования строки даты в объект datetime
    def parse_date(date_str):
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')

    # Сортировка списка словарей по дате
    sorted_list = sorted(dicts_list, key=lambda d: parse_date(d['date']), reverse=order == 'descending')
    return sorted_list

# Пример использования функции
input_dicts = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Вызов функции для сортировки по убыванию
descending_sorted_dicts = sort_dicts_by_date(input_dicts)
print(descending_sorted_dicts)

# Вызов функции для сортировки по возрастанию
ascending_sorted_dicts = sort_dicts_by_date(input_dicts, order='ascending')
print(ascending_sorted_dicts)