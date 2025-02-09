import json
import logging
import os

filename = os.path.basename(__file__)[:-3]
logger = logging.getLogger(filename)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"../logs/{filename}.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def financial_transactions(path):
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding='utf-8') as f:
            logger.info(f"fetch data from file: {path}")
            data = json.load(f)
    except FileNotFoundError:
        logger.error(f"file not found: {path}")
        return []
    except json.decoder.JSONDecodeError:
        logger.error(f"invalid file: {path}")
        return []
    return data
