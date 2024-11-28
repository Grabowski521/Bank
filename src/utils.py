import json
class Any:
    pass

def get_operations_data(file_path: str) -> Any:

    empty_data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                operations = json.load(file)
                if not isinstance(operations, list) or not operations:
                    return empty_data
                else:
                    return operations

            except json.JSONDecodeError:
                print("Ошибка декодирования")
                return empty_data
    except FileNotFoundError:
        print("файл не найден")
        return empty_data


if __name__ == '__main__':
    data = get_operations_data(r'C:\Users\Panasup\PycharmProjects\Bank_Project\data\operations.json')
    print(data)