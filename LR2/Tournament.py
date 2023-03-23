class Tournament:
    def __init__(self, tournament_name='', date='', sport_name='', winner_name='', prize_money=0):
        self.__tournament_name = tournament_name
        self.__date = date
        self.__sport_name = sport_name
        self.__winner_name = winner_name
        self.__prize_money = prize_money
        self.__winner_money = 0
        self.set_winner_money()

    @property
    def tournament_name(self):
        return self.__tournament_name
    
    @tournament_name.setter
    def tournament_name(self, tournament_name):
        self.__tournament_name = tournament_name
        
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def sport_name(self):
        return self.__sport_name

    @sport_name.setter
    def sport_name(self, sport_name):
        self.__sport_name = sport_name

    @property
    def winner_name(self):
        return self.__winner_name

    @winner_name.setter
    def winner_name(self, winner_name):
        self.__winner_name = winner_name

    @property
    def winner_money(self):
        return self.__winner_money

    def set_winner_money(self):
        self.__winner_money = int(0.6 * self.__prize_money)

    @property
    def prize_money(self):
        return self.__prize_money

    @prize_money.setter
    def prize_money(self, prize_money):
        self.__prize_money = prize_money
