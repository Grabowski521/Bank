def filter_dicts_by_state(dicts, state='EXECUTED'):
    return [d for d in dicts if d.get('state') == state]

def sort_dicts_by_date(dicts, order='descending'):
    return sorted(dicts, key=lambda d: d['date'], reverse=(order == 'descending'))

dicts = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтрация по статусу 'EXECUTED'
filtered_dicts = filter_dicts_by_state(dicts)
print(filtered_dicts)

# Фильтрация по статусу 'CANCELED'
filtered_dicts_canceled = filter_dicts_by_state(dicts, 'CANCELED')
print(filtered_dicts_canceled)

# Сортировка по дате в порядке убывания
sorted_dicts_desc = sort_dicts_by_date(dicts)
print(sorted_dicts_desc)

# Сортировка по дате в порядке возрастания
sorted_dicts_asc = sort_dicts_by_date(dicts, order='ascending')
print(sorted_dicts_asc)