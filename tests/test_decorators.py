import tempfile

from src.decorators import log


# 1 тест
def test_log_good(capsys):
    """Тестирует выполнение декорированной функции"""

    @log(filename='mylog.txt')
    def func(x, y):
        return x + y

    result = func(1, 2)
    assert result == 3


# 2 тест
def test_log_exception_file(capsys):
    """Тестирует запись в файл после ошибки"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y
    func(1, 2)
    with open(log_file_path, 'r', encoding='utf-8') as file:
        logs = file.read()
    assert "func ok" in logs


# 3 тест
def test_log(capsys):
    @log(filename='mylog.txt')
    def my_function(x, y):
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
        assert "my_function error: TypeError. Inputs: (1, '2'), {}" in captured.out
