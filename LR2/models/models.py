import tkinter.messagebox as mb
from typing import Dict, List


class Sportsmen:
    __id: int = 0
    __dict_of_sportsmens: dict = {}
    list_of_sports = []
    list_of_ranks = []
    dict_of_filtered_sportsmens: dict = {}
    __validated_filters: dict = {
        'sportsmen_name': '', 'type_of_sport': '', 'low_limit': '', 'high_limit': '', 'rank': ''}
    __paginated_dict_of_filtered_sportsmens: Dict[int, dict] = {}
    current_page: int = 1

    def __init__(self, data: dict, new_id: int):
        self.id = new_id
        self.sportsmen_name = data['sportsmen_name']
        self.compound = data['compound']
        self.position = data['position']
        self.tituls = data['tituls']
        self.type_of_sport = data['type_of_sport']
        self.rank = data['rank']

    @classmethod
    def create_new_sportsmen(cls, data: dict):
        """Вызываем этот метод для добавления новой записи"""
        cls.__id += 1
        new_sportsmen = Sportsmen(data, cls.__id)
        if data['sportsmen_name'] in cls.__dict_of_sportsmens:
            print("Спортсмен с таким именем уже есть")

        cls.__dict_of_sportsmens[data['sportsmen_name']] = new_sportsmen
        if new_sportsmen.type_of_sport not in cls.list_of_sports:
            cls.list_of_sports.append(new_sportsmen.type_of_sport)
        if new_sportsmen.rank not in cls.list_of_ranks:
            cls.list_of_ranks.append(new_sportsmen.rank)

    @classmethod
    def filter_by_name(cls, entry):
        return cls.__validated_filters['sportsmen_name'] in entry[0]

    @classmethod
    def __select_of_suitable_values_sport(cls, entry):
        if cls.__validated_filters['type_of_sport'] == 'none':
            return True
        return cls.__validated_filters['type_of_sport'] in entry[1].type_of_sport

    @classmethod
    def __select_of_suitable_values_rank(cls, entry):
        if cls.__validated_filters['rank'] == 'none':
            return True
        return cls.__validated_filters['rank'] in entry[1].rank

    @classmethod
    def __selection_of_suitable_values_by_tituls(cls, entry, low_high: bool):
        if low_high:
            if cls.__validated_filters['high_limit'] == '':
                return True
            return int(cls.__validated_filters['high_limit']) >= int(entry[1].tituls)
        else:
            if cls.__validated_filters['low_limit'] == '':
                return True
            return int(cls.__validated_filters['low_limit']) <= int(entry[1].tituls)

    @classmethod
    def get_filtered_sportsmens(cls):
        """Для фильтрации спортсменов"""
        cls.dict_of_filtered_sportsmens = dict(
            filter(cls.filter_by_name, cls.__dict_of_sportsmens.items())
        )

        cls.dict_of_filtered_sportsmens = dict(
            filter(cls.__select_of_suitable_values_sport, cls.dict_of_filtered_sportsmens.items()))

        cls.dict_of_filtered_sportsmens = dict(
            filter(lambda x: Sportsmen.__selection_of_suitable_values_by_tituls(x, False),
                   cls.dict_of_filtered_sportsmens.items()))

        cls.dict_of_filtered_sportsmens = dict(
            filter(lambda x: Sportsmen.__selection_of_suitable_values_by_tituls(x, True),
                   cls.dict_of_filtered_sportsmens.items()))

        cls.dict_of_filtered_sportsmens = dict(
            filter(cls.__select_of_suitable_values_rank, cls.dict_of_filtered_sportsmens.items()))

        return cls.dict_of_filtered_sportsmens

    @classmethod
    def __get_paginated_filtered_students(cls, items_per_page: int = 5) -> Dict[int, Dict]:
        cls.__paginated_dict_of_filtered_sportsmens = {}

        num_pages = len(cls.dict_of_filtered_sportsmens) // items_per_page + 1 if len(
            cls.dict_of_filtered_sportsmens) % 5 != 0 else len(cls.dict_of_filtered_sportsmens) // items_per_page

        for i in range(num_pages):
            page = {}
            for j, (key, value) in enumerate(cls.dict_of_filtered_sportsmens.items()):
                if i * items_per_page <= j < (i + 1) * items_per_page:
                    page[key] = value
            cls.__paginated_dict_of_filtered_sportsmens[i + 1] = page

    @classmethod
    def get_pages_of_filtered_sportsmens(cls):
        cls.get_filtered_sportsmens()

        cls.__get_paginated_filtered_students()

        # просто проверка на наличие записи
        if cls.__paginated_dict_of_filtered_sportsmens:
            cls.current_page = 1
            return cls.__paginated_dict_of_filtered_sportsmens[1]
        else:
            return False

    @classmethod
    def get_numbers_of_pages(cls):
        return cls.current_page, len(cls.__paginated_dict_of_filtered_sportsmens)

    @classmethod
    def set_up_filters(cls, filters: dict):
        # ['student_name', 'student_group', 'low_limit', 'high_limit']
        cls.__validated_filters = filters

    @classmethod
    def set_default_filters(cls):
        cls.__validated_filters = {
            'sportsmen_name': '', 'type_of_sport': '', 'low_limit': '', 'high_limit': '', 'rank': ''}

    @classmethod
    def delete_sportsmens(cls, name_of_sportsmen: str = False):
        print(name_of_sportsmen, 'name')
        deleted_sportsmens = []
        if name_of_sportsmen:
            cls.__dict_of_sportsmens.pop(name_of_sportsmen)
            deleted_sportsmens.append(name_of_sportsmen)

        else:
            for sportsmen in list(cls.dict_of_filtered_sportsmens):
                cls.__dict_of_sportsmens.pop(sportsmen)
                deleted_sportsmens.append(sportsmen)
        mb.showinfo("Удаленные спортсмены",
                    f"Имена удаленных спортсменов: {', '.join(deleted_sportsmens)}")

    @classmethod
    def __check_paginated_dict(cls):
        if cls.__paginated_dict_of_filtered_sportsmens and cls.__paginated_dict_of_filtered_sportsmens[1]:
            return True

    @classmethod
    def get_next_page(cls):
        if cls.__check_paginated_dict():
            if cls.current_page + 1 <= len(cls.__paginated_dict_of_filtered_sportsmens):
                cls.current_page += 1
                return cls.__paginated_dict_of_filtered_sportsmens[cls.current_page]

            else:
                mb.showinfo("Инфо", "Это и так последняя страница")
                return cls.__paginated_dict_of_filtered_sportsmens[len(cls.__paginated_dict_of_filtered_sportsmens)]

        else:
            return False

    @classmethod
    def get_last_page(cls):
        if cls.__check_paginated_dict():

            if cls.current_page + 1 <= len(cls.__paginated_dict_of_filtered_sportsmens):
                cls.current_page = list(
                    cls.__paginated_dict_of_filtered_sportsmens.keys())[-1]
                return cls.__paginated_dict_of_filtered_sportsmens[cls.current_page]
            else:
                mb.showinfo("Инфо", "Это и так последняя страница")
                return cls.__paginated_dict_of_filtered_sportsmens[len(cls.__paginated_dict_of_filtered_sportsmens)]
        else:
            return False

    @classmethod
    def get_previous_page(cls):
        if cls.__check_paginated_dict():

            if cls.current_page > 1:
                cls.current_page -= 1
                return cls.__paginated_dict_of_filtered_sportsmens[cls.current_page]
            else:
                mb.showinfo("Инфо", "Это и так первая страница")
                return cls.__paginated_dict_of_filtered_sportsmens[1]
        else:
            # return cls.__paginated_dict_of_filtered_sportsmens[1]
            return False

    @classmethod
    def get_first_page(cls):
        if cls.__check_paginated_dict():
            if cls.current_page != 1:
                cls.current_page = 1
                return cls.__paginated_dict_of_filtered_sportsmens[1]
            else:
                mb.showinfo("Инфо", "Это и так первая страница")
                return cls.__paginated_dict_of_filtered_sportsmens[1]

        else:
            # return cls.__paginated_dict_of_filtered_sportsmens[1]
            return False

    @classmethod
    def get_all_sportsmens_in_list(cls):
        sportsmens_list = []
        for sportsmen in cls.__dict_of_sportsmens.values():
            entry_sportsmen: dict = {}
            entry_sportsmen['id'] = str(sportsmen.id)
            entry_sportsmen['sportsmen_name'] = sportsmen.sportsmen_name
            entry_sportsmen['compound'] = sportsmen.compound
            entry_sportsmen['position'] = sportsmen.position
            entry_sportsmen['tituls'] = sportsmen.tituls
            entry_sportsmen['type_of_sport'] = sportsmen.type_of_sport
            entry_sportsmen['rank'] = sportsmen.rank

            sportsmens_list.append(entry_sportsmen)

        return sportsmens_list

    @classmethod
    def set_sportsmens_from_file(cls, list_of_sportsmens: List[dict]):
        cls.__dict_of_sportsmens = {}
        cls.__id = 0

        for sportsmen in list_of_sportsmens:
            sportsmen.pop('id')
            new_sportsmen = {'sportsmen_name': sportsmen.pop('sportsmen_name'),
                             'compound': sportsmen.pop('compound'),
                             'position': sportsmen.pop('position'),
                             'tituls': sportsmen.pop('tituls'),
                             'type_of_sport': sportsmen.pop('type_of_sport'),
                             'rank': sportsmen.pop('rank')
                             }
            print("Новый спортсмен: ", new_sportsmen)
            cls.create_new_sportsmen(new_sportsmen)
