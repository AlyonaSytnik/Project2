from masks import get_mask_account, get_mask_card_number
from transactions import (get_financial_transactions_csv,
                          get_financial_transactions_xlsx)
from utils import (financial_transactions, find_transactions_with_search_word,
                   get_sorted_transactions_by_date,
                   get_transactions_by_currency, get_transactions_by_state)


def main():
    transactions = None
    print(
        """Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями."""
    )
    user_input = input(
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Пользователь:
    """)
    while user_input not in ["1", "2", "3"]:
        user_input = input(
            """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Пользователь:
    """)
    if user_input == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = financial_transactions("../data/operations.json")
    elif user_input == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = get_financial_transactions_csv("../data/transactions.csv")
    elif user_input == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = get_financial_transactions_xlsx(
            "../data/transactions_excel.xlsx"
        )

    print(
        """\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
    )
    user_input = input("Пользователь: ")
    while user_input.lower() not in ["executed", "cancelled", "pending"]:
        print(f'\nСтатус операции "{user_input}" недоступен.\n')
        print(
            """\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        )
        user_input = input("Пользователь: ")
    transactions = get_transactions_by_state(transactions, user_input.lower())

    print("""\nПрограмма: Отсортировать операции по дате? Да/Нет\n""")
    user_input = input("Пользователь: ")
    while user_input.lower() not in ["да", "нет"]:
        print(f'\nНедопустимое значение "{user_input}"\n')
        print("""\nПрограмма: Отсортировать операции по дате? Да/Нет\n""")
        user_input = input("Пользователь: ")
    if user_input.lower() == "да":
        print("\nПрограмма: Отсортировать по возрастанию или по убыванию?\n")
        user_input = input("Пользователь: ")
        while user_input.lower() not in ["по возрастанию", "по убыванию"]:
            print(f"\nНедопустимое значение {user_input}\n")
            print("\nПрограмма: Отсортировать по возрастанию или по убыванию?\n")
            user_input = input("Пользователь: ")
        transactions = get_sorted_transactions_by_date(transactions, user_input.lower())
    print("\nПрограмма: Выводить только рублевые тразакции? Да/Нет\n")
    user_input = input("Пользователь: ")
    while user_input.lower() not in ["да", "нет"]:
        print(f"\nНедопустимое значение {user_input}\n")
        print("\nПрограмма: Выводить только рублевые тразакции? Да/Нет\n")
        user_input = input("Пользователь: ")
    if user_input.lower() == "да":
        transactions = get_transactions_by_currency(transactions, "RUB")

    print(
        """\nПрограмма: Отфильтровать список транзакций по определенному слову
в описании? Да/Нет\n"""
    )
    user_input = input("Пользователь: ")
    while user_input.lower() not in ["да", "нет"]:
        print(f"\nНедопустимое значение {user_input}\n")
        print(
            """\nПрограмма: Отфильтровать список транзакций по определенному слову
        в описании? Да/Нет\n"""
        )
        user_input = input("Пользователь: ")

    if user_input.lower() == "да":
        print("\nПрограмма: Введите это слово\n")
        user_input = input("Пользователь: ")
        transactions = find_transactions_with_search_word(transactions, user_input)

    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")
    print("Программа:")
    if not transactions:
        print(
            """Программа: Не найдено ни одной транзакции, подходящей под ваши
условия фильтрации"""
        )
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}\n")
        for transaction in transactions:
            description = transaction.get("description")
            if "открытие" in description.lower():
                print(f"Счет {get_mask_account(transaction.get('to').split()[1])}")
            else:
                frm = transaction.get("from").split()
                to = transaction.get("to").split()
                frm_num = frm[-1]
                to_num = to[-1]
                frm = " ".join(frm[:-1])
                to = " ".join(to[:-1])
                if frm.lower() == "счет":
                    frm_num = get_mask_account(frm_num)
                else:
                    frm_num = get_mask_card_number(frm_num)
                if to.lower() == "счет":
                    to_num = get_mask_account(to_num)
                else:
                    to_num = get_mask_card_number(to_num)
                print(f"{frm} {frm_num} -> {to} {to_num}")
            if not transaction.get("operationAmount"):
                print(f'Сумма {transaction["amount"]} {transaction["currency_code"]}\n')
            else:
                print(
                    f'Сумма {transaction["operationAmount"]["amount"]}'
                    f'{transaction["operationAmount"]["currency"]["name"]}\n'
                )


if __name__ == "__main__":
    main()
