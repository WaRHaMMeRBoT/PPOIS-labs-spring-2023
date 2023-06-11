from utils.Interface import GuiAtm
import json
import sys
from typing import Optional
import click
import regex as regEX
import utils.Exceptions as excep
from utils.ATM import ATM
from utils.ATM_interface import ATMInterface
from utils.Money_Storage import MoneyStorage
from utils.Plastic_Card import PlasticCard

pin_attempts: int = 3
plastic_card: Optional[PlasticCard]
card_active: bool = False


@click.group()
def CLI():
    load_state()
    money_vault: MoneyStorage = ATMInterface.find_money_vault()
    ATMInterface.atm = ATM(money_vault, plastic_card)


@click.command()
def start_gui():
    GuiAtm.run()


@click.command()
@click.argument('card_number')
@click.option('--card_number', '-n', help="Inserting card number")
def insert_card(card_number):
    global plastic_card
    plastic_card = ATMInterface.find_card_by_card_num(card_number)
    if plastic_card is None:
        print("Card is not valid\n")
    else:
        if plastic_card.is_blocked:
            print("Your card is blocked\nCall the bank to solve this")
        if plastic_card.is_expired:
            print("Your card is expired\nGet the new one at the bank")
    save_state()


@click.command()
def get_card_back():
    global plastic_card, pin_attempts, card_active
    if plastic_card is not None:
        plastic_card = None
    pin_attempts = 3
    card_active = False
    save_state()


@click.command()
@click.argument('card_pin')
@click.option('--card_pin', '-p', help="Pin code of inserted card")
def check_pin(card_pin):
    global pin_attempts, card_active
    if plastic_card is not None:
        if plastic_card.is_blocked or plastic_card.is_expired:
            print("Card is invalid, take it back\n")
        else:
            if not ATMInterface.atm.check_card_pin(card_pin):
                pin_attempts -= 1
                print("Incorrect PIN!\n"
                      f"{pin_attempts} attempts left")
            else:
                print("You can use card")
                card_active = True
                pin_attempts = 3
        if pin_attempts <= 0:
            ATMInterface.atm.block_card()
            ATMInterface.save_cards_status()
            print("You have failed all 3 attempts to enter PIN\n"
                  "Blocking the plastic card...\n"
                  "Connect the bank to unblock")
    else:
        print("Insert the card first\n")
    save_state()


@click.command()
def get_balance():
    if card_active:
        print(f"Your balance is {plastic_card.card_acc.balance}")
    else:
        print("You can't use card")


@click.command()
@click.argument('amount_of_money')
@click.option('--amount_of_money', '-a', help="Amount of money to get")
def get_cash_money(amount_of_money):
    if card_active:
        money_amount: int = int(amount_of_money)
        try:
            ATMInterface.atm.get_cash_money(money_amount)
        except excep.NotEnoughMoney:
            print("Not enough money!")
            sys.exit()
        except excep.NoAvailableMoneyConfig:
            print("That sum of money is unavailable to get!")
            sys.exit()
        else:
            ATMInterface.save_money_vault()
            ATMInterface.save_card_accounts()
            print("Here are your money!")
    else:
        print("Can't do operations")
    save_state()


@click.command()
@click.argument('phone_number')
@click.argument('amount_of_money')
@click.option('--phone_number', '-n', help="Phone number to put money")
@click.option('--amount_of_money', '-a', help="Amount of money to put on phone")
def put_money_on_phone(phone_number, amount_of_money):
    if card_active:
        if not regEX.fullmatch(r"\+375(29|33|25|44|17|29)\d{7}", phone_number):
            print("Incorrect phone number!")
            sys.exit()
        money_amount: float = float(amount_of_money)
        try:
            ATMInterface.atm.custom_operation(money_amount)
        except excep.NotEnoughMoney:
            print("Not enough money!")
            sys.exit()
        else:
            ATMInterface.save_card_accounts()
            print("Successful!")
    else:
        print("Can't do operations")
    save_state()


def save_state():
    data_to_save = {}
    if plastic_card is not None:
        data_to_save['CardID'] = plastic_card.card_id
    else:
        data_to_save['CardID'] = ''
    data_to_save['IsCardActive'] = card_active
    data_to_save['PinAttempts'] = pin_attempts
    with open("./JSON_files/ATMstate.json", "w") as state_file:
        json.dump(data_to_save, state_file, indent=6)


def load_state():
    with open("./JSON_files/ATMstate.json", "r") as state_file:
        data_to_load = json.load(state_file)
    global pin_attempts, plastic_card, card_active
    if data_to_load['CardID'] == '':
        plastic_card = None
    else:
        plastic_card = ATMInterface.find_card_by_card_num(data_to_load['CardID'])
    card_active = bool(data_to_load['IsCardActive'])
    pin_attempts = int(data_to_load['PinAttempts'])


CLI.add_command(start_gui)
CLI.add_command(get_cash_money)
CLI.add_command(put_money_on_phone)
CLI.add_command(check_pin)
CLI.add_command(get_card_back)
CLI.add_command(insert_card)
CLI.add_command(get_balance)
