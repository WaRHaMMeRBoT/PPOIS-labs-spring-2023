from prettytable import PrettyTable

from garden import *
from help import commands_help
from create_and_update_file import *


class ManageGarden:
    '''Контролирует симуляцию сада.'''

    def __init__(self) -> None:
        self.__garden: Garden = Garden()
        self.__represent_state: ShowGarden = ShowGarden()

    def command_hadler(self) -> None:
        '''Обрабатывает комманды.'''
        exit: bool = False
        load_from_file(self.__garden)
        self.__represent_state.show_field(self.__garden)
        self.__command: List[str] = self.command_input().split()
        while not exit:
            while True:
                try:
                    if self.__command[0] == 'добавить' and self.__command[1] == 'грядку' and len(
                            self.__command) == 2:
                        self.__garden.add_garden_bed()
                    elif self.__command[0] == 'удалить' and self.__command[1] == 'грядку' and len(self.__command) == 3:
                        self.__garden.delete_garden_bed(int(self.__command[2]))
                    elif self.__command[0] == 'далее' and len(self.__command) == 1:
                        break
                    elif self.__command[0] == 'выход' and len(self.__command) == 1:
                        self.save()
                        return None
                    elif self.__command[0] == 'удобрить' and self.__command[1] == 'грядку' and len(self.__command) == 3:
                        self.__garden.fertilizer.save(
                            self.__garden.garden[int(self.__command[2])])
                        self.__garden.fertilizer.fertilize()
                    elif self.__command[0] == 'полить' and self.__command[1] == 'грядку' and len(self.__command) == 3:
                        self.__garden.watering.save(
                            self.__garden.garden[int(self.__command[2])], self.__garden.weather)
                        self.__garden.watering.water()
                    elif self.__command[0] == 'вылечить' and self.__command[1] == 'грядку' and len(self.__command) == 3:
                        self.__garden.disease.save(
                            self.__garden.garden[int(self.__command[2])])
                        self.__garden.disease.treat()
                    elif self.__command[0] == 'посадить' and (self.__command[1] == 'растение' or self.__command[1] == 'дерево') \
                            and len(self.__command) == 5:
                        if len(self.__garden.garden) > int(self.__command[-1]) \
                                and self.__garden.garden[int(self.__command[-1])].type == '0':
                            self.__garden.garden[int(self.__command[-1])] = GardenBed(
                                self.__command[2], self.__command[3], self.__command[1])
                            self.__garden.garden[int(
                                self.__command[-1])].plant()
                        else:
                            print('Ошибка. Данная клетка уже занята!')
                    elif self.__command[0] == 'уничтожить' and self.__command[1] == 'вредителей' and len(self.__command) == 3:
                        self.__garden.pests.save(
                            self.__garden.garden[int(self.__command[2])])
                        self.__garden.pests.kill_pests()
                    elif self.__command[0] == 'прополоть' and self.__command[1] == 'грядку' and len(self.__command) == 3:
                        self.__garden.weed.save(
                            self.__garden.garden[int(self.__command[2])])
                        self.__garden.weed.weed()
                    elif self.__command[0] == 'собрать' and self.__command[1] == 'урожай' and len(self.__command) == 3:
                        if self.__garden.garden[int(
                                self.__command[2])].type != '0':
                            self.__garden.garden[int(
                                self.__command[2])].take_harvest()
                            self.__garden.harvest(int(self.__command[2]))
                    elif self.__command[0] == 'справка' and len(self.__command) == 1:
                        print(commands_help)
                    elif self.__command[0] == 'урожай' and len(self.__command) == 1:
                        for i in self.__garden.get_product.items():
                            print(*i)
                    elif self.__command[0] == 'погода' and len(self.__command) == 1:
                        print(f'Погода: {self.__garden.weather.get_name}')
                    else:
                        print(f'{self.__command} не найдена, повторите снова: ')

                    self.__represent_state.show_field(self.__garden)
                    self.__command = self.command_input().split()
                except IndexError:
                    print('Такой грядки не существует или её нет!')
                    self.__command = self.command_input().split()
            self.next_step()
            self.__represent_state.show_field(self.__garden)
            self.__command = self.command_input().split()

    def command_input(self) -> str:
        '''Ввод новой команды.'''
        return input('Команда: ')

    def next_step(self):
        '''Автоматическое моделирование процессов,
        которые происходят в саду.'''
        for i in self.__garden.garden:
            if i.type != '0':
                i.next_step(self.__garden)
                self.__garden.pests.save(i)
                self.__garden.pests.destroy_plant()
                self.__garden.weed.save(i)
                self.__garden.weed.grow_weed()
                self.__garden.watering.save(i, self.__garden.weather)
                self.__garden.watering.watering()
                self.__garden.disease.save(i)
                self.__garden.disease.disease_damage()
        self.__garden.collect_die_plant()

    def save(self) -> None:
        '''Сохраняет данные в файл.'''
        create_data_for_file(self.__garden.garden, self.__garden.weather)


class ShowGarden:
    '''Отображает поле.'''

    def show_field(self, garden: Garden) -> None:
        '''Отображает таблицу с текущем состоянием сада.'''
        self.__table_object: PrettyTable = PrettyTable()
        self.__table_object.field_names: List[str] = [
            'Номер',
            'Грядка',
            'HP',
            'Вода',
            'Вредители',
            'Сорняки',
            'Засыхает',
            'Болезни',
            'Урожай']
        self.__garden: Garden = garden
        counter: int = 0
        for i in self.__garden.garden:
            if i.type != '0':
                self.__table_object.add_row([counter,
                                             i,
                                             i.plant_data.health,
                                             i.plant_data.water_lavel,
                                             i.get_state['Вредители'],
                                             i.get_state['Сорняки'],
                                             i.get_state['Засыхает'],
                                             i.get_state['Болезни'],
                                             i.get_state['Урожай']])
            else:
                self.__table_object.add_row([counter, 0, 0, 0, 0, 0, 0, 0, 0])
            counter += 1
        print(self.__table_object)
