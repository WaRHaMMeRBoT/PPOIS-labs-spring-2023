
class Card:
    def __init__(self, pin_code, card_number):
        self.pin_code = pin_code
        self.card_number = card_number

    def set_values(self,pin_code,card_number):
        print("Работа с данными пользователя")
        print("Введите данные карты пользователя")
        print("Карта пользователя")
        card_number = int(input())
        print("Пин пользователя")
        pin_code = int(input())

    def update_values(self,pin_code,card_number):
        print("Работа с данными пользователя")
        print("Обновленные данных  карты пользователя")
        print("Новая карта пользователя")
        card_number = int(input())
        print("Новый пин пользователя")
        pin_code = int(input())

    def delete_values(self,pin_code,card_number):
        print("Работа с данными пользователя")
        print("Удаление данных карты  пользователя")
        print("Удаление карты пользователя")
        card_number = 0
        print("Удаление пин пользователя")
        pin_code = 0

class Bank:
    def __init__(self, card_money):
        self.card_money = card_money

    def set_values(self, card_money):
        print("Работа с данными пользователя")
        print("Введите данные счета пользователя")
        print("Деньги на счету пользователя")
        card_money = int(input())

    def update_values(self, card_money):
        print("Работа с данными пользователя")
        print("Обновленные данных пользователя")
        print("Новая карта пользователя")
        card_money = int(input())


    def delete_values(self, card_money):
        print("Работа с данными пользователя")
        print("Удаление данных пользователя")
        print("Удаление карты пользователя")
        card_money = 0

class Atm:
    def __init__(self, atm_money):
        self.atm_money = atm_money

    def set_values(self, atm_money):
        print("Введите кол-во денег банкомата")
        atm_money = int(input())

    def update_values(self, atm_money):
        print("Новое кол-во денег банкомата ")
        atm_money = int(input())

    def delete_values(self, atm_money):
        print("Обнуление денег банкомата")
        atm_money = 0

class Telephone:
    def __init__(self,tel_money):
        self.tel_money = tel_money
    def set_values(self, tel_money):
        print("Введите кол-во денег на телефоне")
        tel_money = int(input())

    def update_values(self, tel_money):
        print("Новое кол-во денег на телефоне ")
        tel_money = int(input())

    def delete_values(self, tel_money):
        print("Обнуление денег на телефоне")
        tel_money = 0
