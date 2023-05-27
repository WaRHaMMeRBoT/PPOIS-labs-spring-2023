from typing import List, Set

from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import MDSlideTransition

from components.dialog import add_dialog, find_dialog
from view import View
from model import Model

class Controller(MDScreenManager):

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.transition = MDSlideTransition()
        self.dialog: MDDialog = NotImplemented
        self.model = Model()
        self.view = View(controller=self)

    def update(self):
        data_table = self.current_screen.data_table
        self.current_screen.remove_widget(data_table)
        self.current_screen.remove_widget(self.current_screen.buttons)
        data_table.row_data = self.get_book_names()
        self.current_screen.add_widget(data_table)
        self.current_screen.add_widget(self.current_screen.buttons)

    def get_book_names(self) -> List[tuple]:
        book_names: List[tuple] = []
        for i in self.model.books:
            book: tuple = (i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)
            book_names.append(book)
        return book_names

    def save(self, obj):
        self.model.save()

    def transition_to_menu(self, *args):
        self.current = 'menu'
        self.update()

    def add_dialog(self, obj):
        self.dialog = add_dialog(self)
        self.dialog.open()

    def find_dialog(self, obj):
        self.dialog = find_dialog(self)
        self.dialog.open()

    def find(self, obj):
        self.current_screen.data_table.row_data = self.filtration
        self.close_dialog(self.dialog)

    @property
    def filtration(self) -> List[tuple]:
        filtraded_books: List[tuple] = []

        if self.dialog.content_cls.ids.name.text != "":
            for i in self.model.books:
                if i.name.__contains__(self.dialog.content_cls.ids.name.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))

        if self.dialog.content_cls.ids.author.text != "":
            print(self.dialog.content_cls.ids.author.text)
            for i in self.model.books:
                if i.author.__contains__(self.dialog.content_cls.ids.author.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))

        if self.dialog.content_cls.ids.publishing_house.text != "":
            print(self.dialog.content_cls.ids.publishing_house.text)
            for i in self.model.books:
                if i.publishing_house.__contains__(self.dialog.content_cls.ids.publishing_house.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))


        if self.dialog.content_cls.ids.max_number_of_volumes.text != "" and self.dialog.content_cls.ids.min_number_of_volumes.text != "":
            print(self.dialog.content_cls.ids.min_number_of_volumes.text)
            print(self.dialog.content_cls.ids.max_number_of_volumes.text)
            for i in self.model.books:
                if i.number_of_volumes > int(self.dialog.content_cls.ids.min_number_of_volumes.text) and  i.number_of_volumes < int(self.dialog.content_cls.ids.max_number_of_volumes.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
        
        elif self.dialog.content_cls.ids.min_number_of_volumes.text != "":
            print(self.dialog.content_cls.ids.min_number_of_volumes.text)
            for i in self.model.books:
                if i.number_of_volumes > int(self.dialog.content_cls.ids.min_number_of_volumes.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))

        elif self.dialog.content_cls.ids.max_number_of_volumes.text != "":
            print(self.dialog.content_cls.ids.max_number_of_volumes.text)
            for i in self.model.books:
                if i.number_of_volumes < int(self.dialog.content_cls.ids.max_number_of_volumes.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))

        if self.dialog.content_cls.ids.max_circulation.text != "" and self.dialog.content_cls.ids.min_circulation.text != "":
            print(self.dialog.content_cls.ids.min_circulation.text)
            print(self.dialog.content_cls.ids.max_circulation.text)
            for i in self.model.books:
                if i.circulation > int(self.dialog.content_cls.ids.min_circulation.text) and  i.circulation < int(self.dialog.content_cls.ids.max_circulation.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
        
        elif self.dialog.content_cls.ids.min_circulation.text != "":
            print(self.dialog.content_cls.ids.min_circulation.text)
            for i in self.model.books:
                if i.circulation > int(self.dialog.content_cls.ids.min_circulation.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))

        elif self.dialog.content_cls.ids.max_circulation.text != "":
            print(self.dialog.content_cls.ids.max_circulation.text)
            for i in self.model.books:
                if i.circulation < int(self.dialog.content_cls.ids.max_circulation.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))

        if self.dialog.content_cls.ids.max_total_volumes.text != "" and self.dialog.content_cls.ids.min_total_volumes.text != "":
            print(self.dialog.content_cls.ids.min_total_volumes.text)
            print(self.dialog.content_cls.ids.max_total_volumes.text)
            for i in self.model.books:
                if i.total_volumes > int(self.dialog.content_cls.ids.min_total_volumes.text) and  i.total_volumes < int(self.dialog.content_cls.ids.max_total_volumes.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
        
        elif self.dialog.content_cls.ids.max_total_volumes.text != "":
            print(self.dialog.content_cls.ids.min_total_volumes.text)
            for i in self.model.books:
                if i.total_volumes > int(self.dialog.content_cls.ids.min_total_volumes.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))

        elif self.dialog.content_cls.ids.min_total_volumes.text != "":
            print(self.dialog.content_cls.ids.max_total_volumes.text)
            for i in self.model.books:
                if i.total_volumes < int(self.dialog.content_cls.ids.max_total_volumes.text):
                    filtraded_books.append((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))
                else:
                    if filtraded_books.count((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes)) > 0:
                        filtraded_books.remove((i.name, i.author, i.publishing_house, i.number_of_volumes, i.circulation, i.total_volumes))

        return list(set(filtraded_books))

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def transition_to_deleting(self, obj):
        self.current = 'remove'
        self.update()

    def delete_selected_rows(self, obj):
        checked_rows = self.current_screen.data_table.get_row_checks()
        print(checked_rows)
        for i in checked_rows:
            self.model.delete_book(i[0])
        self.update()

    def add_book(self, obj):
        name = self.dialog.content_cls.ids.name.text
        author = self.dialog.content_cls.ids.author.text
        publishing_house = self.dialog.content_cls.ids.publishing_house.text
        number_of_volumes = int(self.dialog.content_cls.ids.number_of_volumes.text)
        circulation = int(self.dialog.content_cls.ids.circulation.text)
        total_volumes = number_of_volumes * circulation
        book = Model.Book(name=name, author=author, publishing_house=publishing_house, number_of_volumes=number_of_volumes, circulation=circulation, total_volumes=total_volumes)
        self.model.add_book(book)
        self.close_dialog(self.dialog)
        self.update()