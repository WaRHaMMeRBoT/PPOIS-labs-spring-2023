BANKNOTES_DENOMINATIONS = [1, 2, 5, 10, 20, 50, 100, 200]


class BanknotesStorage:
    existing_denominations = BANKNOTES_DENOMINATIONS

    def __init__(self,
                 storage_banknotes):
        self.storage_banknotes = dict(storage_banknotes)
        self.bill_amount = self.refresh_bill_value()

    def get_storage_banknotes(self):
        return self.storage_banknotes

    def get_bill_amount(self):
        return self.bill_amount

    def refresh_bill_value(self):
        bill_value = 0
        for denomination, amount in self.storage_banknotes.items():
            bill_value += denomination * amount
        return bill_value

    def __lt__(self, other):
        for denomination in BanknotesStorage.existing_denominations:
            if self.storage_banknotes[denomination] < other.storage_banknotes[denomination]:
                return True
        return False

    def __iadd__(self, other):
        for denomination in BanknotesStorage.existing_denominations:
            self.storage_banknotes[denomination] += other.storage_banknotes[denomination]
        self.bill_amount = self.refresh_bill_value()
        return self

    def __isub__(self, other):
        for denomination in BanknotesStorage.existing_denominations:
            self.storage_banknotes[denomination] -= other.storage_banknotes[denomination]
        self.bill_amount = self.refresh_bill_value()
        return self

    def output(self):
        for denomination, amount in self.storage_banknotes.items():
            print("With denomination {0} : {1} banknotes.".format(denomination,
                                                                  amount))
        print("Current storage bill : {}.".format(self.bill_amount))


def decimal_to_storage(bill_to_get_out):
    storage_banknotes = dict().fromkeys(list(BanknotesStorage.existing_denominations))
    reversed_denominations = list(BanknotesStorage.existing_denominations)
    reversed_denominations.reverse()
    for current_denomination in reversed_denominations:
        current_banknotes_amount = bill_to_get_out // current_denomination
        bill_to_get_out -= current_banknotes_amount * current_denomination
        storage_banknotes[current_denomination] = current_banknotes_amount
    return storage_banknotes
