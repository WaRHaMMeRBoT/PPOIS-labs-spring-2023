class CellRand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_id(vector):
    id = 0
    for i in range(len(vector)):
        if (id > vector[i].id):
            id = vector[i].id
    return id + 1

class Plant:
    def __init__(self, column, row, health_points, vector_of_plants):
        self.row = row
        self.column = column
        self.health = health_points
        self.age = 0
        self.id = get_id(vector_of_plants)

    def move(self, world, random_number, vector_of_plants):
        if (self.health == 0):
            index_of_plant = 0
            world[self.row][self.column].plant = 0
            for i in range(len(vector_of_plants)):
                if (vector_of_plants[i].health == 0):
                    index_of_plant == i
                    break
            vector_of_plants.pop(index_of_plant)
            return
        if (self.age < 10):
            self.age += 1
        else:
            index_of_plant = 0
            world[self.row][self.column].herbivore -= 1
            for i in range(len(vector_of_plants)):
                if (vector_of_plants[i].age == 10):
                    index_of_plant == i
                    break
            vector_of_plants.pop(index_of_plant)
            return
        cells = []
        x = self.column
        y = self.row
        for i in [y - 1, y, y + 1]:
            for j in [x - 1, x, x + 1]:
                if (0 <= i < 9 and 0 <= j < 9):
                    a = CellRand(j, i)
                    if (a.x >= 0 and a.y >= 0):
                        cells.append(a)
        child_plant_x = 0
        child_plant_y = 0
        if (random_number >= len(cells) - 1):
            child_plant_x = cells[len(cells) - 1].x
            child_plant_y = cells[len(cells) - 1].y
        else:
            child_plant_x = cells[random_number].x
            child_plant_y = cells[random_number].y
        child_plant = Plant(child_plant_x, child_plant_y, 100, vector_of_plants)

        world[child_plant_y][child_plant_x].countOfLivings += 1
        world[child_plant_y][child_plant_x].plant = 1

        vector_of_plants.append(child_plant)

        self.health -= 25

    def set_column(self, column):
        self.column = column

    def set_row(self, row):
        self.row = row

    def get_column(self):
        return self.column

    def get_row(self):
        return self.row
