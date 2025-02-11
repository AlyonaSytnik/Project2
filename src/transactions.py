import csv

import pandas as pd


def get_financial_transactions_csv(path: str) -> list[dict[str, str]]:
    try:
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            return list(reader)
    except FileNotFoundError:
        return []


def get_financial_transactions_xlsx(path: str) -> list[dict[str, str]]:
    try:
        df = pd.read_excel(path)
        return df.to_dict("records")
    except FileNotFoundError:
        return []
