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

def sort_by_date(dict_list: list[dict[str, str]], date = None) -> list[dict[str, str]]:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(dict_list, key=lambda x: x['date'], reverse=True)
    return sorted_list
