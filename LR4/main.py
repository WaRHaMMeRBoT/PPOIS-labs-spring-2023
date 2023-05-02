import os
import sys
import logMenu
import Commands
from ui_interface import *

from Custom_Widgets.Widgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


atm = Commands.Atm()  # UserList and atmbalance


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.currency = Commands.Currency.currency_value()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        self.ui.homeBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        )
        self.ui.creditCardBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.creditCardPage)
        )
        self.ui.exchangeCurrencyBtn.clicked.connect(
            lambda: self.exchangeCurrencyWindow()
        )
        self.ui.supplyMobilePhoneBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.supplyMobilePhone)
        )
        self.ui.cashBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cashPage)
        )
        self.ui.logOutBtn.clicked.connect(lambda: self.logOut())
        self.ui.usdeurValue.setText(str(round(1 / self.currency.EURUSD, 3)))
        self.ui.usdrubValue.setText(str(self.currency.USDRUB))
        self.ui.eurrubValue.setText(str(self.currency.EURRUB))
        """Логика операци: перевод на карту, обменник и пополнение телефона"""
        self.ui.transactionCard.clicked.connect(
            lambda: self.transactionCard()
        )  # перевод на карту
        self.ui.exchangeCurrency.clicked.connect(
            lambda: self.exchangeCurrency()
        )  # обмен валюты
        self.ui.supplyMobileBalance.clicked.connect(
            lambda: self.supplyMobileBalance()
        )  # пополнить баланс телефонв
        self.ui.getCashButton.clicked.connect(lambda: self.getCash())
        self.show()

    def exchangeCurrencyWindow(self):
        self.ui.dateForCurrencyExchange.setDateTime(QDateTime.currentDateTime())
        self.ui.stackedWidget.setCurrentWidget(self.ui.exchangeCurrencyPage)

    def logOut(self):
        Commands.dataControl.write(atm.UsersList, "dataBase.json")
        self.close()
        self = LogWindow()

    def transactionCard(self):
        cardReciever = self.ui.cardNumberReciever.text().replace(" ", "")
        cvv = self.ui.cvvCodeInput.text()
        amount = self.ui.amountTransaction.text()
        if not len(cvv):
            return
        if not len(amount):
            return
        choice = self.ui.currencyChoice.currentIndex()  # 0-ruble, 1-dollar, 2-euro
        amount = float(amount)
        if self.user.card.CVV != int(cvv):
            return
        if choice == 0:
            if amount > self.user.card.balance.rubles:
                return
        if choice == 2:
            if amount > self.user.card.balance.dollars:
                return
        if choice == 3:
            if amount > self.user.card.balance.euros:
                return
        for user in atm.UsersList:
            if user.card.cardNumber == cardReciever:
                if choice == 0:
                    user.card.balance.rubles += amount
                    self.user.card.balance.rubles -= amount
                    self.updateBalanceInfo()
                if choice == 1:
                    user.card.balance.dollars += amount
                    self.user.card.balance.dollars -= amount
                    self.updateBalanceInfo()
                if choice == 2:
                    user.card.balance.euros += amount
                    self.user.card.balance.euros -= amount
                    self.updateBalanceInfo()

    def exchangeCurrency(self):
        currencyPairChoice = (
            self.ui.choiceOfCurrencyPairComboBox.currentIndex()
        )  # 0-usdeur, 1-usdrub, 2-eurrub
        choiceOperation = (
            self.ui.choiceOfExchangeComboBox.currentIndex()
        )  # 0-buy, 1-sell
        amoutToExhange = self.ui.amountToExchange.text()
        if not len(amoutToExhange):
            return
        amoutToExhange = float(amoutToExhange)
        if currencyPairChoice == 0:  # usdeur
            if choiceOperation == 0:  # buy
                if amoutToExhange > self.user.card.balance.euros:
                    return
                self.user.card.balance.dollars += round(
                    amoutToExhange * self.currency.get_cost_pair("eurusd", True), 2
                )
                self.user.card.balance.euros -= amoutToExhange
            if choiceOperation == 1:
                if amoutToExhange > self.user.card.balance.dollars:
                    return
                self.user.card.balance.euros += round(
                    amoutToExhange * self.currency.get_cost_pair("eurusd", False), 2
                )
                self.user.card.balance.dollars -= amoutToExhange
        if currencyPairChoice == 1:  # usdrub
            if choiceOperation == 0:
                if amoutToExhange > self.user.card.balance.rubles:
                    return
                self.user.card.balance.dollars += round(
                    amoutToExhange * self.currency.get_cost_pair("usdrub", True), 2
                )
                self.user.card.balance.rubles -= amoutToExhange
            if choiceOperation == 1:
                if amoutToExhange > self.user.card.balance.dollars:
                    return
                self.user.card.balance.rubles += round(
                    amoutToExhange * self.currency.get_cost_pair("usdrub", False), 2
                )
                self.user.card.balance.dollars -= amoutToExhange
        if currencyPairChoice == 2:
            if choiceOperation == 0:
                if amoutToExhange > self.user.card.balance.rubles:
                    return
                self.user.card.balance.euros += round(
                    amoutToExhange * self.currency.get_cost_pair("eurrub", False), 2
                )
                self.user.card.balance.rubles -= amoutToExhange
            if choiceOperation == 1:
                if amoutToExhange > self.user.card.balance.euros:
                    return
                self.user.card.balance.rubles += round(
                    amoutToExhange * self.currency.get_cost_pair("eurrub", True), 2
                )
                self.user.card.balance.euros -= amoutToExhange
        self.updateBalanceInfo()

    def supplyMobileBalance(self):
        numberReciever = self.ui.inputPhoneNumber.text().replace("-", "")
        amount = self.ui.inputAmountToSupplyMobile.text()
        if not len(amount):
            return
        if not len(numberReciever):
            return
        amount = float(amount)
        if amount > self.user.card.balance.rubles:
            return
        for user in atm.UsersList:
            if user.phone.number == numberReciever:
                user.phone.balance += amount
                self.user.card.balance.rubles -= amount
        self.updateBalanceInfo()

    def getCash(self):
        amount = self.ui.inputAmountGetCash.text()
        currencyChoice = self.ui.currencyCashComboBox.currentIndex()
        if not len(amount):
            return
        amount = float(amount)
        if currencyChoice == 0:  # rubles
            if amount > self.user.card.balance.rubles:
                return
            self.user.balance.rubles += amount
            self.user.card.balance.rubles -= amount
        elif currencyChoice == 1:
            if amount > self.user.card.balance.dollars:
                return
            self.user.balance.dollars += amount
            self.user.card.balance.dollars -= amount
        elif currencyChoice == 2:
            if amount > self.user.card.balance.euros:
                return
            self.user.balance.euros += amount
            self.user.card.balance.euros -= amount
        self.updateBalanceInfo()

    def updateBalanceInfo(self):  # для обновления инфы баланса(окошко справа)
        self.ui.cardDollarAmountLabel_2.setText(str(self.user.card.balance.dollars))
        self.ui.cardEuroAmountLabel_2.setText(str(self.user.card.balance.euros))
        self.ui.cardRubleAmountLabel_2.setText(str(self.user.card.balance.rubles))
        self.ui.cashDollarValue.setText(str(self.user.balance.dollars))
        self.ui.cashEuroValue.setText(str(self.user.balance.euros))
        self.ui.cashRubleValue.setText(str(self.user.balance.rubles))
        self.ui.phoneRubleAmountLabel_2.setText(
            "Рубль: " + str(self.user.phone.balance)
        )


class LogWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = logMenu.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.autorization())
        self.show()

    def autorization(self):
        cardNumber = self.ui.lineEdit.text().replace(" ", "")
        PIN = self.ui.lineEdit_2.text()
        for user in atm.UsersList:
            if user.card.cardNumber == cardNumber:
                if user.card.PIN == PIN:
                    self.close()
                    self = MainWindow()
                    self.user = user
                    self.ui.userNameLabelInfo.setText(user.Name)
                    self.ui.phoneNumberInfo.setText(user.phone.number)
                    self.ui.cardNumberInfo.setText(user.card.cardNumber)
                    self.updateBalanceInfo()


########################################################################
## EXECUTE APP
########################################################################
def guiATM():
    app = QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window = LogWindow()
    sys.exit(app.exec_())


guiATM()
