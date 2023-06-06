from kivymd.app import MDApp

from kivy.metrics import dp

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDFlatButton

from kivymd.uix.boxlayout import MDBoxLayout

from kivy.core.window import Window


def write(something):
    f = open('text.txt', "w")
    for i in range(len(something)):
        for index in something[i]:
            f.write(index+'\t')
        f.write('\n')
    f.close()



class MyApp(MDApp):
    def build(self):
        self.table = MDDataTable(
            use_pagination=True,
            column_data=[
                ('ФИО игрока', dp(35)),
                ('Дата рождения', dp(20)),
                ('Футбольная команда', dp(35)),
                ('Домашний город', dp(25)),
                ('Номер игрока', dp(20)),
                ('Позиция', dp(25))
            ]
        )
        box = MDBoxLayout(orientation = 'vertical')
        bl = MDBoxLayout(orientation='horizontal', size_hint=[.07,.07])
        bl.add_widget(MDRaisedButton(text='Добавить', on_release=self.add))
        bl.add_widget(MDRaisedButton(text='Удалить', on_release=self.remove))
        bl.add_widget(MDRaisedButton(text='Искать', on_release=self.search))
        bl.add_widget(MDRaisedButton(text='Сохранить', on_release=self.save))
        bl.add_widget(MDRaisedButton(text='Загрузить', on_release=self.clear))

        box.add_widget(bl)
        box.add_widget(self.table)

        return box

    # ДОБАВЛЕНИЕ ИГРОКА!
    def add(self, instance_button: MDRaisedButton):
        self.add_new_player()

    button_add = None

    def add_new_player(self, *args):
        if not self.button_add:
            self.button_add = MDDialog(
                title='Добавление нового игрока',
                type="custom",
                content_cls=MDBoxLayout(
                    MDTextField(
                        id='name',
                        hint_text="ФИО игрока",
                    ),
                    MDTextField(
                        id='data',
                        hint_text="Дата рождения",
                    ),
                    MDTextField(
                        id='team',
                        hint_text="Футбольная команда",
                    ),
                    MDTextField(
                        id='city',
                        hint_text="Домашний город",
                    ),
                    MDTextField(
                        id='number',
                        hint_text="Номер игрока",
                    ),
                    MDTextField(
                        id='position',
                        hint_text="Позиция",
                    ),
                    orientation="vertical",
                    spacing="15dp",
                    size_hint_y=None,
                    height="420dp"
                ),
                buttons=[
                    MDFlatButton(
                        text="Отмена",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_add_dialog
                    ),
                    MDFlatButton(
                        text="Ок",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.info_about_player
                    ),
                ],
            )
        self.button_add.open()

    def close_add_dialog(self, *args):
        self.button_add.dismiss()

    def check_of_line(self):
        for i in self.button_add.content_cls.ids:
            if self.button_add.content_cls.ids[i].text == '':
                return False
        for j in range(len(self.button_add.content_cls.ids.data.text)):
            if self.button_add.content_cls.ids.data.text[j].isalpha():
                return False
        for j in range(len(self.button_add.content_cls.ids.number.text)):
            if self.button_add.content_cls.ids.number.text[j].isalpha():
                return False
        return True

    def info_about_player(self, *args):
        if self.check_of_line():
            new_player = [self.button_add.content_cls.ids.name.text, self.button_add.content_cls.ids.data.text,
                          self.button_add.content_cls.ids.team.text, self.button_add.content_cls.ids.city.text,
                          self.button_add.content_cls.ids.number.text, self.button_add.content_cls.ids.position.text]
            if not new_player in self.table.row_data:
                self.table.row_data.append(new_player)
                self.button_add.dismiss()
            else:
                self.button_add.dismiss()

    # -------------------------------------------------------------------------------------------------------------------
    # УДАЛЕНИЕ ИГРОКА!
    def remove(self, instance_button: MDRaisedButton):
        self.remove_player()

    button_remove = None

    def remove_player(self, *args):
        if not self.button_remove:
            self.button_remove = MDDialog(
                title='Удаление игрока',
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="ФИО",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.remove_first
                    ),
                    MDFlatButton(
                        text="Позиция",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.remove_second
                    ),
                    MDFlatButton(
                        text="Команда",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.remove_third
                    ),
                ],
            )
        self.button_remove.open()

    button_name = None

    def remove_first(self, *args):
        self.button_remove.dismiss()
        if not self.button_name:
            self.button_name = MDDialog(
                title='Удаление по ФИО и дате рождения',
                type='custom',
                content_cls=MDBoxLayout(
                    MDTextField(
                        id='search_name',
                        hint_text='ФИО игрока',
                    ),
                    MDTextField(
                        id='search_data',
                        hint_text='Дата рождения',
                    ),
                    orientation="vertical",
                    spacing="15dp",
                    size_hint_y=None,
                    height="100dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Ок",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.rezult_of_remove_by_name
                    )
                ]
            )
        self.button_name.open()

    def rezult_name(self, *args):
        rez_of_name = []
        task1 = self.button_name.content_cls.ids.search_name.text
        task2 = self.button_name.content_cls.ids.search_data.text
        for i in range(len(self.table.row_data)):
            if self.table.row_data[i][0] == task1 and self.table.row_data[i][1] == task2:
                rez_of_name.append(self.table.row_data[i])
        return rez_of_name

    def rezult_of_remove_by_name(self, *args):
        remove_names = self.rezult_name()
        for i in range(len(remove_names)):
            self.table.row_data.remove(remove_names[i])
        self.button_name.dismiss()

    button_position = None

    def remove_second(self, *args):
        self.button_remove.dismiss()
        if not self.button_position:
            self.button_position = MDDialog(
                title='Удаление по позиции',
                type='custom',
                content_cls=MDBoxLayout(
                    MDTextField(
                        id='search_position',
                        hint_text='Позиция',
                    ),
                    orientation="vertical",
                    spacing="15dp",
                    size_hint_y=None,
                    height="50dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Ок",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.rezult_of_remove_by_position
                    )
                ]
            )
        self.button_position.open()

    def rezult_position(self, *args):
        rez_of_position = []
        task = self.button_position.content_cls.ids.search_position.text
        for i in range(len(self.table.row_data)):
            if self.table.row_data[i][5] == task:
                rez_of_position.append(self.table.row_data[i])
        return rez_of_position

    def rezult_of_remove_by_position(self, *args):
        remove_positions = self.rezult_position()
        for i in range(len(remove_positions)):
            self.table.row_data.remove(remove_positions[i])
        self.button_position.dismiss()

    button_team = None

    def remove_third(self, *args):
        self.button_remove.dismiss()
        if not self.button_team:
            self.button_team = MDDialog(
                title='Удаление по команде',
                type='custom',
                content_cls=MDBoxLayout(
                    MDTextField(
                        id='search_team',
                        hint_text='Команда',
                    ),
                    orientation="vertical",
                    spacing="15dp",
                    size_hint_y=None,
                    height="50dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Ок",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.rezult_of_remove_by_team
                    )
                ]
            )
        self.button_team.open()

    def rezult_team(self, *args):
        rez_of_team = []
        task = self.button_team.content_cls.ids.search_team.text
        for i in range(len(self.table.row_data)):
            if self.table.row_data[i][2] == task:
                rez_of_team.append(self.table.row_data[i])
        return rez_of_team

    def rezult_of_remove_by_team(self, *args):
        remove_teams = self.rezult_team()
        for i in range(len(remove_teams)):
            self.table.row_data.remove(remove_teams[i])
        self.button_team.dismiss()

    # ----------------------------------------------------------------------------------------------------------------------
    # ПОИСК ИГРОКА!

    def search(self, instance_button: MDRaisedButton):
        self.search_player()

    button_search = None

    def search_player(self, *args):
        if not self.button_search:
            self.button_search = MDDialog(
                title='Поиск игрока',
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="ФИО",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.search_first
                    ),
                    MDFlatButton(
                        text="Позиция",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.search_second
                    ),
                    MDFlatButton(
                        text="Команда",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.search_third
                    ),
                ],
            )
        self.button_search.open()

    button_name_search = None

    def search_first(self, *args):
        self.button_search.dismiss()
        if not self.button_name_search:
            self.button_name_search = MDDialog(
                title='Поиск по ФИО и дате рождения',
                type='custom',
                content_cls=MDBoxLayout(
                    MDTextField(
                        id='search_name',
                        hint_text='ФИО игрока',
                    ),
                    MDTextField(
                        id='search_data',
                        hint_text='Дата рождения',
                    ),
                    orientation="vertical",
                    spacing="15dp",
                    size_hint_y=None,
                    height="100dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Ок",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.rezult_of_search_by_name
                    )
                ]
            )
        self.button_name_search.open()

    def rezult_name_search(self, *args):
        rez_of_name = []
        task1 = self.button_name_search.content_cls.ids.search_name.text
        task2 = self.button_name_search.content_cls.ids.search_data.text
        for i in range(len(self.table.row_data)):
            if self.table.row_data[i][0] == task1 and self.table.row_data[i][1] == task2:
                rez_of_name.append(self.table.row_data[i])
        return rez_of_name

    search_by_name = None

    def rezult_of_search_by_name(self, *args):
        search_names = self.rezult_name_search()
        self.button_name_search.dismiss()
        if not self.search_by_name:
            self.search_by_name = MDDialog(
                title='По ФИО и дате рождения',
                type="custom",
                content_cls=MDBoxLayout(
                    MDDataTable(
                        use_pagination=True,
                        column_data=[
                            ('ФИО игрока', dp(35)),
                            ('Дата рождения', dp(20)),
                            ('Футбольная команда', dp(35)),
                            ('Домашний город', dp(25)),
                            ('Номер игрока', dp(20)),
                            ('Позиция', dp(25))
                        ],
                        row_data=search_names
                    ),
                    spacing="15dp",
                    size_hint_y=None,
                    height="505dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Закрыть",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.closed_first
                    ),
                ],
            )
        self.search_by_name.open()

    def closed_first(self, *args):
        self.search_by_name.dismiss()

    button_position_search = None

    def search_second(self, *args):
        self.button_search.dismiss()
        if not self.button_position_search:
            self.button_position_search = MDDialog(
                title='Поиск по позиции',
                type='custom',
                content_cls=MDBoxLayout(
                    MDTextField(
                        id='search_position',
                        hint_text='Позиция',
                    ),
                    orientation="vertical",
                    spacing="15dp",
                    size_hint_y=None,
                    height="50dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Ок",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.rezult_of_search_by_position
                    )
                ]
            )
        self.button_position_search.open()

    def rezult_position_search(self, *args):
        rez_of_position = []
        task = self.button_position_search.content_cls.ids.search_position.text
        for i in range(len(self.table.row_data)):
            if self.table.row_data[i][5] == task:
                rez_of_position.append(self.table.row_data[i])
        return rez_of_position

    search_by_position = None

    def rezult_of_search_by_position(self, *args):
        search_positions = self.rezult_position_search()
        self.button_position_search.dismiss()
        if not self.search_by_position:
            self.search_by_position = MDDialog(
                title='По позиции',
                type="custom",
                content_cls=MDBoxLayout(
                    MDDataTable(
                        use_pagination=True,
                        column_data=[
                            ('ФИО игрока', dp(35)),
                            ('Дата рождения', dp(20)),
                            ('Футбольная команда', dp(35)),
                            ('Домашний город', dp(25)),
                            ('Номер игрока', dp(20)),
                            ('Позиция', dp(25))
                        ],
                        row_data=search_positions
                    ),
                    spacing="15dp",
                    size_hint_y=None,
                    height="505dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Закрыть",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.closed_second
                    ),
                ],
            )
        self.search_by_position.open()

    def closed_second(self, *args):
        self.search_by_position.dismiss()

    button_team_search = None

    def search_third(self, *args):
        self.button_search.dismiss()
        if not self.button_team_search:
            self.button_team_search = MDDialog(
                title='Поиск по команде',
                type='custom',
                content_cls=MDBoxLayout(
                    MDTextField(
                        id='search_team',
                        hint_text='Команда',
                    ),
                    orientation="vertical",
                    spacing="15dp",
                    size_hint_y=None,
                    height="50dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Ок",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.rezult_of_search_by_team
                    )
                ]
            )
        self.button_team_search.open()

    def rezult_team_search(self, *args):
        rez_of_team = []
        task = self.button_team_search.content_cls.ids.search_team.text
        for i in range(len(self.table.row_data)):
            if self.table.row_data[i][2] == task:
                rez_of_team.append(self.table.row_data[i])
        return rez_of_team

    search_by_team = None

    def rezult_of_search_by_team(self, *args):
        search_teams = self.rezult_team_search()
        self.button_team_search.dismiss()
        if not self.search_by_team:
            self.search_by_team = MDDialog(
                title='По команде',
                type="custom",
                content_cls=MDBoxLayout(
                    MDDataTable(
                        use_pagination=True,
                        column_data=[
                            ('ФИО игрока', dp(35)),
                            ('Дата рождения', dp(20)),
                            ('Футбольная команда', dp(35)),
                            ('Домашний город', dp(25)),
                            ('Номер игрока', dp(20)),
                            ('Позиция', dp(25))
                        ],
                        row_data=search_teams
                    ),
                    spacing="15dp",
                    size_hint_y=None,
                    height="505dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Закрыть",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.closed_third
                    ),
                ],
            )
        self.search_by_team.open()

    def closed_third(self, *args):
        self.search_by_team.dismiss()

#--------------------------------------------------------------------------------------------------------------------
#СОХРАНЕНИЕ!

    def save(self, instance_button: MDRaisedButton):
        write(self.table.row_data)

#--------------------------------------------------------------------------------------------------------------------
#ЗАГРУЗКА!

    def clear(self, instance_button: MDRaisedButton):
        for i in range(len(self.table.row_data)):
            self.table.row_data.remove(i)
        self.read()


    def read(self):
        f = open("text.txt")
        lines = f.readlines()
        rez = []
        for i in range(len(lines)):
            rez.append([])
            word = ''
            for j in range(len(lines[i])):
                if lines[i][j] == '\t':
                    rez[i].append(word)
                    word = ''
                elif lines[i][j] == '\n':
                    continue
                else:
                    word += lines[i][j]

        for i in range(len(rez)):
            self.table.row_data.append(rez[i])


MyApp().run()
