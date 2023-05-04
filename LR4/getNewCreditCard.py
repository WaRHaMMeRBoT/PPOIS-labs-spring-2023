from Commands import *
import random


def registerNewUser(name, phoneNumber):
    user = User()
    user.Name = name
    user.balance.dollars = 0.0
    user.balance.euros = 0.0
    user.balance.rubles = 0.0
    user.phone.number = phoneNumber
    user.phone.balance = 0.0
    user.phone.OwnersName = name
    user.card.OwnersName = name
    newCreditCard(user)
    return user


def newCreditCard(user):
    for i in range(1, 17):
        user.card.cardNumber += str(random.randint(1, 9))
        if i % 4 == 0:
            user.card.PIN += str(random.randint(1, 9))
    for i in range(1, 4):
        user.card.CVV += str(random.randint(1, 9))
    user.card.ExpiresDate = (
        str(random.randint(1, 12)) + "/" + str(random.randint(24, 28))
    )
    user.card.balance.dollars = 0.0
    user.card.balance.euros = 0.0
    user.card.balance.rubles = 0.0
