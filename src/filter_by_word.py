import re

from collections import defaultdict


def str_sort(filtered_transactions: list[dict], word: str) -> list[dict]:
    found_operations = []
    for operation in filtered_transactions:
        if re.search(word, operation.get("description", "")):
            found_operations.append(operation)
            filtered_transactions = found_operations
        return filtered_transactions


# def filter_transactions(transactions_list: list[dict], search_string: str) -> list[dict]:
#     """
#     Функция для фильтрации списка словарей с операциями на основе строки поиска.
#     :param transactions_list: список словарей, где каждый словарь представляет собой операцию
#     :param search_string: строка для поиска в описаниях операций
#     :return: список словарей, в которых описание содержит строку поиска
#     """
#     # Компилируем регулярное выражение для поиска
#     pattern = re.compile(re.escape(search_string), re.IGNORECASE)
#
#     # Фильтруем список операций
#     filtered_transactions = [
#         data for data in transactions_list if "description" in data and pattern.search(data["description"])
#     ]
#     return filtered_transactions


def count_operations_by_category(transactions_list: list[dict], categories: list[str]) -> dict[str, int]:
    """Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""

    # Создаем словарь для хранения количества операций по категориям
    category_count = defaultdict(int)

    # Проходим по каждому словарю в списке transactions
    for transaction in transactions_list:
        description = transaction.get("description", "").lower()

        # Проходим по каждой категории и проверяем, соответствует ли описание операции категории
        for category in categories:

            # Используем регулярное выражение для поиска категории в описании
            if re.search(re.escape(category.lower()), description):
                category_count[category] += 1  # Увеличиваем счетчик для найденной категории

    return dict(category_count)  # Преобразуем defaultdict обратно в обычный словарь для возвращения