import pickle
import sys
import threading
import time
import random

from constants import Constants


class Watering:
    def pour_bed(self, bed):
        if bed is None:
            return
        print("---Полив!")
        for temp in bed.place:
            if temp is None:
                continue
            else:
                self.pour_plant(temp)

    def pour_plant(self, plant):
        plant.get_water(self)


class Fertilizer:
    def fertile_garden(self, garden):
        if not garden:
            return
        print("--- Сад удобрен")
        self.fertile_bed(garden.bed)
        self.fertile_trees(garden.trees)

    def fertile_bed(self, bed):
        if not bed:
            return
        for temp in bed.place:
            if not temp:
                continue
            self.fertile_plant(temp)

    def fertile_trees(self, trees):
        for temp in trees:
            self.fertile_plant(temp)

    @staticmethod
    def fertile_plant(plant):
        if plant.get_immunity_info() > Constants.IMMUNITY_MINIMUM:
            plant.cure_disease()
        plant.get_immunity()


class Love:
    def cure_garden(self, garden):
        if garden is None:
            return
        self.cure_bed(garden.bed)
        self.cure_trees(garden.trees)

    def cure_bed(self, bed):
        if bed is None:
            return
        for plant in bed.place:
            if plant is None:
                continue
            self.cure_plant(plant)

    def cure_plant(self, plant):
        temp: Plant = plant
        if temp.get_damage_info() > Constants.DAMAGE_MINIMUM:
            temp.cure_damage()
            if temp.is_wrecked:
                print(" ---Вредители убраны!")

        temp.reduce_damage(self)

    def cure_trees(self, trees):
        for tree in trees:
            self.cure_plant(tree)


class Garden:
    def __init__(self):
        self.trees: [Tree] = []
        self.bed: Bed = Bed(Constants.MAX_SPACE)
        self.misery: Misery = Misery()
        self.weather: Weather = Weather()

        self.is_on: bool = True
        self.is_saved: bool = False

    def new_seed(self):
        if self.bed is not None:
            new_seed = Seed(self.bed)
            self.bed.allocate_space(new_seed)
            print(f"{new_seed} ---Посажено новое семя на грядку!")

    def new_fruit_tree(self):
        new_tree = FruitTree()
        self.trees.append(new_tree)
        print(new_tree, " ---Посажено новое фруктовое дерево в саду!")

    def fertile_garden(self):
        fertilizer = Fertilizer()
        fertilizer.fertile_garden(self)

    def love_garden(self):
        care = Love()
        care.cure_garden(self)

    def weeding_garden(self):
        for plant in self.bed.place:
            if plant is None:
                continue

            if isinstance(plant, Weed):
                self.bed.remove_from_bed(plant)

    def get_trees(self):
        return self.trees

    def new_bed(self):
        if self.bed is None:
            self.bed = Bed(Constants.MAX_SPACE)
            self.bed.place = [None] * Constants.MAX_SPACE
            self.bed.space_tracker = Constants.MAX_SPACE
        print(self.bed, "---Создана грядка!")

    def exist(self):
        if self.is_saved is True:
            self.misery = Misery()
            self.weather = Weather()

        self.is_on = True

        while self.is_on:
            self.misery.misery_is(self)
            self.weather.weather_is(self)

            self.state()
            for tree in self.trees:
                tree.live()
            for plant in self.bed.place:
                if not plant:
                    continue
                temp: Plant = plant
                temp.live()

            for tree in self.trees:
                print(tree)
            for plant in self.bed.place:
                if not plant:
                    continue
                print(plant)
            time.sleep(5)
            print()

    def state(self):
        for tree in self.trees:
            if tree is None:
                continue

            if not tree.state_for_live():
                print(tree, "---Убрано с сада!")
                self.trees.remove(tree)
                return False

        for plant in self.bed.place:
            if plant is None:
                continue

            if not plant.state_for_live():
                if isinstance(plant, Weed):
                    print(plant, "---Погиб!")
                else:
                    print(plant, "---Убрано с грядки!")

                self.bed.remove_from_bed(plant)
                return False

        return True


class Bed:
    def __init__(self, space: int):
        self.place: list[Plant] = [None] * Constants.MAX_SPACE
        self.space_tracker: int = space

    def get_space(self):
        return enumerate(self.place)

    def allocate_space(self, plant):
        if self.space_tracker == -1:
            return
        for i in range(len(self.place)):
            if self.place[i] is None:
                self.place[i] = plant
                self.space_tracker -= 1
                break

    def remove_from_bed(self, to_remove):
        for i in range(len(self.place)):
            i: int
            if self.place[i] == to_remove:
                self.place[i] = None

    def __str__(self):
        return "Грядка "


class Plant:
    def __init__(self):
        self.damage: int = Constants.DAMAGE_SUPPLY
        self.water: int = Constants.WATER_SUPPLY
        self.sun: int = Constants.SOLAR_ENERGY_SUPPLY
        self.immunity: int = Constants.IMMUNITY_SUPPLY
        self.is_ill: bool = False
        self.is_wrecked: bool = False

    def live(self):
        self.use_water()
        self.use_sun()
        if self.is_ill:
            self.use_immunity(Disease())
        if self.is_wrecked:
            self.get_damage(Wrecker())

    def set_tree_water(self):
        self.water = 5 * Constants.WATER_SUPPLY

    def get_water_info(self):
        return self.water

    def get_sun_info(self):
        return self.sun

    def get_immunity_info(self):
        return self.immunity

    def get_damage_info(self):
        return self.damage

    def cure_damage(self):
        self.is_wrecked = False

    def cure_disease(self):
        self.is_ill = False

    # water issues
    def get_water(self, source_of_water):
        if isinstance(source_of_water, Rain):
            self.water += Constants.RAIN_BENEFIT
        if isinstance(source_of_water, Watering):
            self.water += Constants.WATERING_BENEFIT

    def use_water(self):
        self.water -= Constants.WATER_USAGE

    # sun issues
    def get_sun(self):
        self.sun += Constants.SOLAR_ENERGY_BENEFIT
        self.water -= Constants.WATER_USAGE

    def use_sun(self):
        self.sun -= Constants.SOLAR_ENERGY_USAGE

    # immunity issues
    def get_immunity(self):
        if self.immunity > Constants.IMMUNITY_MINIMUM:
            self.is_ill = False
        self.immunity += Constants.FERTILIZER_BENEFIT

    def use_immunity(self, disease):
        self.is_ill = True
        self.immunity -= Constants.IMMUNITY_USAGE

    # damage issues
    def get_damage(self, wrecker):
        self.is_wrecked = True
        self.damage -= Constants.DAMAGE

    def reduce_damage(self, love):
        if self.damage > Constants.DAMAGE_MINIMUM:
            self.is_wrecked = False
        self.damage += Constants.CARE_BENEFIT

    def state_for_fertility(self):
        if self.water < Constants.WATER_MINIMUM:
            return False
        if self.sun < Constants.SOLAR_ENERGY_MINIMUM:
            return False
        if self.immunity < Constants.IMMUNITY_MINIMUM:
            return False
        if self.damage < Constants.DAMAGE_MINIMUM:
            return False
        return True

    def state_for_live(self):
        if self.water < 0:
            return False
        if self.sun < 0:
            return False
        if self.immunity < 0:
            return False
        if self.damage < 0:
            return False
        return True

    def __str__(self):
        res = "Овощ ***вода-{0} солнце-{1} иммунитет-{2} повреждения-{3} ***".format(
            self.get_water_info(), self.get_sun_info(), self.get_immunity_info(), self.get_damage_info())

        if self.is_ill:
            res += " Заражено болезнью!"
        if self.is_wrecked:
            res += " Заражено вредителями!"

        if self.water < Constants.WATER_MINIMUM:
            res += " Необходим полив!"
        if self.sun < Constants.SOLAR_ENERGY_MINIMUM:
            res += " Необходимо солнце!"
        if self.immunity < Constants.IMMUNITY_MINIMUM:
            res += " Необходимо удобрение!"
        if self.damage < Constants.DAMAGE_MINIMUM:
            res += " Необходима забота!"

        return res


class Reader(threading.Thread):
    def run(self):
        global garden_representation
        try:
            with open("store.pickle", "rb") as f:
                garden_representation = pickle.load(f)
                garden_representation.is_saved = True
        except FileNotFoundError:
            garden_representation.new_bed()
            garden_representation.is_saved = False
        garden_representation.exist()


class Writer(threading.Thread):
    def run(self):
        global garden_representation

        while True:
            choice = input()
            if choice == "sd":
                garden_representation.new_seed()
            elif choice == "tr":
                garden_representation.new_fruit_tree()
            elif choice == "fl":
                garden_representation.fertile_garden()
            elif choice == "cr":
                garden_representation.love_garden()
            elif choice == "wt":
                watering = Watering()
                watering.pour_bed(garden_representation.bed)
            elif choice == "wd":
                garden_representation.weeding_garden()
            elif choice == "rt":
                for tree in garden_representation.trees:
                    if tree is None:
                        continue
                    garden_representation.get_trees().remove(tree)
                    break
            elif choice == "rs":
                for plant in garden_representation.bed.place:
                    if plant is None:
                        continue
                    if isinstance(plant, Seed):
                        garden_representation.bed.remove_from_bed(plant)
                        break
            elif choice == "rv":
                for plant in garden_representation.bed.place:
                    if plant is None:
                        continue
                    if not isinstance(plant, (Weed, Seed)):
                        garden_representation.bed.remove_from_bed(plant)
                        break
            elif choice == "rw":
                for plant in garden_representation.bed.place:
                    if plant is None:
                        continue
                    if isinstance(plant, Weed):
                        garden_representation.bed.remove_from_bed(plant)
                        break
            elif choice == "ex":
                with open("store.pickle", "wb") as f:
                    pickle.dump(garden_representation, f)
                garden_representation.is_on = False
                garden_representation.is_saved = True
                sys.exit()


class Seed(Plant):
    def __init__(self, my_bed):
        super().__init__()
        self.my_bed: Bed = my_bed
        self.time_before_blossom: int = Constants.SEED_BLOSSOM_DELAY

    def live(self):
        super().live()
        self.ripen()

    def sprout(self):
        if not self.state_for_fertility():
            return
        new_vegetable = Plant()

        for i in range(len(self.my_bed.place)):
            if self.my_bed.place[i] is None:
                continue
            if self.my_bed.place[i] == self:
                print(self.__str__() + "--- Проросло в овощ!")
                self.my_bed.place[i] = new_vegetable

    def ripen(self):
        if self.time_before_blossom == 0:
            self.sprout()
            return
        self.time_before_blossom -= 1

    def state_for_fertility(self):
        if super().state_for_fertility():
            return True
        else:
            return False

    def __str__(self):
        res = "Семя ***вода-%d солнце-%d иммунитет-%d повреждения-%d время до прорастания-%d***" % (
            self.get_water_info(), self.get_sun_info(), self.get_immunity_info(), self.get_damage_info(),
            self.time_before_blossom)

        if self.is_ill:
            res += " Заражено болезнью!"
        if self.is_wrecked:
            res += " Заражено вредителями!"

        return res


class Weed(Plant):
    def live(self):
        super().live()

    def capture_bed(self, bed: Bed):
        if bed is None:
            return

        for i in range(len(bed.place)):
            if bed.place[i] is None:
                bed.place[i] = self
                break
            if isinstance(bed.place[i], Weed):
                continue
            self.capture_plant(bed.place[i])

    def capture_plant(self, plant):
        plant.live()
        self.get_water(Watering())
        self.get_sun()

    def __str__(self):
        res = "Сорняк ***вода-{} солнце-{} иммунитет-{} повреждения-{} ***".format(self.get_water_info(),
                                                                                   self.get_sun_info(),
                                                                                   self.get_immunity_info(),
                                                                                   self.get_damage_info())

        if self.is_ill:
            res += " Заражено болезнью!"
        if self.is_wrecked:
            res += " Заражено вредителями!"

        return res


class Tree(Plant):
    def __init__(self):
        super().__init__()
        self.water: int = 5 * Constants.WATER_SUPPLY

    def state_for_live(self):
        return super().state_for_live()


class Fruit:
    def __init__(self, tree):
        self.my_tree: Tree = tree
        self.length_of_life: int = Constants.FRUIT_LIFE

    def live(self):
        self.length_of_life -= 1

    def __str__(self):
        return "Фрукт "


class FruitTree(Tree):
    def __init__(self):
        super().__init__()
        self.fruits: [Fruit] = []
        self.time_before_blossom: int = Constants.TREE_BLOSSOM_DELAY
        self.fertility: int = Constants.FRUIT_TREE_FERTILITY

    def ripen(self):
        if self.time_before_blossom == 0:
            self.new_fruit()
            return
        self.time_before_blossom -= 1

    def new_fruit(self):
        if not self.state_for_fertility():
            return
        self.fertility -= 1

        new_fruit = Fruit(self)
        self.fruits.append(new_fruit)
        self.time_before_blossom = Constants.TREE_BLOSSOM_DELAY
        print(self, " ---Вырос новый фрукт!")

    def state_for_live(self):
        if not (super().state_for_live()):
            print(self, "погибло от внешних факторов :(")
            return False
        return True

    def state_for_fertility(self):
        if not self.state_for_live():
            return False

        return self.fertility > 0

    def get_actual_number_of_fruits(self):
        count: int = 0
        for fruit in self.fruits:
            if fruit is not None:
                count += 1

        return count

    def live(self):
        super().live()
        self.ripen()

        for temp_fruit in self.fruits:
            temp_fruit.live()

        for fruit in self.fruits:
            if fruit.length_of_life < 0:
                self.fruits.remove(fruit)
                self.fertility += 1
                print(self, " --- Фрукт упал!")

    def __str__(self):
        res = "Дерево ***вода-{0} солнце-{1} иммунитет-{2} повреждения-{3} кол-во фруктов-{4} время до созревания " \
                "нового фрукта-{5}***".format(
                    self.get_water_info(), self.get_sun_info(), self.get_immunity_info(), self.get_damage_info(),
                    self.get_actual_number_of_fruits(), self.time_before_blossom)

        if self.is_ill:
            res += " Заражено болезнью!"
        if self.is_wrecked:
            res += " Заражено вредителями!"

        if self.get_water_info() < Constants.WATER_MINIMUM:
            res += " Необходим полив!"
        if self.get_sun_info() < Constants.SOLAR_ENERGY_MINIMUM:
            res += " Необходимо солнце!"
        if self.get_immunity_info() < Constants.IMMUNITY_MINIMUM:
            res += " Необходимо удобрение!"
        if self.get_damage_info() < Constants.DAMAGE_MINIMUM:
            res += " Необходима забота!"

        return res


class Wrecker:  # пока не появлялись
    def __init__(self):
        self.before_multiplying: int = Constants.WRECkER_MULTIPLYING_DELAY
        self.number_of_wreckers: int = 1

    def capture_garden(self, my_garden):
        if my_garden is None:
            return
        self.capture_bed(my_garden.bed)
        self.capture_trees(my_garden.get_trees())

    def capture_bed(self, bed):
        if bed is None:
            return
        for temp in bed.place:
            if temp is None:
                continue
            else:
                self.capture_plant(temp)

    def capture_trees(self, trees):
        for temp in trees:
            self.capture_plant(temp)

    def capture_plant(self, plant: Plant):
        if self.state():
            self.number_of_wreckers += 1
            self.before_multiplying = Constants.WRECkER_MULTIPLYING_DELAY
        for degreeOfDamage in range(self.number_of_wreckers):
            plant.get_damage(self)  # []
        self.before_multiplying -= 1

    def state(self):
        return self.before_multiplying == 0

    def __str__(self):
        return " Вредители "


class Disease:
    def infect_garden(self, my_garden):
        if my_garden is None:
            return
        self.infect_bed(my_garden.bed)
        self.infect_trees(my_garden.trees)

    def infect_bed(self, bed):
        if bed is None:
            return
        for temp in bed.place:
            if temp is None:
                continue
            self.infect_plant(temp)

    def infect_trees(self, trees):
        for temp in trees:
            self.infect_plant(temp)

    def infect_plant(self, plant):
        plant.use_immunity(self)


class Misery:
    def __init__(self):
        self.wrecker = None
        self.disease = None
        self.weed = None

    def misery_is(self, my_garden):
        if my_garden is None:
            return

        chance = random.randint(0, 364)
        if chance % 50 == 0:
            self.wrecker = Wrecker()
            self.wrecker.capture_garden(my_garden)

        if chance % 100 == 0:
            self.disease = Disease()
            self.disease.infect_garden(my_garden)

        if chance % 15 == 0:
            self.weed = Weed()
            self.weed.capture_bed(my_garden.bed)


class Sun:
    def shine_in_garden(self, garden):
        if garden is None:
            return
        self.shine_bed(garden.bed)
        self.shine_trees(garden.trees)

    def shine_bed(self, bed):
        if bed is None:
            return
        for temp in bed.place:
            if temp is None:
                continue
            else:
                self.shine_plant(temp)

    def shine_trees(self, trees):
        for temp in trees:
            self.shine_plant(temp)

    @staticmethod
    def shine_plant(plant: Plant):
        plant.get_sun()


class Rain:
    def pour_garden(self, garden):
        if garden is None:
            return
        self.pour_bed(garden.bed)
        self.pour_trees(garden.trees)

    def pour_bed(self, bed):
        if bed is None:
            return
        for temp in bed.place:
            if temp is None:
                continue
            else:
                self.pour_plant(temp)

    def pour_trees(self, trees):
        for temp in trees:
            self.pour_plant(temp)

    def pour_plant(self, plant: Plant):
        plant.get_water(self)


class Weather:
    @staticmethod
    def weather_is(my_garden):
        if my_garden is None:
            return
        chance = random.randint(0, 364)

        if chance % 2 == 0:
            sun = Sun()
            if my_garden is not None:
                sun.shine_in_garden(my_garden)
            print("Светит солнце!")

        if chance % 5 == 0:
            rain = Rain()
            if my_garden is not None:
                rain.pour_garden(my_garden)
            print("Идет дождь!")

        if chance % 3 == 0 and not (chance % 2 == 0) and not (chance % 5 == 0):
            print("Нет солнца и дождя!")


garden_representation = Garden()

reader = Reader()
writer = Writer()

reader.start()
writer.start()

reader.join()
writer.join()





