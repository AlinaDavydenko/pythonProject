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


