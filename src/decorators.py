from datetime import time

from functools import wraps

from typing import Any, Callable


def log(filename: Any) -> Callable:  # создаём будущий декоратор логирования
    """ запись вызова функции и её результат в файл или в консоль """
    def timer(func):  # определяем функцию подсчёта времени исполнения функции
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            result = func(*args, **kwargs)
            try:
                time_1 = time()
                result = func(*args, **kwargs)
                time_2 = time()
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} start in {time_1} \nmy function is ok \nmy function stop in {time_2}')
                else:
                    print(f'{func.__name__} start in {time_1} \nmy function is ok \nmy function stop in {time_2}')
            except Exception as e:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} error: {e}. Input: {args}, {kwargs}\n')
                else:
                    print(f'{func.__name__} error: {e}. Input: {args}, {kwargs}\n')
                    raise
            return result
        return wrapper
    return timer


@log(filename='mylog.txt')
def my_function(x: int, y: int) -> int:
    """ суммирует два значения """
    return x+y


# вызов функции
my_func = my_function(x=5, y=2)
print(my_func)
