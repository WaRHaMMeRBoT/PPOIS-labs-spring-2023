import Currency
import dataControl
from ATM import *

atm = Atm()
atm.balance.dollars = 100
atm.balance.euros = 500
atm.balance.rubles = 10000
currencies = Currency.currency_value()


def get_balance_card(card):  # Получить баланс карточки
    print(f"Balance: {card.balance}")


def get_balance_phone(phone):  # Получить баланс телефона
    print(f"Balance: {phone.balance}₽")


def supply_mobile_balance(card, cash, phone):  # Пополнить баланс телефона
    card.balance.rubles -= cash
    phone.balance += cash
    print(f"Payment No. {phone.number} amount {cash}₽")


def get_cash(user, card, cash, currency):  # Снять наличку
    if currency == "$":
        user.balance.dollars += cash
        card.balance.dollars -= cash
    elif currency == "€":
        user.balance.euros += cash
        card.balance.euros -= cash
    elif currency == "₽":
        user.balance.rubles += cash
        card.balance.rubles -= cash


def supply_balance_by_cash(user, card, cash, currency):  # Пополнить баланс карточки
    get_cash(user, card, -cash, currency)
    print(f"Payment No.{card.cardNumber} amount {cash}" + currency)


def get_user_info(user):  # Получить информацию авторизовавшегося пользователя
    user.print()


def change_pin(user, PIN):  # Функция по измене пин-кода
    user.card.PIN = PIN


def exchanging_currency(
    wallet, cash, first_currency, second_currency, way_to_exchange, currency
):
    print(cash)
    if currency == "eurusd":
        if first_currency == "€" and second_currency == "$":
            wallet.balance.euros -= cash
            wallet.balance.dollars += round(
                cash * round(currencies.get_cost_pair(currency, way_to_exchange), 2), 2
            )

        elif first_currency == "$" and second_currency == "€":
            wallet.balance.dollars -= cash
            wallet.balance.euros += round(
                cash * round(currencies.get_cost_pair(currency, way_to_exchange), 2), 2
            )

    elif currency == "eurrub":
        if first_currency == "€" and second_currency == "₽":
            wallet.balance.euros -= cash
            wallet.balance.rubles += round(
                cash
                * round(currencies.get_cost_pair(currency, way_to_exchange), 2)
                / 10,
                2,
            )

        elif first_currency == "₽" and second_currency == "€":
            wallet.balance.rubles -= cash
            wallet.balance.euros += round(
                cash
                * round(currencies.get_cost_pair(currency, way_to_exchange), 2)
                / 1000,
                2,
            )

    elif currency == "usdrub":
        if first_currency == "$" and second_currency == "₽":
            wallet.balance.dollars -= cash
            wallet.balance.rubles += round(
                cash
                * round(currencies.get_cost_pair(currency, way_to_exchange), 2)
                / 10,
                2,
            )

        elif first_currency == "₽" and second_currency == "$":
            wallet.balance.rubles -= cash
            wallet.balance.dollars += round(
                cash
                * round(currencies.get_cost_pair(currency, way_to_exchange), 2)
                / 1000,
                2,
            )


def exchange_currency(wallet, currency):  # Обмен валют
    money_for_exchange = float(input("Input amount of money for exchange: "))
    buy_sell = input("Choose buy/sell: ").lower()
    way_to_exchange = False
    if buy_sell == "sell":
        way_to_exchange = True
    first_currency, second_currency = Currency.get_currencies_sighns(
        currency, way_to_exchange
    )
    if first_currency == "€" and second_currency == "$":
        if money_for_exchange <= wallet.balance.euros:
            exchanging_currency(
                wallet,
                money_for_exchange,
                first_currency,
                second_currency,
                way_to_exchange,
                currency,
            )
        else:
            print("Not enough money")
    elif first_currency == "$" and second_currency == "€":
        if money_for_exchange <= wallet.balance.dollars:
            exchanging_currency(
                wallet,
                money_for_exchange,
                first_currency,
                second_currency,
                way_to_exchange,
                currency,
            )
        else:
            print("Not enough money")
    elif first_currency == "€" and second_currency == "₽":
        if money_for_exchange <= wallet.balance.euros:
            exchanging_currency(
                wallet,
                money_for_exchange,
                first_currency,
                second_currency,
                way_to_exchange,
                currency,
            )
        else:
            print("Not enough money")
    elif first_currency == "₽" and second_currency == "€":
        if money_for_exchange <= wallet.balance.rubles:
            exchanging_currency(
                wallet,
                money_for_exchange,
                first_currency,
                second_currency,
                way_to_exchange,
                currency,
            )
        else:
            print("Not enough money")
    elif first_currency == "$" and second_currency == "₽":
        if money_for_exchange <= wallet.balance.dollars:
            exchanging_currency(
                wallet,
                money_for_exchange,
                first_currency,
                second_currency,
                way_to_exchange,
                currency,
            )
        else:
            print("Not enough money")
    else:
        if money_for_exchange <= wallet.balance.rubles:
            exchanging_currency(
                wallet,
                money_for_exchange,
                first_currency,
                second_currency,
                way_to_exchange,
                currency,
            )
        else:
            print("Not enough money")


def update_data_base(userlist):
    dataControl.write(userlist, "dataBase.json")
    exit(0)


def exit_atm(userlist):
    update_data_base(userlist)


def get_atm_balance():
    print(atm.balance)


def get_command(user, userlist):  # Обработка входимых команд
    command = input().lower()
    if command == "get_balance_card":
        get_balance_card(user.card)
    elif command == "get_balance_phone":
        get_balance_phone(user.phone)
    elif command == "supply_mobile_balance":
        numberMoney = input("Input phone number&money: ").split()
        found = False
        for User in userlist:
            if User.phone.number == numberMoney[0]:
                supply_mobile_balance(user.card, int(numberMoney[1]), User.phone)
                found = True
        if not found:
            print("Number doesnt exist.")
    elif command == "get_cash":
        cash = float(input("Input the amount: "))
        currency = Currency.currency(input("Select currency $€₽: "))
        if cash > Currency.get_wallet(user.card, currency):
            print("Not enough money on your balance")
        else:
            if Currency.get_wallet(atm, currency) < cash:
                print("Not enough money in atm")
            else:
                get_cash(user, user.card, cash, currency)
    elif command == "get_user_info":
        get_user_info(user)
    elif command == "change_pin":
        if user.card.PIN == input("Input ur PIN: "):
            newPin = input("Input newPin: ")
            if newPin == input("Input newPin again: "):
                change_pin(user, newPin)
                print("Pin has been changed")
            else:
                print("wrong input")
        else:
            print("wrong PIN")
    elif command == "supply_balance_by_cash":
        cardNumber_Cash = input("Input cardNumber&amount of money:").split()
        currency = Currency.currency(input("Select currency $€₽: "))
        cardFound = False
        for targetuser in userlist:
            if targetuser.card.cardNumber == cardNumber_Cash[0]:
                cardFound = True
                if Currency.get_wallet(user, currency) >= int(cardNumber_Cash[1]):
                    supply_balance_by_cash(
                        user, targetuser.card, int(cardNumber_Cash[1]), currency
                    )
                else:
                    print("Not enough cash")
        if not cardFound:
            print(f"The card No.{cardNumber_Cash[0]} doesnt exist")
    elif command == "exchange_currency":
        mthd = input(
            "Select the method u wanna exchange currency wallet, creditcard: "
        ).lower()
        currencyPair = input(
            f"Select the Currency pair\nCurrency pair\tBUY---SELL\nEURUSD: \t{round(currencies.EURUSD*(1+currencies.comission),2)}---{round(currencies.EURUSD/(1+currencies.comission),2)}\nEURRUB: \t{round(currencies.EURRUB*(1+currencies.comission),2)}---{round(currencies.EURRUB/(1+currencies.comission),2)}\nUSDRUB: \t{round(currencies.USDRUB*(1+currencies.comission),2)}---{round(currencies.USDRUB/(1+currencies.comission),2)}\n"
        ).lower()
        if mthd == "wallet":
            exchange_currency(user, currencyPair)
        elif mthd == "creditcard":
            exchange_currency(user.card, currencyPair)
    elif command == "exit_atm":
        exit_atm(userlist)
    elif command == "get_atm_balance":
        get_atm_balance()
    if command == "end_session":
        return True
    else:
        return False
