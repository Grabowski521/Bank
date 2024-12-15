import logging
import os

# Создаем папку logs, если она не существует
logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Функция для настройки логирования
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

# Настройка логеров для модулей
logger_masks = setup_logger('masks', os.path.join(logs_dir, 'masks.log'))
logger_utils = setup_logger('utils', os.path.join(logs_dir, 'utils.log'))

# Пример использования логеров
if __name__ == "__main__":
    logger_masks.info("Это информационное сообщение из модуля masks")
    logger_masks.error("Это сообщение об ошибке из модуля masks")

    logger_utils.debug("Это отладочное сообщение из модуля utils")
    logger_utils.warning("Это предупреждающее сообщение из модуля utils")