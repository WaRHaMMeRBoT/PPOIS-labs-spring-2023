from utils.Plastic_Card import PlasticCard
from utils.Money_Storage import MoneyStorage
from utils.Bank import Bank
import utils.Exceptions as excep
from typing import Optional


class ATM:
    def __init__(self, money_vault: MoneyStorage, plastic_card: Optional[PlasticCard]):
        self.__money_storage: MoneyStorage = money_vault
        self.__plastic_card: Optional[PlasticCard] = plastic_card
        self.__bank = Bank()

    @property
    def get_card_balance(self) -> float:
        if self.__plastic_card is None:
            raise excep.NoCardInserted
        if self.__plastic_card.is_blocked:
            raise excep.CardIsBlocked
        return self.__plastic_card.card_acc.balance

    @property
    def get_card_block_status(self) -> bool:
        if self.__plastic_card is None:
            raise excep.NoCardInserted
        return self.__plastic_card.is_blocked

    @property
    def money_vault(self) -> MoneyStorage:
        return self.__money_storage

    @property
    def card_account_id(self) -> str:
        return self.__plastic_card.card_acc.account_id

    @property
    def card_id(self) -> str:
        return self.__plastic_card.card_id

    def block_card(self):
        if self.__plastic_card is None:
            raise excep.NoCardInserted
        self.__plastic_card.is_blocked = True

    def check_card_pin(self, pin: str) -> bool:
        if self.__plastic_card is None:
            raise excep.NoCardInserted
        return self.__bank.TryPin(self.__plastic_card.card_id, pin)

    def get_cash_money(self, money_value: int):
        if self.__plastic_card is None:
            raise excep.NoCardInserted
        if self.__plastic_card.is_blocked:
            raise excep.CardIsBlocked
        if isinstance(money_value, int):
            if money_value > self.__plastic_card.card_acc.balance:
                raise excep.NotEnoughMoney
            try:
                self.__money_storage.get_money(money_value)
            except excep.NoAvailableMoneyConfig:
                raise excep.NoAvailableMoneyConfig
            else:
                self.__plastic_card.card_acc.subtract_money(money_value)
        else:
            raise ValueError

    def custom_operation(self, money_value: float):
        if self.__plastic_card is None:
            raise excep.NoCardInserted
        if self.__plastic_card.is_blocked:
            raise excep.CardIsBlocked
        if isinstance(money_value, float):
            try:
                self.__plastic_card.card_acc.subtract_money(money_value)
            except excep.NotEnoughMoney:
                raise excep.NotEnoughMoney