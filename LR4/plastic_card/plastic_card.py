from card_account.card_account import CardAccount
from datetime import datetime


class PlasticCard:
    def __init__(self, card_id: str, pin: str, card_acc: CardAccount, expiration_date: str, is_blocked: bool) -> None:
        self.__card_id: str = card_id
        self.__pin: str = pin
        self.__card_acc: CardAccount = card_acc
        self.__expiration_date: datetime = datetime.strptime(expiration_date, "%m/%y")
        self.__is_blocked: bool = is_blocked

    @property
    def card_acc(self) -> CardAccount:
        return self.__card_acc

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

    def check_pin(self, pin: str) -> bool:
        return self.__pin == pin

    def __str__(self) -> str:
        return f"Card ID: {self.__card_id}" \
               f"Balance: {self.__card_acc.balance}"

