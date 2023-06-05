from tkinter import *
from tkinter import ttk
from domXml import *
from person import *
from messageWindow import *
from readParser import *
from tkinter import filedialog as fd
import math


class MainWindow(Tk):

    def __init__(self, people):
        super().__init__()
        self.name_of_file = "players.xml"
        self.information = read_parser(self.name_of_file).information
        self.temp_page = 0
        self.tree = ttk.Treeview(columns="", show="headings")
        self.geometry("1200x600")
        self.title("Лабораторная работа №2")

        self.resizable(True, True)
        self.minsize(300, 200)
        self.maxsize(1260, 860)
        self.option_add("*tearOff", FALSE)

        self.init_widgets()

        self.mainloop()

    def init_widgets(self):
        self.init_labels()
        self.init_menus()
        self.init_table()
        self.init_buttons()

    @staticmethod
    def init_message_window(msg):
        message = Tk()
        message.geometry("240x100")
        message.title("Сообщение")
        message.resizable(False, False)
        message.option_add("*tearOff", FALSE)

        ok_label = ttk.Label(message, text=msg, font=("Algerian", 13))
        ok_label.pack(anchor="center")

        ok_button = ttk.Button(message, text="Ок", command=message.destroy)
        ok_button.pack(anchor="center")

    def open_file(self):
        self.name_of_file = fd.askopenfilename()
        self.information = read_parser(self.name_of_file).information
        self.init_widgets()

    def save_file(self):
        fd.asksaveasfilename()
        for person in self.information:
            if person in read_parser(self.name_of_file).information:
                person
            else:
                create_new_player(person, self.name_of_file)

    def menu_settings(self, main_menu, file_menu):
        file_menu.add_command(label="Новый")
        file_menu.add_command(label="Сохранить", command=lambda: self.save_file())
        file_menu.add_command(label="Открыть", command=lambda: self.open_file())
        file_menu.add_separator()
        file_menu.add_command(label="Выйти")

        main_menu.add_cascade(label="Файл", menu=file_menu)
        main_menu.add_cascade(label="Редактирование")
        main_menu.add_cascade(label="Просмотр")

    def init_menus(self):
        main_menu = Menu()
        file_menu = Menu()
        self.menu_settings(main_menu, file_menu)

        self.config(menu=main_menu)

    @staticmethod
    def init_labels():
        label = ttk.Label(text="Таблица игроков", font="Algerian")
        label.grid(row=0, sticky="n")

    def add_people(self):
        for i in range(5):
            if (self.temp_page*5 + i) < len(self.information):
                person = self.information[self.temp_page*5 + i]
                self.tree.insert("", END, values=person)

    def init_table(self):
        columns = ("full name", "birthday", "team", "home city", "compound", "position")

        self.tree = ttk.Treeview(columns=columns, show="headings")
        self.tree.grid(row=1, column=0, sticky="ns")

        self.tree.heading("full name", text="ФИО игрока")
        self.tree.heading("birthday", text="Дата рождения")
        self.tree.heading("team", text="Команда")
        self.tree.heading("home city", text="Домашний город")
        self.tree.heading("compound", text="Состав")
        self.tree.heading("position", text="Позиция")
        self.add_people()

    def add_person(self, text_full_name, text_birth_date, text_club, text_home_city, text_compound, text_position):
        person = []
        person.append(text_full_name.get())
        person.append(text_birth_date.get())
        person.append(text_club.get())
        person.append(text_home_city.get())
        person.append(text_compound.get())
        person.append(text_position.get())
        tuple_player = (*person,)
        self.information.append(tuple_player)
        self.init_message_window("Игрок был добавлен")
        self.init_table()

    def click_add_button(self):
        window = Tk()
        window.title("Окно добавления игрока")
        window.geometry("600x400")

        label = ttk.Label(window, text="Добавление игроков", font="Algerian")
        label.grid(row=0, column=1, sticky="n")

        label_full_name = ttk.Label(window, text="ФИО игрока", font="Algerian")
        label_full_name.grid(row=1, column=0, sticky="ns")

        text_full_name = ttk.Entry(window, width=45)
        text_full_name.grid(row=1, column=1, sticky="ns")

        label_birth_date = ttk.Label(window, text="Дата рождения", font="Algerian")
        label_birth_date.grid(row=2, column=0, sticky="ns")

        text_birth_date = ttk.Entry(window, width=45)
        text_birth_date.grid(row=2, column=1, sticky="ns")

        label_club = ttk.Label(window, text="Футбольная команда", font="Algerian")
        label_club.grid(row=3, column=0, sticky="ns")

        text_club = ttk.Entry(window, width=45)
        text_club.grid(row=3, column=1, sticky="ns")

        label_home_city = ttk.Label(window, text="Домашний город", font="Algerian")
        label_home_city.grid(row=4, column=0, sticky="ns")

        text_home_city = ttk.Entry(window, width=45)
        text_home_city.grid(row=4, column=1, sticky="ns")

        label_compound = ttk.Label(window, text="Состав", font="Algerian")
        label_compound.grid(row=5, column=0, sticky="ns")

        text_compound = ttk.Entry(window, width=45)
        text_compound.grid(row=5, column=1, sticky="ns")

        label_position = ttk.Label(window, text="Позиция", font="Algerian")
        label_position.grid(row=6, column=0, sticky="ns")

        text_position = ttk.Entry(window, width=45)
        text_position.grid(row=6, column=1, sticky="ns")

        add_button = ttk.Button(window, text="Добавить игрока", command=lambda: self.add_person(
                                                        text_full_name, text_birth_date,
                                                        text_club, text_home_city,
                                                        text_compound, text_position
                                                        ))
        add_button.grid(row=7, column=1, sticky="ns")

    def find_player(self, tree, text_full_name, text_birth_date, text_club, text_home_city, text_compound, text_position):
        for person in tree.get_children(""):
            tree.delete(person)

        for person in self.information:
            if (text_full_name in person[0] and text_birth_date == person[1]) or \
                    (person[2] == text_club or person[3] == text_home_city) or \
                    (person[4] == text_compound or person[5] == text_position):
                tree.insert("", END, values=person)

    def click_find_button(self):
        window = Tk()
        window.title("Окно поиска игроков")
        window.geometry("1200x600")

        label = ttk.Label(window, text="Поиск игроков", font="Algerian")
        label.grid(row=0, column=1, sticky="n")

        label_full_name = ttk.Label(window, text="ФИО игрока", font="Algerian")
        label_full_name.grid(row=1, column=0, sticky="ns")

        text_full_name = ttk.Entry(window, width=100)
        text_full_name.grid(row=1, column=1, sticky="ns")

        label_birth_date = ttk.Label(window, text="Дата рождения", font="Algerian")
        label_birth_date.grid(row=2, column=0, sticky="ns")

        text_birth_date = ttk.Entry(window, width=100)
        text_birth_date.grid(row=2, column=1, sticky="ns")

        label_club = ttk.Label(window, text="Футбольная команда", font="Algerian")
        label_club.grid(row=3, column=0, sticky="ns")

        text_club = ttk.Entry(window, width=100)
        text_club.grid(row=3, column=1, sticky="ns")

        label_home_city = ttk.Label(window, text="Домашний город", font="Algerian")
        label_home_city.grid(row=4, column=0, sticky="ns")

        text_home_city = ttk.Entry(window, width=100)
        text_home_city.grid(row=4, column=1, sticky="ns")

        label_compound = ttk.Label(window, text="Состав", font="Algerian")
        label_compound.grid(row=5, column=0, sticky="ns")

        text_compound = ttk.Entry(window, width=100)
        text_compound.grid(row=5, column=1, sticky="ns")

        label_position = ttk.Label(window, text="Позиция", font="Algerian")
        label_position.grid(row=6, column=0, sticky="ns")

        text_position = ttk.Entry(window, width=100)
        text_position.grid(row=6, column=1, sticky="ns")

        columns = ("full name", "birthday", "team", "home city", "compound", "position")

        tree = ttk.Treeview(window, columns=columns, show="headings")
        tree.grid(row=7, column=0, columnspan=2, sticky="ns")

        tree.heading("full name", text="ФИО игрока")
        tree.heading("birthday", text="Дата рождения")
        tree.heading("team", text="Команда")
        tree.heading("home city", text="Домашний город")
        tree.heading("compound", text="Состав")
        tree.heading("position", text="Позиция")

        find_button = ttk.Button(window, text="Поиск", command=lambda: self.find_player(tree, text_full_name.get(),
                                                                                        text_birth_date.get(),
                                                                                        text_club.get(), text_home_city.get(),
                                                                                        text_compound.get(), text_position.get()
                                                                                        ))
        find_button.grid(row=8, column=0, columnspan=2)

        people = self.information
        for player in people:
            tree.insert("", END, values=player)

    def update_file(self):
        with open(self.name_of_file, "w", encoding="utf-8") as file:
            file.write('<?xml version="1.0" ?> <collection shelf="Football players">')
            for player in self.information:
                file.write("<player full_name='" + player[0] + "'>")
                file.write("<birth_date>" + player[1] + "</birth_date>")
                file.write("<club>" + player[2] + "</club>")
                file.write("<home_city>" + player[3] + "</home_city>")
                file.write("<compound>" + player[4] + "</compound>")
                file.write("<position>" + player[5] + "</position>")
                file.write("</player>")
            file.write('</collection>')

    def delete_player(self, text_full_name, text_birth_date, text_club, text_home_city, text_compound, text_position):
        for person in self.information:
            if (text_full_name in person[0] and text_birth_date == person[1]) or \
                    (person[2] == text_club or person[3] == text_home_city) or \
                    (person[4] == text_compound or person[5] == text_position):
                self.information.remove(person)
                self.update_file()
        self.init_table()
        self.init_message_window("Игрок был удалён")

    def click_remove_button(self):
        window = Tk()
        window.title("Окно удаления игроков")
        window.geometry("600x700")

        label = ttk.Label(window, text="Поиск игроков", font="Algerian")
        label.grid(row=0, column=1, sticky="n")

        label_full_name = ttk.Label(window, text="ФИО игрока", font="Algerian")
        label_full_name.grid(row=1, column=0, sticky="ns")

        text_full_name = ttk.Entry(window, width=45)
        text_full_name.grid(row=1, column=1, sticky="ns")

        label_birth_date = ttk.Label(window, text="Дата рождения", font="Algerian")
        label_birth_date.grid(row=2, column=0, sticky="ns")

        text_birth_date = ttk.Entry(window, width=45)
        text_birth_date.grid(row=2, column=1, sticky="ns")

        label_club = ttk.Label(window, text="Футбольная команда", font="Algerian")
        label_club.grid(row=3, column=0, sticky="ns")

        text_club = ttk.Entry(window, width=45)
        text_club.grid(row=3, column=1, sticky="ns")

        label_home_city = ttk.Label(window, text="Домашний город", font="Algerian")
        label_home_city.grid(row=4, column=0, sticky="ns")

        text_home_city = ttk.Entry(window, width=45)
        text_home_city.grid(row=4, column=1, sticky="ns")

        label_compound = ttk.Label(window, text="Состав", font="Algerian")
        label_compound.grid(row=5, column=0, sticky="ns")

        text_compound = ttk.Entry(window, width=45)
        text_compound.grid(row=5, column=1, sticky="ns")

        label_position = ttk.Label(window, text="Позиция", font="Algerian")
        label_position.grid(row=6, column=0, sticky="ns")

        text_position = ttk.Entry(window, width=45)
        text_position.grid(row=6, column=1, sticky="ns")

        delete_button = ttk.Button(window, text="Удалить игрока", command=lambda: self.delete_player(
                                                                                    text_full_name.get(),
                                                                                    text_birth_date.get(),
                                                                                    text_club.get(),
                                                                                    text_home_city.get(),
                                                                                    text_compound.get(),
                                                                                    text_position.get()
                                                                                    ))
        delete_button.grid(row=8, column=0, columnspan=2)

    def click_prev_page(self):
        if self.temp_page != 0 and math.ceil(len(self.information)/5) != 1:
            self.temp_page = self.temp_page - 1
        self.init_table()

    def click_next_page(self):
        if self.temp_page != math.ceil(len(self.information)/5) - 1:
            self.temp_page = self.temp_page + 1
        self.init_table()

    def init_buttons(self):
        open_add_button = ttk.Button(text="Добавить игрока", command=self.click_add_button)
        open_add_button.grid(row=2, column=0, sticky="nw")

        open_find_button = ttk.Button(text="Поиск игроков", command=self.click_find_button)
        open_find_button.grid(row=2, column=0, sticky="ne")

        open_remove_button = ttk.Button(text="Удаление игроков", command=self.click_remove_button)
        open_remove_button.grid(row=2, column=0, sticky="n")

        previous_button = ttk.Button(text="Предыдущая страница", command=self.click_prev_page)
        previous_button.grid(row=3, column=0, sticky="nw")

        next_button = ttk.Button(text="Следующая страница", command=self.click_next_page)
        next_button.grid(row=3, column=0, sticky="n")
