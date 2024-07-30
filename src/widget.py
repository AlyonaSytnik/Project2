from src import masks


def mask_account_card(string: str) -> str:
    """Функция маскирует номер счета и карты"""
    if "Счет" in string:
        account = string[-20:]
        return string[:len(string)-20] + masks.get_mask_account(account)
    else:
        number_card = string[-16:]
        return string[:len(string) - 16] + masks.get_mask_card_number(number_card)


def get_data(info_data: str) -> str:
    """Функция преобразует дату и время"""
    data_day = info_data.split("T")[0]
    data_day_split = data_day.split("-")
    return f"{data_day_split[-1]}.{data_day_split[-2]}.{data_day_split[0]}"
