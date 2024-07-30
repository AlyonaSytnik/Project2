import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize('dict_list, state_list', [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], 'EXECUTED'),
    ([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED')
])

def test_filter_by_state(dict_list, state_list):
    assert filter_by_state(dict_list, state_list) == dict_list
@pytest.mark.parametrize('reverse, expected_list', [
    (True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
	(False, [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
])


def test_sort_by_date(dict_list, reverse, expected_list):
    assert sort_by_date(dict_list, reverse) == expected_list