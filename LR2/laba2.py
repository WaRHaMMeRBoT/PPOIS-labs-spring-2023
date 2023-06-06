from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import info
import sax
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

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
        dictionary = {'tournaname':self.tournaname.text,
                      'date':self.date.text,
                      'sport':self.sport.text,
                      'winner':self.winner.text,
                      'prize':self.prize.text}
        if self.prize.text.isdigit():
            info.add(file, dictionary)

class SearchScreen(Screen):
    def search_button(self):
        global searchlist
        searchlist = []
        keys = ['tournaname','date','sport','winner']
        values = [self.tournaname.text, self.date.text, self.sport.text, self.winner.text]
        for i in range(len(keys)):
            searchlist += info.search(file, keys[i], values[i])
        
        if self.minprize.text != '' and self.minprize.text.isdigit(): mingain = float(self.minprize.text)
        else: minprize = -1
        if self.maxprize.text != '' and self.maxprize.text.isdigit(): float(self.maxprize.text)
        else: maxprize = -1
        
        if self.mingain.text != '' and self.mingain.text.isdigit(): mingain = float(self.mingain.text)
        else: mingain = -1
        if self.maxgain.text != '':
            if self.maxgain.text.isdigit() and self.maxgain.text.isdigit(): float(self.maxgain.text)
        else: maxgain = -1

        if minprize != -1 or maxprize != -1:
            searchlist += info.range_search(file, 'prize', minprize, maxprize)
        if mingain != -1 or maxgain != -1:
            searchlist += info.range_search(file, 'prize', mingain/0.6, maxgain/0.6)

class DeleteScreen(Screen):
    def delete_button(self):
        global deletelist
        keys = ['tournaname','date','sport','winner']
        values = [self.tournaname.text, self.date.text, self.sport.text, self.winner.text]
        for i in range(len(keys)):
            deletelist += info.delete(file, keys[i], values[i])

        if self.minprize.text != '' and self.minprize.text.isdigit(): mingain = float(self.minprize.text)
        else: minprize = -1
        if self.maxprize.text != '' and self.maxprize.text.isdigit(): float(self.maxprize.text)
        else: maxprize = -1

        if self.mingain.text != '' and self.mingain.text.isdigit(): mingain = float(self.mingain.text)
        else: mingain = -1
        if self.maxgain.text != '':
            if self.maxgain.text.isdigit() and self.maxgain.text.isdigit(): float(self.maxgain.text)
        else: maxgain = -1

        if minprize != -1 or maxprize != -1:
            deletelist += info.range_delete(file, 'prize', minprize, maxprize)
        if mingain != -1 or maxgain != -1:
            deletelist += info.range_delete(file, 'prize', mingain/0.6, maxgain/0.6)

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
                ("[font=Comic][color=#cf1d02]No.[/color][/font]", dp(15), None, "Custom tooltip"),
                ("[font=Comic][color=#cf7d02]Name[/color][/font]", dp(25)),
                ("[font=Comic][color=#cbcf02]Date[/color][/font]", dp(24)),
                ("[font=Comic][color=#02cf5b]Sport[/color][/font]", dp(24)),
                ("[font=Comic][color=#024dcf]Winner[/color][/font]", dp(23)),
                ("[font=Comic][color=#8702cf]Prize[/color][/font]", dp(18)),
                ("[font=Comic][color=#cb02cf]Winner's gain[/color][/font]", dp(25))],
		row_data=sax.work_parser(),)
        self.root.ids.data_scr.ids.data_layout.add_widget(self.data_tables)

    def load_search_table(self):
        self.data_tables = MDDataTable(
        use_pagination=True,
        rows_num = 2,
        elevation=7,
        column_data=[
                ("[font=Comic][color=#cf1d02]Name[/color][/font]", dp(23)),
                ("[font=Comic][color=#cf7d02]Date[/color][/font]", dp(25)),
                ("[font=Comic][color=#cbcf02]Sport[/color][/font]", dp(26)),
                ("[font=Comic][color=#02cf5b]Winner[/color][/font]", dp(26)),
                ("[font=Comic][color=#024dcf]Prize[/color][/font]", dp(20)),
                ("[font=Comic][color=#cb02cf]Winner's gain[/color][/font]", dp(28))],
		row_data = searchlist,)
        self.root.ids.search_scr.ids.data_search.add_widget(self.data_tables)

if __name__ == '__main__':
    MainApp().run() 