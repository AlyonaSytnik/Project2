import pytest
from src.widget import mask_account_card, get_data

@pytest.mark.parametrize('string, expected_result', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Мир 1234432156788765', 'Мир 1234 43** **** 8765'),
    ('Счет 1234567891234567891234', 'Счет 12**1234'),
    ('', ' ** **** ')
])
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result

def test_get_data():
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"


