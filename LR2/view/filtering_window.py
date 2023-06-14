import tkinter as tk
from tkinter import ttk, E
import tkinter.messagebox as mb

from models.models import Sportsmen


class FilteringWindow:
    def __init__(self):
        self.filtering_window = tk.Tk()
        self.filtering_window.title = 'filtering window'
        self.filtering_window.geometry('470x220')

        self.__create_filter_fields()
        tk.Button(self.filtering_window, text='Задать фильтры',
                  command=self.__save_filters).grid(row=10, column=1)
        self.filtering_window.mainloop()

    def __create_filter_fields(self):
        # накинуть валидации
        self.__filter_entries = []
        tk.Label(self.filtering_window, text=f'Фильтрация по ФИО').grid(
            row=0, column=0, sticky=E)
        a = tk.Entry(self.filtering_window, )
        a.grid(row=0, column=1)
        self.__filter_entries.append(a)

        tk.Label(self.filtering_window, text=f'Фильтрация по названию кафедры').grid(
            row=2, column=0, sticky=E)
        sports = Sportsmen.list_of_sports
        combo = ttk.Combobox(self.filtering_window, values=sports)
        combo.set("none")
        combo.config(width=19)
        combo.grid(row=2, column=1)
        self.__filter_entries.append(combo)

        tk.Label(self.filtering_window, text=f'Стаж работы (нижний предел)').grid(
            row=4, column=0, sticky=E)
        upper_limit = tk.Entry(self.filtering_window, )
        upper_limit.grid(row=4, column=1)
        self.__filter_entries.append(upper_limit)

        tk.Label(self.filtering_window, text=f'Стаж работы (верхний предел)').grid(
            row=6, column=0, sticky=E)
        lower_limit = tk.Entry(self.filtering_window, )
        lower_limit.grid(row=6, column=1)
        self.__filter_entries.append(lower_limit)

        tk.Label(self.filtering_window, text=f'Фильтрация по факультету').grid(
            row=8, column=0, sticky=E)
        ranks = Sportsmen.list_of_ranks
        combo = ttk.Combobox(self.filtering_window, values=ranks)
        combo.set("none")
        combo.config(width=19)
        combo.grid(row=8, column=1)
        self.__filter_entries.append(combo)

    def __save_filters(self):
        # список из данных полей
        fields_results = list(map(lambda x: x.get(), self.__filter_entries))
        names = ['sportsmen_name', 'type_of_sport',
                 'low_limit', 'high_limit', 'rank']
        named_parametrs = dict(zip(names, fields_results))
        try:
            Sportsmen.set_up_filters(named_parametrs)
        except ValueError as e:
            mb.showwarning("Предупреждение", e)
