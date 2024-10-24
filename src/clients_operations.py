
import os

from src.utils.date_editor import date_editor

DATA_JSON = os.path.join("C:/Users/Admin/PycharmProjects/Operations/data/operations.json")

def clients_operations():
    """Виджет, который показывает несколько последних успешных банковских операций клиента"""
    load_date = date_editor(DATA_JSON)

    print("\n".join(" ".join(date) for date in load_date))

        # Данные карты от кого идет перевод
        # card_from = str(information["from"])
        # parts = card_from.split(" ")
        # if parts[-1].isdigit():
        #     card_name_from = " ".join(parts[:-1])
        #     card_number_from = parts[-1]
        #     if len(card_number_from) == 16:
        #         print(f"{card_name_from} {card_number_from[:4]} {card_number_from[4:6]}** **** {card_number_from[12:16]}", end="")
        #     else:
        #         print(f"{card_name_from} {card_number_from[:4]} {card_number_from[4:6]}** **** {card_number_from[16:20]}", end="")

        # Данные карты кому идет перевод
        # card_to = str(information["to"])
        # parts = card_to.split(" ")
        # if parts[-1].isdigit():
        #     card_name_to = " ".join(parts[:-1])
        #     card_number_to = parts[-1]
        #     if len(card_number_to) == 20:
        #         print(f" -> {card_name_to} **** **** **** **** {card_number_to[16:20]}")
        #     else:
        #         print(f" -> {card_name_to} **** **** **** {card_number_to[12:16]}")
        #
        # print(f"{information["operationAmount"]["amount"]} {information["operationAmount"]["currency"]["name"]}")
        # print()
clients_operations()