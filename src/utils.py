import json
import logging
import os

# Настройка логирования
def setup_logger(name, log_file, level=logging.DEBUG):
    """Функция для настройки логера"""
    # Создаем логер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Создаем обработчик для записи логов в файл
    file_handler = logging.FileHandler(log_file, mode='w')  # 'w' для перезаписи логов при каждом запуске
    file_handler.setLevel(level)

    # Создаем форматтер для логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логеру
    logger.addHandler(file_handler)

    return logger

# Определяем путь к файлу логов
logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'logs')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

log_file = os.path.join(logs_dir, 'utils.log')
logger_utils = setup_logger('utils', log_file)

class Any:
    pass

def get_operations_data(file_path: str) -> Any:
    empty_data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                operations = json.load(file)
                if not isinstance(operations, list) or not operations:
                    logger_utils.info("Файл пустой или не содержит список операций")
                    return empty_data
                else:
                    logger_utils.info("Данные успешно загружены")
                    return operations

            except json.JSONDecodeError:
                logger_utils.error("Ошибка декодирования JSON")
                return empty_data
    except FileNotFoundError:
        logger_utils.error("Файл не найден")
        return empty_data

if __name__ == '__main__':
    data = get_operations_data(r'C:\Users\Panasup\PycharmProjects\Bank_Project\data\operations.json')
    print(data)