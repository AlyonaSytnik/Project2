import json
import requests


def open_json_file(filepath: str):
    try:
        data = []

        with open(filepath, encoding='utf-8') as f:
            data = json.load(f)

        return data

    except (json.JSONDecodeError, OSError):
        return []


print(open_json_file('../data/operations.json'))
print(open_json_file('../data/none.json'))