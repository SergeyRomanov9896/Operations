
from src.utils.load_data import load_data

def sort_last_five(path: str) -> list:
    """Выводит последние 5 успешных операций клиента, отсортированных по EXECUTED, from и date"""
    data = load_data(path)

    sort_executed = [state for state in data if state.get("state") == "EXECUTED" and state.get("from")] # Отсортировал по EXECUTE и from
    last_five_operations = [sort_executed[i] for i in range(len(sort_executed)-5, len(sort_executed))] # Вывод последних 5 операций
    last_five_operations.sort(reverse=True, key=lambda x: x['date'])

    return last_five_operations
