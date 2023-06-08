import json
import PySimpleGUI as sg

import windows as w
import get_data


class CacheMachine:
    __available_cache: list
    __current_card: str
    __verified: bool = False
    __console: bool = False

    def __init__(self, is_console):
        self.__console = is_console
        with open("cache.json") as file:
            self.__available_cache = json.load(file)
            file.close()

    def is_verified(self):
        return self.__verified

    def get_users_card_number(self, card, pin):
        number: str = card
        self.__verify_users_card_number(number, pin)

    def __verify_users_card_number(self, number, curr_pin):
        pin: str = curr_pin
        with open("users.json") as file:
            data = json.load(file)
            for i in data['users']:
                if i['card_num'] == number and i['pin'] == pin:
                    self.__current_card = number
                    self.__verified = True
                    file.close()
                    return
        print("Wrong card number or pin")

    def __check_pin(self, card, curr_pin):
        pin: str = curr_pin
        with open("users.json") as file:
            data = json.loads(file.read())
            for i in data['users']:
                if i['card_num'] == card and i['pin'] == pin:
                    self.__current_user_cache = i['money']
                    self.__verified = True
                    return

            self.__verified = False
            if self.__console == False:
                sg.popup("Wrong pin")
            else:
                print("Wrong pin\n")

    def __get_current_user_cache(self, card):
        with open("users.json") as file:
            data = json.loads(file.read())
            for i in data['users']:
                if i['card_num'] == card:
                    return i['money']

    def check_account(self, card, curr_pin):
        self.__check_pin(card, curr_pin)
        if self.__verified:
            if self.__console == False:
                sg.popup(f'Your balance: {self.__get_current_user_cache(card)}')
            else:
                print(f'Your balance: {self.__get_current_user_cache(card)}')

    def __cache_in_machine(self):
        cache = 0
        for i in self.__available_cache:
            cache += i
        print("Available: ", cache, "\n")

    def get_cache(self, card, pin):
        self.__check_pin(card, pin)
        if self.__verified:
            print("Your cache: ", self.__get_current_user_cache(card))
            print("Available banknotes: 500, 100, 10\n")
            if self.__console == False:
                value = w.get_money_window()
                value = int(value)
            else:
                value = int(input("Enter value: "))
            if value != 500 and value != 100 and value != 10:
                if self.__console == False:
                    sg.popup("Wrong value!")
                else:
                    print('Wrong value! \n')
                return
            self.__get_user_cache(value, card)
            if self.__console == False:
                sg.popup("Done!")

    def __get_user_cache(self, value: float, card):
        with open('users.json') as file:
            data = json.loads(file.read())
            file.close()
        for i in data['users']:
            if i['card_num'] == card:
                if value < float(i['money']):
                    i['money'] = str(float(i['money']) - value)
                    if self.__remove_from_cache_machine(value):
                        get_data.dump_json(data)
                        break
                else:
                    sg.popup("Not enough money.")
                    print('Not enough money.\n')

    def __remove_from_cache_machine(self, value):
        check = 0
        for i in self.__available_cache['cache']:
            if float(i['id']) == value:
                i['id'] = str(0)
                get_data.dump_cache(self.__available_cache)
                return True
        if check != 0:
            sg.popup("Not enough money in machine")
            print('Not enough money in machine')
            return False

    def pay_phone(self, card, pin):
        self.__check_pin(card, pin)

        if self.__verified:
            if self.__console == False:
                value: float = float(w.get_money_window())
            else:
                value = float(input("Enter value: "))
            with open('users.json', 'r') as file:
                data = json.load(file)
                file.close()
            for i in data['users']:
                if i['card_num'] == card and float(i['money']) > value:
                    i['money'] = str(float(i['money']) - value)
                    break
                if float(i['money']) < value:
                    if self.__console == False:
                        sg.popup("Not enough money")
                    else:
                        print("Not enough money.\n")
                    return
            get_data.dump_json(data)
            if self.__console == False:
                sg.popup("Done!")
