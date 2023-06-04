import read_file
import write_file
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.metrics import dp

players = read_file.read_xml('players.xml')


class MyApp(MDApp):
    title = "Football Players"
    def build(self):
        screen = Screen()

        main_gl = MDGridLayout(rows = 10, cols = 1)
        bl_labels = MDBoxLayout(orientation='horizontal', size_hint=[1, 0.2], padding = dp(20), spacing=dp(15))

        search_button = Button(text="Поиск", on_press=self.btn_press_call_search)
        delete_button = Button(text="Удаление", on_press=self.btn_press_call_delete)
        add_button = Button(text="Добавление", on_press=self.btn_press_call_add)

        bl_labels.add_widget(search_button)
        bl_labels.add_widget(delete_button)
        bl_labels.add_widget(add_button)

        self.table = MDDataTable(size_hint=[1, 1], check=False,
                            use_pagination=True,
                            column_data=[("ФИО", dp(70)),
                                         ("Дата", dp(70)),
                                         ("Команда", dp(70)),
                                         ("Город", dp(70)),
                                         ("Состав", dp(70)),
                                         ("Позиция", dp(70))],
                            row_data=players
                            )

        bl_delete = MDBoxLayout(orientation='vertical')

        self.what_delete = Spinner(
            text='Выберите условие удаления',
            values=('ФИО', 'Дата', 'Команда', 'Город', 'Состав'),
            size_hint=[1, .8]
        )

        self.what_search = Spinner(
            text='Выберите условие поиска',
            values=('ФИО','Дата', 'Команда', 'Город', 'Состав'),
            size_hint=[1, .8]
        )

        self.label_delete = Label()
        self.text_input_delete = TextInput(multiline=False)

        bl_delete.add_widget(self.what_delete)
        bl_delete.add_widget(self.label_delete)
        bl_delete.add_widget(self.text_input_delete)
        bl_delete.add_widget(Button(text='Удалить', on_press=self.btn_press_delete))

        self.delete_popup = Popup(content=bl_delete, title='Окно удаления', size_hint=[.35, .5])

        bl_search = MDBoxLayout(orientation='vertical')

        self.search_popup = Popup(content=bl_search, title='Окно поиска', size_hint=[0.8, 0.8])

        self.table_search = MDDataTable(size_hint=[1, 1], check=False,
                                use_pagination=True,
                                column_data=[("ФИО", dp(30)),
                                            ("Дата", dp(10)),
                                            ("Команда", dp(15)),
                                            ("Город", dp(25)),
                                            ("Состав", dp(25)),
                                            ("Позиция", dp(25))],
                                 )
        self.label_search = Label()
        self.text_input_search = TextInput(multiline=False, size_hint=[1, .7])

        bl_search_menu = MDBoxLayout(orientation='vertical', size_hint=[1, 1], spacing=dp(10), padding=dp(10))

        bl_search_menu.add_widget(self.what_search)
        bl_search_menu.add_widget(self.label_search)
        bl_search_menu.add_widget(self.text_input_search)
        bl_search_menu.add_widget(Button(text='Поиск', on_press=self.btn_press_search, size_hint=[1, .7]))

        bl_search.add_widget(self.table_search)
        bl_search.add_widget(bl_search_menu)

        bl_add = MDBoxLayout(orientation='vertical')

        self.text_input_1 = TextInput(hint_text='ФИО', multiline=False)
        bl_add.add_widget(self.text_input_1)
        self.text_input_2 = TextInput(hint_text='Дата', multiline=False)
        bl_add.add_widget(self.text_input_2)
        self.text_input_3 = TextInput(hint_text='Команда', multiline=False)
        bl_add.add_widget(self.text_input_3)
        self.text_input_4 = TextInput(hint_text='Город', multiline=False)
        bl_add.add_widget(self.text_input_4)
        self.text_input_5 = TextInput(hint_text='Состав', multiline=False)
        bl_add.add_widget(self.text_input_5)
        self.text_input_6 = TextInput(hint_text='Позиция', multiline=False)
        bl_add.add_widget(self.text_input_6)
        bl_add.add_widget(Button(text='Добавить', on_press=self.btn_press_add))


        self.add_popup = Popup(title='Окно добавления', size_hint=[.8, .6], content=bl_add)

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"

        main_gl.add_widget(self.table)
        main_gl.add_widget(bl_labels)
        screen.add_widget(main_gl)
        return screen

    def btn_press_call_delete(self, instance):
        self.delete_popup.open()

    def btn_press_call_search(self, instance):
        self.search_popup.open()

    def btn_press_call_add(self, instance):
        self.add_popup.open()

    def btn_press_delete(self, instance):
        index = -1
        buffer = read_file.read_xml('players.xml')
        counter = 0
        if self.what_delete.text == 'ФИО':
            index = 0
        elif self.what_delete.text == 'Дата':
            index = 1
        elif self.what_delete.text == 'Команда':
            index = 2
        elif self.what_delete.text == 'Город':
            index = 3
        elif self.what_delete.text == 'Состав':
            index = 4

        if index == -1:
            self.label_delete.text = 'Выберите условие'
            counter = -1
        if index != -1:
            counter = 0
            for player in buffer:
                if player[index] == self.text_input_delete.text:
                    players.remove(player)
                    counter += 1
        write_file.write(players, 'players.xml')
        if counter == 0:
            self.label_delete.text = 'Совпадений не найдено'
        elif counter != 0 and counter != -1:
            self.label_delete.text = 'Было удалено ' + str(counter) + ' записей'
        self.table.update_row_data(self.table.row_data, players)

    def btn_press_search(self, instance):
        search_output = []
        counter = 0
        index = -1
        if self.what_search.text == 'ФИО':
            index = 0
        elif self.what_search.text == 'Дата':
            index = 1
        elif self.what_search.text == 'Команда':
            index = 2
        elif self.what_search.text == 'Город':
            index = 3
        elif self.what_search.text == 'Состав':
            index = 4

        if index == -1:
            self.label_search.text = 'Выберите условие'
            counter = -1
        if index != -1:
            counter = 0
            for player in players:
                if str(player[index]) == str(self.text_input_search.text):
                    search_output.append(player)
                    counter += 1
        if counter == 0:
            self.label_search.text = 'Совпадений не найдено'
        elif counter != 0 and counter != -1:
            self.table_search.update_row_data(self.table_search.row_data, search_output)
            self.label_search.text = ''

    def btn_press_add(self, instance):
        player = []
        player.append(self.text_input_1.text)
        player.append(self.text_input_2.text)
        player.append(self.text_input_3.text)
        player.append(self.text_input_4.text)
        player.append(self.text_input_5.text)
        player.append(self.text_input_6.text)
        players.append(player)
        self.table.update_row_data(self.table.row_data, players)
        write_file.write(players, 'players.xml')

MyApp().run()