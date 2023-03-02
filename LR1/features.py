import atmContol
import usersControl
import json as j
import click


def checkActiveNumberCard(number, cvv, userDataBase, idHelper):
    line = ""
    control = False
    for i in range(usersControl.getUserCount(userDataBase)):
        if "**" + number == usersControl.getUserCardNumber(userDataBase, i):
            if control is False:
                control = True
                line = cvv
            if line == usersControl.getCvv(userDataBase, i):
                idHelper.clear()
                idHelper.append(i + 1)
                print("Выполнен вход в аккаунт!")
                return True
            else:
                continue
        else:
            continue

    print("Номер карты не найден или не верный CVV!")
    return False


def checkBalance(userDataBase, idHelper):
    if idHelper[0] != -1:
        return int(usersControl.getBalance(userDataBase, idHelper[0] - 1))


def withdrawlMoney(firstATM, userDataBase, idHelper, wm, count):
    typeOfBanknote = None

    if wm == "5RUB":
        typeOfBanknote = 1
    elif wm == "10RUB":
        typeOfBanknote = 2
    elif wm == "20RUB":
        typeOfBanknote = 3
    elif wm == "50RUB":
        typeOfBanknote = 4
    elif wm == "100RUB":
        typeOfBanknote = 5
    else:
        print("Номинала " + wm + " нету в банкомате.")
        exit()

    if atmContol.getBanknoteNumber(firstATM, typeOfBanknote) >= 1:
        banknotValue = int(count)
        if banknotValue > 0:
            if banknotValue <= atmContol.getBanknoteNumber(firstATM, typeOfBanknote):
                if banknotValue * atmContol.getBanknoteValue(firstATM, typeOfBanknote) <= \
                        int(usersControl.getBalance(userDataBase, idHelper[0] - 1)):
                    usersControl.reduceMoney(userDataBase, idHelper[0] - 1,
                                             banknotValue * atmContol.getBanknoteValue(firstATM, typeOfBanknote))
                    atmContol.banknoteReduce(firstATM, typeOfBanknote, banknotValue)
                    print("Вы получили " + str(banknotValue * atmContol.getBanknoteValue(firstATM, typeOfBanknote))
                          + " RUB наличными.")
                else:
                    print("На вашем банковском счету недостаточно средств!")
            else:
                print("В банкомате нету " + str(banknotValue) + " купюр(-ы)!\nДоступно для выдачи " +
                      str(atmContol.getBanknoteNumber(firstATM, typeOfBanknote)) + " купюр(-ы).")
        else:
            print("Введите натуральное число!")
    else:
        print("В банкомате закончился данный вид купюр!")


def phoneMoney(userDataBase, idHelper, phone):
    if int(phone) > 0:
        if int(phone) <= int(usersControl.getBalance(userDataBase, idHelper[0] - 1)):
            usersControl.reduceMoney(userDataBase, idHelper[0] - 1, int(phone))
            print(str(phone) + " RUB зачислено на номер " + usersControl.getPhoneNumber(userDataBase,
                                                                                        idHelper[0] - 1))
        else:
            print("На вашем банковском счету недостаточно средств!")
    else:
        print("Введите натуральное число!")


def changeCardNumber(userDataBase, idHelper):
    usersControl.changeCardNumber(userDataBase, idHelper)


def saveData(userDataBase, idHelper, firstATM):
    jsonFile = open("dataBase.json", "r")
    userSave = j.load(jsonFile)
    jsonFile.close()

    for user in userSave["userData"]["items"]:
        if user["ID"] == usersControl.getId(userDataBase, idHelper[0] - 1):
            for key in user:
                user[key] = usersControl.getUserData(userDataBase, idHelper[0] - 1, key)

    jsonFile = open("dataBase.json", "w+")
    jsonFile.write(j.dumps(userSave))
    jsonFile.close()

    jsonFile = open("atmDataBase.json", "r")
    atmSave = j.load(jsonFile)
    jsonFile.close()

    i = 1
    for value in atmSave["atmData"]:
        if i == 1:
            atmSave["atmData"][value][0] = str(atmContol.getBanknoteNumber(firstATM, i))
            i += 1
        elif i == 2:
            atmSave["atmData"][value][0] = str(atmContol.getBanknoteNumber(firstATM, i))
            i += 1
        elif i == 3:
            atmSave["atmData"][value][0] = str(atmContol.getBanknoteNumber(firstATM, i))
            i += 1
        elif i == 4:
            atmSave["atmData"][value][0] = str(atmContol.getBanknoteNumber(firstATM, i))
            i += 1
        elif i == 5:
            atmSave["atmData"][value][0] = str(atmContol.getBanknoteNumber(firstATM, i))
            i += 1

    jsonFile = open("atmDataBase.json.", "w+")
    jsonFile.write(j.dumps(atmSave))
    jsonFile.close()


def atmCheck(firstATM):
    atmContol.banknoteShow(firstATM)


@click.command()
@click.option('--number', help="Number or card")
@click.option('--cvv', help="Cvv of card")
@click.option('--balance')
@click.option('--wm')
@click.option('--count', default=1)
@click.option('--phone')
@click.option('--new')
@click.option('--atm')
def startATM(number, cvv, balance, phone, wm, count, new, atm):
    idHelper = [-1]
    firstATM = atmContol.ATM(number)
    userDataBase = usersControl.User()

    if number and cvv:
        if checkActiveNumberCard(number, cvv, userDataBase, idHelper):
            if balance == "-s":
                print("Баланс:", str(checkBalance(userDataBase, idHelper)) + " RUB")
            if phone:
                phoneMoney(userDataBase, idHelper, phone)
            if wm and count:
                withdrawlMoney(firstATM, userDataBase, idHelper, wm, count)
            if new == "-r":
                changeCardNumber(userDataBase, idHelper[0] - 1)
    else:
        print("Недостаточно данных!")

    if atm == "-s":
        atmCheck(firstATM)

    saveData(userDataBase, idHelper, firstATM)
