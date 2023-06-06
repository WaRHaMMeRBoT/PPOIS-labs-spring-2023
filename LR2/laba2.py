from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import info
import sax
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import time_1 as time

file = 'info.xml'
searchlist = []
deletelist = []

class MainWidget(Screen):
    pass

class ColorfulLabel(Label):
    pass

class WindowManager(ScreenManager):
    pass

class MenuScreen(Screen):
    pass

class DataScreen(Screen):
    pass

class AddScreen(Screen):
    def add_button(self):
        dictionary = {'number_of_train':self.numbertrain.text,
                      'departure':self.departure.text,
                      'arrival':self.arrival.text,
                      'departure_data_time':self.datatimedeparture.text,
                      'arrival_data_time':self.datatimearrival.text}
        if time.to_date(self.datatimedeparture.text) != None and time.to_date(self.datatimearrival.text) != None:
            info.add(file, dictionary)

class SearchScreen(Screen):
    def search_button(self):
        global searchlist
        searchlist = []
        keys = ['number_of_train','departure','arrival']
        values = [self.numbertrain.text, self.departure.text, self.arrival.text]
        for i in range(len(keys)):
            searchlist += info.search(file, keys[i], values[i])

        if self.mindatatimedeparture.text != '' and time.to_date(self.mindatatimedeparture.text) != None:
            mindatatimedeparture = self.mindatatimedeparture.text
        else: mindatatimedeparture = -1
        if self.maxdatatimedeparture.text != '' and time.to_date(self.maxdatatimedeparture.text) != None:
            maxdatatimedeparture = self.maxdatatimedeparture.text
        else: maxdatatimedeparture = -1

        if self.mindatatimearrival.text != '' and time.to_date(self.mindatatimearrival.text) != None:
            mindatatimearrival = self.mindatatimearrival.text
        else: mindatatimearrival = -1
        if self.maxdatatimearrival.text != '' and time.to_date(self.maxdatatimearrival.text) != None:
            maxdatatimearrival = self.maxdatatimearrival.text
        else: maxdatatimearrival = -1

        if mindatatimedeparture != -1 or maxdatatimedeparture != -1:
            searchlist += info.range_search(file, 'departure_data_time', mindatatimedeparture, maxdatatimedeparture)
        if mindatatimearrival != -1 or maxdatatimearrival != -1:
            searchlist += info.range_search(file, 'arrival_data_time', mindatatimearrival, maxdatatimearrival)
        
        if self.time.text != '' and time.from_string_to_time(self.time.text) != None:
            searchlist += info.search_time(file, time.from_string_to_time(self.time.text))
        

class DeleteScreen(Screen):
    def delete_button(self):
        global deletelist
        keys = ['number_of_train','departure','arrival']
        values = [self.numbertrain.text, self.departure.text, self.arrival.text]
        for i in range(len(keys)):
            deletelist += info.delete(file, keys[i], values[i])

        if self.mindatatimedeparture.text != '' and time.to_date(self.mindatatimedeparture.text) != None:
            mindatatimedeparture = self.mindatatimedeparture.text
        else: mindatatimedeparture = -1
        if self.maxdatatimedeparture.text != '' and time.to_date(self.maxdatatimedeparture.text) != None:
            maxdatatimedeparture = self.maxdatatimedeparture.text
        else: maxdatatimedeparture = -1

        if self.mindatatimearrival.text != '' and time.to_date(self.mindatatimearrival.text) != None:
            mindatatimearrival = self.mindatatimearrival.text
        else: mindatatimearrival = -1
        if self.maxdatatimearrival.text != '' and time.to_date(self.maxdatatimearrival.text) != None:
            maxdatatimearrival = self.maxdatatimearrival.text
        else: maxdatatimearrival = -1

        if mindatatimedeparture != -1 or maxdatatimedeparture != -1:
            deletelist += info.range_delete(file, 'departure_data_time', mindatatimedeparture, maxdatatimedeparture)
        if mindatatimearrival != -1 or maxdatatimearrival != -1:
            deletelist += info.range_delete(file, 'arrival_data_time', mindatatimearrival, maxdatatimearrival)

        if self.time.text != '' and time.from_string_to_time(self.time.text) != None:
            deletelist += info.delete_time(file, time.from_string_to_time(self.time.text))

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tables = None

    def build(self):
        super(MainApp,self).__init__()
        self.title = "MyApp"
        self.load_kv("struct.kv")
        return WindowManager()
    
    def change_screen(self, screen: str):
        self.root.current = screen

    def load_table(self):
        self.data_tables = MDDataTable(
        use_pagination=True,
        rows_num = 8,
        elevation=7,
        column_data=[
                ("[font=Comic][color=#cc74f2]No.[/color][/font]", dp(7), None, "Custom tooltip"),
                ("[font=Comic][color=#be51ed]Train[/color][/font]", dp(12)),
                ("[font=Comic][color=#aa1ae8]Departure station[/color][/font]", dp(21)),
                ("[font=Comic][color=#8900c4]Arrival station[/color][/font]", dp(21)),
                ("[font=Comic][color=#6e1d91]Departure time[/color][/font]", dp(23)),
                ("[font=Comic][color=#5b117a]Arrival time[/color][/font]", dp(21)),
                ("[font=Comic][color=#2f0342]Travel time[/color][/font]", dp(40))],
		row_data=sax.work_parser(),)
        self.root.ids.data_scr.ids.data_layout.add_widget(self.data_tables)

    def load_search_table(self):
        self.data_tables = MDDataTable(
        use_pagination=True,
        rows_num = 2,
        elevation=7,
        column_data=[
                ("[font=Comic][color=#cc74f2]Train[/color][/font]", dp(23)),
                ("[font=Comic][color=#be51ed]Departure station[/color][/font]", dp(25)),
                ("[font=Comic][color=#aa1ae8]Arrival station[/color][/font]", dp(26)),
                ("[font=Comic][color=#8900c4]Departure time[/color][/font]", dp(26)),
                ("[font=Comic][color=#6e1d91]Arrival time[/color][/font]", dp(20)),
                ("[font=Comic][color=#2f0342]Travel time[/color][/font]", dp(28))],
		row_data = searchlist,)
        self.root.ids.search_scr.ids.data_search.add_widget(self.data_tables)

if __name__ == '__main__':
    MainApp().run() 