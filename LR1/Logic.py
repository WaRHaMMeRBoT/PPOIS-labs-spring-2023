from Wolf import Wolf
from Rabbit import Rabbit
import random


class LogicHandler:

    @staticmethod
    def do_one_step(map):
        for i in range(map.size):
            for j in range(map.size):
                LogicHandler.defining_dead_entities(map.cells[i][j])
                LogicHandler.eating_stage(map.cells[i][j])
                LogicHandler.reproduction_stage(map.cells[i][j])
                LogicHandler.getting_old_stage(map.cells[i][j])
                LogicHandler.moving_stage(map)

    @staticmethod
    def defining_dead_rabbits(cell):
        for rabbit in cell.rabbits:
            if rabbit.is_ready_to_die():
                cell.num_of_rabbits -= 1
                cell.rabbits.remove(rabbit)
                print("Rabbit dead" + " (" + str(cell.x) + "; " + str(cell.y) + ")")

    @staticmethod
    def defining_dead_wolfs(cell):

        for wolf in cell.wolfs:
            if wolf.is_ready_to_die():
                cell.num_of_wolfs -= 1
                cell.wolfs.remove(wolf)
                print("Wolf dead" + " (" + str(cell.x) + "; " + str(cell.y) + ")")

    @staticmethod
    def defining_dead_grass(cell):
        for grass in cell.grass:
            if grass.is_ready_to_die():
                cell.num_of_grass -= 1
                cell.grass.remove(grass)
                print("Grass dead" + " (" + str(cell.x) + "; " + str(cell.y) + ")")

    @staticmethod
    def defining_dead_entities(cell):
        LogicHandler.defining_dead_rabbits(cell)
        LogicHandler.defining_dead_wolfs(cell)
        LogicHandler.defining_dead_grass(cell)

    @staticmethod
    def rabbits_eating_stage(cell):
        for rabbit in cell.rabbits:
            if cell.num_of_grass > 0:
                rabbit.eat()
                cell.num_of_grass -= 1
                cell.grass.pop()

    @staticmethod
    def wolfs_eating_stage(cell):
        for wolf in cell.wolfs:
            if cell.num_of_rabbits > 0:
                wolf.eat()
                cell.num_of_rabbits -= 1
                cell.rabbits.pop()

    @staticmethod
    def eating_stage(cell):
        LogicHandler.rabbits_eating_stage(cell)
        LogicHandler.wolfs_eating_stage(cell)

    @staticmethod
    def rabbits_reproduction_stage(cell):
        for i in range(len(cell.rabbits)):
            for j in range(1, len(cell.rabbits) - 1):
                if cell.rabbits[i].gender != cell.rabbits[j].gender:
                    if cell.rabbits[i].is_ready_to_reproduction() and cell.rabbits[j].is_ready_to_reproduction() \
                            and random.randint(0, 1) == 0:
                        print("Baby rabbit was born!" + " (" + str(cell.x) + "; " + str(cell.y) + ")")
                        cell.num_of_rabbits += 1
                        cell.rabbits.append(Rabbit(cell.x, cell.y))

    @staticmethod
    def wolfs_reproduction_stage(cell):
        for i in range(len(cell.wolfs)):
            for j in range(1, len(cell.wolfs) - 1):
                if cell.wolfs[i].gender != cell.wolfs[j].gender:
                    if cell.wolfs[i].is_ready_to_reproduction() and cell.wolfs[j].is_ready_to_reproduction():
                        print("Baby wolf was born!" + " (" + str(cell.x) + "; " + str(cell.y) + ")")
                        cell.num_of_wolfs += 1
                        cell.wolfs.append(Wolf(cell.x, cell.y))

    @staticmethod
    def reproduction_stage(cell):
        LogicHandler.rabbits_reproduction_stage(cell)
        LogicHandler.wolfs_reproduction_stage(cell)

    @staticmethod
    def rabbits_moving_stage(map):
        for cell_row in map.cells:
            for cell in cell_row:
                for rabbit in cell.rabbits:
                    rabbit.move(map.size)
                    map.cells[rabbit.x][rabbit.y].rabbits.append(rabbit)
                    map.cells[rabbit.x][rabbit.y].num_of_rabbits += 1
                    cell.rabbits.remove(rabbit)
                    cell.num_of_rabbits -= 1

    @staticmethod
    def wolfs_moving_stage(map):
        for cell_row in map.cells:
            for cell in cell_row:
                for wolf in cell.wolfs:
                    wolf.move(map.size)
                    map.cells[wolf.x][wolf.y].wolfs.append(wolf)
                    map.cells[wolf.x][wolf.y].num_of_wolfs += 1
                    cell.wolfs.remove(wolf)
                    cell.num_of_wolfs -= 1

    @staticmethod
    def moving_stage(map):
        LogicHandler.rabbits_moving_stage(map)
        LogicHandler.wolfs_moving_stage(map)

    @staticmethod
    def grass_getting_old(cell):
        for grass in cell.grass:
            grass.getting_old()

    @staticmethod
    def rabbits_getting_old(cell):
        for rabbit in cell.rabbits:
            rabbit.getting_old()

    @staticmethod
    def wolfs_getting_old(cell):
        for wolf in cell.wolfs:
            wolf.getting_old()

    @staticmethod
    def getting_old_stage(cell):
        LogicHandler.rabbits_getting_old(cell)
        LogicHandler.wolfs_getting_old(cell)
        LogicHandler.grass_getting_old(cell)
