import json
import os
from json import load
from typing import List

class Model:
    class Book:
        def __init__(self, name: str, author: str, publishing_house: str, number_of_volumes: int, circulation: int, total_volumes: int):
            self.name = name
            self.author = author
            self.publishing_house = publishing_house
            self.number_of_volumes = number_of_volumes
            self.circulation = circulation
            self.total_volumes = number_of_volumes * circulation

    def __init__(self):
        self.json_dir = "/test.json"
        self.books: List[Model.Book] = self.parse_book()

    def save(self):
        books: List = []

        for i in self.books:
            book: dict = {
                "name": i.author,
                "author": i.author,
                "publishing_house": i.publishing_house,
                "number_of_volumes": i.number_of_volumes,
                "total_volumes": i.total_volumes,
                "circulation": i.circulation,
            }
            books.append(book)

        with open(os.path.realpath(os.path.dirname(__file__)) + self.json_dir, 'w') as fcc_file:
            json.dump({"books": books}, fcc_file, indent=4)

    def parse_book(self) -> List[Book]:
        with open(os.path.realpath(os.path.dirname(__file__)) + self.json_dir, 'r') as fcc_file:
            obj = load(fcc_file)
            raw_list: List[Model.Book] = []
            index = 1
            for i in obj["books"]:
                print(i["name"])
                book: Model.Book = Model.Book(name=i["name"], author=i["author"], publishing_house=i["publishing_house"], number_of_volumes=i["number_of_volumes"], circulation=i["circulation"], total_volumes=i["total_volumes"])
                raw_list.append(book)
                index += 1
        return raw_list

    def add_book(self, book: Book):
        self.books.append(book)

    def get_id_by_name(self, name: str) -> int:
        index: int = 0

        for i in self.books:
            if i.name == name:
                index = self.books.index(i)

        return index

    def delete_book(self, name: str):
        del self.books[self.get_id_by_name(name)]