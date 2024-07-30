import pytest


@pytest.fixture
def first_entry():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def second_entry():
    return 'EXECUTED'

@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]


@pytest.fixture
def expected_list(first_entry):
    return first_entry

@pytest.fixture
def dict_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

