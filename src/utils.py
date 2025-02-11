import re
import json
import logging
import os
import collections
from datetime import datetime

filename = os.path.basename(__file__)[:-3]
logger = logging.getLogger(filename)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"../logs/{filename}.log", mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def financial_transactions(path):
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            logger.info(f"fetch data from file: {path}")
            data = json.load(f)
    except FileNotFoundError:
        logger.error(f"file not found: {path}")
        return []
    except json.decoder.JSONDecodeError:
        logger.error(f"invalid file: {path}")
        return []
    return data


def get_transactions_by_state(
    transactions: list[dict[str, str]], state: str
) -> list[dict[str, str]]:
    return list(
        filter(
            lambda x: (
                x.get("state").lower() == state.lower()
                if type(x.get("state")) == str
                else None
            ),
            transactions,
        )
    )


def find_transactions_with_search_word(
    transactions: list[dict[str, str]], search_word: str = None
) -> list[dict[str, str]]:
    return list(
        filter(
            lambda x: re.search(search_word, x["description"], flags=re.I), transactions
        )
    )


def count_transactions_with_categories(
    transactions: list[dict[str, str]], categories: list
) -> dict[str, int]:
    return dict(
        collections.Counter(
            list(filter(lambda x: x["description"].lower() in categories, transactions))
        )
    )


def get_transactions_by_currency(
    transactions: list[dict[str, str]], currency: str
) -> list[dict[str, str]]:
    if not transactions[0].get("operationAmount"):
        return list(filter(lambda x: x["currency_code"] == currency, transactions))
    else:
        return list(
            filter(
                lambda x: x["operationAmount"]["currency"]["code"] == currency,
                transactions,
            )
        )


def get_sorted_transactions_by_date(
    transactions: list[dict[str, str]],
    sort_param: str,
) -> list[dict[str, str]]:
    return list(
        sorted(
            transactions,
            key=lambda x: datetime.strptime(x["date"].split("T")[0], "%Y-%m-%d"),
            reverse=True if sort_param == "по убыванию" else False,
        )
    )
