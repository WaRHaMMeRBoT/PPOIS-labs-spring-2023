import tkinter as tk
import sys
from view.creation_window import CreationWindow
from tkinter import ttk, BOTH, END, NW
from models.models import Sportsmen
import tkinter.messagebox as mb

from file_handing.xml_writer import XMLWriter
from file_handing.xml_reader import XMLReader

from typing import Dict

from view.filtering_window import FilteringWindow


class MainWindow:
    __dict_of_functions_for_buttons = {
        'update_data': Sportsmen.get_pages_of_filtered_sportsmens,
        'first_page': Sportsmen.get_first_page,
        'next_page': Sportsmen.get_next_page,
        'previous_page': Sportsmen.get_previous_page,
        'last_page': Sportsmen.get_last_page
    }

    def __init__(self):
        self.__main_window = tk.Tk()
        self.__main_window.title("professor community service")
        self.__main_window.geometry("1200x500")

        # табличка
        self.__create_tables()

        # выпадающие менюшки
        self.__create_drop_down_lists()

        # кнопки пагинации
        self.__create_buttons()

        # меню правой кнопки мыши
        self.__m_menu = tk.Menu(self.__main_window, tearoff=0)
        self.__m_menu.add_command(
            label='Удалить выделенную запись', command=self.__delete_choosen_entry)
        self.__main_window.bind('<Button-3>', self.__show_mouse_menu)

    def __show_mouse_menu(self, event):
        self.__m_menu.post(event.x_root, event.y_root)

    def __create_drop_down_lists(self):
        mainmenu = tk.Menu(self.__main_window)
        self.__main_window.config(menu=mainmenu)

        actions_menu = tk.Menu(self.__main_window, tearoff=0)
        actions_menu.add_command(label="Фильтры", command=FilteringWindow)
        actions_menu.add_command(
            label="Добавить новую запись", command=CreationWindow)
        actions_menu.add_command(
            label="Удалить отфильтрованные записи", command=self.__delete_sorted_entries)

        file_menu = tk.Menu(self.__main_window)
        file_menu.add_command(label="открыть...", command=XMLReader.reader)
        file_menu.add_command(label="сохранить", command=XMLWriter.writer)
        file_menu.add_command(label="сохранить как...",
                              command=XMLWriter.writer_as)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=sys.exit)

        mainmenu.add_cascade(label="Файл", menu=file_menu)
        mainmenu.add_cascade(label="Действия", menu=actions_menu)

    def __create_tables(self):
        """Таблица"""
        columns = (
            'stud_name', 'compound', 'position', 'tituls', 'type_of_sport', 'rank')
        self.__main_table = ttk.Treeview(columns=columns, show='headings')
        self.__main_table.pack(fill=BOTH, expand=1)

        self.__main_table.heading('stud_name', text="ФИО преподавателя")
        self.__main_table.column(f'stud_name', width=60)
        self.__main_table.heading('compound', text="Учёная степень")
        self.__main_table.column(f'compound', width=40)
        self.__main_table.heading('position', text="Учёное звание")
        self.__main_table.column(f'position', width=20)
        self.__main_table.heading('tituls', text="Стаж работы")
        self.__main_table.column(f'tituls', width=20)
        self.__main_table.heading('type_of_sport', text="Название кафедры")
        self.__main_table.column(f'type_of_sport', width=20)
        self.__main_table.heading('rank', text="Факультет")
        self.__main_table.column(f'rank', width=20)

    def __create_buttons(self):
        tk.Button(self.__main_window, text="Обновить данные таблицы",
                  command=lambda arg='update_data': self.__build_table(arg)).pack(side=tk.RIGHT)
        tk.Button(self.__main_window, text="1 страница", command=lambda arg='first_page': self.__build_table(arg)).pack(
            side=tk.LEFT)
        tk.Button(self.__main_window, text="<=== предыдущая страница",
                  command=lambda arg='previous_page': self.__build_table(arg)).pack(side=tk.LEFT)
        current_page, last_page = 0, 0
        self.__label_pages = tk.Label(
            self.__main_window, text=f"{current_page}/{last_page}")
        self.__label_pages.pack(side=tk.LEFT)
        tk.Button(self.__main_window, text="следующая страница ===>",
                  command=lambda arg='next_page': self.__build_table(arg)).pack(side=tk.LEFT)
        tk.Button(self.__main_window, text="последняя страница",
                  command=lambda arg='last_page': self.__build_table(arg)).pack(side=tk.LEFT)

    def __build_table(self, arg):
        all_entries: Dict[str: Sportsmen] = self.__class__.__dict_of_functions_for_buttons[arg](
        )
        if all_entries:
            sportsmens = []
            for i in all_entries.values():
                sportsmens.append((i.sportsmen_name, i.compound,
                                   i.position, i.tituls, i.type_of_sport, i.rank))

            self.__main_table.delete(*self.__main_table.get_children())

            for sportsmen in sportsmens:
                self.__main_table.insert("", END, values=sportsmen)

            current_page, last_page = Sportsmen.get_numbers_of_pages()
            self.__label_pages.config(text=f'{current_page}/{last_page}')

        else:
            self.__main_table.delete(*self.__main_table.get_children())
            self.__label_pages.config(text=f'{0}/{0}')

    def __delete_choosen_entry(self):
        choosen_field = self.__main_table.selection()
        choosen_field = self.__main_table.item(choosen_field)
        try:
            choosen_name = choosen_field['values'][0]
            Sportsmen.delete_sportsmens(choosen_name)
            self.__build_table('update_data')
        except IndexError:
            mb.showinfo('Инфо', "Не было выбрано ни одного поля")

    def __delete_sorted_entries(self):
        Sportsmen.delete_sportsmens()
        Sportsmen.set_default_filters()
        self.__build_table('update_data')

    def run_table(self):
        self.__main_window.mainloop()
