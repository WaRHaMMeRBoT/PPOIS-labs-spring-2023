import sys
from PPOIS1labClasses import Card
from PPOIS1labClasses import Bank
from PPOIS1labClasses import Telephone
from PPOIS1labClasses import Atm
f = open("C:\\Users\\kyrill\\Documents\\GitHub\\PPOIS_Spring\\Lab 1.1\\PPOIS1lab.txt","r+")
l = len(sys.argv)

class Display_values():

    def display_values(self, Atm, Bank, Card,Telephone):
        
        pin = 1234
        if Card.pin_code == pin:
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
        
        pin = 1234
        if Card.pin_code == pin:
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
        
        pin = 1234
        if pin == 1234:
            print("Чтение из файла")
            array_of_values = f.readlines()
            array_of_values = list(map(int,array_of_values))
            print(array_of_values)
        else:
            print("Неверный пин")

        return array_of_values

class Add_money():
    def add_money(self, Atm, Card, Bank):
        print("Введите Пин-Код :")
        pin = int(input())
        if Card.pin_code == pin:
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
        print("Введите Пин-Код :")
        pin = int(input())
        if Card.pin_code == pin:
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
        print("Введите Пин-Код :")
        pin = int(input())
        if Card.pin_code == pin:
            print("Введите необходимую сумму для пополнения телефона")
            money = int(input())
            if money <= Atm.atm_money and money <= Bank.card_money:
                Bank.card_money = Bank.card_money - money
                Atm.atm_money = Atm.atm_money - money
                Telephone.tel_money = Telephone.tel_money + money
        else:
            print("Ошибка.Недостаточно средств на карте/терминале")

class Flag_Reader():
    def flag_reader(self,Card):
        print("Проверка карты")

        # if Card.card_number != 0 and Card.pin_code != 0:
        for flag in sys.stdin:
            print(flag)
            flag = flag.rstrip()
            if flag == "-pay_tel":
                print("Флаг -pay_tel")
                display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
                pay.pay_telephone(tel_obj, card_obj, bank_obj, atm_obj)
                display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
                rewrite.rewrite_values(atm_obj,bank_obj,card_obj,tel_obj)
            elif flag == "-add_money":
                print("Флаг -add_money")
                display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
                add.add_money(atm_obj, card_obj, bank_obj)
                display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
                rewrite.rewrite_values(atm_obj,bank_obj,card_obj,tel_obj)
            elif flag == "-display_balance":
                print("Флаг -display_balance")

                print("Остатки на текущий момент")
                display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
                rewrite.rewrite_values(atm_obj,bank_obj,card_obj,tel_obj)
            elif flag == "-get_money":
                print("Флаг -get_money")
                display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
                get.get_money(atm_obj, card_obj, bank_obj)
                display.display_values(atm_obj, bank_obj, card_obj, tel_obj)
                rewrite.rewrite_values(atm_obj,bank_obj,card_obj,tel_obj)
            elif flag == "-quit":
                break
            else:
                print("Ошибка чтения")
read_flag = Flag_Reader()
display = Display_values()
get = Get_money()
add = Add_money()
pay = Pay_telephone()
rewrite = Rewrite_values()
read = Read_values()
arr = read.read_values()
atm = arr[0]
bank = arr[1]
pin = arr[2]
card = arr[3]
tel = arr[4]
atm_obj = Atm(atm)
card_obj = Card(pin,card)
bank_obj = Bank(bank)
tel_obj = Telephone(tel)


if l == 1:
    print("Вызов подсказки . Используемые флаги :")
    print("-pay_tel Оплата телефона")
    print("-add_money Внести наличные")
    print("-get_money Снять наличные")
    print("-display_balance Просмотр остатков кард-счета и хранилища банкнот")
    print("-quit Остановка работы консольного режима")



