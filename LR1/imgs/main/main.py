from ops import Customer
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
@click.argument('location')
@click.argument('phone_number')
def create_account(admin, first_name, last_name, location, phone_number):
    if admin == 'admin':
        customer.create_account(first_name, last_name, location, phone_number)
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
def balance(password):
    if customer.get_now_status():
        customer.balance(customer.get_now_card_number())
    else:
        print('You need to log in')


@click.command()
@click.argument('password')
def transactions(password):
    if customer.get_now_status():
        customer.transactions(customer.get_now_card_number())
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


cli.add_command(create_account)
cli.add_command(deposit)
cli.add_command(withdrawal)
cli.add_command(balance)
cli.add_command(transactions)
cli.add_command(transfer)
cli.add_command(authorization)
cli.add_command(log_out)


if __name__ == '__main__':
    cli()