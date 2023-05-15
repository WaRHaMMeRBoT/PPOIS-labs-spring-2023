from Model.BankComponents.BankEntities import BankUser, BankAccount
from Model.BankComponents.BanknotesStorage import BanknotesStorage, decimal_to_storage


class BankModel:
    def __init__(self):
        self.accounts = []
        self.users = []
        self.authorized = None
        self.current_working_entity = None

    def add_user_account_entity(self,
                                user_name,
                                bank_storage,
                                user_storage,
                                bank_bill,
                                user_phone_bill,
                                card_password,
                                before_being_blocked_situation,
                                steps_before_being_blocked):
        self.accounts.append(BankAccount(card_password,
                                         before_being_blocked_situation,
                                         steps_before_being_blocked,
                                         bank_storage,
                                         bank_bill))
        self.users.append((BankUser(user_name,
                                    user_storage,
                                    user_phone_bill)))

    def set_authorized(self,
                       authorized):
        self.authorized = authorized

    def set_current_working_entity(self,
                                   number):
        if number <= 0 or number > len(self.users):
            raise NameError("DataWithWrongValue")
        self.current_working_entity = number - 1
        self.set_authorized(False)

    def password_checker(self,
                         entered_password):
        if self.current_working_entity is None:
            return "CurrentWorkingEntityMissed"
        working_card = self.accounts[self.current_working_entity].bank_card
        if working_card.get_steps_before_being_blocked() == 0:
            return "NoAttemptsRemain"
        if entered_password == working_card.get_card_password():
            working_card.set_before_being_blocked_situation(False)
            working_card.set_steps_to_default()
            self.set_authorized(True)
            return "Correct"
        working_card.decrease_steps()
        if working_card.get_steps_before_being_blocked() == 0:
            if not working_card.get_before_being_blocked_situation():
                working_card.set_before_being_blocked_situation(True)
                return "Incorrect"
            else:
                self.accounts.pop(self.current_working_entity)
                self.users.pop(self.current_working_entity)
                self.current_working_entity = None
                return "Blocked"
        else:
            return "Incorrect"

    def bank_call(self):
        if self.current_working_entity is None:
            return "CurrentWorkingEntityMissed"
        working_card = self.accounts[self.current_working_entity].bank_card
        if working_card.get_steps_before_being_blocked() != 0:
            return "NotUsedAttemptsRemain"
        working_card.increase_steps()
        return "Correct"

    @staticmethod
    def increase(get_from_object,
                 get_to_object,
                 get_from_object_attribute,
                 get_to_object_attribute,
                 increase_value):
        if get_from_object_attribute == "bill" and get_from_object.bill < increase_value:
            return "Incorrect"
        elif get_from_object_attribute == "storage" and get_from_object.storage < increase_value:
            return "Incorrect"
        if get_from_object_attribute == "bill" and get_to_object_attribute == "storage":
            get_from_object.bill -= increase_value
            get_to_object.storage += BanknotesStorage(decimal_to_storage(increase_value))
        elif get_from_object_attribute == "bill" and get_to_object_attribute == "bill":
            get_from_object.bill -= increase_value
            get_to_object.bill += increase_value
        elif get_from_object_attribute == "storage" and get_to_object_attribute == "storage":
            get_from_object.storage -= increase_value
            get_to_object.storage += increase_value
        elif get_from_object_attribute == "storage" and get_to_object_attribute == "bill":
            get_from_object.storage -= increase_value
            get_to_object.bill += increase_value.get_bill_amount()
        return "Correct"

    def increase_bank_storage_with_user_storage(self,
                                                storage):
        if not self.authorized:
            return "NotAuthorized"
        return BankModel.increase(self.users[self.current_working_entity],
                                  self.accounts[self.current_working_entity],
                                  "storage",
                                  "storage",
                                  BanknotesStorage(storage))

    def increase_bank_bill_with_user_storage(self,
                                             storage):
        if not self.authorized:
            return "NotAuthorized"
        return BankModel.increase(self.users[self.current_working_entity],
                                  self.accounts[self.current_working_entity],
                                  "storage",
                                  "bill",
                                  BanknotesStorage(storage))

    def increase_user_phone_with_bank_bill(self,
                                           bill):
        if not self.authorized:
            return "NotAuthorized"
        return BankModel.increase(self.accounts[self.current_working_entity],
                                  self.users[self.current_working_entity],
                                  "bill",
                                  "bill",
                                  bill)

    def increase_user_storage_with_bank_bill(self,
                                             bill):
        if not self.authorized:
            return "NotAuthorized"
        return BankModel.increase(self.accounts[self.current_working_entity],
                                  self.users[self.current_working_entity],
                                  "bill",
                                  "storage",
                                  bill)

    def increase_user_storage_with_bank_storage(self,
                                                storage):
        if not self.authorized:
            return "NotAuthorized"
        return BankModel.increase(self.accounts[self.current_working_entity],
                                  self.users[self.current_working_entity],
                                  "storage",
                                  "storage",
                                  BanknotesStorage(storage))

    def get_authorized(self):
        return self.authorized

    def get_user_phone_bill(self):
        if not self.authorized:
            return "NotAuthorized"
        return self.users[self.current_working_entity].bill

    def get_bank_account_bill(self):
        if not self.authorized:
            return "NotAuthorized"
        return self.accounts[self.current_working_entity].bill

    def get_user_cash_storage(self):
        if not self.authorized:
            return "NotAuthorized"
        return dict(self.users[self.current_working_entity].storage.get_storage_banknotes())

    def get_bank_account_storage(self):
        if not self.authorized:
            return "NotAuthorized"
        return dict(self.accounts[self.current_working_entity].storage.get_storage_banknotes())

    def get_usernames(self):
        usernames = [user.user_name for user in self.users]
        return usernames

    def get_amount_of_attempts(self):
        if self.current_working_entity is None:
            return "CurrentWorkingEntityMissed"
        return self.accounts[self.current_working_entity].bank_card.get_steps_before_being_blocked()

    def get_info(self):
        info = dict()
        info["authorized"] = self.authorized
        info["current working entity"] = self.current_working_entity
        entities = []
        for account, user in zip(self.accounts, self.users):
            entity = dict()
            entity["account"] = account.get_info()
            entity["user"] = user.get_info()
            entities.append(entity)
        info["entities"] = entities
        return info
