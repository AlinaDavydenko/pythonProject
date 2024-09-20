from src.masks import get_mask_account, get_mask_card_number

# функция для работы с новыми возможностями приложения.


def mask_account_card(get_card: str) -> str:  # функция принимает название карты и её номер
    """ функция умеет обрабатывать информацию как о картах, так и о счетах """
    if 'visa platinum' or 'maestro' in get_card:
        i = get_card.split(' ')
        for element in i:
            if element.isdigit():
                return get_mask_card_number(element)

    if 'счeт' in get_card:
        i = get_card.split(' ')
        for element in i:
            if element.isdigit():
                return get_mask_account(element)


def get_date(data_information: str) -> str:  # из "2024-03-11T02:26:18.671407" -> в формат "ДД.ММ.ГГГГ" ("11.03.2024")
    """ Принимает на вход строку с датой и возвращает сокращенный формат """
    return f'{data_information[8:10]}.{data_information[5:7]}.{data_information[0:4]}'


# get_card = str(input('Введите наименование и номер карты.')).lower()
# data_information = str(input('Введите дату'))

