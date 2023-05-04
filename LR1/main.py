from getNewCreditCard import *


def autorization():
    while True:
        autorized = False
        while not autorized:
            command = input("Log in/ Sign up: ").lower()
            if command == "sign up":
                name = input("Input ur Name: ")
                phoneNumber = input("Input ur phone number: ")
                newUser = registerNewUser(name, phoneNumber)
                atm.UsersList.append(newUser)
                newUser.print()
                autorized = True
            else:
                autorized = True
        while True:
            user = atm.inputCard()
            while True:
                session_ended = get_command(user, atm.UsersList)
                if session_ended:
                    autorized = False
                    break
            if not autorized:
                break


autorization()
