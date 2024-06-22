from datetime import datetime

def convert_date(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
    return date_object.strftime('%d.%m.%Y')

input_date = '2018-07-11T02:26:18.671407'
formatted_date = convert_date(input_date)
print(formatted_date)