from typing import List

from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.transition import MDSlideTransition

from model import Model, Author, Book
from view import View, MainScreen
from components.dialog import add_dialog, find_dialog


class Controller(MDScreenManager):
    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.transition = MDSlideTransition()
        self.dialog: MDDialog = NotImplemented
        self.model = Model()
        self.view = View(controller=self)

    def find_dialog(self, obj):
        self.dialog = find_dialog(self)
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def find(self, obj):
        table = self.current_screen.table
        self.current_screen.remove_widget(table)
        self.current_screen.remove_widget(self.current_screen.buttons)
        table.row_data = self.filtration()
        self.current_screen.add_widget(table)
        self.current_screen.add_widget(self.current_screen.buttons)
        self.close_dialog(self.dialog)

    def filtration(self) -> List[tuple]:
        filtered_books: List[tuple] = []
        if self.dialog.content_cls.ids.book_name.text != "":
            for i in self.model.all_books:
                lower_case_name = i.book_name.lower()
                author_full_name = i.author.first_name + " " + i.author.surname + " " + i.author.last_name
                if lower_case_name.__contains__(self.dialog.content_cls.ids.book_name.text.lower()):
                    filtered_books.append((i.book_name,
                                           author_full_name,
                                           i.publishing_house,
                                           i.volumes,
                                           i.circulation,
                                           i.total_volumes))
                # else:
                #     if filtered_books.count((i.book_name,
                #                              i.author,
                #                              i.publishing_house,
                #                              i.volumes,
                #                              i.circulation,
                #                              i.total_volumes)) > 0:
                #         filtered_books.remove((i.book_name,
                #                                i.author,
                #                                i.publishing_house,
                #                                i.volumes,
                #                                i.circulation,
                #                                i.total_volumes))

        if self.dialog.content_cls.ids.author.text != "":
            for i in self.model.all_books:
                author_full_name = i.author.first_name + " " + i.author.surname + " " + i.author.last_name
                if (author_full_name.lower()).__contains__(self.dialog.content_cls.ids.author.text.lower()):
                    filtered_books.append((i.book_name,
                                           author_full_name,
                                           i.publishing_house,
                                           i.volumes,
                                           i.circulation,
                                           i.total_volumes))
                # else:
                #     if filtered_books.count((i.book_name,
                #                              i.author,
                #                              i.publishing_house,
                #                              i.volumes,
                #                              i.circulation,
                #                              i.total_volumes)) > 0:
                #         filtered_books.remove((i.book_name,
                #                                i.author,
                #                                i.publishing_house,
                #                                i.volumes,
                #                                i.circulation,
                #                                i.total_volumes))

        if self.dialog.content_cls.ids.publishing_house.text != "":
            for i in self.model.all_books:
                lower_case_publishing_house = i.publishing_house.lower()
                author_full_name = i.author.first_name + " " + i.author.surname + " " + i.author.last_name
                if lower_case_publishing_house.__contains__(self.dialog.content_cls.ids.publishing_house.text.lower()):
                    filtered_books.append((i.book_name,
                                           author_full_name,
                                           i.publishing_house,
                                           i.volumes,
                                           i.circulation,
                                           i.total_volumes))

        if self.dialog.content_cls.ids.circulation.text != "":
            for i in self.model.all_books:
                symbol_more_than = False
                symbol_less_than = False
                num = self.dialog.content_cls.ids.circulation.text
                if self.dialog.content_cls.ids.circulation.text.__contains__(">"):
                    symbol_more_than = True
                    num = num.replace(">", "")
                    num = int(num)
                if self.dialog.content_cls.ids.circulation.text.__contains__("<"):
                    symbol_less_than = True
                    num = num.replace("<", "")
                    num = int(num)

                author_full_name = i.author.first_name + " " + i.author.surname + " " + i.author.last_name
                if symbol_more_than:
                    if i.circulation > num:
                        filtered_books.append((i.book_name,
                                               author_full_name,
                                               i.publishing_house,
                                               i.volumes,
                                               i.circulation,
                                               i.total_volumes))

                if symbol_less_than:
                    if i.circulation < num:
                        filtered_books.append((i.book_name,
                                               author_full_name,
                                               i.publishing_house,
                                               i.volumes,
                                               i.circulation,
                                               i.total_volumes))

        if self.dialog.content_cls.ids.total_volumes.text != "":
            for i in self.model.all_books:
                symbol_more_than = False
                symbol_less_than = False
                num = self.dialog.content_cls.ids.total_volumes.text
                if self.dialog.content_cls.ids.total_volumes.text.__contains__(">"):
                    symbol_more_than = True
                    num = num.replace(">", "")
                    num = int(num)
                if self.dialog.content_cls.ids.total_volumes.text.__contains__("<"):
                    symbol_less_than = True
                    num = num.replace("<", "")
                    num = int(num)

                author_full_name = i.author.first_name + " " + i.author.surname + " " + i.author.last_name
                if symbol_more_than:
                    if i.total_volumes > num:
                        filtered_books.append((i.book_name,
                                               author_full_name,
                                               i.publishing_house,
                                               i.volumes,
                                               i.circulation,
                                               i.total_volumes))

                if symbol_less_than:
                    if i.total_volumes < num:
                        filtered_books.append((i.book_name,
                                               author_full_name,
                                               i.publishing_house,
                                               i.volumes,
                                               i.circulation,
                                               i.total_volumes))

        return list(set(filtered_books))

    def add_dialog(self, obj):
        self.dialog = add_dialog(self)
        self.dialog.open()

    def add_book(self, obj):

        book_name = self.dialog.content_cls.ids.book_name.text
        author_full_name: str = self.dialog.content_cls.ids.author.text
        name_lst = author_full_name.split(' ')
        # if len(name_lst) == 2:
        #     author = Author(first_name=name_lst[0], surname="", last_name=name_lst[1])
        # if len(name_lst) == 3:
        #     author = Author(first_name=name_lst[0], surname=name_lst[1], last_name=name_lst[2])
        author = Author(first_name=name_lst[0], surname=name_lst[1], last_name=name_lst[2])
        publishing_house = self.dialog.content_cls.ids.publishing_house.text
        volumes = int(self.dialog.content_cls.ids.volumes.text)
        circulation = int(self.dialog.content_cls.ids.circulation.text)
        a_book = Book(book_name, author, publishing_house, volumes, circulation)
        self.model.add_book(a_book)
        self.close_dialog(self.dialog)
        self.update()
        print(name_lst)

    def update(self):
        table = MDDataTable(
            column_data=[
                ("Book name", dp(40)),
                ("Author", dp(40)),
                ("Publishing house", dp(30)),
                ("Volumes", dp(20)),
                ("Circulation", dp(25)),
                ("Total volumes", dp(30))
            ],

            row_data=self.model.table_rows,
            rows_num=7,
            size_hint=(1, 1),
            use_pagination=True,
            elevation=0
        )

        table = self.current_screen.table
        self.current_screen.remove_widget(table)
        self.current_screen.remove_widget(self.current_screen.buttons)
        table.row_data = self.model.table_rows
        self.current_screen.add_widget(table)
        self.current_screen.add_widget(self.current_screen.buttons)

    def transition_to_deleting(self, obj):
        self.current = 'remove'
        # self.update()

    def transition_to_menu(self, *args):
        self.current = 'main'
        self.update()

    def delete_selected_rows(self, obj):
        checked_rows = self.current_screen.table.get_row_checks()
        print(checked_rows)
        for i in checked_rows:
            self.model.delete_book(i[0])

        self.update()

    def save(self, obj):
        self.model.save()
