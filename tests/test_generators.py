import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)
from tests.conftest import data_for_generators_test, usd_transactions


# тестирование filter_by_currency с использованием фикстур
def test_filter_by_currency(data_for_generators_test, usd_transactions):
    """ функция тестирует фильтрацию по операциям """
    assert next(filter_by_currency(data_for_generators_test, "USD")) == usd_transactions


# тестирование transaction_descriptions с использованием фикстур
def test_transaction_descriptions(data_for_generators_test):
    """ функция тестирует генератор транзакций """
    num = transaction_descriptions(data_for_generators_test)
    assert next(num) == "Перевод организации"
    assert next(num) == "Перевод со счета на счет"


# тестирование card_number_generator с использованием параметризации
@pytest.mark.parametrize('start, stop, expected_result', [
    (2, 4, ['0000 0000 0000 0002', '0000 0000 0000 0003', '0000 0000 0000 0004']),
    (33333, 33335, ['0000 0000 0003 3333', '0000 0000 0003 3334', '0000 0000 0003 3335'])
])
def test_card_number_generator(start, stop, expected_result):
    assert card_number_generator(start, stop) == expected_result
