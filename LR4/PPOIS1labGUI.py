import sqlite3
import sys

from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.datatables.datatables import MDDataTable
from kivymd.uix.menu.menu import MDDropdownMenu
from kivy.clock import Clock
from typing import Optional
from kivymd.uix.screenmanager import MDScreenManager
from PPOIS1lab import Rewrite_values,Get_money,Add_money,Pay_telephone,Read_values,Display_values,Flag_Reader,arr
from PPOIS1labClasses import Atm,Card,Bank,Telephone
f = open("C:\\Users\\kyrill\\Documents\\GitHub\\PPOIS_Spring\\Lab 1.1\\PPOIS1lab.txt","r+")
l = len(sys.argv)
read_flag = Flag_Reader()
display = Display_values()
get = Get_money()
add = Add_money()
pay = Pay_telephone()
rewrite = Rewrite_values()
read = Read_values()
atm = arr[0]
bank = arr[1]
pin = arr[2]
card = arr[3]
tel = arr[4]
atm_obj = Atm(atm)
card_obj = Card(pin, card)
bank_obj = Bank(bank)
tel_obj = Telephone(tel)
# atm_obj = Atm(atm)
# card_obj = Card(pin,card)
# bank_obj = Bank(bank)
# tel_obj = Telephone(tel)

class WindowManager(MDScreenManager):
    def __init__(self, *args, **kwargs):
        super(WindowManager,self).__init__(*args, **kwargs)

                
class MenuScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(MenuScreen,self).__init__(*args, **kwargs)
    def cli(self):
        read_flag.flag_reader(card_obj)
class AddMoneyScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(AddMoneyScreen, self).__init__(*args, **kwargs)

    def add(self):

        atm = arr[0]
        bank = arr[1]
        pin = arr[2]
        card = arr[3]
        tel = arr[4]

        money = self.ids.tel.text
        money = int(money)

        if money != 0:
            bank = bank + money
            atm = atm + money

            atm_obj = Atm(atm)
            card_obj = Card(pin, card)
            bank_obj = Bank(bank)
            tel_obj = Telephone(tel)
            rewrite.rewrite_values(atm_obj, bank_obj, card_obj, tel_obj)
        else:
            print("Не внесены средства ")
class GetMoneyScreen(MDScreen):
    def __init__(self,*args, **kwargs):
        super(GetMoneyScreen,self).__init__(*args, **kwargs)
    def get(self):

        atm = arr[0]
        bank = arr[1]
        pin = arr[2]
        card = arr[3]
        tel = arr[4]

        money = self.ids.tel.text
        money = int(money)

        if money <= atm and money <= bank:
            bank = bank - money
            atm = atm - money

            atm_obj = Atm(atm)
            card_obj = Card(pin, card)
            bank_obj = Bank(bank)
            tel_obj = Telephone(tel)
            rewrite.rewrite_values(atm_obj, bank_obj, card_obj, tel_obj)
        else:
            print("Ошибка.Недостаточно средств на карте/терминале")
class PayTelephoneScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(PayTelephoneScreen,self).__init__(*args, **kwargs)
    def pay_tel(self):

        atm = arr[0]
        bank = arr[1]
        pin = arr[2]
        card = arr[3]
        tel = arr[4]

        money = self.ids.tel.text
        money = int(money)

        if money <= atm and money <= bank:
                bank = bank - money
                atm = atm - money
                tel = tel + money

                atm_obj = Atm(atm)
                card_obj = Card(pin, card)
                bank_obj = Bank(bank)
                tel_obj = Telephone(tel)
                rewrite.rewrite_values(atm_obj, bank_obj, card_obj, tel_obj)
        else:
            print("Ошибка.Недостаточно средств на карте/терминале")
class DisplayScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(DisplayScreen,self).__init__(*args, **kwargs)
        title = "Остатки на всех счетах"
        data_tables = None
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Atm", dp(30)),
                ("Bank", dp(30)),
                ("Pin", dp(30)),
                ("Card", dp(30)),
                ("Tel", dp(30)),
            ],
            row_data=[
                
                (atm,
                 bank,
                 pin,
                 card,
                 tel,
                 ),
            ],
        )
        
        self.add_widget(self.data_tables)
    def update(self):
        arr = read.read_values()

class AtmApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        Builder.load_file('Gui4lab.kv')
        screen_manager = WindowManager()
        
        
        screen_manager.add_widget(MenuScreen(name = "menu"))
        screen_manager.add_widget(AddMoneyScreen(name = "add"))
        screen_manager.add_widget(GetMoneyScreen(name = "get"))
        screen_manager.add_widget(DisplayScreen(name = "display"))
        screen_manager.add_widget(PayTelephoneScreen(name = "pay"))
        


        return screen_manager
    
AtmApp().run()

