from Model.BankComponents.BanknotesStorage import BanknotesStorage
from Model.BankComponents.BankCard import BankCard


class BankEntity:
    def __init__(self,
                 storage,
                 bill):
        self.storage = BanknotesStorage(storage)
        self.bill = bill

    def get_info(self):
        pass


class BankAccount(BankEntity):
    def __init__(self,
                 card_password,
                 before_being_blocked_situation,
                 steps_before_being_blocked,
                 bank_storage,
                 bank_bill):
        super(BankAccount, self).__init__(bank_storage,
                                          bank_bill)
        self.bank_card = BankCard(card_password,
                                  before_being_blocked_situation,
                                  steps_before_being_blocked)

    def get_info(self):
        info = dict()
        info["card password"] = self.bank_card.get_card_password()
        info["before being blocked situation"] = self.bank_card.get_before_being_blocked_situation()
        info["steps before being blocked"] = self.bank_card.get_steps_before_being_blocked()
        info["bank storage"] = self.storage.get_storage_banknotes()
        info["bank bill"] = self.bill
        return info


class BankUser(BankEntity):
    def __init__(self,
                 user_name,
                 user_storage,
                 user_phone_bill):
        super(BankUser, self).__init__(user_storage,
                                       user_phone_bill)
        self.user_name = user_name

    def get_info(self):
        info = dict()
        info["user name"] = self.user_name
        info["user storage"] = self.storage.get_storage_banknotes()
        info["user phone bill"] = self.bill
        return info
