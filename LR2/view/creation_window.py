import tkinter as tk
import tkinter.messagebox as mb

from models.models import Sportsmen


class CreationWindow:

    def __init__(self):
        self.creation_window = tk.Tk()
        self.creation_window.title = 'creation window'
        self.creation_window.geometry('370x310')

        self._create_entries_fields()

        tk.Button(self.creation_window, text='Создать новую запись',
                  command=self.__save_entry).grid(row=13, column=1)
        self.creation_window.mainloop()

    def __save_entry(self):
        new_entry = {'sportsmen_name': self.entries[0].get(), 'compound': self.entries[1].get(),
                     'position': self.entries[2].get(), 'tituls': self.entries[3].get(),
                     'type_of_sport': self.entries[4].get(), 'rank': self.entries[5].get()}
        try:
            Sportsmen.create_new_sportsmen(new_entry)
        except ValueError as er:
            mb.showwarning("Предупреждение", er)

    def _create_entries_fields(self):
        self.entries = []
        tk.Label(self.creation_window, text=f'ФИО преподавателя').grid(
            row=0, column=0)
        a = tk.Entry(self.creation_window)
        a.grid(row=0, column=1)
        self.entries.append(a)

        tk.Label(self.creation_window, text=f'Учёная степень').grid(
            row=1, column=0)
        a = tk.Entry(self.creation_window)
        a.grid(row=1, column=1)
        self.entries.append(a)

        tk.Label(self.creation_window, text=f'Учёное звание').grid(
            row=2, column=0)
        a = tk.Entry(self.creation_window)
        a.grid(row=2, column=1)
        self.entries.append(a)

        tk.Label(self.creation_window, text=f'Стаж работы').grid(
            row=3, column=0)
        a = tk.Entry(self.creation_window)
        a.grid(row=3, column=1)
        self.entries.append(a)

        tk.Label(self.creation_window, text=f'Название кафедры').grid(
            row=4, column=0)
        a = tk.Entry(self.creation_window)
        a.grid(row=4, column=1)
        self.entries.append(a)

        tk.Label(self.creation_window, text=f'Факультет').grid(
            row=5, column=0)
        a = tk.Entry(self.creation_window)
        a.grid(row=5, column=1)
        self.entries.append(a)
