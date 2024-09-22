from functools import wraps

from typing import Any, Optional


def log(filename: Optional[str]) -> None:
    """Decorator create log about function operation."""
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # time_1 = time()
                result = func(*args, **kwargs)
                # time_2 = time()
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                raise e
        return wrapper
    return my_decorator


@log(filename='mylog.txt')
def my_function(x: int, y: int) -> int:
    """ суммирует два значения """
    return x+y


my_function(3, 3)
