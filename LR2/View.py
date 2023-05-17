from Controller import Controller
from kivymd.uix.textfield import MDTextField
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.stacklayout import MDStackLayout



class MainScreen(Screen):
    def __init__(self,_controller:Controller, **kw):
        super().__init__(**kw)
        self.name = "MainWindow"
        self.addition_dialog=None
        self.load_dialog = None
        self.btn_layout = BoxLayout(orientation='horizontal', size_hint =(1,0.1))
        self.search_layout = BoxLayout(orientation='horizontal', size_hint =(1,0.1))
        self.controller=_controller
        self.records_table =self.controller.get_record_list() 
        self.main_layout = BoxLayout(orientation = 'vertical')
        self.checked_rows=[]
        self.create_buttons()
        self.create_search_main()
        self.create_table()
        self.fill_table(self.records_table)
        self.add_widget(self.main_layout)

    def btn_del_press(self,instance):
        if not self.table.get_row_checks():
            print('checked rows empty')
        else:
            for row in self.table.get_row_checks():
                self.controller.remove_elm(row[0])
            self.checked_rows=[]
            self.filter_records()
            
    
    def btn_save_press(self,instance):
        self.controller.save()  
    
    def btn_load_press(self,instance):
        self.show_load_dialog()
    
    def show_load_dialog(self):
        self.load_dialog = None
        if not self.load_dialog: 
            self.load_dialog= MDDialog(
                    text = "Load records",
                    type = "custom",
                    content_cls = LoadDialogContent(),
                    buttons = [
                        MDFlatButton(text = "Cancel", on_press = self.dialog_addition_cancel),
                        MDFlatButton(text = "Continue", on_press=self.dialog_load_ok),
                    ],
                    size_hint=(1.0, 1.0),
                )
            self.load_dialog.open()

    def dialog_load_cancel(self,*args):
         self.load_dialog.dismiss()
    
    def dialog_load_ok(self,*args):
         path = self.load_dialog.content_cls.txtf_path.text
         self.controller.change_model(path)
         self.filter_records()
         self.create_search_utils()
         self.load_dialog.dismiss()

    def btn_add_press(self, instance):
        self.show_addition_dialog()

    def show_addition_dialog(self):
         self.addition_dialog=None
         if not self.addition_dialog:
            self.addition_dialog = MDDialog(
                   text = "Add a new record",
                   type = "custom",
                   content_cls = AdditionDialogContent(),
                   buttons = [
                        MDFlatButton(text = "Cancel", on_press = self.dialog_addition_cancel),
                        MDFlatButton(text = "Add", on_press=self.dialog_addition_ok),
                   ],
                   size_hint=(1.0, 1.0),
              )
            self.addition_dialog.open()

    def dialog_addition_cancel(self, *args):
         self.addition_dialog.dismiss()
    
    def dialog_addition_ok(self, *args):
        fullName=self.addition_dialog.content_cls.txtf_fullName.text
        rank = self.addition_dialog.content_cls.txtf_rank.text
        sport = self.addition_dialog.content_cls.txtf_sport.text
        position = self.addition_dialog.content_cls.txtf_position.text
        squad = self.addition_dialog.content_cls.txtf_squad.text
        titles = self.addition_dialog.content_cls.txtf_titles.text
        if titles == '':
            titles = '[]'
        # do something with the name
        self.controller.make_record(fullName,rank,sport,position,squad,titles)
        self.create_search_utils()
        self.filter_records()
        self.addition_dialog.dismiss()

    def filter_records(self):
        self.records_table=self.controller.get_records()           
        if not (self.dropdown_rank_filter.current_item=="by rank" or self.dropdown_rank_filter.current_item=="All") :
             self.records_table=self.controller.filter_rank(self.dropdown_rank_filter.current_item,self.records_table)
        if not (self.dropdown_sport_filter.current_item=="by sport" or self.dropdown_sport_filter.current_item=="All") :
             self.records_table=self.controller.filter_sports(self.dropdown_sport_filter.current_item,self.records_table)
        if not (self.dropdown_titles_value_filter.current_item=="by titles value" or self.dropdown_titles_value_filter.current_item == "All"):
             self.records_table=self.controller.filter_titles_values(self.dropdown_titles_value_filter.current_item,self.records_table)
        if not self.txtf_search_by_name.text == '':
             self.records_table=self.controller.search_by_name(self.txtf_search_by_name.text,self.records_table)
        self.fill_table(self.controller.convert_records_to_list(self.records_table))
         

    def btn_search_press(self,instance):
        self.filter_records()
        return

    def create_search_utils(self):
        ##Ranks
        ranks=self.controller.get_ranks()
        ranks.add('All')
        rank_menu_items = [{"text": f"{item}","height":60,
                        "viewclass": "OneLineListItem",
                        "on_press": lambda x=f"{item}": self.set_rank_dropdown_line_up(x) 
                        }for item in ranks]
        self.ranks_drop_down_line_up = MDDropdownMenu(
            caller=self.dropdown_rank_filter,
            items=rank_menu_items,
            width_mult=4,
            )
        self.dropdown_rank_filter.set_item("by rank")
        self.dropdown_rank_filter.bind(on_press=lambda x: self.ranks_drop_down_line_up.open())
        ##Sports
        sports = self.controller.get_sports()
        sports.add('All')
        sports_menu_items = [{"text": f"{item}","height":60,
                        "viewclass": "OneLineListItem",
                        "on_press": lambda x=f"{item}": self.set_sports_dropdown_line_up(x) 
                        }for item in sports]
        self.sports_drop_down_line_up = MDDropdownMenu(
            caller=self.dropdown_sport_filter,
            items=sports_menu_items,
            width_mult=4,
            )
        self.dropdown_sport_filter.set_item("by sport")
        self.dropdown_sport_filter.bind(on_press=lambda x: self.sports_drop_down_line_up.open())

        ##TitleValue
        titles_values=self.controller.get_title_values()
        titles_values.add('All')
        titles_value_menu_items = [{"text": f"{item}","height":60,
                        "viewclass": "OneLineListItem",
                        "on_press": lambda x=f"{item}": self.set_titles_value_dropdown_line_up(x) 
                        }for item in titles_values]
        self.title_value_drop_down_line_up = MDDropdownMenu(
            caller=self.dropdown_titles_value_filter,
            items=titles_value_menu_items,
            width_mult=4,
            )
        self.dropdown_titles_value_filter.set_item('by titles value')
        self.dropdown_titles_value_filter.bind(on_press=lambda x: self.title_value_drop_down_line_up.open())

    def create_search_main(self):
        ##Search utils
        self.txtf_search_by_name = MDTextField(hint_text = "Search by name:", size_hint = (0.2,1.0))
        filter_label=MDLabel(text ='Filters:',size_hint = (0.2,1.0))
        self.dropdown_rank_filter = MDDropDownItem(size_hint = (0.2,1.0))
        self.dropdown_sport_filter = MDDropDownItem(size_hint = (0.2,1.0))
        self.dropdown_titles_value_filter = MDDropDownItem(size_hint= (0.2,1.0))
        self.create_search_utils()
        self.search_layout.add_widget(self.txtf_search_by_name)
        self.search_layout.add_widget(filter_label)
        self.search_layout.add_widget(self.dropdown_rank_filter)
        self.search_layout.add_widget(self.dropdown_sport_filter)
        self.search_layout.add_widget(self.dropdown_titles_value_filter)
        self.main_layout.add_widget(self.search_layout)

    def set_rank_dropdown_line_up(self, item: str):
            self.dropdown_rank_filter.set_item(item)
            self.ranks_drop_down_line_up.dismiss()

    def set_sports_dropdown_line_up(self, item: str):
            self.dropdown_sport_filter.set_item(item)
            self.sports_drop_down_line_up.dismiss()

    def set_titles_value_dropdown_line_up(self, item: str):
            self.dropdown_titles_value_filter.set_item(item)
            self.title_value_drop_down_line_up.dismiss()
    
    def create_buttons(self):
        ##Main Buttons
        self.btn_search = Button(text ='Search',font_size=dp(30))
        self.btn_search.bind(on_press= self.btn_search_press)
        self.btn_add = Button(text ='Add',font_size=dp(30))
        self.btn_add.bind(on_press= self.btn_add_press)
        self.btn_del = Button(text = 'Delete',font_size=dp(30))
        self.btn_del.bind(on_press=self.btn_del_press)
        self.btn_save = Button(text = 'Save',font_size=dp(30))
        self.btn_save.bind(on_press= self.btn_save_press)
        self.btn_load = Button(text = 'Load',font_size=dp(30))
        self.btn_load.bind(on_press= self.btn_load_press)
        self.buttons = list((self.btn_search,self.btn_add,self.btn_del, self.btn_save, self.btn_load))
        for btn in self.buttons:
            self.btn_layout.add_widget(btn)
        ##Main layout modify
        self.main_layout.add_widget(self.btn_layout)

    def fill_table(self,records):
         self.table.row_data=[]
         self.table.row_data=records
         
    def create_table(self):
        self.tblLayout = BoxLayout()
        self.table = MDDataTable(
            check=True,
            use_pagination=True,
            column_data =
            [
                ('FullName:', dp(80)),
                ('Rank:',dp(30)),
                ('Sport:',dp(30)),
                ('Position:',dp(30)),
                ('Squad:', dp(30)),
                ('Titles:', dp(180))
            ]
        )
        self.tblLayout.add_widget(self.table)
        self.main_layout.add_widget(self.tblLayout)

class LoadDialogContent(MDStackLayout):
    txtf_path = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height="100dp"
        self.width="100dp"
        self.txtf_path = MDTextField(
             hint_text = "Enter file path:",
             required = True
        )
        self.add_widget(self.txtf_path)

class AdditionDialogContent(MDStackLayout):
    txtf_fullName = ObjectProperty(None)
    txtf_rank = ObjectProperty(None)
    txtf_sport = ObjectProperty(None)
    txtf_position = ObjectProperty(None)
    txtf_squad = ObjectProperty(None)
    txtf_titles = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="tb-lr"
        self.spacing="10dp"
        self.size_hint_y=None
        self.height="500dp"
        self.width="500dp"
        self.txtf_fullName = MDTextField(
            hint_text="Enter fullName",
            required=True,
        )
        self.txtf_rank=MDTextField(
            hint_text="Enter rank",
            required=True,
        )
        self.txtf_sport=MDTextField(
            hint_text="Enter sport",
            required=True,
        )
        self.txtf_position=MDTextField(
            hint_text="Enter position",
            required=True,
        )
        self.txtf_squad=MDTextField(
            hint_text="Enter squad",
            required=True,
        )
        self.txtf_titles=MDTextField(
            hint_text="Enter titles"
        )
        self.add_widget(self.txtf_fullName)
        self.add_widget(self.txtf_rank)
        self.add_widget(self.txtf_sport)
        self.add_widget(self.txtf_position)
        self.add_widget(self.txtf_squad)
        self.add_widget(self.txtf_titles)


class MainApp(MDApp):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller_main = controller

    def build(self):
        return MainScreen(self.controller_main)
    
    

