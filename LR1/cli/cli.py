import json
from atm.atm import ATM
from card_account.card_account import CardAccount
from plastic_card.plastic_card import PlasticCard
from typing import Optional
from money_vault.money_vault import MoneyVault
import exceptions.exceptions as exc
import regex as re
import os
import sys
from abc import abstractmethod
import time


class AtmInterface:
    atm: Optional[ATM] = None

    @classmethod
    @abstractmethod
    def start(cls):
        pass

    @classmethod
    def find_card_by_card_num(cls, card_num: str) -> Optional[PlasticCard]:
        with open("../json/plastic_cards.json", "r") as plastic_cards_file:
            cards_data = json.load(plastic_cards_file)
        plastic_card: Optional[PlasticCard] = None
        for card in cards_data:
            if card["card_id"] == card_num:
                card_account: CardAccount = cls.find_card_account_by_id(card["card_acc"])
                plastic_card = PlasticCard(card_id=card["card_id"], pin=card["pin"],
                                           card_acc=card_account, expiration_date=card["expiration_date"],
                                           is_blocked=card["is_blocked"])
                break
        return plastic_card

    @classmethod
    def find_card_account_by_id(cls, acc_id: str) -> Optional[CardAccount]:
        with open("../json/card_accounts.json", "r") as card_accounts_file:
            card_accounts_data = json.load(card_accounts_file)
        card_account: Optional[CardAccount] = None
        for account in card_accounts_data:
            if account["acc_id"] == acc_id:
                card_account = CardAccount(*list(account.values()))
        return card_account

    @classmethod
    def find_money_vault(cls) -> MoneyVault:
        with open("../json/money_vault.json", "r") as money_vault_file:
            money_vault_raw = json.load(money_vault_file)
            money_vault = dict()
            for key in money_vault_raw.keys():
                money_vault[int(key)] = money_vault_raw[key]
            money_vault = MoneyVault(money_vault)
        return money_vault

    @classmethod
    def save_money_vault(cls) -> None:
        money_vault_raw: dict[int, int] = cls.atm.money_vault.money_vault
        money_vault = dict()
        for key in money_vault_raw.keys():
            money_vault[str(key)] = money_vault_raw[key]
        with open("../json/money_vault.json", "w") as money_vault_file:
            json.dump(money_vault, money_vault_file, indent=6)

    @classmethod
    def save_card_accounts(cls) -> None:
        if cls.atm is not None:
            with open("../json/card_accounts.json", "r") as card_accounts_file:
                card_accounts_data = json.load(card_accounts_file)
            for account in card_accounts_data:
                if account["acc_id"] == cls.atm.card_account_id:
                    account["balance"] = cls.atm.get_card_balance
                    break
            with open("../json/card_accounts.json", "w") as card_accounts_file:
                json.dump(card_accounts_data, card_accounts_file, indent=6)

    @classmethod
    def save_cards_status(cls) -> None:
        if cls.atm is not None:
            with open("../json/plastic_cards.json", "r") as plastic_cards_file:
                cards_data = json.load(plastic_cards_file)
            for card in cards_data:
                if card["card_id"] == cls.atm.card_id:
                    card["is_blocked"] = cls.atm.get_card_block_status
                    break
            with open("../json/plastic_cards.json", "w") as plastic_cards_file:
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


class CliAtm(AtmInterface):
    pin_attempts: int = 3

    @staticmethod
    def __console_clear():
        os.system("cls" if os.name == "nt" else "clear")

    @classmethod
    def start(cls):
        card_num: str = input("Enter card number: ")
        while not re.fullmatch(r"\d{16}", card_num):
            print("Enter appropriate card number (16 digits)!")
            time.sleep(0.2)
            CliAtm.__console_clear()
            card_num = input("Enter card number: ")
        CliAtm.__console_clear()
        plastic_card: PlasticCard = cls.find_card_by_card_num(card_num)
        if plastic_card is None:
            print("Closed due to technical issues\n(choose existing card from json file)")
            sys.exit()
        if plastic_card.is_blocked:
            print("Your card is blocked\nCall the bank to solve this")
            time.sleep(0.5)
            CliAtm.__console_clear()
            sys.exit()
        if plastic_card.is_expired:
            print("Your card is expired\nGet the new one at the bank")
            time.sleep(0.5)
            CliAtm.__console_clear()
            sys.exit()
        money_vault: MoneyVault = cls.find_money_vault()
        if money_vault:
            cls.atm = ATM(money_vault=money_vault, plastic_card=plastic_card)
        CliAtm.check_pin()

    @classmethod
    def check_pin(cls):
        CliAtm.__console_clear()
        pin: str = input(f"Enter card PIN\n"
                         f"{CliAtm.pin_attempts} attempts left: ")
        cls.pin_attempts -= 1
        while cls.pin_attempts > 0:
            if not cls.atm.check_card_pin(pin):
                print("Incorrect PIN!\n"
                      f"{CliAtm.pin_attempts} attempts left")
                cls.pin_attempts -= 1
                time.sleep(0.2)
                CliAtm.__console_clear()
                pin = input("Enter card PIN: ")
            else:
                break
        if CliAtm.pin_attempts <= 0:
            cls.atm.block_card()
            cls.save_cards_status()
            print("You have failed all 3 attempts to enter PIN\n"
                  "Blocking the plastic card...\n"
                  "Connect the bank to unblock")
            sys.exit()
        cls.main_menu()

    @classmethod
    def main_menu(cls):
        CliAtm.__console_clear()
        choice: Optional[str] = "0"
        while choice < "1" or choice > "4":
            CliAtm.__console_clear()
            print("1. Get account balance\n"
                  "2. Get money in cash\n"
                  "3. Put money on the phone\n"
                  "4. Get card back")
            choice = input("Choose your option: ")
            if choice == "1":
                CliAtm.get_balance()
            elif choice == "2":
                CliAtm.get_cash_money()
            elif choice == "3":
                CliAtm.put_money_on_phone()
            elif choice == "4":
                CliAtm.__console_clear()
                print("Goodbye!")
                sys.exit()
            else:
                print("Incorrect option, try again")

    @classmethod
    def get_balance(cls):
        CliAtm.__console_clear()
        print(f"Your balance is {cls.atm.get_card_balance}")
        input("Press Enter to proceed...")
        CliAtm.pin_attempts = 3
        CliAtm.check_pin()

    @classmethod
    def get_cash_money(cls):
        CliAtm.__console_clear()
        money_amount: int = int(input("Enter amount of money to get: "))
        try:
            cls.atm.get_cash_money(money_amount)
        except exc.NotEnoughMoney:
            CliAtm.__console_clear()
            print("Not enough money!")
            time.sleep(0.5)
            cls.pin_attempts = 3
            cls.check_pin()
        except exc.NoAvailableMoneyConfig:
            CliAtm.__console_clear()
            print("That sum of money is unavailable to get!")
            time.sleep(0.5)
            cls.pin_attempts = 3
            cls.check_pin()
        else:
            CliAtm.__console_clear()
            cls.save_money_vault()
            cls.save_card_accounts()
            print("Here are your money!")
            cls.pin_attempts = 3
            cls.check_pin()

    @classmethod
    def put_money_on_phone(cls):
        CliAtm.__console_clear()
        phone_number: str = input("Enter phone number: ")
        while not re.fullmatch(r"\+375(29|33|25|44|17|29)\d{7}", phone_number):
            CliAtm.__console_clear()
            print("Incorrect phone number!")
            input("Press Enter to proceed")
            CliAtm.__console_clear()
            phone_number = input("Enter phone number: ")
        money_amount: float = float(input("Enter amount of money to get: "))
        try:
            cls.atm.custom_operation(money_amount)
        except exc.NotEnoughMoney:
            CliAtm.__console_clear()
            print("Not enough money!")
            time.sleep(0.5)
            cls.pin_attempts = 3
            cls.check_pin()
        else:
            CliAtm.__console_clear()
            cls.save_card_accounts()
            print("Successful!")
            cls.pin_attempts = 3
            cls.check_pin()
