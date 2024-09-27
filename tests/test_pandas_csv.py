from unittest.mock import Mock, patch
from src.pandas_csv import read_csv, read_excel


# использую часть от всего списка с заголовками
date_test_csv = (
    ['id', 'state', 'date', 'amount', 'currency_name'],
    ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'Sol']
)

date_test_excel = (
    ['id', 'state', 'date', 'amount', 'currency_name'],
    ['650703', "EXECUTED", "2023-09-05T11:30:32Z", "16210", "Sol"])

output_inf_csv = [
    {'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol'}
]


# реализация тестирования двух функций
# тестирование функции csv
@patch('src.pandas_csv.pd.read_csv')
def test_read_csv(mock_reader):
    mock_reader.return_value = date_test_csv
    assert read_csv("../data/transactions.csv") == output_inf_csv

