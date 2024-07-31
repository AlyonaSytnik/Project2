def get_mask_card_number(card_number: str) -> str:
    """Возвращает маскированные номера карт"""
    masked_card = (
        card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    )
    return masked_card


def get_mask_account(account_number: str) -> str:
    """Возвращает маскированные номера счетов"""
    masked_account = "**" + account_number[-4:]
    return masked_account
