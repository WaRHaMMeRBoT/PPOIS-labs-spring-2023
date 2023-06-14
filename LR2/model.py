import json
from typing import List
from typing import Tuple
from typing import NamedTuple


class Author(NamedTuple):
    first_name: str
    surname: str
    last_name: str


class Book:
    book_name: str
    author: Author
    publishing_house: str
    volumes: int
    circulation: int
    total_volumes: int

    def __init__(self, book_name: str, author: Author, publishing_house: str, volumes: int, circulation: int):
        self.book_name = book_name
        self.author = author
        self.publishing_house = publishing_house
        self.volumes = volumes
        self.circulation = circulation
        self.total_volumes = self.volumes * self.circulation


def read_books_storage() -> List[Book]:
    with open("/Users/egorvasilkov/PycharmProjects/videoKivy/books_storage.json", 'r') as file:
        books: dict = json.load(file)
    book_lst: List[Book] = []

    for item in books['books']:
        an_author = Author(item['author']['first_name'], item['author']['surname'], item['author']['last_name'])

        a_book = Book(item['book_name'], an_author, item['publishing_house'], item['volumes'],
                      item['circulation'])
        book_lst.append(a_book)
    return book_lst


class Model:
    all_books: List[Book]
    table_rows: List[Tuple]

    def __init__(self):
        self.all_books = read_books_storage()
        self.table_rows = self.fill_table_rows()

    def add_book(self, book: Book):
        self.all_books.append(book)
        self.table_rows = self.fill_table_rows()

    def fill_table_rows(self) -> List[Tuple]:
        books: List[Tuple] = []
        for item in self.all_books:
            author_full_name = item.author.first_name + " " + item.author.surname + " " + item.author.last_name
            a_book: Tuple = (item.book_name,
                             author_full_name,
                             item.publishing_house,
                             item.volumes,
                             item.circulation,
                             item.total_volumes)
            books.append(a_book)
        return books

    # def get_id_by_identifier(self, identifier: int) -> int:
    #     index: int = 0
    #
    #     for i in self.all_books:
    #         if int(i.identifier) == identifier:
    #             index = self.persons.index(i)
    #
    #     return index

    def delete_book(self, name: str):
        for item in self.all_books:
            if item.book_name == name:
                self.all_books.remove(item)
                self.table_rows = self.fill_table_rows()

        # del self.all_books[identifier]

    def save(self):
        books: List = []

        for i in self.all_books:
            an_author: dict = {"first_name": i.author.first_name, "surname": i.author.surname,
                               "last_name": i.author.last_name}
            a_book: dict = {
                "book_name": i.book_name,
                "author": an_author,
                "publishing_house": i.publishing_house,
                "volumes": i.volumes,
                "circulation": i.circulation,
                "total_volumes": i.total_volumes,
            }

            books.append(a_book)

        with open("/Users/egorvasilkov/PycharmProjects/videoKivy/books_storage.json", 'w') as file:
            json.dump({"books": books}, file, indent=4)
