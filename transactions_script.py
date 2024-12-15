import pandas as pd

# Чтение данных из CSV-файла
csv_file_path = 'transactions.csv'
csv_data = pd.read_csv(csv_file_path)
print("Данные из CSV-файла:")
print(csv_data.head())  # Выводим первые 5 строк для проверки

# Чтение данных из XLSX-файла
xlsx_file_path = 'transactions_excel.xlsx'
xlsx_data = pd.read_excel(xlsx_file_path)
print("\nДанные из XLSX-файла:")
print(xlsx_data.head())  # Выводим первые 5 строк для проверки