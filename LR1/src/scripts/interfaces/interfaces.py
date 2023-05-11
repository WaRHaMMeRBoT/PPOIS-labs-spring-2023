from abc import ABC, abstractmethod


class IBank(ABC):
    @abstractmethod
    def get_account(self, card_number, owner):
        pass

    def update_account(self, obj):
        pass

    def add_account(self, obj, card_number):
        pass


class IBankAccount(ABC):
    @abstractmethod
    def get_account_data(self):
        pass


class IATMBank(ABC):
    @abstractmethod
    def insert_card(self, number_card, bank):
        pass

    @abstractmethod
    def check_pin(self, _pin):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_bank_account(self):
        pass

    @abstractmethod
    def block_card(self):
        pass
