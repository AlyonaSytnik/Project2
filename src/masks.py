import logging
import os

filename = os.path.basename(__file__)[:-3]
logger = logging.getLogger(filename)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"../logs/{filename}.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Возвращает маскированные номера карт"""
    if len(card_number) != 16:
        logger.error(f"invalid card number length: {len(card_number)}")
    masked_card = (
        card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    )
    logger.info(f"masked card: {masked_card}")
    return masked_card


def get_mask_account(account_number: str) -> str:
    """Возвращает маскированные номера счетов"""
    if len(account_number) != 4:
        logger.error(f"invalid account number length: {len(account_number)}")
    masked_account = "**" + account_number[-4:]
    logger.info(f"masked account: {masked_account}")
    return masked_account
