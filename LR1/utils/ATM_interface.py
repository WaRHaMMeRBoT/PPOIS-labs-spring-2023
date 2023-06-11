import json
from utils.ATM import ATM
from utils.Bank import Bank
from utils.Bank_Account import BankAccount
from utils.Plastic_Card import PlasticCard
from utils.Money_Storage import MoneyStorage
from abc import abstractmethod
import utils.Exceptions as excep
import regex as regEX
from typing import Optional

class ATMInterface:
    atm: Optional[ATM] = None
    @classmethod
    @abstractmethod
    def start(cls):
        pass

    @classmethod
    def find_card_by_card_num(cls, card_num: str) -> Optional[PlasticCard]:
        with open("./JSON_files/cards.json", "r") as plastic_cards_file:
            cards_data = json.load(plastic_cards_file)
        plastic_card: Optional[PlasticCard] = None
        for card in cards_data:
            if card["card_id"] == card_num:
                card_account: BankAccount = cls.find_card_account_by_id(card["card_acc"])
                plastic_card = PlasticCard(card_id=card["card_id"],
                                           bank_account=card_account, expiration_date=card["expiration_date"],
                                           is_blocked=card["is_blocked"])
                break
        return plastic_card

    @classmethod
    def find_card_account_by_id(cls, acc_id: str) -> Optional[BankAccount]:
        with open("./JSON_files/accounts.json", "r") as card_accounts_file:
            card_accounts_data = json.load(card_accounts_file)
        card_account: Optional[BankAccount] = None
        for account in card_accounts_data:
            if account["acc_id"] == acc_id:
                card_account = BankAccount(*list(account.values()))
        return card_account

    @classmethod
    def find_money_vault(cls) -> MoneyStorage:
        with open("./JSON_files/vault.json", "r") as money_vault_file:
            money_vault_raw = json.load(money_vault_file)
            money_vault = dict()
            for key in money_vault_raw.keys():
                money_vault[int(key)] = money_vault_raw[key]
            money_vault = MoneyStorage(money_vault)
        return money_vault

    @classmethod
    def save_money_vault(cls) -> None:
        money_vault_raw: dict[int, int] = cls.atm.money_vault.moneyStorage
        money_vault = dict()
        for key in money_vault_raw.keys():
            money_vault[str(key)] = money_vault_raw[key]
        with open("./JSON_files/vault.json", "w") as money_vault_file:
            json.dump(money_vault, money_vault_file, indent=6)

    @classmethod
    def save_card_accounts(cls) -> None:
        if cls.atm is not None:
            with open("./JSON_files/accounts.json", "r") as card_accounts_file:
                card_accounts_data = json.load(card_accounts_file)
            for account in card_accounts_data:
                if account["acc_id"] == cls.atm.card_account_id:
                    account["balance"] = cls.atm.get_card_balance
                    break
            with open("./JSON_files/accounts.json", "w") as card_accounts_file:
                json.dump(card_accounts_data, card_accounts_file, indent=6)

    @classmethod
    def save_cards_status(cls) -> None:
        if cls.atm is not None:
            with open("./JSON_files/cards.json", "r") as plastic_cards_file:
                cards_data = json.load(plastic_cards_file)
            for card in cards_data:
                if card["card_id"] == cls.atm.card_id:
                    card["is_blocked"] = cls.atm.get_card_block_status
                    break
            with open("./JSON_files/cards.json", "w") as plastic_cards_file:
                json.dump(cards_data, plastic_cards_file, indent=6)

    @classmethod
    @abstractmethod
    def check_pin(cls):
        pass

    @classmethod
    @abstractmethod
    def main_menu(cls):
        pass

    @classmethod
    @abstractmethod
    def get_balance(cls):
        pass

    @classmethod
    @abstractmethod
    def get_cash_money(cls):
        pass

    @classmethod
    @abstractmethod
    def put_money_on_phone(cls):
        pass