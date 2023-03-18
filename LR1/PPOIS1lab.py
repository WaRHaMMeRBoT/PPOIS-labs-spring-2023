import sys

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

class Display_values():

    def display_values(self, Atm, Bank, Card,Telephone):
        print("Введите Пин-Код :")
        if Card.pin_code == 1488:
            print("Кол-во денег на карте")
            print(Bank.card_money)
            print("Кол-во денег в банкомате")
            print(Atm.atm_money)
            print("Кол-во денег на телефоне")
            print(Telephone.tel_money)
        else:
            print("Неверный пин")

class Rewrite_values():

    def rewrite_values(self, Atm, Bank, Card,Telephone):
        print("Введите Пин-Код :")
        if Card.pin_code == 1488:
            print("Запись в файл")
            f.seek(0)
            f.write('%d' % Atm.atm_money +'\n')
            f.write('%d' % Bank.card_money +'\n')
            f.write('%d' % Card.pin_code +'\n')
            f.write('%d' % Card.card_number +'\n')
            f.write('%d' % Telephone.tel_money +'\n')
            f.truncate()
            
        else:
            print("Неверный пин")

class Read_values():
    def read_values(self):
        pin = 1488
        print("Введите Пин-Код :")
        if pin == 1488:
            print("Чтение из файла")
            array_of_values = f.readlines()
            array_of_values = list(map(int,array_of_values))
            print(array_of_values)
        else:
            print("Неверный пин")

        return array_of_values

class Add_money():
    def add_money(self, Atm, Card, Bank):
        if Card.pin_code == 1488:
            print("Внесите сумму для пополнения")
            money = int(input())
            if money > 0:
                Bank.card_money = Bank.card_money + money
                Atm.atm_money = Atm.atm_money + money
            else:
                print("Ошибка.Средства не внесены")
        else:
            print("Неверный пин")

class Get_money():
    def get_money(self, Atm, Card, Bank):
        if Card.pin_code == 1488:
            print("Введите необходимую сумму для снятия")
            money = int(input())
            if money <= Atm.atm_money and money <= Bank.card_money:
                print("Выберите подходящие для вас банкноты")
                print(" a ",money//50," * 50"," b ",money//20," * 20"," c ",money//10," * 10")
                choice = str(input())
                if choice == "a" and money % 50 == 0:
                    print("Выдано",money//50,"банкнот(ы)")
                elif choice == "b"and money % 20 == 0:
                    print("Выдано",money//20,"банкнот(ы)")
                elif choice == "c"and money % 10 == 0:
                    print("Выдано",money//10,"банкнот(ы)")
                else:
                    print("Введите кратное значение")
                Bank.card_money = Bank.card_money - money
                Atm.atm_money = Atm.atm_money - money    
            else:
                print("Ошибка.Недостаточно средств на карте/терминале")
                
        else:
            print("Неверный пин")

class Pay_telephone():
    def pay_telephone(self,Telephone,Card,Bank,Atm):
        if Card.pin_code == 1488:
            print("Введите необходимую сумму для пополнения телефона")
            money = int(input())
            if money <= Atm.atm_money and money <= Bank.card_money:
                Bank.card_money = Bank.card_money - money
                Atm.atm_money = Atm.atm_money - money
                Telephone.tel_money = Telephone.tel_money + money
        else:
            print("Ошибка.Недостаточно средств на карте/терминале")
f = open("C:\\Users\\kyrill\\Downloads\\Telegram Desktop\\PPOIS1lab.txt","r+")
l = len(sys.argv)
print("Длина массива аргументов CLI",l)
if l == 1:
    print("Вызов подсказки . Используемые флаги :")
    print("-p Оплата телефона")
    print("-a Внести наличные")
    print("-g Снять наличные")
    print("-d Просмотр остатков кард-счете и хранилища банкнот")

display = Display_values()
get = Get_money()
add = Add_money()
pay = Pay_telephone()
rewrite = Rewrite_values()
read = Read_values()


for i in range(l):
    print(sys.argv[i])
# display.display_values(atm_obj, bank_obj,card_obj,tel_obj)
# get.get_money(atm_obj, card_obj, bank_obj)
# display.display_values(atm_obj, bank_obj,card_obj,tel_obj)
# add.add_money(atm_obj, card_obj, bank_obj)
# display.display_values(atm_obj, bank_obj,card_obj,tel_obj)
# pay.pay_telephone(tel_obj,card_obj,bank_obj,atm_obj)
# display.display_values(atm_obj, bank_obj,card_obj,tel_obj)
# rewrite.rewrite_values(atm_obj,bank_obj,card_obj,tel_obj)


for i in range(l):
    if sys.argv[i] == "-p":
        print("Флаг -p")
        arr =read.read_values()
        atm = arr[0]
        bank = arr[1]
        pin = arr[2]
        card = arr[3]
        tel = arr[4]
        atm_obj = Atm(atm)
        card_obj = Card(pin,card)
        bank_obj = Bank(bank)
        tel_obj = Telephone(tel)
        
        display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
        pay.pay_telephone(tel_obj, card_obj, bank_obj, atm_obj)
        display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
        rewrite.rewrite_values(atm_obj,bank_obj,card_obj,tel_obj)
    elif sys.argv[i] == "-a":
        print("Флаг -a")
        arr =read.read_values()
        atm = arr[0]
        bank = arr[1]
        pin = arr[2]
        card = arr[3]
        tel = arr[4]
        atm_obj = Atm(atm)
        card_obj = Card(pin,card)
        bank_obj = Bank(bank)
        tel_obj = Telephone(tel)
        
        display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
        add.add_money(atm_obj, card_obj, bank_obj)
        display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
        rewrite.rewrite_values(atm_obj,bank_obj,card_obj,tel_obj)
    elif sys.argv[i] == "-d":
        print("Флаг -d")
        arr =read.read_values()
        atm = arr[0]
        bank = arr[1]
        pin = arr[2]
        card = arr[3]
        tel = arr[4]
        atm_obj = Atm(atm)
        card_obj = Card(pin,card)
        bank_obj = Bank(bank)
        tel_obj = Telephone(tel)
        
        print("Остатки на текущий момент")
        display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
        rewrite.rewrite_values(atm_obj,bank_obj,card_obj,tel_obj)
    elif sys.argv[i] == "-g":
        print("Флаг -g")
        f = open("C:\\Users\\kyrill\\Downloads\\Telegram Desktop\\PPOIS1lab.txt","r+")
        arr =read.read_values()
        atm = arr[0]
        bank = arr[1]
        pin = arr[2]
        card = arr[3]
        tel = arr[4]
        atm_obj = Atm(atm)
        card_obj = Card(pin,card)
        bank_obj = Bank(bank)
        tel_obj = Telephone(tel)
        
        display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
        get.get_money(atm_obj, card_obj, bank_obj)
        display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
        rewrite.rewrite_values(atm_obj,bank_obj,card_obj,tel_obj)
    
f.close()
