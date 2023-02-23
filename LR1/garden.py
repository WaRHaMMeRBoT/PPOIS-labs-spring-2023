from typing import *
from abc import ABC, abstractmethod
import random


class Weather(ABC):
    '''Абстрактный класс погоды.'''
    @abstractmethod
    def get_days(self) -> int:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def increase_days(self) -> None:
        pass


class Garden:
    '''Реализует модель сада.'''

    def __init__(self) -> None:
        self.__garden_state: List[GardenBed] = []
        self.__garden_product: Dict[str, int] = {}
        self.weather: Weather = Sun()
        self.pests: Pests = Pests()
        self.weed: Weed = Weed()
        self.fertilizer: Fertilizer = Fertilizer()
        self.watering: Warning = Watering()
        self.disease: Disease = Disease()

    def add_garden_bed(self) -> None:
        '''Добавялет новую грядку.'''
        self.__garden_state.append(GardenBed('0', '0', '0'))

    def delete_garden_bed(self, index: int) -> None:
        '''Удаляет грядку.'''
        try:
            del self.__garden_state[index]
        except BaseException:
            print('Такой грядки не существует!')

    @property
    def get_product(self) -> Dict[str, int]:
        '''Возвращает словарь с урожаем.'''
        return self.__garden_product

    @property
    def garden(self) -> List['GardenBed']:
        '''Возвращает список с грядками.'''
        return self.__garden_state

    def harvest(self, index: int) -> None:
        '''Обновление собранного урожая.'''
        if self.__garden_product.get(
                self.__garden_state[index].plant_data.product.product_data[1]):
            self.__garden_product[self.__garden_state[index].plant_data.product.product_data[1]
                                  ] += self.__garden_state[index].plant_data.product.product_data[0]
        else:
            self.__garden_product[self.__garden_state[index].plant_data.product.product_data[1]
                                  ] = self.__garden_state[index].plant_data.product.product_data[0]

    def collect_die_plant(self) -> None:
        '''Проверка мертвых растений.'''
        for i in self.__garden_state:
            if i.type != '0':
                i.check_health()
                i.plant_die()
        self.__garden_state[:] = [
            i for i in self.__garden_state if i.die == False]


class GardenBed:
    '''Модель грядки.'''

    def __init__(self, name, product_name, type) -> None:
        self.__name: str = name
        self.__type: str = type
        self.__product_name: str = product_name
        self.__state: Dict[str,
                           str] = {'Вредители': 'Нет',
                                   'Сорняки': 'Нет',
                                   'Засыхает': 'Нет',
                                   'Болезни': 'Нет',
                                   'Урожай': 'Нет'}
        self.__inside_step: int = 0
        self.__die: bool = False

    def plant(self) -> None:
        '''Посадка растения на выбранную грядку.'''
        if self.__type == 'растение':
            self.__object: Plant = Plant(self.__product_name)
        else:
            self.__object: Tree = Tree(self.__product_name)

    def next_step(self, object: Garden) -> None:
        '''ОБработка автоматического моделироавния.'''
        self.__inside_step += 1
        object.weather.increase_days()
        self.harvest()
        random_number: int = random.randint(0, 3)
        if random_number == 0:
            if isinstance(object.weather, Sun):
                object.weather = Rain()
            else:
                object.weather = Sun()

    def __str__(self) -> str:
        return self.__name

    @property
    def name(self) -> str:
        '''Возвращает имя.'''
        return self.__name

    @property
    def get_state(self) -> Dict[str, str]:
        '''Возвращает список состояния.'''
        return self.__state

    @get_state.setter
    def get_state(self, value: Dict[str, str]) -> None:
        '''Изменяем список состояния.'''
        self.__state = value

    def set_state(self, type: str, value: str) -> None:
        '''Частичное изменение списка состояния.'''
        self.__state[type] = value

    @property
    def plant_data(self) -> object:
        '''Возвращает объект грядки.'''
        return self.__object

    @property
    def step(self) -> int:
        '''Возвращает текущий шаг.'''
        return self.__inside_step

    @step.setter
    def step(self, value: int) -> None:
        '''Изменяет шаг.'''
        self.__inside_step = value

    def harvest(self) -> None:
        '''Проверка готовности урожая.'''
        if self.__inside_step % 5 == 0:
            self.__state['Урожай'] = 'Готов'

    def take_harvest(self) -> None:
        '''Сбор урожая.'''
        if self.__state['Урожай'] == 'Готов':
            self.__state['Урожай'] = 'Нет'
            self.__object.add_product()
        else:
            print('Урожай еще не готов!')

    def plant_die(self) -> None:
        '''Проверка на смерть от возраста.'''
        if self.__object.AGE < self.__inside_step:
            print(f'{self.__name} погиб(')
            self.__die = True

    def check_health(self) -> None:
        '''Проверка на смерть от болезней, вредителей и т.д.'''
        if self.__object.health < 0 or self.__object.water_lavel < 0:
            print(f'{self.__name} погиб(')
            self.__die = True

    @property
    def die(self):
        '''Возвращает смерть растения.'''
        return self.__die

    @die.setter
    def die(self, value):
        '''Обновляем смерть растения.'''
        self.__die = value

    @property
    def type(self):
        '''Возвращаем тип растенияю.'''
        return self.__type


class Tree(GardenBed):
    '''Модель деревьев.'''
    AGE: int = 25

    def __init__(self, product_name: str) -> None:
        self.__health: int = 100
        self.__water_lavel: int = 100
        self.__product: TreeProduct = TreeProduct(product_name)

    @property
    def health(self) -> int:
        '''Возвращает здоровье.'''
        return self.__health

    @health.setter
    def health(self, value: int) -> None:
        '''Обновляет здоровье'''
        self.__health += value

    def load_health(self, value: int) -> None:
        '''Загрузка здоровья.'''
        self.__health = value

    def health_damage(self, value: int) -> None:
        '''Уменьшаем здоровье.'''
        self.__health -= value

    def water_damage(self, value: int) -> None:
        '''Уменьшаем воду.'''
        self.__water_lavel -= value

    def add_product(self) -> None:
        '''Добавление собранного урожая.'''
        self.__product.set_amount_harvest()

    @property
    def water_lavel(self) -> int:
        '''Возвращаем уровень воды.'''
        return self.__water_lavel

    @water_lavel.setter
    def water_lavel(self, value: int) -> None:
        '''Установливаем уровня воды.'''
        self.__water_lavel = value

    @property
    def product(self) -> 'TreeProduct':
        '''Возвращаем объект грядки.'''
        return self.__product


class Plant(GardenBed):
    '''Модель растений.'''
    AGE: int = 15

    def __init__(self, product_name: str) -> None:
        self.__health: int = 100
        self.__water_lavel: int = 100
        self.__product: PlantProduct = PlantProduct(product_name)

    @property
    def health(self) -> int:
        '''Возвращает здоровье.'''
        return self.__health

    @health.setter
    def health(self, value: int) -> None:
        '''Обновляет здоровье'''
        self.__health += value

    def load_health(self, value: int) -> None:
        '''Загрузка здоровья.'''
        self.__health = value

    def health_damage(self, value: int) -> None:
        '''Уменьшаем здоровье.'''
        self.__health -= value

    def water_damage(self, value: int) -> None:
        '''Уменьшаем воду.'''
        self.__water_lavel -= value

    def add_product(self) -> None:
        '''Добавление собранного урожая.'''
        self.__product.set_amount_harvest()

    @property
    def water_lavel(self) -> int:
        '''Возвращаем уровень воды.'''
        return self.__water_lavel

    @water_lavel.setter
    def water_lavel(self, value: int) -> None:
        '''Установливаем уровня воды.'''
        self.__water_lavel = value

    @property
    def product(self) -> 'PlantProduct':
        '''Возвращаем объект грядки.'''
        return self.__product

class TreeProduct(Tree):
    '''Класс реализует продукты дерева.'''

    def __init__(self, product_name: str) -> None:
        self.__product_name: str = product_name
        self.__amount_product: int = 0

    def set_amount_harvest(self) -> None:
        '''Обновляем урожай.'''
        self.__amount_product += 10

    @property
    def product_data(self) -> object:
        '''Возвращаем кортеж имя продукта и количество.'''
        return (self.__amount_product, self.__product_name)

    @product_data.setter
    def product_data(self, value: int) -> None:
        '''Обновялем урожай.'''
        self.__amount_product = value


class PlantProduct(Plant):
    '''Класс реализует продукты растений.'''

    def __init__(self, product_name: str) -> None:
        self.__product_name: str = product_name
        self.__amount_product: int = 0

    def set_amount_harvest(self) -> None:
        '''Обновляем урожай.'''
        self.__amount_product += 10

    @property
    def product_data(self) -> object:
        '''Возвращаем кортеж имя продукта и количество.'''
        return (self.__amount_product, self.__product_name)

    @product_data.setter
    def product_data(self, value: int) -> None:
        '''Обновялем урожай.'''
        self.__amount_product = value


class Pests:
    '''Класс реализует поведение вредителей.'''

    def save(self, object: GardenBed) -> None:
        '''Сохраняем объект.'''
        self.__object: GardenBed = object

    def destroy_plant(self) -> None:
        '''Вредители на грядке.'''
        if self.__object.get_state['Вредители'] == 'Заражен вредителями':
            self.__object.plant_data.health_damage(10)
        elif random.randint(0, 5) == 0:
            self.__object.set_state('Вредители', 'Заражен вредителями')

    def kill_pests(self) -> None:
        '''Убиваем вредителей.'''
        self.__object.set_state('Вредители', 'Нет')


class Weed:
    '''Класс реализует модель сорняков.'''

    def save(self, object: GardenBed) -> None:
        self.__object: GardenBed = object

    def grow_weed(self) -> None:
        '''Рост сорняков.'''
        if self.__object.get_state['Сорняки'] == 'Есть':
            self.__object.plant_data.health_damage(10)
        elif self.__object.step % 10 == 0:
            self.__object.set_state('Сорняки', 'Есть')

    def weed(self) -> None:
        '''Удаление сорняков.'''
        self.__object.set_state('Сорняки', 'Нет')


class Fertilizer:
    '''Модель удобрения.'''

    def save(self, object: GardenBed) -> None:
        self.__object: GardenBed = object

    def fertilize(self) -> None:
        '''Удобрение грядки.'''
        if self.__object.type != '0':
            self.__object.plant_data.health = 10


class Watering:
    '''Модель полива.'''

    def save(self, object: GardenBed, weather: Weather) -> None:
        self.__object: GardenBed = object
        self.__weather: Weather = weather

    def watering(self) -> None:
        '''Проверка на засыхание.'''
        if self.__object.get_state['Засыхает'] == 'Да':
            if self.__weather.get_name == 'дождь' or self.__weather.get_days == 1:
                self.water()
                return None
            self.__object.plant_data.water_damage(10)
        elif self.__weather.get_name == 'солнце' and self.__weather.get_days % 5 == 0:
            self.__object.set_state('Засыхает', 'Да')

    def water(self) -> None:
        '''Полив.'''
        self.__object.set_state('Засыхает', 'Нет')


class Disease:
    '''Класс реализует бользнь растений и деревьев.'''

    def save(self, object: GardenBed) -> None:
        self.__object: GardenBed = object

    def disease_damage(self) -> None:
        '''Урон от болезни.'''
        if self.__object.get_state['Болезни'] == 'Болен':
            self.__object.plant_data.health_damage(10)
        elif random.randint(0, 5) == 5:
            self.__object.set_state('Болезни', 'Болен')

    def treat(self) -> None:
        '''Лечение.'''
        self.__object.set_state('Болезни', 'Нет')


class Rain(Weather):
    '''Класс реализует дождь.'''

    def __init__(self) -> None:
        self.__days: int = 1
        self.__name: str = 'дождь'

    @property
    def get_days(self) -> int:
        '''Количество дней.'''
        return self.__days

    @get_days.setter
    def get_days(self, value: int) -> None:
        '''Обновление количества дней.'''
        self.__days = value

    @property
    def get_name(self) -> str:
        '''Текущая погода.'''
        return self.__name

    def increase_days(self) -> None:
        '''Продолжительность погоды.'''
        self.__days += 1


class Sun(Weather):
    '''Класс реализуте солнце.'''

    def __init__(self) -> None:
        self.__days: int = 1
        self.__name: str = 'солнце'

    @property
    def get_days(self) -> int:
        '''Количество дней.'''
        return self.__days

    @get_days.setter
    def get_days(self, value: int) -> None:
        '''Обновление количества дней.'''
        self.__days = value

    @property
    def get_name(self) -> str:
        '''Текущая погода.'''
        return self.__name

    def increase_days(self) -> None:
        '''Продолжительность погоды.'''
        self.__days += 1
