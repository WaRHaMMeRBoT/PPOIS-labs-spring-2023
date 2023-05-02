from prettytable import PrettyTable

from garden import *
from help import commands_help
from create_and_update_file import *


class ManageGarden:
    '''Контролирует симуляцию сада.'''

    def __init__(self) -> None:
        self.__garden: Garden = Garden()
        self.__represent_state: ShowGarden = ShowGarden()

    def command_hadler(self, args) -> None:
        '''Обрабатывает комманды.'''
        load_from_file(self.__garden)
        self.__command = args[2:]
        try:
            if self.__command[0] == 'add' and len(self.__command) == 1:
                self.__garden.add_garden_bed()
            elif self.__command[0] == 'rm' and len(self.__command) == 2:
                self.__garden.delete_garden_bed(int(self.__command[1]))
            elif self.__command[0] == 'next' and len(self.__command) == 1:
                self.next_step()
            elif self.__command[0] == 'fert' and len(self.__command) == 2:
                self.__garden.fertilizer.save(
                    self.__garden.garden[int(self.__command[1])])
                self.__garden.fertilizer.fertilize()
            elif self.__command[0] == 'water' and len(self.__command) == 2:
                self.__garden.watering.save(
                    self.__garden.garden[int(self.__command[1])], self.__garden.weather)
                self.__garden.watering.water()
            elif self.__command[0] == 'hp' and len(self.__command) == 2:
                self.__garden.disease.save(
                    self.__garden.garden[int(self.__command[1])])
                self.__garden.disease.treat()
            elif self.__command[0] == 'new' and (self.__command[1] == 't' or self.__command[1] == 'p') \
                    and len(self.__command) == 5:
                if len(self.__garden.garden) > int(self.__command[-1]) \
                        and self.__garden.garden[int(self.__command[-1])].type == '0':
                    self.__garden.garden[int(self.__command[-1])] = GardenBed(
                        self.__command[2], self.__command[3], self.__command[1])
                    self.__garden.garden[int(
                        self.__command[-1])].plant()
                else:
                    print('Ошибка. Данная клетка уже занята!')
            elif self.__command[0] == 'rmpest'  and len(self.__command) == 2:
                self.__garden.pests.save(
                    self.__garden.garden[int(self.__command[1])])
                self.__garden.pests.kill_pests()
            elif self.__command[0] == 'weed'  and len(self.__command) == 2:
                self.__garden.weed.save(
                    self.__garden.garden[int(self.__command[1])])
                self.__garden.weed.weed()
            elif self.__command[0] == 'take' and len(self.__command) == 2:
                if self.__garden.garden[int(self.__command[1])].type != '0':
                    self.__garden.garden[int(self.__command[1])].take_harvest()
                    self.__garden.harvest(int(self.__command[1]))
            elif self.__command[0] == 'harvest' and len(self.__command) == 1:
                for i in self.__garden.get_product.items():
                    print(*i)
            elif self.__command[0] == 'weather' and len(self.__command) == 1:
                print(f'Погода: {self.__garden.weather.get_name}')
            elif self.__command[0] == 'show' and len(self.__command) == 1:
                self.__represent_state.show_field(self.__garden)
            else:
                print(f'{self.__command} не найдена, повторите снова: ')
        except IndexError:
            print('Такой грядки не существует или её нет!')        
        self.save()

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

    @property
    def garden(self):
        return self.__garden


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
