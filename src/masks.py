import logging

# Логирование
# Настройки формата и хэндлера, добавление в логгер
logger = logging.getLogger('get operation data')  # Получаем корневой логер с именем функции модуля
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding="utf-8")  # Создаем хендлер для вывода в файл
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')  # Настройка формата
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)  # Добавляем хэндллер с форматов в логгер

logger.setLevel(logging.DEBUG)  # Устанавливаем уровень


def get_mask_card_number(card_number: str) -> str:
    """ принимает на вход номер карты и возвращает ее маску """
    try:
        logger.debug('Неверная переменная')
        return f'{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}'  # выход функции
    except Exception as e:
        logger.error(f'Произошла ошибка {e}')  # логгер Error информирует об ошибки


def get_mask_account(account_number: str) -> str:
    """ принимает на вход номер счета и возвращает его маску """
    try:
        logger.debug('Debug massage')
        return f'**{account_number[-4:]}'  # выход функции
    except Exception as e:
        logger.error(f'Произошла ошибка {e}')  # логгер Error информирует об ошибки
