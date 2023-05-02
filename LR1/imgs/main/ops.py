import os
import datetime
import random
import string
import csv


class Person:
    cust_profile = open('pers_profile.txt', 'a+')

    def deposit_cash(self, username, deposit_amount):
        filename = username + '.txt'
        if not os.path.exists(filename):
            open(filename, 'w+')
        transactionfilename = username + '_transactionhistory.txt'
        transactionfile = open(transactionfilename, 'a')
        balance = 0
        new_balance = 0
        with open(filename, 'r') as file:
            for i in file:
                balance = float(i)
        with open(filename, 'w+') as file:
            new_balance = str(balance + float(deposit_amount))
            file.write(new_balance)
            print(str(username), ' new balance is:', new_balance)
        transactionfile.write(str(datetime.datetime.now()) + '\nPrevious balance: ' + str(balance)
                                  + '. Deposit amount is:' + str(deposit_amount) + 'New balance:'
                                  + str(new_balance) + '\n')
        file.close()
        transactionfile.close()

    def withdrawal_cash(self, username, withdrawn_amount):
        filename = username + '.txt'
        if not os.path.exists(filename):
            open(filename, 'w+')
        transactionfilename = username + '_transactionhistory.txt'
        transactionfile = open(transactionfilename, 'a')
        balance = 0
        new_balance = 0
        with open(filename, 'r') as file:
            for i in file:
                balance = float(i)
        with open(filename, 'w+') as file:
            if float(withdrawn_amount) > balance:
                print('You have insufficient balance. Your balance is:', balance)
            else:
                new_balance = str(balance - float(withdrawn_amount))
                file.write(new_balance)
                print(str(username), ' new balance is:', new_balance)
                transactionfile.write(str(datetime.datetime.now()) + '\nPrevious balance: ' + str(balance)
                                      + '. Withdrawn amount is:' + str(withdrawn_amount) + 'New balance:'
                                      + str(new_balance) + '\n')
        file.close()
        transactionfile.close()

    def balance(self, username):
        filename = username + '.txt'
        if not os.path.exists(filename):
            open(filename, 'w+')
        file = open(filename, 'r')
        if file.read(1):
            file.seek(0)
            for i in file:
                balance = float(i)
            print('Your balance is:', balance)
        else:
            print('You have no balance left.')
        file.close()

    def transactions(self, username):
        transactionfilename = username + '_transactionhistory.txt'
        if not os.path.exists(transactionfilename):
            open(transactionfilename, 'w+')
        transactionfile = open(transactionfilename, 'r')
        if transactionfile.read(1):
            transactionfile.seek(0)
            print(transactionfile.read())
        else:
            print('There is no transaction history.')
        transactionfile.close()

    def transfer_cash(self, username_from, username_to, transfer_amount):
        file = open(username_from + '.txt', 'r')
        if not os.path.exists(username_from + '.txt'):
            open(file, 'w+')
            balance = 0
        else:
            for i in file:
                balance = float(i)
        if balance >= float(transfer_amount):
            self.withdrawal_cash(username_from, transfer_amount)
            self.deposit_cash(username_to, transfer_amount)
            print('Transfer success')
        else:
            print('There are not enough money on your balance.')
        file.close()

    def random_password(self):
        profiles = self.cust_profile.read()
        password = ''.join(random.choice(string.digits) for x in range(4))
        check = True
        while check:
            check = False
            if password in profiles:
                check = True
                password = ''.join(random.choice(string.digits) for x in range(4))
        return password

    def create_account(self, firstname, lastname, addres, phone_number):
        profiles = self.cust_profile.read()
        username = '425519012624' + ''.join(random.choice(string.digits) for x in range(4))
        check = True
        while check:
            check = False
            if username in profiles:
                check = True
                username = '425519012624' + ''.join(random.choice(string.digits) for x in range(4))
        password = self.random_password()
        time = datetime.datetime.now()
        time = time.replace(year=time.year + 5)
        self.cust_profile.write(username + '\t' + password + '\t' + firstname + '\t' + lastname + '\t' + addres + '\t' + phone_number + '\t' + str(time) + '\n')
        print('Created username: ', username, 'and password is ', password, '\n')

    def authorization(self, username, password):
        check = False
        cust_profile = open('cust_profile.txt', 'r')
        file = open('now_in_process', 'w')
        reader = csv.reader(cust_profile)
        allLines = [line for line in reader]
        for line in allLines:
            if str(username) in ''.join(line) and str(password) in ''.join(line):
                if datetime.datetime.strptime(''.join(line[0][-26:]), '%Y-%m-%d %H:%M:%S.%f') > datetime.datetime.now():
                    file.write('True\n' + username)
                    check = True
                else:
                    check = True
                    print('Your card is no longer valid, contact the bank.')
        if not check:
            print('Incorrect input')

    def get_now_status(self):
        file = open('now_in_process', 'r')
        line = file.read()
        if os.stat('now_in_process').st_size == 0:
            return False
        return bool(line.split('\n')[0])

    def get_now_card_number(self):
        file = open('now_in_process', 'r')
        line = file.read()
        return str(line.split('\n')[1])