import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


def test_filter_by_currency_exceptions(transactions):
    result = filter_by_currency(transactions, "EUR")
    assert list(result) == []
    result = filter_by_currency([], "EUR")
    assert result == "Список пустой!"


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [([], "EUR", "Список пустой!"), ([], "RUB", "Список пустой!")],
)
def test_filter_by_currency_exceptions(transactions, currency, expected):
    result = filter_by_currency(transactions, currency)
    assert result == expected


def test_transaction_descriptions(transactions_fixture):
    result = transaction_descriptions(transactions_fixture)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"


def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == ["Список пустой!"]


def test_card_number_generator():
    result = card_number_generator(1, 5)
    assert next(result) == "0000 0000 0000 0001"
    assert next(result) == "0000 0000 0000 0002"
    assert next(result) == "0000 0000 0000 0003"
    assert next(result) == "0000 0000 0000 0004"
    assert next(result) == "0000 0000 0000 0005"
