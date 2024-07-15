def filter_by_state(
    dict_list: list[dict[str, str]], state: str = "EXECUTED"
) -> list[dict[str, str]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    flake указанному значению"""
    filtered_list = []

    for dict in dict_list:
        if dict["state"] == state:
            filtered_list.append(dict)

    return filtered_list


def sort_by_date(
    dict_list: list[dict[str, str]], reverse: bool = True
) -> list[dict[str, str]]:
    """Функция возвращает новый список, отсортированный по дате"""

    sorted_list = sorted(dict_list, key=lambda x: x["date"], reverse=reverse)
    return sorted_list
