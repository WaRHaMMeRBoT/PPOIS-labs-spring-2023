import PySimpleGUI as sg
import click

import cacheMachine
import windows as w

console = False


@click.command()
@click.option('--check_account', prompt='Choose what to do', help='Possible arguments:\n\n'
                                                                  '1 - check account\n\n'
                                                                  '2 - get cache\n\n'
                                                                  '3 - pay phone')
def check(check_account):
    my_machine = cacheMachine.CacheMachine(console)

    if check_account == '1':
        card = input("Enter card number: ")
        pin = input("Enter pin: ")
        my_machine.check_account(card, pin)
        return
    if check_account == '2':
        a = input('Do you want to check your account? Y/N ')
        if a == 'Y':
            card = input("Enter card number: ")
            pin = input("Enter pin: ")
            my_machine.check_account(card, pin)
        if a != 'Y' and a != 'N':
            print('Error \n')
        card = input("Enter card number: ")
        pin = input("Enter pin: ")
        my_machine.get_cache(card, pin)
        return
    if check_account == '3':
        a = input('Do you want to check your account? Y/N ')
        if a == 'Y':
            card = input("Enter card number: ")
            pin = input("Enter pin: ")
            my_machine.check_account(card, pin)
        if a != 'Y' and a != 'N':
            print('Error \n')
        card = input("Enter card number: ")
        pin = input("Enter pin: ")
        my_machine.pay_phone(card, pin)
        return
    print('Error')


def main():
    my_machine = cacheMachine.CacheMachine(console)

    button_check = sg.Button(button_text="Check", key='-check_account-')
    button_get = sg.Button(button_text="Get Cache", key='-get_cache-')
    button_pay = sg.Button(button_text="Pay Phone", key='-pay_phone-')
    layout = [[button_check, button_get, button_pay]]
    window = sg.Window("Find", layout, size=(250, 90), resizable=True)

    while True:
        event, values = window.read()

        if event == "-check_account-":
            card, pin = w.verify()
            my_machine.get_users_card_number(card, pin)
            my_machine.check_account(card, pin)

        if event == "-get_cache-":
            card, pin = w.verify()
            my_machine.get_users_card_number(card, pin)
            my_machine.get_cache(card, pin)

        if event == "-pay_phone-":
            card, pin = w.verify()
            my_machine.get_users_card_number(card, pin)
            my_machine.pay_phone(card, pin)

        if event == sg.WIN_CLOSED:
            return False


if __name__ == "__main__":
    if console:
        check()
    else:
        main()
