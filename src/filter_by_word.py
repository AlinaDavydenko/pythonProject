import re

from collections import Counter


def str_sort(filtered_transactions: list[dict], word: str) -> list[dict]:
    found_operations = []
    for operation in filtered_transactions:
        if re.search(word, operation.get("description", "")):
            found_operations.append(operation)
            filtered_transactions = found_operations
        return filtered_transactions


def count_operations_by_category(transactions_list: list[dict], categories: list[str]) -> dict[str, int]:
    """Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""

    # Создаем словарь для хранения количества операций по категориям
    category_count = Counter(int)

    # Проходим по каждому словарю в списке transactions
    for transaction in transactions_list:
        description = transaction.get("description", "").lower()

        # Проходим по каждой категории и проверяем, соответствует ли описание операции категории
        for category in categories:

            # Используем регулярное выражение для поиска категории в описании
            if re.search(re.escape(category.lower()), description):
                category_count[category] += 1  # Увеличиваем счетчик для найденной категории

    return dict(category_count)  # Преобразуем defaultdict обратно в обычный словарь для возвращения
