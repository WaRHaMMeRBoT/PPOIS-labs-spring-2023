from datetime import datetime
from utils.Bank_Account import BankAccount


class PlasticCard:
    def __init__(self, card_id: str, bank_account: BankAccount, expiration_date: str, is_blocked: bool) -> None:
        self.__card_id: str = card_id
        self.__bank_account: BankAccount = bank_account
        self.__expiration_date: datetime = datetime.strptime(expiration_date, "%m/%y")
        self.__is_blocked: bool = is_blocked



    @property
    def card_acc(self) -> BankAccount:
        return self.__bank_account

    @property
    def expiration_date(self) -> datetime:
        return self.__expiration_date

    @property
    def is_expired(self) -> bool:
        return self.__expiration_date < datetime.now()

    @property
    def card_id(self) -> str:
        return self.__card_id

    @property
    def is_blocked(self) -> bool:
        return self.__is_blocked

    @is_blocked.setter
    def is_blocked(self, new_block_status: bool):
        self.__is_blocked = new_block_status

    def __str__(self) -> str:
        return f"Card ID: {self.__card_id}\nBalance: {self.__bank_account.balance}"
