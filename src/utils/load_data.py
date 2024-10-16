
import json

def load_data(path: str) -> dict:
    with open(path, encoding="UTF-8") as file:
        dats_json = json.load(file)
        return dats_json
