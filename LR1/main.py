import sys
from src.data import read_data, write_data


def main():
    accounts, cards, repository, atm, bank = read_data()

    main_args = '\t-atm\n' \
                '\t-bank'

    atm_args = f'\t-insert-card.py (card.py number)\n' \
               f'\t-extract-card\n' \
               f'\t-input-pin (PIN-code)\n' \
               f'\t-balance\n' \
               f'\t-put-money (amount)\n' \
               f'\t-get-money (amount)'

    bank_args = f'\t-register-acc (login) (password)\n' \
                f'\t-login (login) (password)\n' \
                f'\t-logout\n' \
                f'\t-register-card.py (PIN-code)' \

    try:

        match sys.argv[1]:
            case '-atm':
                try:
                    match sys.argv[2]:
                        case '-insert-card':
                            atm.insert_card(sys.argv[3])
                        case '-extract-card':
                            atm.extract_card()
                        case '-input-pin':
                            atm.input_pin(sys.argv[3])
                        case '-balance':
                            atm.card_balance()
                        case '-put-money':
                            atm.put_money(sys.argv[3])
                        case '-get-money':
                            atm.get_money(sys.argv[3])
                        case _:
                            print(f'Неизвестный флаг:\n\t{sys.argv[2]}\n'
                                  f'Возможные флаги:\n' + atm_args)
                except IndexError:
                    print('Отсутствуют флаги, возможные флаги:\n' + atm_args)
            case '-bank':
                try:
                    match sys.argv[2]:
                        case '-register-acc':
                            bank.register_acc(sys.argv[3], sys.argv[4])
                        case '-login':
                            bank.login(sys.argv[3], sys.argv[4])
                        case '-logout':
                            bank.logout()
                        case '-register-card.py':
                            bank.register_card(sys.argv[3])
                        case _:
                            print(f'Неизвестный флаг:\n\t{sys.argv[2]}\n'
                                  f'Возможные флаги:\n' + bank_args)
                except IndexError:
                    print('Отсутствуют флаги, возможные флаги:\n' + bank_args)
            case _:
                print(f'Неизвестный флаг:\n\t{sys.argv[1]}\n'
                      f'Возможные флаги:\n' + main_args)
    except IndexError:
        print('Отсутствуют флаги, возможные флаги:\n' + main_args)

    write_data(accounts, cards, repository, atm, bank)


if __name__ == '__main__':
    main()
