from kivymd.app import MDApp
import read_file
import write_file
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.metrics import dp

teachers = read_file.read_xml('teachers.xml')


class MyApp(MDApp):
    def build(self):
        screen = Screen()

        main_gl = MDGridLayout(rows=1)
        bl_labels = MDBoxLayout(orientation='vertical', size_hint=[.2, 1], padding=dp(30), spacing=dp(150),)

        search_button = Button(text="Поиск", font_size="40", on_press=self.btn_press_call_search)
        delete_button = Button(text="Удаление", font_size="40", on_press=self.btn_press_call_delete)
        add_button = Button(text="Добавление", font_size="40", on_press=self.btn_press_call_add)

        bl_labels.add_widget(search_button)
        bl_labels.add_widget(delete_button)
        bl_labels.add_widget(add_button)

        self.table = MDDataTable(size_hint=[.7, 1], check=False,
                            use_pagination=True,
                            column_data=[("Факультет", dp(35)),
                                         ("Название\n кафедры", dp(40)),
                                         ("        ФИО\n преподавателя", dp(45)),
                                         ("Ученое\n звание", dp(40)),
                                         ("Ученая\n степень", dp(55)),
                                         (" Стаж\nработы", dp(25))],
                            row_data=teachers,
                                 elevation=2,
                                 pagination_menu_pos="center"
                            )

        bl_delete = MDBoxLayout(orientation='vertical', spacing=dp(20), padding=dp(20))

        self.what_delete = Spinner(
            text='Выберите условие удаления',
            values=('Факультет', '        ФИО\nпреподавателя', 'Название\n кафедры', 'Ученое\nзвание', ' Стаж\nработы'),
            size_hint=[1, .5]
        )

        self.what_search = Spinner(
            text='Выберите условие поиска',
            values=('Факультет', '        ФИО\nпреподавателя', 'Название\n кафедры', 'Ученое\nзвание', ' Стаж\nработы'),
            size_hint=[1, .4]
        )

        self.label_delete = Label()
        self.text_input_delete = TextInput(multiline=False, size_hint=[1, .35])

        bl_delete.add_widget(self.what_delete)
        bl_delete.add_widget(self.label_delete)
        bl_delete.add_widget(self.text_input_delete)
        bl_delete.add_widget(Button(text='Удалить', font_size="30", on_press=self.btn_press_delete))

        self.delete_popup = Popup(content=bl_delete, title='Окно удаления', size_hint=[.4, .8])

        bl_search = MDBoxLayout(orientation='horizontal')

        self.search_popup = Popup(content=bl_search, title='Окно поиска', size_hint=[.9, .8])

        self.table_search = MDDataTable(size_hint=[.7, 1], check=False,
                                 use_pagination=True,
                                 column_data=[("Факультет", dp(25)),
                                         ("Название\n кафедры", dp(30)),
                                         ("        ФИО\nпреподавателя", dp(35)),
                                         ("Ученое\nзвание", dp(30)),
                                         ("Ученая\nстепень", dp(45)),
                                         (" Стаж\nработы", dp(15))]
                                 )
        self.label_search = Label()
        self.text_input_search = TextInput(multiline=False, size_hint=[1, .35])

        bl_search_menu = MDBoxLayout(orientation='vertical', size_hint=[.3, 1], spacing=dp(30), padding=dp(30))

        bl_search_menu.add_widget(self.what_search)
        bl_search_menu.add_widget(self.label_search)
        bl_search_menu.add_widget(self.text_input_search)
        bl_search_menu.add_widget(Button(text='Поиск', on_press=self.btn_press_search, size_hint=[1, .3]))

        bl_search.add_widget(self.table_search)
        bl_search.add_widget(bl_search_menu)

        bl_add = MDBoxLayout(orientation='vertical', spacing=dp(15), padding=dp(15))

        self.text_input_1 = TextInput(hint_text='Факультет', multiline=False)
        bl_add.add_widget(self.text_input_1)
        self.text_input_2 = TextInput(hint_text='Название кафедры', multiline=False)
        bl_add.add_widget(self.text_input_2)
        self.text_input_3 = TextInput(hint_text='ФИО преподавателя', multiline=False)
        bl_add.add_widget(self.text_input_3)
        self.text_input_4 = TextInput(hint_text='Ученое звание', multiline=False)
        bl_add.add_widget(self.text_input_4)
        self.text_input_5 = TextInput(hint_text='Ученая степень', multiline=False)
        bl_add.add_widget(self.text_input_5)
        self.text_input_6 = TextInput(hint_text='Стаж работы', multiline=False)
        bl_add.add_widget(self.text_input_6)
        bl_add.add_widget(Button(text='Добавить', on_press=self.btn_press_add))


        self.add_popup = Popup(title='Окно добавления', size_hint=[.8, .6], content=bl_add)

        main_gl.add_widget(self.table)
        main_gl.add_widget(bl_labels)
        screen.add_widget(main_gl)
        return screen

    def btn_press_save(self, instance):
        write_file.write(teachers, self.path.text)

    def btn_press_call_delete(self, instance):
        self.delete_popup.open()

    def btn_press_call_search(self, instance):
        self.search_popup.open()

    def btn_press_call_add(self, instance):
        self.add_popup.open()

    def btn_press_delete(self, instance):
        index = -1
        buffer = read_file.read_xml('teachers.xml')
        counter = 0
        if self.what_delete.text == 'Факультет':
            index = 0
        elif self.what_delete.text == 'Название\n кафедры':
            index = 1
        elif self.what_delete.text == '        ФИО\nпреподавателя':
            index = 2
        elif self.what_delete.text == 'Ученое\nзвание':
            index = 3
        elif self.what_delete.text == ' Стаж\nработы':
            index = 5

        if index == -1:
            self.label_delete.text = 'Вы не указали условие удаления'
            counter = -1
        if index != -1 and index != 5:
            counter = 0
            for teacher in buffer:
                if teacher[index] == self.text_input_delete.text:
                    teachers.remove(teacher)
                    counter += 1
        if index == 5:
            counter = 0
            print(len(buffer))
            for teacher in buffer:
                print(teacher)
                if int(teacher[index]) == int(self.text_input_delete.text):
                    teachers.remove(teacher)
                    counter += 1
        write_file.write(teachers, 'teachers.xml')
        if counter == 0:
            self.label_delete.text = 'По вашему запросу ничего не найдено'
        elif counter != 0 and counter != -1:
            self.label_delete.text = 'Было удалено ' + str(counter) + ' записей'
        self.table.update_row_data(self.table.row_data, teachers)

    def btn_press_search(self, instance):
        search_output = []
        counter = 0
        index = -1
        if self.what_search.text == 'Факультет':
            index = 0
        elif self.what_search.text == 'Название\n кафедры':
            index = 1
        elif self.what_search.text == '        ФИО\nпреподавателя':
            index = 2
        elif self.what_search.text == 'Ученое\nзвание':
            index = 3
        elif self.what_search.text == ' Стаж\nработы':
            index = 5

        if index == -1:
            self.label_search.text = 'Вы не указали условие поиска'
            counter = -1
        if index != -1 and index != 5:
            counter = 0
            for teacher in teachers:
                if teacher[index] == self.text_input_search.text:
                    search_output.append(teacher)
                    counter += 1
        if index == 5:
            counter = 0
            for teacher in teachers:
                if int(teacher[index]) == int(self.text_input_search.text):
                    search_output.append(teacher)
                    counter += 1
        if counter == 0:
            self.label_search.text = 'По вашему запросу ничего не найдено'
        elif counter != 0 and counter != -1:
            self.table_search.update_row_data(self.table_search.row_data, search_output)
            self.label_search.text = ''

    def btn_press_add(self, instance):
        teacher = []
        teacher.append(self.text_input_1.text)
        teacher.append(self.text_input_2.text)
        teacher.append(self.text_input_3.text)
        teacher.append(self.text_input_4.text)
        teacher.append(self.text_input_5.text)
        teacher.append(self.text_input_6.text)
        teachers.append(teacher)
        self.table.update_row_data(self.table.row_data, teachers)
        write_file.write(teachers, 'teachers.xml')