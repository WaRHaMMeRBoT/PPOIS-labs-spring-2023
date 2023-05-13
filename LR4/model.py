from __future__ import annotations
import json
import random


class Model:
    __TREE = ['apple', 'peer']
    __HERBS = ['potato', 'tomato', 'pepper']
    __Weather = ['rain', 'sun', 'hurricane']

    def __init__(self, money=500, garden_bed_kol=0, weather='sun', day=1) -> None:
        self.__money = money  # Количество денег
        self.__garden_bed_kol = garden_bed_kol  # Количество грядок
        self.__garden_bed = []  # Список грядок
        self.__trees = []  # Список деревьев
        self.__day = day  # День по счёту (пока нету сохранения в файл)
        self.__weather = weather  # Погода

    def add_garden_bed(self) -> str:
        if self.garden_bed_kol() >= 7:
            status = 'Не хватает места для грядок'
        elif self.__money < 10:
            status = 'Не хватает денег'
        else:
            self.__garden_bed.append(GardenBed(0, False, False))
            self.__garden_bed_kol += 1
            self.__money -= 10
            status = 'Грядка добавлена'
        return status

    def plant_tree(self, tree_name: str) -> str:
        if self.tree_kol() >= 5:
            status = 'Не хватает места для деревьев'
        elif self.__money < 25:
            status = 'Не хватает денег )'
        elif self.__TREE.count(tree_name) == 0:
            status = "Такиких саженцев нет"
        else:
            if tree_name == self.__TREE[0]:
                self.__trees.append(AppleTree(0, 0, False, False))  # сюдамс
            else:
                self.__trees.append(PeerTree(0, 0, False, False))  # сюдамс
            self.__money -= 25
            status = 'Дерево ' + tree_name + ' посажено'
        return status

    def plant_cultivated_plant(self, cultivated_plant_name: str,
                               num: int) -> str:  # Посадить культурное растение (тут в грядку)
        if self.__money < 20:
            status = 'Не хватает денег'
        elif len(self.__garden_bed) <= num:
            status = "Грядки с таким номером нет"
        elif self.__garden_bed[num].check_herb():
            status = '!Грядка {} занята!'.format(num + 1)
        elif self.__garden_bed[num].get_weed():
            status = '!Грядку {} необходимо прополоть'.format(num + 1)
        elif self.__HERBS.count(cultivated_plant_name) == 0:
            status = 'Таких семян нет в магазине'
        else:
            self.__garden_bed[num].plant_herb(cultivated_plant_name)
            self.__money -= 20
            status = 'Растение посажено'
        return status

    def weeding(self, num: int) -> str:
        if self.__money < 10:
            status = 'Не хватает денег'
        elif len(self.__garden_bed) <= num:
            status = "Грядки с таким номером нет"
        elif not self.__garden_bed[num].get_weed():
            status = 'На грядке нет сорняка'
        else:
            self.__money -= 10
            self.__garden_bed[num].weeding()
            status = 'Грядка прополота'
        return status

    def watering(self, num: int) -> str:
        if self.__money < 10:
            status = 'Не хватает денег'
        elif len(self.__garden_bed) <= num:
            status = "Грядки с таким номером нет"
        elif not self.__garden_bed[num].check_herb():
            status = "Растения на грядке нет"
        else:
            self.__garden_bed[num].water()
            status = "Растение полито"
            self.__money -= 10
        return status

    def fertilize(self, num: int) -> str:
        if self.__money < 10:
            status = 'Не хватает денег'
        elif len(self.__garden_bed) <= num:
            status = "Грядки с таким номером нет"
        elif not self.__garden_bed[num].check_herb():
            status = "Растения на грядке нет"
        else:
            self.__garden_bed[num].fertilize()
            status = "Растение удобрено"
            self.__money -= 10
        return status

    def kill_pest(self, type_herb: str, num: int) -> str:
        if self.__money < 10:
            status = 'Не хватает денег'
        elif type_herb == "tree":
            if len(self.__trees) <= num:
                status = "Дерева с таким номером нет"
            else:
                self.__trees[num].pest_control()
                self.__money -= 10
                status = 'Вредители повержены'
        elif type_herb == "cult":
            if len(self.__garden_bed) <= num:
                status = "Грядки с таким номером нет"
            elif not self.__garden_bed[num].check_herb():
                status = "На грядке нет растения"
            else:
                tmp_herb = self.__garden_bed[num].get_herb()
                tmp_herb.pest_control()
                self.__money -= 10
                status = 'Вредители повержены'
        else:
            status = "Такого типа растений нет"
        return status

    def treatment(self, type_herb: str, num: int) -> str:
        if self.__money < 10:
            status = 'Не хватает денег'
        elif type_herb == "tree":
            if len(self.__trees) <= num:
                status = "Дерева с таким номером нет"
            else:
                self.__trees[num].disease_control()
                self.__money -= 10
                status = 'Растение вылечено'
        elif type_herb == "cult":
            if len(self.__garden_bed) <= num:
                status = "Грядки с таким номером нет"
            elif not self.__garden_bed[num].check_herb():
                status = "На грядке нет растения"
            else:
                tmp_herb = self.__garden_bed[num].get_herb()
                tmp_herb.disease_control()
                self.__money -= 10
                status = 'Растение вылечено'
        else:
            status = "Такого типа растений нет"
        return status

    def harvesting(self, type_herb: str, num: int) -> str:
        if type_herb == "tree":
            if len(self.__trees) <= num:
                status = "Дерева с таким номером нет"
            elif not self.__trees[num].check_harvest():
                status = "У дерева нет урожая"
            else:
                self.__money += self.__trees[num].harvesting()
                status = 'Урожай собран'
        elif type_herb == "cult":
            tmp_herb = self.__garden_bed[num].get_herb()
            if len(self.__garden_bed) <= num:
                status = "Грядки с таким номером нет"
            elif not self.__garden_bed[num].check_herb():
                status = "На грядке нет растения"
            elif not tmp_herb.check_harvest():
                status = "У растения нет урожая"
            else:
                self.__money += tmp_herb.harvesting()
                status = 'Урожай собран'
        else:
            status = "Такого типа растений нет"
        return status

    def money(self) -> int:
        return self.__money

    def garden_bed_kol(self) -> int:
        return self.__garden_bed_kol

    def tree_kol(self):
        return len(self.__trees)

    def day(self) -> int:
        return self.__day

    def get_weather(self) -> str:
        return self.__weather

    def next_day(self) -> None:
        tmp_trees = []
        for tree in self.__trees:
            tree.day()
            tree.maybe_ill_pest()
            if tree.check_alive():
                tmp_trees.append(tree)
        self.__trees = tmp_trees
        for bed in self.__garden_bed:
            if bed.check_herb():
                tmp_herb = bed.get_herb()
                tmp_herb.day()
                if bed.get_weed():
                    tmp_herb.min_w(10)
                else:
                    bed.maybe_weed()
                if not tmp_herb.check_alive():
                    bed.del_herb()
            else:
                bed.day()
        self.__day += 1
        self.__money += 15
        self.weather()
        for bed in self.__garden_bed:
            if bed.check_herb():
                tmp_herb = bed.get_herb()
                if not tmp_herb.check_alive():
                    bed.del_herb()

    def weather(self) -> None:
        self.__weather = random.choice(self.__Weather)
        for bed in self.__garden_bed:
            if bed.check_herb():
                tmp_herb = bed.get_herb()
                if self.__weather == 'rain':
                    tmp_herb.set_water_level(tmp_herb.water_level() + 25)
                elif self.__weather == 'sun':
                    tmp_herb.set_water_level(tmp_herb.water_level() - 25)
                elif self.__weather == 'hurricane':
                    tmp_herb.set_fertilization_level(0)

    def show(self) -> None:
        st = "Day: {}".format(self.__day) + '\n' + "Weather: {}".format(self.__weather) + '\n' + "Money: {}".format(self.__money)+ '\n' +"Кол-во деревьев: {}".format(len(self.__trees))+ '\n' +"Кол-во грядок: {}".format(self.__garden_bed_kol)
        counter = 1
        for tree in self.__trees:
            st += '\n' + ("-" * 180)
            temp_str = tree.get_name()
            if tree.get_ill():
                temp_str = temp_str + "|Ill+|"
            else:
                temp_str = temp_str + "|Ill-|"
            if tree.get_pest():
                temp_str = temp_str + "Pest+|"
            else:
                temp_str = temp_str + "Pest-|"
            if tree.check_harvest():
                temp_str = temp_str + "Harvest+|"
            else:
                temp_str = temp_str + "Harvest-|"
            st += '\n' + "|Tree {}".format(counter) + "|" + temp_str
            counter = counter + 1
        st += '\n' + ("=" * 90)
        counter = 1
        for bed in self.__garden_bed:
            temp_str = "|Garden bed {}".format(counter)
            if not bed.check_herb():
                temp_str = temp_str + "|-|"
            else:
                tmp_herb = bed.get_herb()
                temp_str = temp_str + "|{}|".format(tmp_herb.get_name())
                temp_str = temp_str + tmp_herb.get_short_info()
            if bed.get_weed():
                temp_str = temp_str + "Weed+|"
            else:
                temp_str = temp_str + "Weed-|"
            st += '\n' + temp_str
            st += '\n' + ("-" * 180)
            counter = counter + 1
        return st

    def get_data_from_file(self) -> None:
        with open('data.json', 'r', encoding="utf-8") as file:
            info = json.load(file)
            self.__init__(info['money'], info['garden_bed_kol'], info['weather'], info['day'])
            for bed in info['garden_bed']:
                temp_bed = GardenBed(bed['DAY'], bed['WEED'], bed['HERB'])
                if isinstance(bed['HERB'], dict):
                    herb = bed['HERB']
                    if herb['type'] == 'tomato':
                        temp_bed.set_herb(
                            Tomato(herb['water'], herb['level_fertilization'], herb['life_day'], herb['harvest_day'],
                                   herb['ill'], herb['pest']))
                    elif herb['type'] == 'potato':
                        temp_bed.set_herb(
                            Potato(herb['water'], herb['level_fertilization'], herb['life_day'], herb['harvest_day'],
                                   herb['ill'], herb['pest']))
                    else:
                        temp_bed.set_herb(
                            Pepper(herb['water'], herb['level_fertilization'], herb['life_day'], herb['harvest_day'],
                                   herb['ill'], herb['pest']))
                self.__garden_bed.append(temp_bed)
            for tree in info['tree']:
                if tree['type'] == 'apple':
                    temp_tree = AppleTree(tree['life_day'], tree['harvest_day'], tree['ill'], tree['pest'])
                else:
                    temp_tree = PeerTree(tree['life_day'], tree['harvest_day'], tree['ill'], tree['pest'])
                self.__trees.append(temp_tree)

    def set_data_in_file(self) -> None:
        with open('data.json', 'r', encoding="utf-8") as file:
            temp_dict = {"money": self.__money, "garden_bed_kol": self.__garden_bed_kol, "day": self.__day,
                         "weather": self.__weather}
            temp_tree_list = []
            for tree in self.__trees:
                temp_tree = tree.get_info()
                temp_tree["type"] = tree.get_name()
                temp_tree_list.append(temp_tree)
            temp_dict["tree"] = temp_tree_list
            temp_bed_list = []
            for bed in self.__garden_bed:
                temp_bed = bed.get_info()
                if not bed.check_herb():
                    temp_bed["HERB"] = False
                else:
                    tmp_herb = bed.get_herb()
                    temp_bed["HERB"] = tmp_herb.get_info()
                temp_bed_list.append(temp_bed)
            temp_dict["garden_bed"] = temp_bed_list
            with open('data.json', 'w', encoding="utf-8") as w:
                json.dump(temp_dict, w, indent=2)


class GardenBed:  # ГрядОчка
    def __init__(self, day: int, weed: bool, herb: bool) -> None:
        self.__DAY = day
        self.__WEED = weed
        self.__HERB = herb

    def check_herb(self) -> bool:
        if isinstance(self.__HERB, Herb):
            return True
        else:
            return False

    def get_herb(self) -> Herb:
        if isinstance(self.__HERB, Herb):
            return self.__HERB

    def plant_herb(self, cultivated_plant_name: str) -> None:
        if cultivated_plant_name == 'potato':
            self.__HERB = Potato(100, 100, 0, 0, False, False)
        elif cultivated_plant_name == 'tomato':
            self.__HERB = Tomato(100, 100, 0, 0, False, False)
        else:
            self.__HERB = Pepper(100, 100, 0, 0, False, False)

    def day(self) -> None:
        self.__DAY += 1
        if self.__DAY > 2:
            self.__WEED = True

    def weeding(self) -> None:
        self.__WEED = False

    def get_info(self) -> dict:
        tmp_dict = {"DAY": self.__DAY, "WEED": self.__WEED}
        return tmp_dict

    def get_weed(self) -> bool:
        return self.__WEED

    def set_herb(self, herb: Herb) -> None:
        self.__HERB = herb

    def water(self) -> None:
        if isinstance(self.__HERB, (Potato, Tomato, Pepper)):
            self.__HERB.water()

    def fertilize(self) -> None:
        if isinstance(self.__HERB, (Potato, Tomato, Pepper)):
            self.__HERB.fertilize()

    def del_herb(self) -> None:
        self.__HERB = False

    def maybe_weed(self) -> None:
        if random.choice([1, 2, 3]) == 1:
            self.__WEED = True


class Herb:  # Все растения
    def __init__(self, life_day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        self.__age = life_day
        self.__disease = disease
        self.__pest = pest
        self.__harvest_day = harvest_day

    def pest_control(self) -> None:
        if self.__pest is True:
            self.__pest = False
            print('Растение успешно обработано от вредителей')
        else:
            print('Растению не нужна обработка от вредителей')

    def disease_control(self) -> None:
        if self.__disease is True:
            self.__disease = False
            print('Растение успешно вылечено от болезней')
        else:
            print('Растение не заражено болезнями')

    def get_age(self) -> int:
        return self.__age

    def get_name(self) -> str:
        return "None"

    def day(self) -> None:
        self.__age += 1

    def get_info(self) -> dict:
        tmp_dict = {"ill": self.__disease, "pest": self.__pest, "life_day": self.__age,
                    "harvest_day": self.__harvest_day, "type": self.get_name()}
        return tmp_dict

    def get_ill(self) -> bool:
        return self.__disease

    def get_pest(self) -> bool:
        return self.__pest

    def get_harvest_day(self) -> int:
        return self.__harvest_day

    def harvesting(self) -> None:
        self.__harvest_day = 0

    def plus_harvest_day(self) -> None:
        self.__harvest_day += 1

    def maybe_ill_pest(self) -> None:
        if not self.get_pest():
            if random.choice([1, 2, 3, 4, 5]) == 1:
                self.__pest = True
        if not self.get_ill():
            if random.choice([1, 2, 3, 4, 5]) == 1:
                self.__disease = True


class Tree(Herb):  # Деревья
    def __init__(self, life_day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(life_day, harvest_day, disease, pest)
        self.__fruiting_period = 5
        self.__growth_time = 7

    def check_harvest(self) -> bool:
        if super().get_harvest_day() >= self.__fruiting_period:
            return True
        else:
            return False

    def day(self) -> None:
        super().day()
        if super().get_age() >= self.__growth_time:
            super().plus_harvest_day()


class AppleTree(Tree):  # Яблоня
    def __init__(self, life_day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(life_day, harvest_day, disease, pest)
        self.__name = 'apple'
        self.__lifetime = 22
        self.__crop_price = 20

    def get_name(self) -> str:
        return self.__name

    def harvesting(self) -> int:
        super().harvesting()
        return self.__crop_price

    def check_alive(self) -> bool:
        if super().get_pest() and super().get_ill():
            return False
        elif super().get_age() >= self.__lifetime:
            return False
        else:
            return True


class PeerTree(Tree):  # Груша
    def __init__(self, life_day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(life_day, harvest_day, disease, pest)
        self.__name = 'peer'
        self.__lifetime = 20
        self.__crop_price = 20

    def get_name(self) -> str:
        return self.__name

    def harvesting(self) -> int:
        super().harvesting()
        return self.__crop_price

    def check_alive(self) -> bool:
        if super().get_pest() and super().get_ill():
            return False
        elif super().get_age() >= self.__lifetime:
            return False
        else:
            return True


class CultivatedPlant(Herb):  # Культурные растения
    def __init__(self, water: int, fertilizer: int, life_day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(life_day, harvest_day, disease, pest)
        self.__water_lvl = water
        self.__fertilization_lvl = fertilizer
        self.__fruiting_period = 3
        self.__growth_time = 4

    def check_harvest(self) -> bool:
        if super().get_harvest_day() >= self.__fruiting_period:
            return True
        else:
            return False

    def water_level(self) -> int:
        return self.__water_lvl

    def set_water_level(self, num: int) -> None:
        self.__water_lvl = num

    def fertilization_level(self) -> int:
        return self.__fertilization_lvl

    def set_fertilization_level(self, num: int) -> None:
        self.__fertilization_lvl = num

    def water(self) -> None:  # Полить
        self.__water_lvl = 100

    def fertilize(self) -> None:  # Удобрить
        self.__fertilization_lvl = 100

    def get_info(self) -> dict:
        tmp_dict = super().get_info()
        tmp_dict["water"] = self.__water_lvl
        tmp_dict["level_fertilization"] = self.__fertilization_lvl
        return tmp_dict

    def get_short_info(self) -> str:
        if super().get_ill():
            tmp_str = "Ill+|"
        else:
            tmp_str = "Ill-|"
        if super().get_pest():
            tmp_str = tmp_str + "Pest+|"
        else:
            tmp_str = tmp_str + "Pest-|"
        if self.check_harvest():
            tmp_str = tmp_str + "Harvest+|"
        else:
            tmp_str = tmp_str + "Harvest-|"
        tmp_str = tmp_str + "Water-{}".format(self.__water_lvl) + "|Fertiliser-{}|".format(self.__fertilization_lvl)
        return tmp_str

    def min_w(self, num: int) -> None:
        self.__water_lvl -= num

    def day(self) -> None:
        super().day()
        if super().get_age() >= self.__growth_time:
            super().plus_harvest_day()


class Potato(CultivatedPlant):
    def __init__(self, water: int, fertilizer: int, day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(water, fertilizer, day, harvest_day, disease, pest)
        self.__name = 'potato'
        self.__lifetime = 10
        self.__crop_price = 10
        self.__water_consumption = 5
        self.__fertilizer_consumption = 5

    def day(self) -> None:
        super().day()
        super().set_water_level(super().water_level() - self.__water_consumption)
        super().set_fertilization_level(super().fertilization_level() - self.__fertilizer_consumption)

    def get_name(self) -> str:
        return self.__name

    def harvesting(self) -> int:
        super().harvesting()
        return self.__crop_price

    def check_alive(self) -> bool:
        if super().water_level() < 0 or super().fertilization_level() < 0:
            return False
        elif super().get_age() >= self.__lifetime:
            return False
        else:
            return True


class Tomato(CultivatedPlant):
    def __init__(self, water: int, fertilizer: int, day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(water, fertilizer, day, harvest_day, disease, pest)
        self.__name = 'tomato'
        self.__lifetime = 14
        self.__crop_price = 14
        self.__water_consumption = 10
        self.__fertilizer_consumption = 15

    def day(self) -> None:
        super().day()
        super().set_water_level(super().water_level() - self.__water_consumption)
        super().set_fertilization_level(super().fertilization_level() - self.__fertilizer_consumption)

    def get_name(self) -> str:
        return self.__name

    def harvesting(self) -> int:
        super().harvesting()
        return self.__crop_price

    def check_alive(self) -> bool:
        if super().water_level() < 0 or super().fertilization_level() < 0:
            return False
        elif super().get_age() >= self.__lifetime:
            return False
        else:
            return True


class Pepper(CultivatedPlant):
    def __init__(self, water: int, fertilizer: int, day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(water, fertilizer, day, harvest_day, disease, pest)
        self.__name = 'pepper'
        self.__lifetime = 12
        self.__crop_price = 12
        self.__water_consumption = 10
        self.__fertilizer_consumption = 10

    def day(self) -> None:
        super().day()
        super().set_water_level(super().water_level() - self.__water_consumption)
        super().set_fertilization_level(super().fertilization_level() - self.__fertilizer_consumption)

    def get_name(self) -> str:
        return self.__name

    def harvesting(self) -> int:
        super().harvesting()
        return self.__crop_price

    def check_alive(self) -> bool:
        if super().water_level() < 0 or super().fertilization_level() < 0:
            return False
        elif super().get_age() >= self.__lifetime:
            return False
        else:
            return True