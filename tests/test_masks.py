import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("123456789123456789", "1234 56** **** 6789"),
        ("", " ** **** "),
        ("1", "1 ** **** 1"),
    ],
)
def test_get_mask_card_number(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize(
    "account_number, expected_result",
    [
        ("73654108430135874305", "**4305"),
        ("108430135874305", "**4305"),
        ("DE89370400440532013000", "**3000"),
    ],
)
def test_get_mask_account(account_number, expected_result):
    assert get_mask_account(account_number) == expected_result
