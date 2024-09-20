import pytest

from src.widget import get_date, mask_account_card


# testing mask_account_card
@pytest.mark.parametrize('get_card, expected_result', [
    ('Visa Platinum 7000792289606361', '7000 79** **** 6361'),
    ('', None),
    ('Maestro 7000792289606361', '7000 79** **** 6361'),
    ('Счет 73654108430135874305', '7365 41** **** 4305')
])
def test_mask_account_card(get_card, expected_result):
    assert mask_account_card(get_card) == expected_result


# testing get_date
@pytest.mark.parametrize('data_information, expected_result', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2024-03-11T02:26:18671407', '11.03.2024')
])
def test_get_date(data_information, expected_result):
    assert get_date(data_information) == expected_result
