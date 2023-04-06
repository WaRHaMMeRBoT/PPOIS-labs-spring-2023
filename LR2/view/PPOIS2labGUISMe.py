import sqlite3
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
my_path = "C:\\Users\\kyrill\\Documents\\GitHub\\PPOIS_Spring\\Lab 2.2\\PPOIS2lab.db"
connection = sqlite3.connect(my_path)
cursor = connection.cursor()

class WindowManager(MDScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
# Главное окно
class FirstWindow(MDScreen):
    pass
#Отображение таблицы 
class SecondWindow(MDScreen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)
        title = "Student table"
        
        data_tables = None
        cursor.execute("SELECT * FROM Students4")
        rows = cursor.fetchall()
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("No.", dp(10)),
                ("Column 1", dp(20)),
                ("Column 2", dp(20)),
                ("Column 3", dp(20)),
                ("Column 4", dp(20)),
                ("Column 5", dp(20)),
                ("Column 6", dp(20)),
                ("Column 7", dp(20)),
                ("Column 8", dp(20)),
                ("Column 9", dp(20)),
                ("Column 10", dp(20)),
                ("Column 11", dp(20)),
                ("Column 12", dp(20)),
                ("Column 13", dp(20)),
            ],
            row_data=[
                row for row in rows
            ],
        )
        
        
        self.add_widget(self.data_tables)
    
    def display_121701(self) :
        cursor.execute("SELECT * FROM Students4 Where GroupNumber = 121701")
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)

    def display_121702(self):
        cursor.execute("SELECT * FROM Students4 Where GroupNumber = 121702")
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)    

    def display_121703(self) :    
        cursor.execute("SELECT * FROM Students4 Where GroupNumber = 121703")
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)  

    def display_all(self):    
        cursor.execute("SELECT * FROM Students4 ")
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)     

    def find(self) -> None:    
        cursor.execute("SELECT * FROM Students4 Where FullName = 'Find Slava'")
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)   
# Поиск по имени или номеру группы
class ThirdWindow(MDScreen):
    def __init__(self, **kwargs):
        super(ThirdWindow, self).__init__(**kwargs)
        title = "Поиск студента"
        data_tables = None
        cursor.execute("SELECT * FROM Students4")
        rows = cursor.fetchall()
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("No.", dp(10)),
                ("Column 1", dp(20)),
                ("Column 2", dp(20)),
                ("Column 3", dp(20)),
                ("Column 4", dp(20)),
                ("Column 5", dp(20)),
                ("Column 6", dp(20)),
                ("Column 7", dp(20)),
                ("Column 8", dp(20)),
                ("Column 9", dp(20)),
                ("Column 10", dp(20)),
                ("Column 11", dp(20)),
                ("Column 12", dp(20)),
                ("Column 13", dp(20)),
            ],
            row_data=[
                row for row in rows
            ],
        )
        
        self.add_widget(self.data_tables)
    def find_by_name(self):    
        val1 = self.ids.name.text 
        cursor.execute("SELECT * FROM Students4 Where FullName = ?",(val1,))
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)  
        
    def find_by_group(self):    
        val1 = self.ids.group.text 
        cursor.execute("SELECT * FROM Students4 Where GroupNumber = ?",(val1,))
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)   
#Поиск -//- и количеству общ работы  
class FourthWindow(MDScreen):
    def __init__(self, **kwargs):
        super(FourthWindow, self).__init__(**kwargs)
        title = "Поиск студента"
        data_tables = None
        cursor.execute("SELECT * FROM Students4")
        rows = cursor.fetchall()

        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("No.", dp(10)),
                ("Column 1", dp(20)),
                ("Column 2", dp(20)),
                ("Column 3", dp(20)),
                ("Column 4", dp(20)),
                ("Column 5", dp(20)),
                ("Column 6", dp(20)),
                ("Column 7", dp(20)),
                ("Column 8", dp(20)),
                ("Column 9", dp(20)),
                ("Column 10", dp(20)),
                ("Column 11", dp(20)),
                ("Column 12", dp(20)),
                ("Column 13", dp(20)),
            ],
            row_data=[
                row for row in rows
            ],
        )

        self.add_widget(self.data_tables)
    def find_by_group(self):    
        val1 = self.ids.max.text 
        val2 = self.ids.min.text 
        val3 = self.ids.group.text 
        cursor.execute("SELECT * FROM Students4  Where GroupNumber =?3 AND Sem_total BETWEEN ?2 AND ?1",(val1,val2,val3))
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)   

    def find_by_name(self):    
        val1 = self.ids.max.text 
        val2 = self.ids.min.text 
        val3 = self.ids.name.text 
        
        cursor.execute("SELECT * FROM Students4  Where FullName =?3 AND Sem_total BETWEEN ?2 AND ?1",(val1,val2,val3))
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)   
# Добавление
class FifthWindow(MDScreen):
    def __init__(self, **kwargs):
        super(FifthWindow, self).__init__(**kwargs)
    def add_data(self) :   
        val1 = self.ids.name.text 
        val2 = self.ids.group.text 
        val3 = self.ids.sem1.text 
        val4 = self.ids.sem2.text 
        val5 = self.ids.sem3.text 
        val6 = self.ids.sem4.text 
        val7 = self.ids.sem5.text 
        val8 = self.ids.sem6.text 
        val9 = self.ids.sem7.text 
        val10 = self.ids.sem8.text 
        val11 = self.ids.sem9.text 
        val12 = self.ids.sem10.text 
        cursor.execute("INSERT INTO Students4 (FullName , GroupNumber, Sem1 ,Sem2 ,Sem3 ,Sem4 ,Sem5 ,Sem6 ,Sem7 ,Sem8 ,Sem9 ,Sem10 ) VALUES (?,?,?,?,? ,? ,? , ? , ? , ? , ? , ?)",(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12))
        connection.commit()
# Удаление по имени и группе (Добавить 2 поиск )
class SixthWindow(MDScreen):
    def __init__(self, **kwargs):
        super(SixthWindow, self).__init__(**kwargs)
    def delete_by_name(self) :       
        val1 = self.ids.name.text 
        val2 = self.ids.max.text 
        val3 = self.ids.min.text
        cursor.execute("DELETE FROM Students4 WHERE FullName=?1 AND Sem_total BETWEEN ?3 and ?2",(val1,val2,val3))
        connection.commit()
    def delete_by_group(self) :       
        val1 = self.ids.group.text 
        val2 = self.ids.max.text 
        val3 = self.ids.min.text
        cursor.execute("DELETE FROM Students4 WHERE GroupNumber=?1 AND Sem_total BETWEEN ?3 and ?2",(val1,val2,val3))
        connection.commit()


class Example(MDApp):
    def build(self):
        title = "Student App"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        Builder.load_file('main.kv')
        screen_manager = WindowManager()
        screen_manager.add_widget(FirstWindow(name = "main"))
        screen_manager.add_widget(SecondWindow(name = "all"))
        screen_manager.add_widget(ThirdWindow(name = "find"))
        screen_manager.add_widget(FourthWindow(name = "find_amount"))
        screen_manager.add_widget(FifthWindow(name = "add"))
        screen_manager.add_widget(SixthWindow(name = "delete"))

        return screen_manager
    
Example().run()
connection.close()