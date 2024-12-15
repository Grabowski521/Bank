import json
import csv
import pandas as pd

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def read_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def read_xlsx_file(file_path):
    return pd.read_excel(file_path).to_dict(orient='records')