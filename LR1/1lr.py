import atms
import click
import users

@click.command()
@click.option('-u','usr', required=True, help='File for users information [file]')
@click.option('-d', 'database', required=True, help='File for atms database [file]')
@click.option('--card-number', prompt=True, help = "Your cards number [card number]")
@click.option('--password', prompt=True, hide_input = True, help='Enter your password [password]')
@click.option('-get', 'amount', default=0, help='Withdrawal of money [amount]')
@click.option('-to', nargs=2, default=(0, 0), help='Transfer money [card number and amount]')
@click.option('-check/-no-check', default=False, help='Check your balance [None]')
def main(usr, database, password, card_number, amount, to, check):
    atm = atms.Atm(database)
    user = users.User(usr)

    if atm.check(int(password),int(card_number)):  
        if amount:
             atm.give_money(int(amount))
        if int(to[0]) and int(to[1]):
             atm.transfer(int(to[1]), int(to[0]))
        if check:
            atm.check_balance()
        atm.save(database)
        user.save(usr)
    
if __name__ == '__main__':
    main()


