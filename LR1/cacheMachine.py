import json

import click


class CacheMachine:
    __available_cache: list
    __current_card: str
    __verified: bool = False

    def __init__(self):
        with open("cache.json") as file:
            self.__available_cache = json.load(file)
            file.close()

    def is_verified(self):
        return self.__verified

    def get_users_card_number(self):
        number: str = input("Enter your card number: ")
        self.__verify_users_card_number(number)

    def __verify_users_card_number(self, number):
        pin: str = input("Enter your pin: ")
        with open("users.json") as file:
            data = json.load(file)
            for i in data['users']:
                if i['card_num'] == number and i['pin'] == pin:
                    self.__current_card = number
                    self.__verified = True
                    file.close()
                    return
        print("Wrong card number or pin")

    def __check_pin(self):
        pin: str = input("Enter your pin: ")
        with open("users.json") as file:
            data = json.loads(file.read())
            for i in data['users']:
                if i['card_num'] == self.__current_card and i['pin'] == pin:
                    self.__current_user_cache = i['money']
                    self.__verified = True
                    return

            self.__verified = False
            print("Wrong pin\n")

    def __get_current_user_cache(self):
        with open("users.json") as file:
            data = json.loads(file.read())
            for i in data['users']:
                if i['card_num'] == self.__current_card:
                    return i['money']

    def check_account(self):
        self.__check_pin()
        if self.__verified:
            print(f'Your balance: {self.__get_current_user_cache()}')

    def __cache_in_machine(self):
        cache = 0
        for i in self.__available_cache:
            cache += i
        print("Available: ", cache, "\n")

    def get_cache(self):
        self.__check_pin()

        if self.__verified:
            print("Your cache: ", self.__get_current_user_cache())
            print("Available banknotes: 500, 100, 10\n")
            value: float = float(input("Enter amount: "))
            if value != 500 and value != 100 and value != 10:
                print('Wrong value! \n')
                return
            self.__get_user_cache(value)

    def __get_user_cache(self, value: float):
        with open('users.json') as file:
            data = json.loads(file.read())
            file.close()
        for i in data['users']:
            if i['card_num'] == self.__current_card:
                if value < float(i['money']):
                    i['money'] = str(float(i['money']) - value)
                    if self.__remove_from_cache_machine(value):
                        with open('users.json', 'w') as file:
                            data_json = json.dumps(data, indent=3)
                            file.write(data_json)
                            file.close()
                            break
                else:
                    print('Not enough money.\n')

    def __remove_from_cache_machine(self, value):
        check = 0
        for i in self.__available_cache['cache']:
            if float(i['id']) == value:
                i['id'] = str(0)
                with open('cache.json', 'w+') as file:
                    data_json = json.dumps(self.__available_cache, indent=2)
                    file.write(data_json)
                    file.close()
                    return True
        if check != 0:
            print('Not enough money in machine')
            return False

    def pay_phone(self):
        self.__check_pin()

        if self.__verified:
            value: float = float(input('Enter value: '))
            with open('users.json', 'r') as file:
                data = json.load(file)
                file.close()
            for i in data['users']:
                if i['card_num'] == self.__current_card and float(i['money']) > value:
                    i['money'] = str(float(i['money']) - value)
                    print('            ', i['money'])
                    break
                if float(i['money']) < value:
                    print("Not enough money.\n")
                    return
            with open('users.json', 'w') as file1:

                data_json = json.dumps(data, indent=3)
                file1.write(data_json)
                file1.close()
