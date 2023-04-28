from Model.BankModel import BankModel
from Model.BankComponents.BankCard import DEFAULT_AMOUNT_OF_STEPS
from Model.BankComponents.BanknotesStorage import BANKNOTES_DENOMINATIONS, decimal_to_storage
import json


class BankController:
    def __init__(self):
        self.model = BankModel()

    @staticmethod
    def storage_denominations_checker(storage_denominations):
        for index in range(len(storage_denominations)):
            storage_denominations[index] = int(storage_denominations[index])
            if storage_denominations[index] < 0:
                raise NameError("DataWithWrongValue")

    @staticmethod
    def integer_values_checker(first,
                               second):
        try:
            first = int(first)
            second = int(second)
            if first < 0 or second < 0:
                raise NameError("DataWithWrongValue")
        except ValueError:
            return "DataWithWrongType"
        except NameError:
            return "DataWithWrongValue"
        return 0

    @staticmethod
    def add_user_account_entity_value_checker(bank_storage_value,
                                              user_storage_value):
        answer = BankController.integer_values_checker(bank_storage_value,
                                                       user_storage_value)
        if answer == "DataWithWrongType" or answer == "DataWithWrongValue":
            return answer
        return (bill_to_storage_denomination_list(int(bank_storage_value)),
                bill_to_storage_denomination_list(int(user_storage_value)))

    @staticmethod
    def increase_with_storage_value_checker(denomination,
                                            amount):
        answer = BankController.integer_values_checker(denomination,
                                                       amount)
        if answer == "DataWithWrongType" or answer == "DataWithWrongValue":
            return answer
        return denomination_and_amount_to_storage_denomination_list(int(denomination),
                                                                    int(amount))

    def add_user_account_entity_validated(self,
                                          user_name,
                                          bank_storage_denominations,
                                          user_storage_denominations,
                                          bank_bill,
                                          user_phone_bill,
                                          card_password):
        try:
            BankController.storage_denominations_checker(bank_storage_denominations)
            BankController.storage_denominations_checker(user_storage_denominations)
            bank_bill = int(bank_bill)
            user_phone_bill = int(user_phone_bill)
            if bank_bill < 0 or user_phone_bill < 0:
                raise NameError("DataWithWrongValue")
        except ValueError:
            return "DataWithWrongType"
        except NameError:
            return "DataWithWrongValue"
        bank_storage_denominations = {denomination: amount for denomination, amount in zip(BANKNOTES_DENOMINATIONS,
                                                                                           bank_storage_denominations)}
        user_storage_denominations = {denomination: amount for denomination, amount in zip(BANKNOTES_DENOMINATIONS,
                                                                                           user_storage_denominations)}
        self.model.add_user_account_entity(user_name,
                                           bank_storage_denominations,
                                           user_storage_denominations,
                                           bank_bill,
                                           user_phone_bill,
                                           card_password,
                                           False,
                                           DEFAULT_AMOUNT_OF_STEPS)
        return "Correct"

    def set_current_working_entity_validated(self,
                                             number):
        try:
            number = int(number)
        except ValueError:
            return "DataWithWrongType"
        try:
            self.model.set_current_working_entity(number)
        except NameError:
            return "DataWithWrongValue"
        return "Correct"

    def password_checker(self,
                         password):
        return self.model.password_checker(password)

    def bank_call(self):
        return self.model.bank_call()

    def increase_bank_storage_with_user_storage_validated(self,
                                                          storage_denominations):
        try:
            BankController.storage_denominations_checker(storage_denominations)
        except ValueError:
            return "DataWithWrongType"
        except NameError:
            return "DataWithWrongValue"
        storage_denominations = {denomination: amount for denomination, amount in zip(BANKNOTES_DENOMINATIONS,
                                                                                      storage_denominations)}
        return self.model.increase_bank_storage_with_user_storage(storage_denominations)

    def increase_bank_bill_with_user_storage_validated(self,
                                                       storage_denominations):
        try:
            BankController.storage_denominations_checker(storage_denominations)
        except ValueError:
            return "DataWithWrongType"
        except NameError:
            return "DataWithWrongValue"
        storage_denominations = {denomination: amount for denomination, amount in zip(BANKNOTES_DENOMINATIONS,
                                                                                      storage_denominations)}
        return self.model.increase_bank_bill_with_user_storage(storage_denominations)

    def increase_user_phone_with_bank_bill_validated(self,
                                                     bill):
        try:
            bill = int(bill)
            if bill < 0:
                raise NameError("DataWithWrongValue")
        except ValueError:
            return "DataWithWrongType"
        except NameError:
            return "DataWithWrongValue"
        return self.model.increase_user_phone_with_bank_bill(bill)

    def increase_user_storage_with_bank_bill_validated(self,
                                                       bill):
        try:
            bill = int(bill)
            if bill < 0:
                raise NameError("DataWithWrongValue")
        except ValueError:
            return "DataWithWrongType"
        except NameError:
            return "DataWithWrongValue"
        return self.model.increase_user_storage_with_bank_bill(bill)

    def increase_user_storage_with_bank_storage_validated(self,
                                                          storage_denominations):
        try:
            BankController.storage_denominations_checker(storage_denominations)
        except ValueError:
            return "DataWithWrongType"
        except NameError:
            return "DataWithWrongValue"
        storage_denominations = {denomination: amount for denomination, amount in zip(BANKNOTES_DENOMINATIONS,
                                                                                      storage_denominations)}
        return self.model.increase_user_storage_with_bank_storage(storage_denominations)

    def get_authorized(self):
        return self.model.get_authorized()

    def get_user_phone_bill(self):
        return self.model.get_user_phone_bill()

    def get_bank_account_bill(self):
        return self.model.get_bank_account_bill()

    def get_user_cash_storage(self):
        return self.model.get_user_cash_storage()

    def get_bank_account_storage(self):
        return self.model.get_bank_account_storage()

    def get_usernames(self):
        return self.model.get_usernames()

    def get_amount_of_attempts(self):
        return self.model.get_amount_of_attempts()

    def write_to_file(self):
        info = self.model.get_info()
        with open("Model/BankData.json", "w") as f:
            json.dump(info, f, indent=5)

    def read_from_file(self):
        with open("Model/BankData.json", "r") as f:
            info = json.load(f)
        if len(info) == 0:
            return
        entities = info["entities"]
        for entity in entities:
            new_bank_storage = {int(key): value for key, value in entity["account"]["bank storage"].items()}
            new_user_storage = {int(key): value for key, value in entity["user"]["user storage"].items()}
            self.model.add_user_account_entity(entity["user"]["user name"],
                                               new_bank_storage,
                                               new_user_storage,
                                               entity["account"]["bank bill"],
                                               entity["user"]["user phone bill"],
                                               entity["account"]["card password"],
                                               entity["account"]["before being blocked situation"],
                                               entity["account"]["steps before being blocked"])
        if info["current working entity"] is not None:
            self.model.set_current_working_entity(info["current working entity"] + 1)
        if info["authorized"] is not None:
            self.model.set_authorized(info["authorized"])


def bill_to_storage_denomination_list(number):
    return list(decimal_to_storage(number).values())


def denomination_and_amount_to_storage_denomination_list(denomination,
                                                         amount):
    storage = [0 for index in range(len(BANKNOTES_DENOMINATIONS))]
    try:
        storage[BANKNOTES_DENOMINATIONS.index(denomination)] = amount
    except ValueError:
        return "DataWithWrongValue"
    return storage
