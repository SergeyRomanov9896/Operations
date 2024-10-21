import os

from src.utils.last_5_executed import last_5_executed

DATA_JSON = os.path.join("C:/Users/Admin/PycharmProjects/Operations/data/operations.json")

def clients_operations():
    """Виджет, который показывает несколько последних успешных банковских операций клиента"""
    last_5 = last_5_executed(DATA_JSON)

    last_5.sort(reverse=True, key=lambda x: x['date'])
    for date in last_5:
        pruning = date["date"][:-16]
        point = pruning.replace("-", ".")
        print(point)

clients_operations()