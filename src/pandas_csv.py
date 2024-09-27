import pandas as pd


# Функция для считывания финансовых операций из csv
def read_csv(file_path: str) -> list[dict]:
    """ функция принимает путь к файлу csv и выдаёт список словарей с транзакциями """
    transactions_csv = pd.read_csv(file_path, delimiter=';')
    df_dict = transactions_csv.to_dict(orient='records')
    return df_dict


# Функция для считывания финансовых операций из Excel
def read_excel(file_path: str) -> list[dict]:
    """ функция принимает путь к файлу Excel и выдаёт список словарей с транзакциями """
    excel_data = pd.read_excel(file_path)
    df_dict = excel_data.to_dict(orient='records')
    return df_dict


# if __name__ == '__main__':
#     print(read_excel("../data/transactions_excel.xlsx"))


if __name__ == '__main__':
    print(read_csv("../data/transactions.csv"))

# excel_data = pd.read_excel("../data/transactions_excel.xlsx")
# print(excel_data.head())
