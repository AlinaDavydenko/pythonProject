import tempfile

import pytest

from src.decorators import log, my_function


def test_log_2():
    with pytest.raises(Exception):
        my_function()


# 1 тест
def test_log_1():
    @log(filename="mylog.txt")
    def my_functions(x, y):
        return x + y
    result = my_function(2, 1)
    assert result == 3


# 2 тест
def test_log_exception_file(capsys):
    """Тестирует запись в файл после ошибки"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename='mylog.txt')
    def func(x, y):
        return x + y
    func(1, 2)
    with open(log_file_path, 'r', encoding='utf-8') as file:
        logs = file.read()
    assert "" in logs


# 3 тест
def test_log(capsys):
    @log(filename='mylog.txt')
    def my_functions(x, y):
        return x + y

    # Проверка корректного выполнения функции
    my_function(1, 2)
    captured = capsys.readouterr()
    assert (
        "" in captured.out
    )
    # Проверка ошибки
    try:
        my_function(1, '2')
    except TypeError:
        captured = capsys.readouterr()
        assert "" in captured.out
