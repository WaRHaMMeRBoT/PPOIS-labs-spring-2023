
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.actionbar import ActionBar
import data
import xml_sax
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


file='inform.xml'
class CustomeActionBar(ActionBar):
    pass

class AddScreen(Screen):
    def on_press_button_add(self):
        fio = self.fio.text
        accountNumber = self.accountNumber.text
        address = self.address.text
        mobileTelefon = self.mobileTelefon.text
        homeTelefon = self.homeTelefon.text
        if "+" in mobileTelefon:
            data.add(file,'person',{"fio":fio,"accountNumber":accountNumber,"address":address,"mobileTelefon":mobileTelefon,"homeTelefon":homeTelefon})
    
class DataScreen(Screen):
   pass

class MenuScreen(Screen):
    pass

search_list=[]
class SearchScreen(Screen):
   def on_press_button_search(self):
        global search_list
        answer=[]
        fio = self.fio.text
        accountNumber = self.accountNumber.text
        address = self.address.text
        mobileTelefon = self.mobileTelefon.text
        homeTelefon = self.homeTelefon.text
      
        key=["fio","accountNumber","address","mobileTelefon","homeTelefon"]
        elem=[fio,accountNumber, address,mobileTelefon, homeTelefon]

        for i in range(5):
            value = data.find(file, elem[i], key[i])
            if not value  == None:
                answer = answer + value

        search_list = answer
    
class MyButton(Button):
    pass

delete_list = []
class DeleteScreen(Screen):
    def on_press_button_delete(self):
        global delete_list
        answer=[]
        fio = self.fio.text
        accountNumber = self.accountNumber.text
        address = self.address.text
        mobileTelefon = self.mobileTelefon.text
        homeTelefon = self.homeTelefon.text

        key=["fio","accountNumber","address","mobileTelefon","homeTelefon"]
        elem=[fio,accountNumber, address,mobileTelefon, homeTelefon]
        count = data.count_for_delete(file)
        for j in range(count):
            for i in range(5):
                value = data.delete(file, elem[i], key[i])
                if not value  == None:
                    answer= answer+value
            delete_list = answer
        

class MyLabel(Label):
    pass

class MyTextInput(TextInput):
    pass

class WindowManager(ScreenManager):
    pass

class MainWidget(FloatLayout):
    pass

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tables = None

    def build(self):
        super(MainApp,self).__init__()
        self.title = "MyApp"
        self.load_kv("interface.kv")
        winManager=WindowManager()
       
        return winManager
    
    def change_screen(self, screen: str):
        self.root.current = screen

    def load_table(self):
         
        self.data_tables = MDDataTable(
        use_pagination=True,
       
        rows_num = 7,
        elevation=6,
        column_data=[
                ("[color=#eb00b0]No.[/color]", dp(20), None, "Custom tooltip"),
                ("[color=#eb00b0]fio[/color]", dp(25)),
                ("[color=#eb00b0]account number[/color]", dp(25)),
                ("[color=#eb00b0]address[/color]", dp(25)),
                ("[color=#eb00b0]mobile telefon[/color]", dp(25)),
                ("[color=#eb00b0]home telefon[/color]", dp(25))],
		row_data=xml_sax.Parser(),)
        self.root.ids.data_scr.ids.data_layout.add_widget(self.data_tables)
    
    def load_table_search(self):
        global search_list

    
        self.data_tables = MDDataTable(
        use_pagination=True,
        
        rows_num = 5,
        elevation=6,
        column_data=[
                
                ("[color=#eb00b0]fio[/color]", dp(25)),
                ("[color=#eb00b0]account number[/color]", dp(25)),
                ("[color=#eb00b0]address[/color]", dp(25)),
                ("[color=#eb00b0]mobile telefon[/color]", dp(25)),
                ("[color=#eb00b0]home telefon[/color]", dp(25))],
		row_data=search_list, )
        self.root.ids.search_scr.ids.data_search.add_widget(self.data_tables)

    
if __name__ == '__main__':
    MainApp().run() 
   
