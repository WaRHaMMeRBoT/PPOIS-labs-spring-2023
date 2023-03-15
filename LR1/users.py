
class Card():
    """ Basic class for USERS_CARD """
    card_number:int

    def __init__(self, card_number:int=0):
        self.card_number = card_number

           
class Wallet():
    """ Basic class for USERS_WALLET """
    user_card:Card = None
  
    def __init__(self, number_card:int=0):
        self.user_card = Card(number_card)

    def set_card(self, number_card:int):
        self.user_card = Card(number_card)

    def printf(self):
        print(self.user_card.card_number)
   

class User():
    """ Basic class for USER """
    user_name:str = None
    user_wallet:Wallet = None       

    def __init__(self, file_name:str):
        """ The constructor of user """
        self.read_file(file_name)
        
    def printf(self):
        """ Overloading print """
        print(self.user_name) 
        self.user_wallet.printf()

    def save(self, file_user:str):
        """ This method rewrites database of the user """
        with open(file_user, 'w') as file: 
             file.write(self.user_name)
             file.write('\n')
             file.write(str(self.user_wallet.user_card.card_number))
             file.write('\n')

    def read_file(self, file_name:str):
        """ This method fills database of the user """
        with open(file_name, 'r') as file:
            self.user_name = file.readline().replace("\n", '')
            card_number = int(file.readline().replace("\n", ''))
            self.user_wallet = Wallet(card_number)
