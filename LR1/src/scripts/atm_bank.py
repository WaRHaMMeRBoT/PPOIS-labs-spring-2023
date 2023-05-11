from .interfaces.interfaces import IATMBank


class ATMBank(IATMBank):
    def __init__(self):
        self.bank_account_data = None
        self.card = None

    def insert_card(self, card, bank):
        self.card = card
        card_number = card.card_number
        owner = card.owner
        self.bank_account_data = bank.get_account(card_number, owner) if bank.get_account(card_number, owner) else None
        valid_card = self.bank_account_data[card_number].get('card_blocked') is None
        if self.bank_account_data and valid_card:
            return True
        return False

    def check_pin(self, _pin):
        pin = self.bank_account_data[self.card.card_number]['pin']
        if pin == _pin:
            return True
        else:
            return False

    def withdraw(self, amount):
        card_balance = self.bank_account_data[self.card.card_number]['balance']
        if card_balance - amount >= 0:
            card_balance -= amount
            self.bank_account_data[self.card.card_number]['balance'] = card_balance
            return True
        return False

    def deposit(self, amount):
        card_balance = self.bank_account_data[self.card.card_number]['balance']
        card_balance += amount
        self.bank_account_data[self.card.card_number]['balance'] = card_balance

    def get_balance(self):
        card_balance = self.bank_account_data[self.card.card_number]['balance']
        return card_balance

    def get_bank_account(self):
        return self.bank_account_data

    def block_card(self):
        self.get_bank_account()[self.card.card_number]['card_blocked'] = True
