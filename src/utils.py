import json


def financial_transactions(path):
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []
    return data


#print(financial_transactions("../data/operations_sample.json"))



