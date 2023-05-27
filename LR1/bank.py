# from currency_converter import CurrencyConverter
from random import choice
from datetime import date
from datetime import datetime
import pandas as pd

class ATM():
    def __init__(self, card_number: int):
        self.storage = self.Money_storage()
        self.our_card = self.Plastic_card(card_number)

    def check_card(self):
        if self.our_card.is_registered_card():
            if self.our_card.is_still_available():
                return True
            else:
                print("Validity period is expired")
        else:
            print('This card doesnt registered')
        return False

    def put_money_on_card(self):
        print('Введите номиналы банкнот которые вы положите в банкомат')
        denominations_of_banknotes = [int(i) for i in input().split()]
        df = pd.read_csv('dataframe', index_col=0)
        for denomination in denominations_of_banknotes:
            left_bills_in_this_denomination = self.storage.bills.get(denomination)
            if left_bills_in_this_denomination is None:
                print(f'Wrong denomination {denomination}')
            else:
                print(f'How many bills will you put in ? Denomination - {denomination}')
                count_bills = int(input())
                self.our_card.card_balance += count_bills * denomination
                self.storage.bills[denomination] += count_bills
        df.loc[self.our_card.card_number, 'balance'] = self.our_card.card_balance
        with open('dataframe', 'w') as f:
            df.to_csv(f)

    def get_money(self):
        def help_func(value:int, amount_to_withdraw: int):
            bills = amount_to_withdraw // value
            amount_to_withdraw -= bills * value
            return bills, amount_to_withdraw

        print('How much money to withdraw')
        amount_to_withdraw = int(input())
        safe_amount_to_withdraw = int(amount_to_withdraw)
        df = pd.read_csv('dataframe', index_col=0)
        if amount_to_withdraw > self.our_card.card_balance:
            print('Not enough money on your card')
        else:
            bills_100, amount_to_withdraw = help_func(100, amount_to_withdraw)
            bills_50, amount_to_withdraw = help_func(50, amount_to_withdraw)
            bills_20, amount_to_withdraw = help_func(20, amount_to_withdraw)
            bills_10, amount_to_withdraw = help_func(10, amount_to_withdraw)
            bills_5, amount_to_withdraw = help_func(5, amount_to_withdraw)
            bills_1, amount_to_withdraw = help_func(1, amount_to_withdraw)
            if amount_to_withdraw == 0:
                for key in self.storage.bills:
                    self.storage.bills[key] += bills_1
                print(f'''
                Denomination: 100; count: {bills_100}
                Denomination: 50; count: {bills_50}
                Denomination: 20; count: {bills_20}
                Denomination: 10; count: {bills_10}
                Denomination: 5; count: {bills_5}
                Denomination: 1; count: {bills_1}
                ''')
                self.storage.bills[1] += bills_1
                self.storage.bills[5] += bills_5
                self.storage.bills[10] += bills_10
                self.storage.bills[20] += bills_20
                self.storage.bills[50] += bills_50
                self.storage.bills[100] += bills_100

                self.our_card.card_balance -= safe_amount_to_withdraw
                df.loc[self.our_card.card_number, 'balance'] = self.our_card.card_balance
                with open('dataframe', 'w') as f:
                    df.to_csv(f)
            else:
                print('Not enough money in atm')

    def put_money_on_phone_number(self):
        df = pd.read_csv('phone_numbers', index_col=0)
        print('Phone number ?')
        phone_number = input()
        if len(phone_number) == 12:
            try:
                phone_balance = df.loc[int(phone_number), 'balance']
                print('How much money would u prefer to put on phone number ?')
                amount = int(input())
                if self.our_card.card_balance > amount:
                    self.our_card.card_balance -= amount
                    phone_balance += amount
                    df.loc[int(phone_number), 'balance'] = phone_balance
                    with open('phone_numbers', 'w') as f:
                        df.to_csv(f)

                    df = pd.read_csv('dataframe', index_col=0)
                    df.loc[self.our_card.card_number, 'balance'] = self.our_card.card_balance
                    with open('dataframe', 'w') as f:
                        df.to_csv(f)
                else:
                    print('Not enough money on the card')

            except:
                print('Phone number doesnt exist')
        else:
            print('Wrong number')





    class Money_storage():
        def __init__(self):
            self.bills = {1: choice(range(100, 10000)), 5: choice(range(100, 5000)), 10: choice(range(100, 2000)),
                          20: choice(range(100, 250)), 50: choice(range(10, 100)), 100: choice(range(10, 100))}

            self.bills_1 = {'left': choice(range(100, 10000)), 'value': 1}
            self.bills_5 = {'left': choice(range(100, 5000)), 'value': 5}
            self.bills_10 = {'left': choice(range(100, 2000)), 'value': 10}
            self.bills_20 = {'left': choice(range(100, 250)), 'value': 20}
            self.bills_50 = {'left': choice(range(10, 100)), 'value': 50}
            self.bills_100 = {'left': choice(range(10, 100)), 'value': 100}

    class Plastic_card():
        def __init__(self,
                     card_number: int):  # , card_bill: str, VALID_THRY: datetime.date, pin: int, card_balance: int
            self.card_number = card_number


        def is_registered_card(self):
            df = pd.read_csv('dataframe', index_col=0)
            try:
                info = df.loc[self.card_number, :]
                return True
            except:
                return False

        def is_still_available(self):
            df = pd.read_csv('dataframe', index_col=0)
            info = df.loc[self.card_number, :]
            validity_period = datetime.strptime(info.VALID_THRY, '%m/%Y').date()
            if validity_period > date.today():
                self.pin = info.pin
                self.card_bill = info.card_bill
                self.card_balance = info.balance
                return True
            else:
                return False

        def enter_pin(self):
            counter_attempt = 0
            while counter_attempt != 3:
                print('Enter pin ')
                enter_pin = int(input())
                if enter_pin == self.pin:
                    return True
                else:
                    counter_attempt += 1
                    print(f'Wrong pin code. Attempt lefts {4-counter_attempt}')
            return False

        def check_balance(self):
            return self.card_balance