from ATM_Operations import Customer
import click


customer = Customer()


@click.group()
def cli():
    pass


@click.command()
@click.argument('username')
@click.argument('password')
def authorization(username, password):
    customer.authorization(username, password)


@click.command()
@click.argument('password')
@click.argument('deposit_amount')
def deposit(password, deposit_amount):
    if customer.get_now_status():
        customer.deposit_cash(customer.get_now_card_number(), deposit_amount)
    else:
        print('You need to log in')


@click.command()
@click.argument('admin')
@click.argument('first_name')
@click.argument('last_name')
@click.argument('address')
@click.argument('phone_number')
def create_account(admin, first_name, last_name, address, phone_number):
    if admin == 'admin':
        customer.create_account(first_name, last_name, address, phone_number)
    else:
        print('Error')


@click.command()
@click.argument('password')
@click.argument('withdrawal_amount')
def withdrawal(password, withdrawal_amount):
    if customer.get_now_status():
        customer.withdrawal_cash(customer.get_now_card_number(), withdrawal_amount)
    else:
        print('You need to log in')


@click.command()
@click.argument('password')
def check_balance(password):
    if customer.get_now_status():
        customer.balance(customer.get_now_card_number())
    else:
        print('You need to log in')


@click.command()
@click.argument('password')
def check_transaction_history(password):
    if customer.get_now_status():
        customer.check_transaction_history(customer.get_now_card_number())
    else:
        print('You need to log in')


@click.command()
@click.argument('password')
@click.argument('username_to')
@click.argument('transfer_amount')
def transfer(password, username_to, transfer_amount):
    if customer.get_now_status():
        customer.transfer_cash(customer.get_now_card_number(), username_to, transfer_amount)
    else:
        print('You need to log in')


@click.command()
@click.argument('password')
@click.argument('phone_number')
@click.argument('transfer_amount')
def transfer_by_phone(password, phone_number, transfer_amount):
    if customer.get_now_status():
        customer.transfer_by_phone(customer.get_now_card_number(), phone_number, transfer_amount)
    else:
        print('You need to log in')


@click.command()
def log_out():
    customer.log_out()


cli.add_command(create_account)
cli.add_command(deposit)
cli.add_command(withdrawal)
cli.add_command(check_balance)
cli.add_command(check_transaction_history)
cli.add_command(transfer)
cli.add_command(transfer_by_phone)
cli.add_command(authorization)
cli.add_command(log_out)


if __name__ == '__main__':
    cli()
