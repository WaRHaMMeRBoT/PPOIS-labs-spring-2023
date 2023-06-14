import copy

from kivy.metrics import dp

from kivymd.app import *
from kivymd.uix.datatables.datatables import *
from kivymd.uix.dialog import *
from kivy.uix.anchorlayout import *
from kivy.uix.stacklayout import *
from kivy.uix.button import *
from kivy.uix.boxlayout import *
from kivymd.uix.button import *
from kivymd.uix.stacklayout import *
from kivymd.uix.textfield import *
from kivymd.uix.menu import *
from kivymd.uix.label import *
from kivymd.uix.dropdownitem import *

import ButtonsActions
import SAXParser


def save_button_action(core_object):
    def callback(*args):
        core_object.save_button_output()

    return callback


def load_button_action(core_object):
    def callback(*args):
        core_object.load_button_output()

    return callback


def add_button_action(core_object):
    def callback(*args):
        core_object.add_button_input()

    return callback


def delete_button_action(core_object):
    def callback(*args):
        core_object.delete_button_input()

    return callback


def search_button_action(core_object):
    def callback(*args):
        core_object.search_input()

    return callback


class Core(MDApp):
    dialog_save = None
    dialog_load = None
    dialog_add = None
    dialog_delete = None
    drop_down_rank = None
    rank_item = None
    drop_down_achievement = None
    achievement_list = None
    drop_down_line_up = None
    line_up_list = None
    dialogue_search = None
    buffer_data = None


    def search_process(self):
        search_attributes = self.collect_delete_attributes(self.dialogue_search)
        temp_copy = copy.copy(self.data_table.row_data)
        search_result = []
        if len(self.data_table.row_data) > 1:
            for row in temp_copy:
                if row[0] == search_attributes[0] and row[4] == search_attributes[1]:
                    self.buffer_data.add_row(row)
                elif row[3] == self.achievement_list.current_item:
                    self.buffer_data.add_row(row)
                elif row[0] == search_attributes[0] and self.rank_item.current_item == row[5]:
                    self.buffer_data.add_row(row)

    def search_table_init(self):
        self.buffer_data = MDDataTable(use_pagination=True, size_hint=(0.8, 0.5),
                                       column_data=[("F.I.O.", dp(30)), ("Uchenaja zvanie", dp(30)),
                                                    ("Staj rabot", dp(30)), ("Uchenaja stepen", dp(30)),
                                       ("Kafedra", dp(30)), ("Facult", dp(30))])

    def search_data_cleaner(self):
        while len(self.buffer_data.row_data)>=1:
            self.buffer_data.remove_row(self.buffer_data.row_data[-1])

    def search_correct_exit(self):
        self.dialogue_search.dismiss()

    def search_input(self):
        self.drop_down_rank_list()
        self.drop_down_achievement_list()
        self.search_table_init()

        self.dialogue_search = MDDialog(
            title="Find",
            type="custom",
            buttons=[MDFlatButton(text="Find", on_press=lambda x: self.search_process()),
                     MDFlatButton(text="Clear",
                                  on_press=lambda x: self.search_data_cleaner()),
                     MDFlatButton(text="Cancel", on_press=lambda x: self.search_correct_exit())],
            content_cls=MDStackLayout(MDTextField(
                id="name",
                hint_text="F.I.O.",
                helper_text_mode="on_error"
            ),
                self.rank_item,
                self.achievement_list,
                MDTextField(
                    id="sports discipline",
                    hint_text="Kafedra",
                    helper_text_mode="on_error"
                ),
                self.buffer_data,
                orientation="tb-lr",
                spacing="10dp",
                size_hint_y=None,
                height="600dp"
            )
        )
        self.dialogue_search.open()

    def drop_down_line_up_list(self):
        self.line_up_list = MDDropDownItem(id="line-up", pos_hint={'center_x': .5, 'center_y': .5},
                                           current_item="n/a")
        menu_items = [{"text": "docent",
                       "viewclass": "OneLineListItem",
                       "height": dp(60),
                       "on_press": lambda x="docent": self.set_line_up(x)
                       },
                      {"text": "professor",
                       "viewclass": "OneLineListItem",
                       "height": dp(60),
                       "on_press": lambda x="professor": self.set_line_up(x)
                       },
                      {"text": "n/a",
                       "viewclass": "OneLineListItem",
                       "height": dp(60),
                       "on_press": lambda x="n/a": self.set_line_up(x)
                       }]
        self.drop_down_line_up = MDDropdownMenu(
            caller=self.line_up_list,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.line_up_list.set_item("n/a")
        self.line_up_list.bind(on_press=lambda x: self.drop_down_line_up.open())

    def set_line_up(self, item: str):
        self.line_up_list.set_item(item)
        self.drop_down_line_up.dismiss()

    def drop_down_rank_list(self):
        self.rank_item = MDDropDownItem(id="rank", pos_hint={'center_x': .5, 'center_y': .5},
                                        current_item="n/a")
        menu_items = [
            {"text": f"n/a",
             "viewclass": "OneLineListItem",
             "height": dp(60),
             "on_press": lambda x=f"n/a": self.set_rank(x), }
        ]
        menu_items.append({"text": "FKP", "viewclass": "OneLineListItem", "height": dp(60),
                           "on_press": lambda x="FKP": self.set_rank(x), }, )
        menu_items.append({"text": "FITU", "viewclass": "OneLineListItem", "height": dp(60),
                           "on_press": lambda x="FITU": self.set_rank(x)})
        self.drop_down_rank = MDDropdownMenu(
            caller=self.rank_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.rank_item.set_item("n/a")
        self.rank_item.bind(on_press=lambda x: self.drop_down_rank.open())

    def set_rank(self, rank: str):
        self.rank_item.set_item(rank)
        self.drop_down_rank.dismiss()

    def drop_down_achievement_list(self):
         self.achievement_list = MDDropDownItem(id="achievement", pos_hint={'center_x': .5, 'center_y': .5},
                                                current_item="n/a")
         menu_items = [{"text": "n/a", "viewclass": "OneLineListItem", "height": dp(60), "on_press": lambda
                        x="n/a": self.set_achievement(x)}, {"text": "Kandidat nauk", "viewclass": "OneLineListItem", "height": dp(60),
                            "on_press": lambda x="Kandidat nauk": self.set_achievement(x)}, {"text": "Doctor nauk", "viewclass": "OneLineListItem", "height": dp(60),
                            "on_press": lambda x="Doctor nauk": self.set_achievement(x)}]


         self.drop_down_achievement = MDDropdownMenu(
             caller=self.achievement_list,
             items=menu_items,
             position="center",
             width_mult=4,
         )
         self.achievement_list.set_item("n/a")
         self.achievement_list.bind(on_press=lambda x: self.drop_down_achievement.open())

    def set_achievement(self, x: int):
        self.achievement_list.set_item(str(x))
        self.drop_down_achievement.dismiss()

    def delete_button_description(self):
        delete_attributes = self.collect_delete_attributes(self.dialog_delete)
        self.delete_button_output(delete_attributes[0], delete_attributes[1])

    def delete_button_input(self):
        self.drop_down_rank_list()
        self.drop_down_achievement_list()
        self.dialog_delete = MDDialog(
            title="Delete",
            type="custom",
            buttons=[MDFlatButton(text="Delete", on_press=lambda x:self.delete_button_description()),
                     MDFlatButton(text="Cancel", on_press=lambda x:self.dialog_delete.dismiss())],
            content_cls=MDStackLayout(MDTextField(
                id="name",
                hint_text="F.I.O",
                helper_text_mode="on_error"
            ),
                self.rank_item,
                self.achievement_list,
                MDTextField(
                    id="sports discipline",
                    hint_text="Kafedra",
                    helper_text_mode="on_error"
                ),
                orientation="tb-lr",
                spacing="10dp",
                size_hint_y=None,
                height="500dp"
            )
        )
        self.dialog_delete.open()

    def add_button_input(self):
        self.drop_down_rank_list()
        self.drop_down_achievement_list()
        self.drop_down_line_up_list()
        self.dialog_add = MDDialog(
            title="Add",
            type="custom",
            buttons=[MDFlatButton(text="Save", on_press=lambda
                     x: self.add_button_logic(self.dialog_add.content_cls)),
                     MDFlatButton(text="Cancel", on_press=lambda x: self.dialog_add.dismiss())],
            content_cls=MDStackLayout(
                MDTextField(
                    id='name',
                    hint_text="F.I.O",
                    required=True,
                    helper_text_mode="on_error",
                    helper_text="Fill all field"
                ),
                self.line_up_list,
                MDTextField(
                    id='position',
                    hint_text="Staj rabot",
                    required=True,
                    helper_text_mode="on_error",
                    helper_text="Fill all field"
                ),
                self.achievement_list,
                MDTextField(
                    id='sports discipline',
                    hint_text='Kafedra',
                    required=True,
                    helper_text_mode="on_error",
                    helper_text="Fill all field"
                ),
                self.rank_item,
                orientation="tb-lr",
                spacing="10dp",
                size_hint_y=None,
                height="500dp",
                width="500dp"
            )
        )
        self.dialog_add.open()


    def delete_button_output(self, name_text: str, sports_discipline_text: str):
        if len(self.data_table.row_data) > 1:
            copy_of_row_data = copy.copy(self.data_table.row_data)
            for row in copy_of_row_data:
                if (row[0] == name_text and row[4] == sports_discipline_text) or row[3] \
                        == self.achievement_list.current_item \
                        or (row[0] == name_text and self.rank_item.current_item == row[5]):
                    self.data_table.remove_row(row)
            self.dialog_delete.dismiss()

    def add_button_logic(self, content: MDStackLayout):
        data_for_addition = content.ids

        def collect_sportsmen_data():
            return {
                "name": data_for_addition.get("name").text,
                "line-up": self.line_up_list.current_item,
                "position": data_for_addition.get("position").text,
                "achievements": self.achievement_list.current_item,
                "sports discipline": data_for_addition.get("sports discipline").text,
                "rank": self.rank_item.current_item
            }

        keys, output = zip(*collect_sportsmen_data().items())
        self.data_table.add_row(output)
        self.dialog_add.dismiss()


    def collect_delete_attributes(self, content: MDStackLayout):
        data_for_deletion = content.content_cls.ids

        def collect_attributes():
            return {
                "name": data_for_deletion.get("name").text,
                "sports discipline": data_for_deletion.get("sports discipline").text
            }

        keys, output = zip(*collect_attributes().items())
        return output

    def save_button_output(self):
        self.dialog_save = MDDialog(
            title="Save?",
            type="custom",
            buttons=[MDFlatButton(text="Yes",
                                  on_press=lambda x: ButtonsActions.save_button(self.data_table.row_data)),
                     MDFlatButton(text="No", on_press=lambda x: self.dialog_save.dismiss())]
        )
        self.dialog_save.open()

    def load_button_output(self):
        self.dialog_load = MDDialog(
            title="Load?",
            type="custom",
            buttons=[MDFlatButton(text="Yes", on_press=lambda x: self.load_button_logic()),
                     MDFlatButton(text="No", on_press=lambda x: self.dialog_load.dismiss())]
        )
        self.dialog_load.open()

    def load_button_logic(self):
        new_row_data = SAXParser.sax_parser_of_save()
        self.data_table.row_data = new_row_data
        self.dialog_load.dismiss()

    def build(self):
        table_layout = AnchorLayout(anchor_x='left', anchor_y='center', size_hint=(1, 1))
        self.data_table = MDDataTable(
            use_pagination=True,
            size_hint=(0.9, 1),
            column_data=[("F.I.O", dp(100)),
                         ("Uchenaja zvanie", dp(30)),
                         ("Staj rabot", dp(30)),
                         ("Uchenaja stepen", dp(30)),
                         ("Kafedra", dp(30)),
                         ("Facult", dp(30))],
        )
        table_layout.add_widget(self.data_table)
        buttons_layout = StackLayout(orientation='bt-lr', size_hint=(0.2, 1))
        search_button = Button(text="Find", size_hint_y=0.2, on_press=search_button_action(self),
                               background_color=[0, 0, 0, 0.75])
        delete_button = Button(text="Delete", size_hint_y=0.2, on_press=delete_button_action(self),
                               background_color=[0, 0, 0, 0.75])
        save_button = Button(text="Save", size_hint_y=0.2, on_press=save_button_action(self),
                             background_color=[0, 0, 0, 0.75])
        load_button = Button(text="load", size_hint_y=0.2, on_press=load_button_action(self),
                             background_color=[0, 0, 0, 0.75])
        edit_button = Button(text="Add", size_hint_y=0.2, on_press=add_button_action(self),
                             background_color=[0, 0, 0, 0.75])
        buttons_layout.add_widget(save_button)
        buttons_layout.add_widget(load_button)
        buttons_layout.add_widget(search_button)
        buttons_layout.add_widget(delete_button)
        buttons_layout.add_widget(edit_button)
        main_layout = BoxLayout()
        main_layout.add_widget(table_layout)
        main_layout.add_widget(buttons_layout)
        return main_layout
