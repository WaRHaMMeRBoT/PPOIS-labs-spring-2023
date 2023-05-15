from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from Model.BankComponents.BanknotesStorage import BANKNOTES_DENOMINATIONS


class DenominationInputComponent(BoxLayout):
    def get_input_data(self):
        return [self.ids["input_{}".format(index + 1)].text for index in range(len(self.ids))]

    def clear_input_data(self):
        for index in range(len(self.ids)):
            self.ids["input_{}".format(index + 1)].text = ""


class StartScreen(Screen):
    def set_dialog_to_default(self):
        self.ids.dialog_window.text = "Dialog Window"

    def set_dialog_to_unauthorized(self):
        self.ids.dialog_window.text = "Unauthorized"

    def on_add_new_user_press(self):
        self.manager.current = "AddNewUserScreen"
        self.set_dialog_to_default()

    def on_work_with_existing_users_press(self):
        self.manager.choose_entity_screen.refresh_name_table_data()
        self.manager.current = "ChooseEntityScreen"
        self.set_dialog_to_default()

    def on_last_authorized_press(self):
        if self.manager.controller.get_authorized():
            self.set_dialog_to_default()
            self.manager.current = "ActionDecisionScreen"
        else:
            self.set_dialog_to_unauthorized()


class AddNewUserScreen(Screen):
    banknotes_denominations = [str(denomination) for denomination in BANKNOTES_DENOMINATIONS]

    def clear_info(self):
        self.ids.name_input.text = ""
        self.ids.bank_bill_input.text = ""
        self.ids.user_phone_bill_input.text = ""
        self.ids.card_password_input.text = ""
        self.ids.dialog_window.text = "Dialog Window"
        self.ids.bank_storage_input.clear_input_data()
        self.ids.user_storage_input.clear_input_data()

    def on_apply_information_press(self):
        self.ids.dialog_window.text = self.manager.controller.add_user_account_entity_validated(
                                                                  self.ids.name_input.text,
                                                                  self.ids.bank_storage_input.get_input_data(),
                                                                  self.ids.user_storage_input.get_input_data(),
                                                                  self.ids.bank_bill_input.text,
                                                                  self.ids.user_phone_bill_input.text,
                                                                  self.ids.card_password_input.text)

    def on_back_press(self):
        self.clear_info()
        self.manager.current = "StartScreen"


class ChooseEntityScreen(Screen):
    def __init__(self):
        super(ChooseEntityScreen, self).__init__()
        main_grid = GridLayout(cols=1)
        self.name = "ChooseEntityScreen"
        self.name_table = MDDataTable(
            use_pagination=True,
            column_data=[
                ("No.", dp(60)),
                ("Name", dp(400)),
            ])
        back_button = Button(text="Back",
                             size_hint=(1, .1))
        self.name_table.bind(on_row_press=self.on_row_press)
        back_button.bind(on_press=self.on_back_press)
        main_grid.add_widget(self.name_table)
        main_grid.add_widget(back_button)
        self.add_widget(main_grid)

    def refresh_name_table_data(self):
        new_usernames = self.manager.controller.get_usernames()
        self.name_table.row_data = [(str(new_usernames.index(username) + 1), username) for username in new_usernames]

    def on_row_press(self, instance_table, instance_row):
        self.manager.controller.set_current_working_entity_validated(int(instance_row.index / 2) + 1)
        self.manager.password_checker_screen.start_working_call()
        self.manager.current = "PasswordCheckerScreen"

    def on_back_press(self,
                      instance):
        self.manager.current = "StartScreen"


class PasswordCheckerScreen(Screen):
    def refresh_attempts_amount(self):
        self.ids.attempts_amount.text = "Attempts remain: " + str(self.manager.controller.get_amount_of_attempts())

    def clear_input(self):
        self.ids.password_input.text = ""

    def clear_dialog_window(self):
        self.ids.dialog_window.text = "Dialog Window"

    def refresh_buttons_state(self):
        if self.ids.dialog_window.text == "Blocked":
            self.ids.apply_button.disabled = True
            self.ids.bank_call_button.disabled = True
        elif self.manager.controller.get_amount_of_attempts() == 0:
            self.ids.apply_button.disabled = True
            self.ids.bank_call_button.disabled = False
        else:
            self.ids.apply_button.disabled = False
            self.ids.bank_call_button.disabled = True

    def start_working_call(self):
        self.refresh_attempts_amount()
        self.clear_input()
        self.clear_dialog_window()
        self.refresh_buttons_state()

    def on_apply_password_press(self):
        answer = self.manager.controller.password_checker(self.ids.password_input.text)
        if answer == "Correct":
            self.manager.current = "ActionDecisionScreen"
        elif answer == "Blocked":
            self.ids.dialog_window.text = "Blocked"
            self.refresh_buttons_state()
            self.clear_input()
        else:
            self.ids.dialog_window.text = answer
            self.refresh_attempts_amount()
            self.clear_input()
            self.refresh_buttons_state()

    def on_bank_call_press(self):
        self.manager.controller.bank_call()
        self.refresh_attempts_amount()
        self.refresh_buttons_state()

    def on_back_press(self):
        self.manager.current = "StartScreen"


class ActionDecisionScreen(Screen):
    def switch_const_screen(self,
                            name):
        self.manager.current = name + "Screen"

    def show_phone_bill(self):
        self.manager.show_phone_bill_screen.refresh_bill_output()
        self.manager.current = "ShowPhoneBillScreen"

    def show_bank_account_bill(self):
        self.manager.show_bank_account_bill_screen.refresh_bill_output()
        self.manager.current = "ShowAccountBillScreen"

    def show_cash_storage(self):
        self.manager.show_cash_storage_screen.refresh_storage_output()
        self.manager.current = "ShowCashStorageScreen"

    def show_account_storage(self):
        self.manager.show_account_storage_screen.refresh_storage_output()
        self.manager.current = "ShowAccountStorageScreen"


class IncreaseInstanceWithStorageTemplate(Screen):
    banknotes_denominations = [str(denomination) for denomination in BANKNOTES_DENOMINATIONS]
    action_message = None

    def clear_dialog_window(self):
        self.ids.dialog_window.text = "Dialog Window"

    def screen_action(self):
        pass

    def on_action_press(self):
        self.ids.dialog_window.text = self.screen_action()

    def on_back_press(self):
        self.ids.storage_input.clear_input_data()
        self.clear_dialog_window()
        self.manager.current = "ActionDecisionScreen"


class IncreaseInstanceWithBillTemplate(Screen):
    action_message = None

    def clear_bill_input(self):
        self.ids.bill_input.text = ""

    def clear_dialog_window(self):
        self.ids.dialog_window.text = "Dialog Window"

    def screen_action(self):
        pass

    def on_action_press(self):
        self.ids.dialog_window.text = self.screen_action()

    def on_back_press(self):
        self.clear_bill_input()
        self.clear_dialog_window()
        self.manager.current = "ActionDecisionScreen"


class IncreaseBankStorageWithUserStorageScreen(IncreaseInstanceWithStorageTemplate):
    action_message = "Enter Amounts to Increase Account Storage"
    name = "IncreaseBankStorageWithUserStorageScreen"

    def screen_action(self):
        return self.manager.controller.increase_bank_storage_with_user_storage_validated(self.ids.storage_input.get_input_data())


class IncreaseBankBillWithUserStorageScreen(IncreaseInstanceWithStorageTemplate):
    action_message = "Enter Amounts to Increase Account Bill"
    name = "IncreaseBankBillWithUserStorageScreen"

    def screen_action(self):
        return self.manager.controller.increase_bank_bill_with_user_storage_validated(self.ids.storage_input.get_input_data())


class IncreaseUserStorageWithBankStorageScreen(IncreaseInstanceWithStorageTemplate):
    action_message = "Enter Amounts to Increase User Cash"
    name = "IncreaseUserStorageWithBankStorageScreen"

    def screen_action(self):
        return self.manager.controller.increase_user_storage_with_bank_storage_validated(self.ids.storage_input.get_input_data())


class IncreaseUserPhoneWithBankBillScreen(IncreaseInstanceWithBillTemplate):
    action_message = "Enter Account Bill to Increase User Phone Bill"
    name = "IncreaseUserPhoneWithBankBillScreen"

    def screen_action(self):
        return self.manager.controller.increase_user_phone_with_bank_bill_validated(self.ids.bill_input.text)


class IncreaseUserStorageWithBankBillScreen(IncreaseInstanceWithBillTemplate):
    action_message = "Enter Account Bill to Increase User Cash"
    name = "IncreaseUserStorageWithBankBillScreen"

    def screen_action(self):
        return self.manager.controller.increase_user_storage_with_bank_bill_validated(self.ids.bill_input.text)


class ShowBillInstanceTemplate(Screen):
    action_message = None

    def get_bill(self):
        pass

    def refresh_bill_output(self):
        self.ids.bill_output.text = str(self.get_bill())

    def on_back_press(self):
        self.manager.current = "ActionDecisionScreen"


class ShowStorageInstanceTemplate(Screen):
    action_message = None

    def get_storage(self):
        pass

    def refresh_storage_output(self):
        new_storage = self.get_storage()
        denominations = list(new_storage.keys())
        amounts = list(new_storage.values())
        for index in range(len(denominations)):
            self.ids["d_{}".format(index + 1)].text = str(denominations[index])
            self.ids["a_{}".format(index + 1)].text = str(amounts[index])

    def on_back_press(self):
        self.manager.current = "ActionDecisionScreen"


class ShowPhoneBillScreen(ShowBillInstanceTemplate):
    action_message = "Phone Bill"
    name = "ShowPhoneBillScreen"

    def get_bill(self):
        return self.manager.controller.get_user_phone_bill()


class ShowAccountBillScreen(ShowBillInstanceTemplate):
    action_message = "Account Bill"
    name = "ShowAccountBillScreen"

    def get_bill(self):
        return self.manager.controller.get_bank_account_bill()


class ShowCashStorageScreen(ShowStorageInstanceTemplate):
    action_message = "Cash Storage"
    name = "ShowCashStorageScreen"

    def get_storage(self):
        return self.manager.controller.get_user_cash_storage()


class ShowAccountStorageScreen(ShowStorageInstanceTemplate):
    action_message = "Account Storage"
    name = "ShowAccountStorageScreen"

    def get_storage(self):
        return self.manager.controller.get_bank_account_storage()
