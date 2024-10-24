
import os

from src.utils.date_editor import date_editor
from src.utils.card_details import card_details
from src.utils.transfer_amount import transfer_amount

DATA_JSON = os.path.join("C:/Users/Admin/PycharmProjects/Operations/data/operations.json")

def clients_operations():
    """Виджет, который показывает несколько последних успешных банковских операций клиента"""
    load_date = date_editor(DATA_JSON)
    load_card = card_details(DATA_JSON)
    load_amount = transfer_amount(DATA_JSON)

    for information in range(len(load_date)):
        print(f"{load_date[information]}\n{load_card[information]}\n{load_amount[information]}")
        print()

clients_operations()