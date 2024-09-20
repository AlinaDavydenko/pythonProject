from typing import Any, Union

from src.date_for_functions import data_fo_function

test_result = data_fo_function()


# модуль реализует генераторы для обработки данных
# реализация генератора, фильтрующего словари по параметрам
def filter_by_currency(transactions: list[dict], currency: str) -> Union[iter, str]:
    """ принимает список словарей и возвращает итератор по заданному фильтру """
    try:
        for element in transactions:
            if element["operationAmount"]["currency"]["code"] == currency:
                yield element
    except StopIteration:
        if not transactions == []:
            return 'Нет транзакций'


# реализация генератора, выводящего описания каждой транзакции
def transaction_descriptions(data: Any) -> iter:
    """ генератор принимает список словарей с транзакциями и возвращает описание каждой операции """
    try:
        for element in data:
            yield element["description"]
    except StopIteration:
        if not data == []:
            return 'пустой словарь'


# реализация генератора, который генерирует диапазон номеров
def card_number_generator(start: int, stop: int) -> list:
    """ генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX """
    start1 = 10000000000000000 + start
    list_of_numbers = []
    while start <= stop:
        start1 = str(start1)
        list_of_numbers.append(f'{start1[1:5]} {start1[5:9]} {start1[9:13]} {start1[13:17]}')
        start1 = int(start1)
        start1 += 1
        start += 1
    return list_of_numbers
