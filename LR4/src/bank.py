from src.account import Account
from src.card import Card


class Bank:

    def __init__(self, accounts: list, cards: list, account: Account = None):
        self.__accounts = accounts
        self.__cards = cards

        self.__logged = False
        if account is not None:
            self.__logged = True
        self.__account = account

    def as_dict(self) -> dict:
        account_id = None
        if self.__logged:
            account_id = self.__account.id
        dct = {
            "logged": self.__logged,
            "account-id": account_id
        }
        return dct

    @property
    def account(self):
        return self.__account

    @property
    def logged(self) -> bool:
        return self.__logged

    def register_acc(self, login: str, password: str) -> bool:

        if self.__logged:
            print(f'Для начала выйдите из аккаунта {self.__account.login}')
            return False

        if [x.login for x in self.__accounts].count(login):
            print('Этот логин уже занят, придумайте другой')
            return False

        self.__accounts.append(Account(login, password))
        print(f'Создан счет:\n\n\tЛогин: {login}\n\tПароль: {password}\n')
        return True

    def login(self, login: str, password: str) -> bool:

        if self.__logged:
            print(f'Для начала выйдите из аккаунта {self.__account.login}')
            return False

        acc = None
        for x in self.__accounts:
            if x.login == login:
                acc = x
        if acc is None:
            print(f'Счета с таким логином не существует')
            return False
        elif acc.get_access(password):
            self.__logged = True
            self.__account = acc
            print(f'Вы вошли в аккаунт {self.__account.login}!')
            return True
        else:
            print('Неверный пароль!')
            return False

    def logout(self):

        if not self.__logged:
            print(f'Вы еще не зашли в аккаунт!')
            return

        acc = self.__account
        self.__logged = False
        self.__account = None
        print(f'Вы вышли из аккаунта {acc.login}')

    def register_card(self, pin: str) -> bool:

        if not self.__logged:
            print(f'Вы еще не зашли в аккаунт!')
            return False

        if len(pin) != 4:
            print('PIN - код должен состоять из 4 цифр!')
            return False

        if not pin.isdigit():
            print('PIN - код должен состоять только из цифр!')
            return False

        card = Card(pin, self.__account)
        self.__cards.append(card)

        print(f'Зарегистрирова новая карта:\n\n'
              f'\tНомер карты: {card.number}\n'
              f'\tСрок обслуживания до: {card.date}\n'
              f'\tCVV: {card.cvv}\n')
        return True
