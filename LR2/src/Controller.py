import random
from xml.dom.minidom import parse, parseString, getDOMImplementation
import xml.sax
from dicttoxml import dicttoxml
import xmltodict

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarActionButton
from kivymd.uix.transition.transition import MDSlideTransition
from kivy.core.audio import SoundLoader
from kivymd.uix.toolbar.toolbar import MDActionBottomAppBarButton
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, ListProperty
from kivymd.uix.label.label import MDLabel

from src.Model import StudentEntry


class SortDialog(MDDialog):

    sort_argument = StringProperty('name')
    filter_argument = StringProperty('name')

    def __init__(self):
        super().__init__()
        sort_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "name",
                "height": 56,
                "on_release": lambda x=1: self.set_sort_argument('name'),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "surname",
                "height": 56,
                "on_release": lambda x=1: self.set_sort_argument('surname'),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "group",
                "height": 56,
                "on_release": lambda x=1: self.set_sort_argument('group'),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "average mark (ascending)",
                "height": 56,
                "on_release": lambda x=1: self.set_sort_argument('marks (a)'),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "average mark (descending)",
                "height": 56,
                "on_release": lambda x=1: self.set_sort_argument('marks (d)'),
            }
        ]
        filter_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "name",
                "height": 56,
                "on_release": lambda x=1: self.set_filter_argument('name'),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "surname",
                "height": 56,
                "on_release": lambda x=1: self.set_filter_argument('surname'),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "average mark (more than)",
                "height": 56,
                "on_release": lambda x=1: self.set_filter_argument('marks >'),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "average mark (less than)",
                "height": 56,
                "on_release": lambda x=1: self.set_filter_argument('marks <'),
            }
        ]

        self.sort_menu = MDDropdownMenu(
            caller=self.ids.sort_dropdown,
            items=sort_items,
            position="center",
            width_mult=4,
        )
        self.filter_menu = MDDropdownMenu(
            caller=self.ids.filter_dropdown,
            items=filter_items,
            position="center",
            width_mult=4,
        )
        self.sort_menu.bind()
        self.filter_menu.bind()

    def set_sort_argument(self, argument):
        self.sort_argument = argument
        self.ids.sort_dropdown.set_item(argument)
        self.sort_menu.dismiss()

    def set_filter_argument(self, argument):
        self.filter_argument = argument
        self.ids.filter_dropdown.set_item(argument)
        self.filter_menu.dismiss()

    def apply(self, *args):
        filter_state = self.ids.filter_checkbox.active
        sort_state = self.ids.sort_checkbox.active
        filter_parameter = self.ids.filter_textfield.text
        data = MDApp.get_running_app().root.ids.base_screen.ids.students_scroll_view.data

        MDApp.get_running_app().main_screen.ids.base_screen.data = data

        if sort_state is True:
            if self.sort_argument in ['name', 'surname', 'patronym', 'group']:
                data = sorted(data, key=lambda entry: entry[self.sort_argument])
            elif self.sort_argument in ['marks (a)']:
                data = sorted(data, key=lambda entry: sum(entry['marks']) / len(entry['marks']))
            elif self.sort_argument in ['marks (d)']:
                data = sorted(data, key=lambda entry: -sum(entry['marks']) / len(entry['marks']))

        if filter_state is True:
            if self.filter_argument in ['name', 'surname', 'patronym']:
                data = [elem for elem in data if filter_parameter in elem[self.filter_argument]]
            elif self.filter_argument in ['marks >']:
                data = [elem for elem in data if (sum(elem['marks']) / len(elem['marks'])) > float(filter_parameter)]
            elif self.filter_argument in ['marks <']:
                data = [elem for elem in data if (sum(elem['marks']) / len(elem['marks'])) < float(filter_parameter)]

        MDApp.get_running_app().root.ids.base_screen.ids.students_scroll_view.data = data


class UserCreateScreen(MDDialog):

    def apply(self):
        MDApp.get_running_app().main_screen.add_student(StudentEntry(group=self.ids.group_field.text,
                                                        name=self.ids.name_field.text,
                                                        surname=self.ids.surname_field.text,
                                                        patronym=self.ids.patronym_field.text))


class UserContentScreen(MDDialog):
    name = StringProperty()
    surname = StringProperty()
    patronym = StringProperty()
    group = StringProperty()
    marks = ListProperty()
    icon = StringProperty()
    description = StringProperty()

    def __init__(self, data):
        super().__init__()
        print('data marks', data['marks'])
        self.name = data['name']
        self.surname = data['surname']
        self.patronym = data['patronym']
        self.group = data['group']
        self.marks = data['marks']
        self.icon = data['icon']
        self.ids.marks_table_layout.add_widget(MDDataTable(
            use_pagination=False,
            check=False,
            column_data=[(str(i + 1), 5) for i in range(9)],
            row_data=[self.marks],
            background_color='#212121',
            pos_hint={"center_y": 0.5, "center_x": 0.5}

        ))


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    pass


class StudentItem(RecycleDataViewBehavior, MDBoxLayout):
    name = StringProperty()
    surname = StringProperty()
    patronym = StringProperty()
    group = StringProperty()
    marks = ListProperty()
    icon = StringProperty()
    description = StringProperty()
    callback = ObjectProperty()
    mean_mark = StringProperty()

    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def __init__(self):
        super().__init__()
        self.start = 0
        self.single_hit = 0
        self.timed_out = False
        self.touchup_triggered = False

    def open_user_dialog(self, data):
        UserContentScreen(data).open()

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super().refresh_view_attrs(rv, index, data)

    def on_single_press(self, touch):

        if len(MDApp.get_running_app().root.ids.base_screen.ids.students_scroll_view.layout_manager.selected_nodes) > 0:
            Clock.schedule_once(self.callback)
            return self.parent.select_with_touch(self.index, touch)
        else:
            data = MDApp.get_running_app().root.ids.base_screen.ids.students_scroll_view.data[self.index]
            print(data)
            self.open_user_dialog(data)

    def on_long_press(self, touch):
        if len(MDApp.get_running_app().root.ids.base_screen.ids.students_scroll_view.layout_manager.selected_nodes) == 0:
            Clock.schedule_once(self.callback)
            return self.parent.select_with_touch(self.index, touch)

    def on_touch_down(self, touch):
        self.timed_out = False
        self.touchup_triggered = False

        if self.collide_point(touch.x, touch.y):

            def timeout(*args):
                self.timed_out = True

            def callback(*args):
                self.on_long_touch_up(touch)

            Clock.schedule_once(timeout, 0.4)
            Clock.schedule_once(callback, 0.4)
        else:
            return super().on_touch_down(touch)

    def on_long_touch_up(self, touch):
        if self.timed_out and not self.touchup_triggered:
            self.on_long_press(touch)

    def on_touch_up(self, touch):
        if not self.timed_out:
            self.touchup_triggered = True

            if self.collide_point(touch.x, touch.y):
                self.on_single_press(touch)
            else:
                return super().on_touch_down(touch)
        else:
            self.timed_out = False

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        rv.data[index]["selected"] = is_selected


class BaseScreen(Screen):
    selected_cards = False
    snackbar = None
    data = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Download",
                "height": (56),
                "on_release": lambda x=1: self.menu_callback('Download'),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Upload",
                "height": (56),
                "on_release": lambda x=1: self.menu_callback('Upload'),
            }
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def download_data(self):
        file = open('database.xml', 'rb')
        input_str = file.read()
        input_dict = xmltodict.parse(input_str)['root']
        print(input_dict)
        for elem in input_dict.keys():
            elem = input_dict[elem]
            marks = [int(x['#text']) for x in elem['marks']['item']]
            surname = elem['surname']['#text'] if len(elem['surname']) > 1 else ''
            patronym = elem['patronym']['#text'] if len(elem['patronym']) > 1 else ''
            description = elem['description']['#text'] if len(elem['description']) > 1 else ''
            self.ids.students_scroll_view.data.append(
                {
                    'group': elem['group']['#text'],
                    'name': elem['name']['#text'],
                    'surname': surname,
                    'patronym': patronym,
                    'icon': elem['icon']['#text'],
                    'marks': marks,
                    'mean_mark': str(sum(marks) / len(marks))[:3],
                    'description': description,
                    'selected': False,
                    'callback': self.on_tap_card
                })


    def upload_data(self):
        data = MDApp.get_running_app().root.ids.base_screen.ids.students_scroll_view.data
        output = dict()

        for i, elem in enumerate(data):
            entry = dict()
            for k, v in elem.items():
                if k not in ['callback', 'selected', 'mean_mark']:
                    entry[k] = v
            print(entry)
            output[i] = entry

        file = open('database.xml', 'wb')
        file.write(dicttoxml(output))
        file.close()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        if text_item is 'Download':
            self.download_data()
        elif text_item is 'Upload':
            self.upload_data()

    def open_sort_dialog(self, *args):
        SortDialog().open()

    def show_data(self, *args):
        if self.data is not None:
            MDApp.get_running_app().root.ids.base_screen.ids.students_scroll_view.data = self.data

    def toggle_button_menu(self, root):
        if root.ids.topbar.is_active is False:
            root.ids.topbar_manager.transition = MDSlideTransition(direction='down')
            root.ids.topbar_manager.current = 'topbar_buttons'
            root.ids.topbar.is_active = True
            root.ids.topbar.left_action_items = [['triangle', lambda x: self.toggle_button_menu(root)]]
        else:
            root.ids.topbar_manager.transition = MDSlideTransition(direction='up')
            root.ids.topbar_manager.current = 'empty_screen'
            root.ids.topbar.is_active = False
            root.ids.topbar.left_action_items = [['menu', lambda x: self.toggle_button_menu(root)]]

    def open_create_user_dialog(self):
        UserCreateScreen().open()

    def on_tap_card(self, *args):
        datas = [data["selected"] for data in self.ids.students_scroll_view.data]
        if True in datas and not self.selected_cards:
            self.ids.bottom_appbar.action_items = [
                MDActionBottomAppBarButton(icon="trash-can-outline", on_press=self.remove_selected_data),
                MDActionBottomAppBarButton(icon="star", on_press=self.call_favorites_snackbar),
                MDActionBottomAppBarButton(icon="flag", on_press=self.call_report_snackbar),
            ]
            self.ids.fab_button.icon = "pencil"
            self.selected_cards = True
        else:
            if len(list(set(datas))) == 1 and not list(set(datas))[0]:
                self.selected_cards = False
            if not self.selected_cards:
                self.ids.bottom_appbar.action_items = [
                    MDActionBottomAppBarButton(icon="magnify", on_press=self.open_sort_dialog),
                    MDActionBottomAppBarButton(icon="keyboard-return", on_press=self.show_data),
                ]
                self.ids.fab_button.icon = "plus"

    def remove_selected_data(self, *args):
        print([data["selected"] for data in self.ids.students_scroll_view.data])
        print(self.ids.students_scroll_view.layout_manager.selected_nodes)
        sv = self.ids.students_scroll_view
        entry_list = [sv.data[i] for i in sv.layout_manager.selected_nodes]

        sv.layout_manager.clear_selection()

        for entry in entry_list:
            sv.data.remove(entry)

        self.on_tap_card()

    def close_snackbar(self, *args):
        self.snackbar.dismiss()

    def open_snackbar(self, text):
        if self.snackbar is not None:
            self.close_snackbar()

        self.snackbar = MDSnackbar(
            MDLabel(
                text=text,
                theme_text_color="Custom",
                text_color="#8E353C",
            ),
            MDSnackbarActionButton(
                text="Done",
                theme_text_color="Custom",
                text_color="#8E353C",
                font_size=16,
                on_release=self.close_snackbar,
                pos_hint={'center_y': 0.5, 'x': 0.8}),
            y=48,
            pos_hint={"center_x": 0.5},
            size_hint_x=0.6,
            md_bg_color="#fee9e2",
        )
        self.snackbar.open()

    def call_favorites_snackbar(self, *args):
        self.open_snackbar('Added to favorites.')

    def call_report_snackbar(self, *args):
        self.open_snackbar('Report sent.')


class Root(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_student(self, student_entry):

        marks = [random.randint(3, 10) for _ in range(9)] if student_entry.marks is None else student_entry.marks
        icon = 'assets/empty_profile_icon.png' if student_entry.icon is None else student_entry.icon
        patronym = '' if student_entry.patronym is None else student_entry.patronym
        description = '' if student_entry.description is None else student_entry.description

        self.ids.base_screen.ids.students_scroll_view.data.append(
            {
                'group': student_entry.group,
                'name': student_entry.name,
                'surname': student_entry.surname,
                'patronym': patronym,
                'icon': icon,
                'marks': marks,
                'mean_mark': str(sum(marks) / len(marks))[:3],
                'description': description,
                'selected': False,
                'callback': self.ids.base_screen.on_tap_card
            }
        )


class Test(MDApp):

    def on_start(self):
        self.main_screen.add_student(StudentEntry(group='121701', name='Alexander', surname='Isaychikov',
                                     patronym='Igorevitch', description='Hello, my name is Alexander'))
        self.main_screen.add_student(StudentEntry(group='121703', name='Natariel', surname='Everlicht', icon='assets/start.jpg'))
        self.main_screen.add_student(StudentEntry(group='121701', name='Azazel', surname='Gideona', patronym='Arma'))
        self.main_screen.add_student(StudentEntry(group='121702', name='Serazil', surname='Bloodthirst XIV'))
        self.main_screen.add_student(StudentEntry(group='121701', name='Fall-from-Grace', surname='', icon='assets/darkholme1.jpg'))
        self.main_screen.add_student(StudentEntry(group='121701', name='Michael', surname='The Heiliger'))
        self.main_screen.add_student(StudentEntry(group='121701', name='Michael', surname='The Heiliger'))
        self.main_screen.add_student(StudentEntry(group='121701', name='Michael', surname='The Heiliger'))
        self.main_screen.add_student(StudentEntry(group='121701', name='Michael', surname='The Heiliger'))
        self.main_screen.add_student(StudentEntry(group='121701', name='Michael', surname='The Heiliger'))
        self.main_screen.add_student(StudentEntry(group='121701', name='Michael', surname='The Heiliger'))

    def __init__(self):
        super().__init__()
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        self.sound = SoundLoader.load('assets/magic.mp3')

        Builder.load_file('src/View/baseScreen.kv')
        Builder.load_file('src/View/MDDataTable.kv')
        Builder.load_file('src/View/sortDialogScreen.kv')
        Builder.load_file('src/View/studentItem.kv')
        Builder.load_file('src/View/transitionScreen.kv')
        Builder.load_file('src/View/userContentScreen.kv')
        Builder.load_file('src/View/userCreateScreen.kv')

        self.main_screen = Root()

        Clock.schedule_once(self.splash_phase_1, 0.25)

    def splash_phase_1(self, time):
        self.main_screen.current = 'empty_white_screen'
        Clock.schedule_once(self.splash_phase_2, 1)

    def splash_phase_2(self, time):
        self.main_screen.current = 'logo_screen'
        Clock.schedule_once(self.splash_phase_3, 2)
        if self.sound:
            self.sound.play()

    def splash_phase_3(self, time):
        self.main_screen.current = 'empty_white_screen'
        Clock.schedule_once(self.splash_phase_4, 0.5)

    def splash_phase_4(self, time):
        self.main_screen.current = 'main_screen'

    def build(self):
        return self.main_screen
