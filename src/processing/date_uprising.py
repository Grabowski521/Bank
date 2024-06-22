def filter_dicts_by_state(dicts_list, state='EXECUTED'):
    return [d for d in dicts_list if d.get('state') == state]

# Пример использования функции
input_dicts = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Вызов функции с параметром по умолчанию
default_state_output = filter_dicts_by_state(input_dicts)
print(default_state_output)

# Вызов функции с параметром 'CANCELED'
canceled_state_output = filter_dicts_by_state(input_dicts, 'CANCELED')
print(canceled_state_output)