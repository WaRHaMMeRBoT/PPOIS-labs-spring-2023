import ATM
import Users
import json as j
import click

def checkEffectiveCard(number, Pin, usersDate, assistan):
    S = ""
    control = False
    for i in range(Users.getUsersNum(usersDate)):
        if "***" + number == Users.getUsersCardNum(usersDate, i):
            if control is False:
                control = True
                S = Pin
            if S == Users.getPIN(usersDate, i):
                assistan.clear()
                assistan.append(i+1)
                print("Карта активизирована!")
                return True
            else:
                continue
        else:
            continue

    print("Номер карты не найден или не верный Pin!")
    return False
            
def checkBalance(usersDate, assistan):
    if assistan[0] != -1:
        return int(Users.getBalanc(usersDate, assistan[0] - 1))

def removalMoney(Atm, usersData, assistant, rmoney, count):
    typeOfBanknote = None

    if rmoney == "5Rub":
        typeOfBanknote = 1
    elif rmoney == "10Rub":
        typeOfBanknote = 2
    elif rmoney == "20Rub":
        typeOfBanknote = 3
    elif rmoney == "50Rub":
        typeOfBanknote = 4
    elif rmoney == "100Rub":
        typeOfBanknote = 5
    elif rmoney == "200Rub":
        typeOfBanknote = 6
    elif rmoney == "500Rub":
        typeOfBanknote = 7
    else:
        print("Номинала " + rmoney + " нету в банкомате.")
        exit()

    if ATM.getBanknoteNumb(Atm, typeOfBanknote) >= 1:
        banknotValue = int(count)
        if banknotValue > 0:
            if banknotValue <= ATM.getBanknoteNumb(Atm, typeOfBanknote):
                if banknotValue * ATM.getBanknoteVal(Atm, typeOfBanknote) <= \
                        int(Users.getBalanc(usersData, assistant[0] - 1)):
                    Users.reduceMoney(usersData, assistant[0] - 1,
                                             banknotValue * ATM.getBanknoteVal(Atm, typeOfBanknote))
                    ATM.banknoteReduc(Atm, typeOfBanknote, banknotValue)
                    print("Вы сняли " + str(banknotValue * ATM.getBanknoteVal(Atm, typeOfBanknote))
                          + " Rub.")
                else:
                    print("На вашей карте недостаточно средств!")
            else:
                print("В банкомате отсутствуют " + str(banknotValue) + " купюры!\nДоступны для выдачи " +
                      str(ATM.getBanknoteNumb(Atm, typeOfBanknote)) + " купюры.")
        else:
            print("Введите натуральное число!")
    else:
        print("В банкомате закончился данный вид купюр!")


def phoneMoney(usersData, assistant, phone):
    if int(phone) > 0:
        if int(phone) <= int(Users.getBalanc(usersData, assistant[0] - 1)):
            Users.reduceMoney(usersData, assistant[0] - 1, int(phone))
            print(str(phone) + " Rub зачислено на номер " + Users.getPhoneNum(usersData, assistant[0] - 1))
        else:
            print("На вашем банковском счету недостаточно средств!")
    else:
        print("Введите натуральное число!")

def changeCardNumber(usersData, assistant):
    Users.changeCardNumb(usersData, assistant)


def saveInform(usersData, assistan, Atm):
    jsonfile = open("information.json", "r")
    usersSave = j.load(jsonfile)
    jsonfile.close()

    for users in usersSave["usersInform"]["items"]:
        if users["phoneNumber"] == Users.getPhoneNum(usersData, assistan[0] - 1):
            for key in users:
                users[key] = Users.getUsers(usersData, assistan[0] - 1, key)

    jsonfile = open("information.json", "w+")
    jsonfile.write(j.dumps(usersSave))
    jsonfile.close()

    jsonfile = open("ATM.json", "r")
    atmSave = j.load(jsonfile)
    jsonfile.close()

    i = 1
    for value in atmSave["ATMinfm"]:
        if i == 1:
            atmSave["ATMinfm"][value][0] = str(ATM.getBanknoteNumb(Atm, i))
            i += 1
        elif i == 2:
            atmSave["ATMinfm"][value][0] = str(ATM.getBanknoteNumb(Atm, i))
            i += 1
        elif i == 3:
            atmSave["ATMinfm"][value][0] = str(ATM.getBanknoteNumb(Atm, i))
            i += 1
        elif i == 4:
            atmSave["ATMinfm"][value][0] = str(ATM.getBanknoteNumb(Atm, i))
            i += 1
        elif i == 5:
            atmSave["ATMinfm"][value][0] = str(ATM.getBanknoteNumb(Atm, i))
            i += 1
        elif i == 6:
            atmSave["ATMinfm"][value][0] = str(ATM.getBanknoteNumb(Atm, i))
            i += 1
        elif i == 7:
            atmSave["ATMinfm"][value][0] = str(ATM.getBanknoteNumb(Atm, i))
            i += 1

    jsonfile = open("ATM.json.", "w+")
    jsonfile.write(j.dumps(atmSave))
    jsonfile.close()


def atmCheck(Atm):
    ATM.banknotShow(Atm)


@click.command()
@click.option('--number', help="Number of card")
@click.option('--pin', help="pin of card")
@click.option('--balance')
@click.option('--rmoney')
@click.option('--count', default=1)
@click.option('--phone')
@click.option('--new')
@click.option('--atm')
def beginATM(number, pin, balance, phone, rmoney, count, new, atm):
    assistant = [-1]
    Atm = ATM.ATM(number)
    usersData = Users.Users()

    if number and pin:
        if checkEffectiveCard(number, pin, usersData, assistant):
            if balance == "-r":
                print("Баланс:", str(checkBalance(usersData, assistant)) + " Rub")
            if phone:
                phoneMoney(usersData, assistant, phone)
            if rmoney and count:
                removalMoney(Atm, usersData, assistant, rmoney, count)
            if new == "-a":
                changeCardNumber(usersData, assistant[0] - 1)
    else:
        print("Недостаточно данных!")

    if atm == "-s":
        atmCheck(Atm)

    saveInform(usersData, assistant, Atm)



