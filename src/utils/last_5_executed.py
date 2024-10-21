
from src.utils.load_data import load_data

def last_5_executed(path: str) -> list:
    """Выводит последние 5 успешных операций клиента"""
    data = load_data(path)

    sort_executed = [state for state in data if state.get("state") == "EXECUTED" and state.get("from")] # Отсортировал по EXECUTE и from
    last_five_operations = [sort_executed[i] for i in range(len(sort_executed)-5, len(sort_executed))] # Вывод последних 5 операций

    return last_five_operations


