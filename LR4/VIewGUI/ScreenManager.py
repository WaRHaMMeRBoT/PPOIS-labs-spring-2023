from Controller.BankController import BankController
from VIewGUI.MainScreens import StartScreen, AddNewUserScreen, ChooseEntityScreen, PasswordCheckerScreen, ActionDecisionScreen
from VIewGUI.MainScreens import IncreaseBankStorageWithUserStorageScreen, IncreaseBankBillWithUserStorageScreen, IncreaseUserStorageWithBankStorageScreen
from VIewGUI.MainScreens import IncreaseUserPhoneWithBankBillScreen, IncreaseUserStorageWithBankBillScreen, ShowPhoneBillScreen
from VIewGUI.MainScreens import ShowAccountBillScreen, ShowCashStorageScreen, ShowAccountStorageScreen
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager


class BankScreenManagerView(ScreenManager):
    def __init__(self):
        super(BankScreenManagerView, self).__init__()
        self.controller = BankController()
        self.controller.read_from_file()
        self.add_widget(StartScreen())
        self.add_widget(AddNewUserScreen())
        self.choose_entity_screen = ChooseEntityScreen()
        self.add_widget(self.choose_entity_screen)
        self.password_checker_screen = PasswordCheckerScreen()
        self.add_widget(self.password_checker_screen)
        self.add_widget(ActionDecisionScreen())
        self.add_widget(IncreaseBankBillWithUserStorageScreen())
        self.add_widget(IncreaseBankStorageWithUserStorageScreen())
        self.add_widget(IncreaseUserPhoneWithBankBillScreen())
        self.add_widget(IncreaseUserStorageWithBankBillScreen())
        self.add_widget(IncreaseUserStorageWithBankStorageScreen())
        self.show_phone_bill_screen = ShowPhoneBillScreen()
        self.add_widget(self.show_phone_bill_screen)
        self.show_bank_account_bill_screen = ShowAccountBillScreen()
        self.add_widget(self.show_bank_account_bill_screen)
        self.show_cash_storage_screen = ShowCashStorageScreen()
        self.add_widget(self.show_cash_storage_screen)
        self.show_account_storage_screen = ShowAccountStorageScreen()
        self.add_widget(self.show_account_storage_screen)


class MainScreensApp(MDApp):
    def build(self):
        self.bank_screen_manager_view = BankScreenManagerView()
        return self.bank_screen_manager_view

    def on_stop(self):
        super(MainScreensApp, self).on_stop()
        self.bank_screen_manager_view.controller.write_to_file()
