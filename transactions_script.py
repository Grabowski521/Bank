import pandas as pd


def read_csv_transactions(file_path):
    """
    Считывает финансовые операции из CSV-файла и возвращает их в виде списка словарей.

    :param file_path: Путь к CSV-файлу
    :return: Список словарей с транзакциями
    """
    # Чтение данных из CSV-файла
    csv_data = pd.read_csv(file_path)
    # Преобразование DataFrame в список словарей
    transactions = csv_data.to_dict(orient='records')
    return transactions


def read_excel_transactions(file_path):
    """
    Считывает финансовые операции из XLSX-файла и возвращает их в виде списка словарей.

    :param file_path: Путь к XLSX-файлу
    :return: Список словарей с транзакциями
    """
    # Чтение данных из XLSX-файла
    xlsx_data = pd.read_excel(file_path)
    # Преобразование DataFrame в список словарей
    transactions = xlsx_data.to_dict(orient='records')
    return transactions


# Пример использования функций
csv_file_path = 'transactions.csv'
csv_transactions = read_csv_transactions(csv_file_path)
print("Данные из CSV-файла:")
print(csv_transactions[:5])  # Выводим первые 5 транзакций для проверки

xlsx_file_path = 'transactions_excel.xlsx'
xlsx_transactions = read_excel_transactions(xlsx_file_path)
print("\nДанные из XLSX-файла:")
print(xlsx_transactions[:5])  # Выводим первые 5 транзакций для проверки