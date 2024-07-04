
def sort_by_date(dictionaries: list, list_dicts=None) -> list:
    sorted_list = sorted(list_dicts, key=lambda x: x['date'], reverse=True)
    return sorted_list
