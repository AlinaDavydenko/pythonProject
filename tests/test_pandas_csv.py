from unittest.mock import Mock, patch

import pandas as pd
import pytest
from src.pandas_csv import read_csv, read_excel


# использую часть от всего списка с заголовками
output_inf = [
    {'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol'}
]


# реализация тестирования двух функций
# тестирование функции csv
@pytest.fixture
def return_data_frame():
    df = pd.DataFrame({'id': [650703],
                      'state': ['EXECUTED'],
                      'date': ['2023-09-05T11:30:32Z'],
                      'amount': [16210.0],
                      'currency_name': ['Sol']})
    return df


@patch('src.pandas_csv.pd.read_csv')
def test_read_csv(mock_reader, return_data_frame):
    mock_reader.return_value = return_data_frame
    assert read_csv("../data/transactions.csv") == output_inf
    mock_reader.assert_called_once_with("../data/transactions.csv", delimiter=';')


@patch('src.pandas_csv.pd.read_excel')
def test_read_excel(mock_reader, return_data_frame):
    mock_reader.return_value = return_data_frame
    assert read_excel("../data/transactions_excel.xlsx") == output_inf
    mock_reader.assert_called_once_with("../data/transactions_excel.xlsx")
