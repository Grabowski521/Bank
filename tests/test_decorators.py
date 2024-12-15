import pytest
import unittest
import os
from src.decorators import *

class TestLogDecorator(unittest.TestCase):

    def setUp(self):
        # Удаляем файл логов перед каждым тестом, чтобы начать с чистого листа
        if os.path.exists("testlog.txt"):
            os.remove("testlog.txt")

    def test_successful_execution_logging(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)  # Проверяем, что функция возвращает ожидаемый результат
        with open("testlog.txt", "r") as file:
            log_contents = file.read()
            self.assertIn("divide ok", log_contents)  # Проверяем, что в логах есть запись об успешном выполнении

    def test_exception_logging(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)  # Вызываем функцию с некорректными аргументами, ожидаем исключение
        with open("testlog.txt", "r") as file:
            log_contents = file.read()
            self.assertIn("divide error", log_contents)  # Проверяем, что в логах есть запись об ошибке

if __name__ == "__main__":
    unittest.main()
