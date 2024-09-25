from unittest.mock import Mock, patch

from src.external_api import sum_of_transactions

date_test_rub = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

date_test_usd = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }


# тестирование функции с RUB
@patch('src.external_api.requests.get')
def test_sum_of_transactions(mock_get):
    mock_responce = Mock()
    mock_responce.json.return_value = {
          "date": "2021-04-06",
          "historical": True,
          "info": {
            "rate": 91.593311,
            "timestamp": 1617753599
          },
          "query": {
            "amount": 31957.58,
            "from": "RUB",
            "to": "RUB"
          },
          "result": 31957.58,
          "success": True
        }
    mock_get.return_value = mock_responce
    assert sum_of_transactions(date_test_rub) == 31957.58


# тестирование функции с USD
@patch('src.external_api.requests.get')
def test_sum_of_transactions_usd(mock_get):
    mock_responce = Mock()
    mock_responce.json.return_value = {
          "date": "2021-04-06",
          "historical": True,
          "info": {
            "rate": 91.593311,
            "timestamp": 1617753599
          },
          "query": {
            "amount": 8221.37,
            "from": "USD",
            "to": "RUB"
          },
          "result": 762915.92,
          "success": True
        }
    mock_get.return_value = mock_responce
    assert sum_of_transactions(date_test_usd) == 762915.92