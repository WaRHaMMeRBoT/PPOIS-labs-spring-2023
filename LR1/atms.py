import users
import sys
import exception as e

def list_to_int(lst:list):
    """ Converts list to list of int """
    for i in range(len(lst)):
        lst[i]=int(lst[i])

class Atm():
    """ Basic class for ATM """
    def __get_card(self, card_number:int):
        """ This method takes a users card number """
        self.card_number = card_number
        return True

    def give_card(self):
        """ This method returns a users card number """
        self.buf_card = None
        return True

    def give_money(self, amount:int):
        """ This method allows withdraw money from your card """
        index_number = e.Ex_n.ex_index(e.Ex_n,self.cards_numbers, self.card_number)

        if self.cards_amounts[index_number] >= amount: # if you have enough money
            if sum(self.storage) >= amount:
                self.cards_amounts[index_number] -= amount # withdrawal of money
                print('Your cash is ready\n', *self.find_sum(amount))
                return amount
            else:
                print('Sorry, we do not have enough funds')
        else:  # if you have not enough money
            print('Sorry, insufficient funds\n')
            return 0

    def check(self, pin:int, value:str): 
        """ This method allows check your pincode"""
        print("You are welcome\n")

        if self.__get_card(value):
            index_pin = e.Ex_p.ex_index(e.Ex_p, self.cards_pins, pin)
            index_number = e.Ex_n.ex_index(e.Ex_n, self.cards_numbers, self.card_number)
            if index_pin == index_number: # if your pin is right
                   print('Your pin is correct\n')
                   return True
            else:  # if your pin is not right
                   print('Your pin isnt correct\n')
                   return False

    def transfer(self, amount:int, receiver:int):
        """ This method allows transfer money from your card to another """
        index_from = e.Ex_n.ex_index(e.Ex_n, self.cards_numbers, self.card_number)
        index_to = e.Ex_n.ex_index(e.Ex_n, self.cards_numbers, receiver)

        if self.cards_amounts[index_from] >= amount:# if you have enough money
            self.cards_amounts[index_from] -= amount  # withdrawal of money
            self.cards_amounts[index_to] += amount
            print('Funds transferred\n')
        else: # if you have not enough money
            print('Sorry, insufficient funds\n')
        return True

    def __init__(self, file_name:str):
        """ The constructor of atm """
        self.card_number:int = 0 
        self.cards_amounts:list = []
        self.cards_numbers:list = []
        self.cards_pins:list = []
        self.storage:list = []
        self.read_file(file_name) # reading a file
   
    def printf(self):
        """ Overloading print """
        print(*self.cards_amounts, sep = ', ')
        print(*self.cards_numbers, sep = ', ')
        print(*self.cards_pins, sep = ', ')
        print(*self.storage, sep = ', ')

    def check_balance(self, flag:bool=1):
        """ This method shows the balance og your card """
        if flag: # if you wanna see a message about balance
            print('Your balance: ', end = '')
            index_number = e.Ex_n.ex_index(e.Ex_n, self.cards_numbers, self.card_number)
            print(self.cards_amounts[index_number], '\n')
        return self.cards_amounts[index_number]

    def save(self, file_atm:str):
        """ This method rewrites database of the atm"""
        with open(file_atm, 'w') as file:   # rewrite every list
             self.write_list(self.cards_amounts, file)
             self.write_list(self.cards_numbers, file)
             self.write_list(self.cards_pins, file)
             self.write_list(self.storage, file)

    def read_file(self, file_name:str):
        """ This method fills database of the atm """
        with open(file_name, 'r') as file:  # fill every list
            self.cards_amounts = self.read_list(self.cards_amounts, file)
            self.cards_numbers = self.read_list(self.cards_numbers, file)
            self.cards_pins = self.read_list(self.cards_pins, file)
            self.storage = self.read_list(self.storage, file)
             
    def write_list(self, lst:list, file):
        """ This method rewrites a list """
        for i in range(len(lst)):
            if i < len(lst)-1:
                lst[i]=str(lst[i])
                file.write(lst[i]+' ')
            else:
                lst[i]=str(lst[i])
                file.write(lst[i])
        file.write('\n')

    def read_list(self, lst:list, file):
        """ This method fills a list as an int"""
        lst = file.readline().replace("\n",'').split(' ')
        list_to_int(lst)

        return lst

    def find_sum(self, amount:int):
        """ Find necessary banknotes """
        buf:list = [0]
        while amount > 0:
            for index in range(len(self.storage)-1,-1,-1):
                if amount >= self.storage[index]:
                    buf.append(self.storage[index])
                    amount -= self.storage[index]
                    self.storage.remove(self.storage[index])
                    break
            
        return buf
