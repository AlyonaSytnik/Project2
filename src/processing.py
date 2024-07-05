def filter_by_state(dict_list: list[dict[str, str]], state: str = 'EXECUTED') -> list[dict[str, str]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению"""
    filtered_list1 = []
    filtered_list2 = []

    for dicts in dict_list:
        if dicts['state'] == state:
            filtered_list1.append(dicts)
        else:
            filtered_list2.append(dicts)

    return filtered_list1, filtered_list2

def sort_by_date(dict_list: list[dict[str, str]], date: str = None, reverse: bool = True) -> list[dict[str, str]]:
    """Функция возвращает новый список, отсортированный по дате"""
    if date is not None:
        filtered_list = [d for d in dict_list if d.get('date') == date]
    else:
        filtered_list = dict_list

    sorted_list = sorted(filtered_list, key=lambda x: x['date'], reverse=reverse)
    return sorted_list
