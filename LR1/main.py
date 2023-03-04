import click

import cacheMachine


@click.command()
@click.option('--check_account', prompt='Choose what to do ', help='Possible arguments:\n\n'
                                                                   '1 - check account\n\n'
                                                                   '2 - get cache\n\n'
                                                                   '3 - pay phone')
def check(check_account):
    my_machine = cacheMachine.CacheMachine()
    my_machine.get_users_card_number()

    if my_machine.is_verified():
        print('User verified')
    else:
        return
    if check_account == '1':
        my_machine.check_account()
        return
    if check_account == '2':
        a = input('Do you want to check your account? Y/N ')
        if a == 'Y':
            my_machine.check_account()
        if a != 'Y' and a != 'N':
            print('Error \n')
        my_machine.get_cache()
        return
    if check_account == '3':
        a = input('Do you want to check your account? Y/N ')
        if a == 'Y':
            my_machine.check_account()
        if a != 'Y' and a != 'N':
            print('Error \n')
        my_machine.pay_phone()
        return
    print('Error')


if __name__ == "__main__":
    check()
