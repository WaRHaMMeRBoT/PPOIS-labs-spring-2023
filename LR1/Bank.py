from dataControl import *
import UsersList


class Bank:
    __bankName = "Belarusbank"

    def __init__(self):
        self.__Users = []

    @property
    def Users(self):
        return self.__Users

    @Users.setter
    def Users(self, Users):
        self.__Users = Users
