import click
import sys
from scripts.bank import Bank
from scripts.atm_bank import ATMBank
from scripts.card import Card


@click.group()
def atm():
    pass


@atm.command()
@click.option('--card', help="Write number's card")
@click.option('--owner', help="Write owner's card")
def deposit(card, owner):
    bank = Bank('../src/assets/bank_data.json')
    card = Card(card, owner)
    atm_bank = ATMBank()
    if atm_bank.insert_card(card, bank):
        attempts = 3
        while True:
            pin = click.prompt(f"Write your pin, your attempts {attempts}")
            if atm_bank.check_pin(pin):
                click.echo("Successful")
                break
            elif attempts == 1:
                atm_bank.block_card()
                bank.update_account(atm_bank.get_bank_account())
                click.echo("You blocked your card")
                sys.exit(0)
            else:
                attempts -= 1
                click.echo(f"Incorrect pin")
        value_to_deposit = click.prompt("How much do you want to deposit?", type=int)
        atm_bank.deposit(value_to_deposit)
        click.echo("The deposit is successful")
    else:
        click.echo("Your card has been blocked")


@atm.command()
@click.option('--card', help="Write number's card")
@click.option('--owner', help="Write owner's card")
def withdraw(card, owner):
    bank = Bank('../src/assets/bank_data.json')
    card = Card(card, owner)
    atm_bank = ATMBank()
    if atm_bank.insert_card(card, bank):
        attempts = 3
        while True:
            pin = click.prompt(f"Write your pin, your attempts {attempts}")
            if atm_bank.check_pin(pin):
                click.echo("Successful")
                break
            elif attempts == 1:
                atm_bank.block_card()
                bank.update_account(atm_bank.get_bank_account())
                click.echo("You blocked your card")
                sys.exit(0)
            else:
                attempts -= 1
                click.echo(f"Incorrect pin")
        value_to_withdraw = click.prompt("How much do you want to withdraw?", type=int)
        if atm_bank.withdraw(value_to_withdraw):
            click.echo("The withdraw is successful")
        else:
            click.echo("Transaction rejected. Insufficient funds")
    else:
        click.echo("Your card has been blocked")


@atm.command()
@click.option('--card', help="Write number's card")
@click.option('--owner', help="Write owner's card")
def balance(card, owner):
    bank = Bank('../src/assets/bank_data.json')
    card = Card(card, owner)
    atm_bank = ATMBank()
    if atm_bank.insert_card(card, bank):
        attempts = 3
        while True:
            pin = click.prompt(f"Write your pin, your attempts {attempts}")
            if atm_bank.check_pin(pin):
                click.echo("Successful")
                break
            elif attempts == 1:
                atm_bank.block_card()
                bank.update_account(atm_bank.get_bank_account())
                click.echo("You blocked your card")
                sys.exit(0)
            else:
                attempts -= 1
                click.echo(f"Incorrect pin")
        click.echo(f"Your balance is {atm_bank.get_balance()}")
    else:
        click.echo("Your card has been blocked")


@atm.command()
@click.option('--card', help="Write number's card")
@click.option('--owner', help="Write owner's card")
def add_account(card, owner):
    bank = Bank('../src/assets/bank_data.json')
    if bank.add_account(card, owner):
        click.echo("Added")
    else:
        click.echo("This user already exists")


if __name__ == '__main__':
    atm()
