import json
import pprint


# Обработка JSON-файла: функция чтения JSON-файла
def get_operations_data(path: str) -> list[dict]:
    """ возвращает список словарей с данными о финансовых транзакциях """
    empty_list = []
    try:
        with open(path) as f:
            try:
                operation_data = json.load(f)
            except json.JSONDecodeError:
                print('Ошибка декодирования файла')
                return empty_list
    except FileNotFoundError:
        print('Файл не найден')
        return empty_list
    pprint.pp(operation_data)
    return operation_data


if __name__ == '__main__':
    get_operations_data('../data/operations.json')
