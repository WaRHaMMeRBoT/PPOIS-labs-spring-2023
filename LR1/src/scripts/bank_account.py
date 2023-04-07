from .interfaces.interfaces import IBankAccount


class BankAccount(IBankAccount):
    def __init__(self, number, pin, owner, balance=0):
        self.number = str(number)
        self.pin = str(pin)
        self.owner = str(owner)
        self.balance = balance

    def get_account_data(self):
        data = dict()
        data[self.number] = {
            'pin': self.pin,
            'owner': self.owner,
            'balance': self.balance,
        }
        return data
