from src import masks

def mask_account_card(string: str) -> str:
    """Функция маскирует номер счета и карты"""
    if "Cчет" in string:
        account = string[-20:]
        return string[:20] + masks.get_mask_card_number(account)
    else:
        number_card = "".join(string[-16:].split())
        return string[:16] + masks.get_mask_account(number_card)


def get_data(info_data: str) -> str:
    """Функция преобразует дату и время"""
    data_day = info_data.split("T")[0]

    return f"{data_day}-{info_data.split('-')[1]}.{info_data.split('-')[-2]}.{info_data.split('-')[-3]}"
