
from src.utils.sort_last_five import sort_last_five

def date_editor(path):
    load_five = sort_last_five(path)

    list_date = []

    for information in load_five:
        date = information["date"][8:-16]
        month = information["date"][5:-19]
        year = information["date"][:-22]
        list_date.append([date, month, year + " " + "Перевод организации"])
    return list_date
