from atm.atm import ATM
from plastic_card.plastic_card import PlasticCard
from typing import Optional
from money_vault.money_vault import MoneyVault
import exceptions.exceptions as exc
import regex as re
import os
import sys
from atm_interface.atm_interface import AtmInterface
import time


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
