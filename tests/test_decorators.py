# import pytest
import tempfile

from src.decorators import log


def test_log_good(capsys):
    """Тестирует выполнение декорированной функции"""

    @log(filename='mylog.txt')
    def func(x, y):
        return x + y

    result = func(1, 2)
    assert result == 3


# def test_log_exception_file_log(capsys):
#     """Тестирует запись в файл после ошибки"""
#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         log_file_path = tmp_file.name
#
#     @log(filename=log_file_path)
#     def func(x, y):
#         return x + y
#     func(1, "2")
#     with open(log_file_path, 'r', encoding='utf-8') as file:
#         logs = file.read()
#     assert "my function error: unsupported operand type(s) for +: 'int' and 'str'. " in logs


# def test_log_exception_file(capsys):
#     """Тестирует запись в файл после ошибки"""
#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         log_file_path = tmp_file.name
#
#     @log(filename=log_file_path)
#     def func(x, y):
#         return x + y
#     func(1, 2)
#     with open(log_file_path, 'r', encoding='utf-8') as file:
#         logs = file.read()
#     assert "my function start in 00:00:00 \nmy function is ok \nmy function stop in 00:00:00" in logs
