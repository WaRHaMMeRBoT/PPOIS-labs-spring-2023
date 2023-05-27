import pandas as pd
from datetime import datetime
from bank import *
import pickle
import json

#
# 375292620440

if __name__ == '__main__':
    while True:
        print('Number card')
        num_card = input().replace(' ', '')
        if num_card.isdigit() and len(num_card) == 16:
            atm = ATM(int(num_card))
            if atm.check_card() and atm.our_card.enter_pin():
                while True:
                     print('0 - Check balance')
                     print('1 - Putting money on the card')
                     print('2 - Get money form the card')
                     print('3 - Put money on the phone')
                     print('9 - Pull out card')
                     n = int(input())

                     if n == 0:
                         print(atm.our_card.check_balance())

                     elif n == 1:
                         atm.put_money_on_card()

                     elif n == 2:
                         atm.get_money()

                     elif n == 3:
                         atm.put_money_on_phone_number()

                     elif n == 9:
                         break

                     else:
                         print('Wrong command')

        else:
            print('Wrong number card')
