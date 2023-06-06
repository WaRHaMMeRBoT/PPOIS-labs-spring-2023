import json


def add_book_from_window(self, *args):

    if len(str(self.dialog_add.content_cls.ids.book_name.text)) == 0:
        return
    else:
        book_name = str(self.dialog_add.content_cls.ids.book_name.text)
        author_name = str(self.dialog_add.content_cls.ids.author_name.text)
        publishing_house = str(self.dialog_add.content_cls.ids.publisher.text)
        number_of_tom = int(self.dialog_add.content_cls.ids.number_of_volumes.text)
        number_of_editions = int(self.dialog_add.content_cls.ids.print_run.text)
        all_editions = number_of_tom * number_of_editions

        # Читаем данные из файла
        with open('sw_templates.json', 'r') as f:
            data = json.load(f)
        # Создаем словарь с информацией о новой книге
        new_book = {
            "number": len(data) + 1,
            "book_name": book_name,
            "author_name": author_name,
            "publishing_house": publishing_house,
            "number_of_tom": number_of_tom,
            "number_of_editions": number_of_editions,
            "all_editions": all_editions
        }



        # Добавляем новую книгу в данные
        data.append(new_book)

        # Записываем измененные данные в файл
        with open('sw_templates.json', 'w',) as f:
            json.dump(data, f, indent=4)
        self.dialog_add.dismiss()


def update_row_data():
    with open('sw_templates.json', 'r') as f:
        data = json.load(f)
    row_data = [(i+1, d['book_name'], d['author_name'], d['publishing_house'], d['number_of_tom'],
                 d['number_of_editions'], d['all_editions']) for i, d in enumerate(data)]
    return row_data


def update_file(data):
    new_data = []
    for i in range(len(data)):
        new_book = {
            "number": i+1,
            "book_name": data[i][1],
            "author_name": data[i][2],
            "publishing_house": data[i][3],
            "number_of_tom": data[i][4],
            "number_of_editions": data[i][5],
            "all_editions": data[i][6]
        }
        new_data.append(new_book)
    with open('sw_templates.json', 'w',) as f:
        json.dump(new_data, f, indent=4)


def add_book_from_input():
    # Запрашиваем у пользователя информацию о книге
    book_name = input("Введите название книги: ")
    author_name = input("Введите имя автора: ")
    publishing_house = input("Введите название издательства: ")
    number_of_tom = int(input("Введите количество томов: "))
    number_of_editions = int(input("Введите количество изданий: "))
    all_editions = number_of_tom * number_of_editions
    # Читаем данные из файла
    with open('sw_templates.json', 'r') as f:
        data = json.load(f)
    # Создаем словарь с информацией о новой книге
    new_book = {
        "number": len(data) + 1,
        "book_name": book_name,
        "author_name": author_name,
        "publishing_house": publishing_house,
        "number_of_tom": number_of_tom,
        "number_of_editions": number_of_editions,
        "all_editions": all_editions
    }



    # Добавляем новую книгу в данные
    data.append(new_book)

    # Записываем измененные данные в файл
    with open('sw_templates.json', 'w') as f:
        json.dump(data, f, indent=4)


def delete_book(author_name=None, publishing_house=None, book_name=None, num_of_tom_min=None,
                num_of_tom_max=None, num_of_editions_min=None, num_of_editions_max=None, all_editions_min=None,
                all_editions_max=None):
    # Читаем данные из файла
    with open('sw_templates.json', 'r') as f:
        data = json.load(f)

    # Создаем список для хранения индексов книг, которые нужно удалить
    indexes_to_remove = []

    # Проходим по каждой книге в данных
    for i, book in enumerate(data):
        # Проверяем параметры поиска и фильтруем данные, если необходимо
        if author_name is not None and book['author_name'] != author_name:
            continue
        if publishing_house is not None and book['publishing_house'] != publishing_house:
            continue
        if book_name is not None and book['book_name'] != book_name:
            continue
        if num_of_tom_min is not None and book['number_of_tom'] < num_of_tom_min:
            continue
        if num_of_tom_max is not None and book['number_of_tom'] > num_of_tom_max:
            continue
        if num_of_editions_min is not None and book['number_of_editions'] < num_of_editions_min:
            continue
        if num_of_editions_max is not None and book['number_of_editions'] > num_of_editions_max:
            continue
        if all_editions_min is not None and book['all_editions'] < all_editions_min:
            continue
        if all_editions_max is not None and book['all_editions'] > all_editions_max:
            continue

        # Если книга соответствует параметрам поиска, добавляем ее индекс в список для удаления
        indexes_to_remove.append(i)

    # Удаляем книги из списка данных в обратном порядке, чтобы не нарушить порядок индексов
    for i in reversed(indexes_to_remove):
        del data[i]

    # Записываем измененные данные в файл
    with open('books.json', 'w') as f:
        json.dump(data, f)

    # Выводим сообщение об удалении книг
    if len(indexes_to_remove) > 0:
        print(f"Удалено {len(indexes_to_remove)} книг(и).")
    else:
        print("Книги не найдены.")

delete_book(book_name='aq')