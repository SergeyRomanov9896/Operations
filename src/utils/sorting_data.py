import os
from load_data import load_data

DATA_JSON = os.path.join("C:/Users/Admin/PycharmProjects/Operations/data/operations.json")


def sorting_data():
    """Сортировка данных клиента"""
    data = load_data(DATA_JSON)

    for i in data:
        if i["state"] in "EXECUTED":
            print(i)

sorting_data()
