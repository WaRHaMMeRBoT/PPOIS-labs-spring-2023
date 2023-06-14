import tkinter as tk
from tkinter import messagebox
import regex as regEX
from utils.ATM_interface import ATMInterface
from utils.ATM import ATM
from utils.Plastic_Card import PlasticCard
from typing import Optional
from utils.Money_Storage import MoneyStorage
import utils.Exceptions as excep

class GuiAtm(ATMInterface):
    pin_attempts: int = 3
    root = tk.Tk()
    root.geometry('900x800')
    root.title('ATM')
    frame = tk.Frame(root)

    @classmethod
    def clear_window(cls):
        for widget in cls.frame.winfo_children():
            widget.destroy()
        cls.frame.pack_forget()

    @classmethod
    def start(cls):
        cls.clear_window()
        enter_label = tk.Label(cls.frame, text='Enter card number', font=('Arial', 20))
        enter_label.pack()
        card_number = tk.StringVar(cls.root)
        card_number_field = tk.Entry(cls.frame, textvariable=card_number, font=('Arial', 20))
        card_number_field.pack()
        submit_button = tk.Button(cls.frame, text='Enter', font=('Arial', 20),
                                  command=lambda: cls.__make_card(card_number.get()))
        submit_button.pack(pady=5)
        return_button = tk.Button(cls.frame, text='RETURN CARD', font=('Arial', 20), command=cls.root.quit)
        return_button.pack(pady=5)
        cls.frame.place(relx=0.5, rely=0.5, anchor='center')

    @classmethod
    def __make_card(cls, card_num: str):
        if not bool(regEX.fullmatch(r'\d{16}', card_num)):
            messagebox.showinfo('Error', 'Wrong card number!')
            return
        plastic_card: Optional[PlasticCard] = cls.find_card_by_card_num(card_num)
        if plastic_card is None:
            messagebox.showinfo('Error', 'ATM is closed on maintenance\n(enter existing card)')
            cls.root.quit()
            return
        if plastic_card.is_blocked:
            cls.__show_error_message('YOUR CARD IS BLOCKED. CALL YOUR BANK')
            return
        if plastic_card.is_expired:
            cls.__show_error_message('YOUR CARD IS EXPIRED.\nGET THE NEW ONE AT YOUR BANK')
            return
        money_vault: MoneyStorage = cls.find_money_vault()
        if money_vault:
            cls.atm = ATM(money_vault=money_vault, plastic_card=plastic_card)
        cls.check_pin()

    @classmethod
    def check_pin(cls):
        cls.clear_window()
        pin_var = tk.StringVar(cls.root)
        widgets = [
            tk.Label(cls.frame, text='ENTER PIN', font=('Arial', 20)),
            tk.Entry(cls.frame, textvariable=pin_var, font=('Arial', 20)),
            tk.Button(cls.frame, text='Enter', font=('Arial', 20),
                      command=lambda: cls.__validate_pin(pin_var.get())),
            tk.Button(cls.frame, text='RETURN CARD', font=('Arial', 20), command=cls.root.quit)
        ]
        for widget in widgets:
            widget.pack(pady=5)
        cls.frame.place(relx=0.5, rely=0.5, anchor='center')

    @classmethod
    def __validate_pin(cls, pin: str):
        if cls.pin_attempts > 0:
            cls.pin_attempts -= 1
            if cls.atm.check_card_pin(pin):
                cls.main_menu()
            else:
                messagebox.showinfo('ERROR', f'ERROR. Incorrect PIN. {cls.pin_attempts} attempts left')
                if cls.pin_attempts <= 0:
                    cls.atm.block_card()
                    cls.save_cards_status()
                    cls.__show_error_message('YOU HAVE FAILED 3 ATTEMPTS TO ENTER CORRECT PIN.\n'
                                             'BLOCKING CARD. CONNECT BANK TO UNBLOCK')
                    return

    @classmethod
    def main_menu(cls):
        cls.clear_window()
        widgets = [
            tk.Button(cls.frame, text='BALANCE', font=('Arial', 20), command=cls.get_balance),
            tk.Button(cls.frame, text='GET CASH', font=('Arial', 20), command=cls.get_cash_money),
            tk.Button(cls.frame, text='MONEY ON PHONE', font=('Arial', 20), command=cls.put_money_on_phone),
            tk.Button(cls.frame, text='RETURN CARD', font=('Arial', 20), command=cls.root.quit)
        ]
        for i in range(len(widgets)):
            widgets[i].grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky='nsew')
        cls.frame.place(relx=0.5, rely=0.5, anchor='center')

    @classmethod
    def get_balance(cls):
        cls.clear_window()
        cls.pin_attempts = 3
        widgets = [
            tk.Label(cls.frame, text='YOUR CARD ACCOUNT BALANCE IS', font=('Arial Bold', 20)),
            tk.Label(cls.frame, text=f'{cls.atm.get_card_balance} BYN', font=('Arial', 20), bg='yellow'),
            tk.Button(cls.frame, text='RETURN', font=('Arial', 20), command=cls.main_menu)
        ]
        for widget in widgets:
            widget.pack(pady=10)
        cls.frame.place(relx=0.5, rely=0.5, anchor='center')

    @classmethod
    def get_cash_money(cls):
        cls.clear_window()
        cls.pin_attempts = 3
        money_vault = cls.atm.money_vault.moneyStorage
        max_money_amount = int(0.75 * sum([banknote_status[0] * banknote_status[1] for banknote_status
                                          in money_vault.items()]))
        max_money_amount -= max_money_amount % (10**(len(str(max_money_amount)) - 1))
        max_money_amount = int(max_money_amount)
        money_amount = tk.StringVar()
        available_banknotes = ' '.join(list(map(str, [banknote for banknote in money_vault.keys()
                                                      if money_vault[banknote] > 0])))
        widgets = [
            tk.Label(cls.frame, text='ENTER AMOUNT OF MONEY YOU WANT TO GET', font=('Arial Bold', 20)),
            tk.Entry(cls.frame, textvariable=money_amount, font=('Arial', 20)),
            tk.Label(cls.frame, text=f'AVAILABLE BANKNOTES\n'
                                     f'{available_banknotes}', font=('Arial Bold', 20)),
            tk.Label(cls.frame, text=f'MAX AMOUNT MONEY TO GET: {max_money_amount} BYN', font=('Arial Bold', 20)),
            tk.Button(cls.frame, text='GET MONEY', font=('Arial', 20), command=lambda: cls.__validate_cash_get(
                money_amount.get(), max_money_amount
            )),
            tk.Button(cls.frame, text='RETURN', font=('Arial', 20), command=cls.main_menu)
        ]
        for widget in widgets:
            widget.pack(pady=10, fill=tk.X)
        cls.frame.place(relx=0.5, rely=0.5, anchor='center')

    @classmethod
    def __validate_cash_get(cls, money_amount: str, max_money_amount: int):
        try:
            money_amount = int(money_amount)
        except ValueError:
            messagebox.showinfo('Error', 'Enter correct data in Money amount field')
            return
        if money_amount > max_money_amount:
            messagebox.showinfo('Error', 'Impossible to give money:\n'
                                         'Not enough money in ATM money vault')
            return
        try:
            cls.atm.get_cash_money(money_amount)
        except excep.NotEnoughMoney:
            messagebox.showinfo('Failure', 'Impossible to give money:\n'
                                           'Not enough money on your bank account!')
            return
        except excep.NoAvailableMoneyConfig:
            messagebox.showinfo('Failure', 'Impossible to give money:\n'
                                           'Can\'t form set of banknotes to give')
            return
        else:
            cls.save_money_vault()
            cls.save_card_accounts()
            messagebox.showinfo('Success', 'Take your money')
            cls.pin_attempts = 3
            cls.main_menu()

    @classmethod
    def put_money_on_phone(cls):
        cls.clear_window()
        cls.pin_attempts = 3
        phone_number = tk.StringVar()
        money_amount = tk.StringVar()
        widgets = [
            tk.Label(cls.frame, text='ENTER YOUR PHONE NUMBER', font=('Arial Bold', 20)),
            tk.Entry(cls.frame, textvariable=phone_number, font=('Arial', 20)),
            tk.Label(cls.frame, text='ENTER MONEY AMOUNT', font=('Arial Bold', 20)),
            tk.Entry(cls.frame, textvariable=money_amount, font=('Arial', 20)),
            tk.Button(cls.frame, text='PUT MONEY ON BALANCE', font=('Arial', 20),
                      command=lambda: cls.__validate_phone_fill_operation(phone_number.get(), money_amount.get())),
            tk.Button(cls.frame, text='RETURN', font=('Arial', 20), command=cls.check_pin)
        ]
        for widget in widgets:
            widget.pack(pady=10, fill=tk.X)
        cls.frame.place(relx=0.5, rely=0.5, anchor='center')

    @classmethod
    def __validate_phone_fill_operation(cls, phone_number: str, money_amount: str):
        try:
            money_amount = float(money_amount)
        except ValueError:
            messagebox.showinfo('Error', 'Impossible to perform operation:\n'
                                         'Enter correct data in Money amount field')
            return
        if not regEX.fullmatch(r"\+375(29|33|25|44|17|29)\d{7}", phone_number):
            messagebox.showinfo('Error', 'Impossible to perform operation:\n'
                                         'Enter correct phone number')
            return
        try:
            cls.atm.custom_operation(money_amount)
        except excep.NotEnoughMoney:
            messagebox.showinfo('Error', 'Impossible to perform operation:\n'
                                         'Not enough money on bank account')
            return
        else:
            cls.save_card_accounts()
            messagebox.showinfo('Success', 'Operation performed successfully!')
            cls.pin_attempts = 3
            cls.main_menu()

    @classmethod
    def __show_error_message(cls, error_message: str):
        cls.clear_window()
        widgets = [
            tk.Label(cls.frame, text=error_message.upper(), font=('Arial Bold', 20), fg='red'),
            tk.Button(cls.frame, text='QUIT', font=('Arial', 20), command=cls.root.quit)
        ]
        for widget in widgets:
            widget.pack(pady=5)
        cls.frame.place(relx=0.5, rely=0.5, anchor='center')

    @classmethod
    def run(cls):
        cls.start()
        cls.root.mainloop()
