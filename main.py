import os
import sys, datetime
from utils import read_json_file, read_csv_file, read_xlsx_file
from filters import filter_transactions_by_description, categorize_transactions

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input("Пользователь: ")
    file_path = ""

    if file_choice == '1':
        file_path = 'operations.json'
        transactions = read_json_file(file_path)
    elif file_choice == '2':
        file_path = 'transactions.csv'
        transactions = read_csv_file(file_path)
    elif file_choice == '3':
        file_path = 'transactions.xlsx'
        transactions = read_xlsx_file(file_path)
    else:
        print("Неверный выбор файла.")
        sys.exit(1)

    print(f"Для обработки выбран {os.path.splitext(file_path)[1][1:].upper()}-файл.")

    status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: ").upper()
    while status not in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f"Статус операции \"{status}\" недоступен.")
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: ").upper()

    print(f"Операции отфильтрованы по статусу \"{status}\"")

    transactions = [t for t in transactions if t.get('state', '').upper() == status]

    sort_by_date = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower() == 'да'
    if sort_by_date:
        sort_order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        reverse = sort_order != 'по возрастанию'
        transactions.sort(key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=reverse)

    rub_only = input("Выводить только рублевые тразакции? Да/Нет\nПользователь: ").strip().lower() == 'да'
    if rub_only:
        transactions = [t for t in transactions if t.get('currency', {}).get('name') == 'руб.']

    search_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").strip().lower() == 'да'
    if search_description:
        search_string = input("Введите слово для поиска:\nПользователь: ")
        transactions = filter_transactions_by_description(transactions, search_string)

    print("Распечатываю итоговый список транзакций...")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            date = datetime.datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
            description = transaction['description']
            from_ = transaction.get('from', '')
            to = transaction['to']
            amount = transaction['operationAmount']['amount']
            currency = transaction['operationAmount']['currency']['name']
            print(f"{date} {description}")
            if from_:
                print(f"{from_} -> {to}")
            else:
                print(f"-> {to}")
            print(f"Сумма: {amount} {currency}\n")

if __name__ == "__main__":
    main()