import os
import random
import xml.etree.ElementTree as Elementor

import numpy
from lxml import etree

from LR1.garden.plants import Plant, Seed, whatThePlant, Weed, whatTheSeed
from LR1.garden.weather import Weather

dictonary = [
    "tomato",
    "carrot",
    "potato",
    "cucumber",
    "zucchini",
    "weed"
]


def create_xml(x, y):
    root = etree.Element('garden')
    square = etree.SubElement(root, "square")
    etree.SubElement(square, "x").text = str(x)
    etree.SubElement(square, "y").text = str(y)

    weather = etree.SubElement(root, "weather")

    etree.SubElement(weather, "type").text = "clear"
    etree.SubElement(weather, "time").text = str(10)
    etree.SubElement(root, 'time').text = str(0)

    seeds = etree.SubElement(root, 'seeds')

    for i in range(0, random.randint(0, x * y)):
        page = etree.SubElement(seeds, "entity")
        etree.SubElement(page, "name").text = random.choice(dictonary)
        etree.SubElement(page, "health").text = "100"
        etree.SubElement(page, "time").text = "0"
        position = etree.SubElement(page, "position")
        etree.SubElement(position, "x").text = str(random.randint(0, x - 1))
        etree.SubElement(position, "y").text = str(random.randint(0, y - 1))

    doc = etree.ElementTree(root)
    doc.write(os.getcwd() + '/.gardenrc/Entities/plants.xml', pretty_print=True,
              xml_declaration=True,
              encoding='utf-8')


def create_dir(x, y):
    try:
        os.makedirs(os.path.join(os.getcwd() + "/.gardenrc/", "Entities"))
        try:
            create_xml(x, y)
        except OSError as error:
            print(error)
    except OSError as error:
        print(error)


def init(x, y):
    create_dir(x, y)


class Garden:

    def __init__(self, x, y):
        self.weather = Weather
        create_dir(x, y)
        self._x = x
        self._y = y
        self.matrix = numpy.empty((x, y), dtype="object")
        self.time = 0

    def getEntity(self, x, y):
        return self.matrix[x][y]

    def addEntity(self, plant, x, y):
        self.matrix[x][y] = plant

    def removeEntity(self, x, y):
        self.matrix[x][y] = None

    def warp(self, index: int):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] is not None:
                    print(f'{self.matrix[i][j].time} , {self.matrix[i][j]}')
                    self.matrix[i][j].time += index
        self.time += index

    def print(self):
        details = numpy.chararray((self._x, self._y), unicode=True)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] is not None:
                    details[i][j] = self.matrix[i][j].icon
                else:
                    details[i][j] += " "
        return details

    # def spawnWeed(self):
    #     if self.time % 10 == 0:
    #         for i in range(len(self.matrix)):
    #             for j in range(len(self.matrix[0])):
    #                 if self.matrix[i][j] is None:
    #                     self.matrix[i][j] = WeedSeed()

    def garbageCollector(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] is not None:
                    if not issubclass(self.matrix[i][j].__class__, Plant) and self.matrix[i][j].time >= 10:
                        time = self.matrix[i][j].time
                        self.matrix[i][j] = whatThePlant(self.matrix[i][j].name)
                        self.matrix[i][j].time = time
                    self.findNearestWeed(i, j)
                    self.matrix[i][j].get_weather(self.weather)
                    # self.spawnWeed()
                    if self.matrix[i][j].health <= 0:
                        print(f'{type(self.matrix[i][j]).__name__} (x: {i} y: {j}) has been died')
                        self.removeEntity(i, j)

    def findNearestWeed(self, x, y):
        if x != len(self.matrix[0]) - 1 and y != len(self.matrix) - 1 and self.matrix[x][y] is not None:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if x + i != len(self.matrix) and y + j != len(self.matrix[0]):
                        if self.matrix[x + i][y + j] is not self.matrix[x][y]:
                            if self.matrix[x + i][y + j].__class__ == Weed:
                                self.matrix[x][y].health -= self.matrix[x + i][y + j].damage

    def save(self):
        root = etree.Element('garden')
        square = etree.SubElement(root, "square")
        etree.SubElement(square, "x").text = str(self._x)
        etree.SubElement(square, "y").text = str(self._y)

        weather = etree.SubElement(root, "weather")
        if self.weather.time == 0:
            self.weather.time = 10
            self.weather.type = "clear"
        etree.SubElement(weather, "type").text = self.weather.type
        etree.SubElement(weather, "time").text = str(self.weather.time - 1)
        etree.SubElement(root, 'time').text = str(self.time)
        plant = etree.SubElement(root, 'plants')
        seeds = etree.SubElement(root, 'seeds')
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] is not None:
                    if issubclass(self.matrix[i][j].__class__, Plant):
                        page = etree.SubElement(plant, "entity")
                        etree.SubElement(page, "name").text = self.matrix[i][j].name
                        etree.SubElement(page, "length").text = str(self.matrix[i][j].length)
                        etree.SubElement(page, "time").text = str(self.matrix[i][j].time)
                        etree.SubElement(page, "health").text = str(self.matrix[i][j].health)
                        position = etree.SubElement(page, "position")
                        etree.SubElement(position, "x").text = str(i)
                        etree.SubElement(position, "y").text = str(j)
                    else:
                        page = etree.SubElement(seeds, "entity")
                        etree.SubElement(page, "name").text = self.matrix[i][j].name
                        etree.SubElement(page, "health").text = str(self.matrix[i][j].health)
                        etree.SubElement(page, "time").text = str(self.matrix[i][j].time)
                        position = etree.SubElement(page, "position")
                        etree.SubElement(position, "x").text = str(i)
                        etree.SubElement(position, "y").text = str(j)

        doc = etree.ElementTree(root)
        doc.write(os.getcwd() + '/.gardenrc/Entities/plants.xml', pretty_print=True,
                  xml_declaration=True,
                  encoding='utf-8')


def load() -> Garden:
    tree = Elementor.parse(r'.gardenrc/Entities/plants.xml')
    root = tree.getroot()

    garden = Garden

    for child in root:
        match child.tag:
            case "square":
                position = []
                for pos in child:
                    position.append(int(pos.text))
                garden = Garden(position[0], position[1])
            case "weather":
                for weather in child:
                    match weather.tag:
                        case "time":
                            garden.weather.time = int(weather.text)
                        case "type":
                            garden.weather.type = weather.text
            case "time":
                garden.time = int(child.text)
            case "plants":
                plant = Plant
                for plants in child:
                    for configs in plants:
                        match configs.tag:
                            case "name":
                                plant = whatThePlant(configs.text)
                            case "length":
                                plant.length = int(configs.text)
                            case "time":
                                plant.time = int(configs.text)
                            case "health":
                                plant.health = int(configs.text)
                            case "position":
                                position = []
                                for pos in configs:
                                    position.append(pos.text)
                                garden.addEntity(plant, int(position[0]), int(position[1]))
            case "seeds":
                seed = Seed
                for seeds in child:
                    for configs in seeds:
                        match configs.tag:
                            case "name":
                                seed = whatTheSeed(configs.text)
                            case "time":
                                seed.time = int(configs.text)
                            case "health":
                                seed.health = int(configs.text)
                            case "position":
                                position = []
                                for pos in configs:
                                    position.append(pos.text)
                                garden.addEntity(seed, int(position[0]), int(position[1]))

    return garden
