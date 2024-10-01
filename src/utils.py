import json
import pprint
import logging  # Импортируем модуль logging


# Логирование
# Настройки формата и хэндлера, добавление в логгер
logger = logging.getLogger('get operation data')  # Получаем корневой логер с именем функции модуля
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding="utf-8")  # Создаем хендлер для вывода в файл
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')  # Настройка формата
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)  # Добавляем хэндллер с форматов в логгер

logger.setLevel(logging.DEBUG)  # Устанавливаем уровень


# Обработка JSON-файла: функция чтения JSON-файла
def get_operations_data(path: str) -> list[dict]:
    """ возвращает список словарей с данными о финансовых транзакциях """
    empty_list = []
    try:
        with open(path) as f:
            try:
                logger.debug('Путь к файлу неверный')  # логгер Debug информирует об ошибки в определении пути к файлу
                operation_data = json.load(f)
            except json.JSONDecodeError:
                print('Ошибка декодирования файла')
                return empty_list
    except FileNotFoundError:
        print('Файл не найден')
        logger.error(f'Произошла ошибка {FileNotFoundError}')  # логгер Error информирует об ошибки
        return empty_list
    pprint.pp(operation_data)
    return operation_data


# if __name__ == '__main__':
#     get_operations_data('../data/operations.json')
